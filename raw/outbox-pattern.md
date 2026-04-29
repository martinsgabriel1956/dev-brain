---
date: 2026-04-13
tags: [tech-mentor, backend, outbox, transactional-messaging, cdc, debezium]
skill: tech-mentor-backend/references/messaging
level: avançado
---

# Outbox Pattern

## Contexto

O **Dual Write Problem**: você precisa salvar dados no banco E publicar um evento no broker. Se fizer os dois separadamente, uma das operações pode falhar:

```
1. INSERT order no PostgreSQL → OK
2. PUBLISH order.placed no Kafka → FALHA

Resultado: banco tem o pedido, mas ninguém foi notificado.
Pedido "fantasma" que nunca avança no fluxo.
```

A solução ingênua de retry não resolve — se o app crashar entre as duas operações, o evento nunca é publicado.

**O Outbox Pattern garante**: ou ambos acontecem, ou nenhum.

## Como Funciona

### Conceito

Em vez de publicar direto no broker, você escreve o evento em uma tabela `outbox` **na mesma transaction** que os dados de negócio. Um processo separado lê a tabela outbox e publica no broker.

```
                   ┌─────────────────────────┐
PlaceOrderUseCase ─→ BEGIN TRANSACTION       │
                  │  INSERT INTO orders ...  │  ← dados de negócio
                  │  INSERT INTO outbox ...  │  ← evento serializado
                  └─ COMMIT ────────────────┘
                              │
                    ┌─────────▼──────────┐
                    │  Outbox Publisher   │
                    │  (processo separado)│
                    └─────────┬──────────┘
                              │  publica no Kafka
                              ▼
                         [Kafka Topic]
                              │
                    marks as published
```

### Implementação

**Tabela outbox:**
```sql
CREATE TABLE outbox_events (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  aggregate_type VARCHAR(100) NOT NULL,  -- "Order"
  aggregate_id   VARCHAR(100) NOT NULL,  -- order ID
  event_type     VARCHAR(200) NOT NULL,  -- "order.placed"
  payload        JSONB NOT NULL,
  occurred_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  published_at   TIMESTAMPTZ,           -- NULL = pendente
  published      BOOLEAN NOT NULL DEFAULT false
);

CREATE INDEX idx_outbox_unpublished ON outbox_events (published, occurred_at)
  WHERE published = false;
```

**Use Case — escreve no outbox na mesma transaction:**
```typescript
class PlaceOrderUseCase {
  async execute(input: PlaceOrderInput): Promise<void> {
    await prisma.$transaction(async tx => {
      // 1. Salva o pedido
      const order = await tx.order.create({
        data: {
          id: randomUUID(),
          customerId: input.customerId,
          total: input.total,
          status: "placed"
        }
      });

      // 2. Escreve no outbox NA MESMA TRANSACTION
      await tx.outboxEvent.create({
        data: {
          aggregateType: "Order",
          aggregateId: order.id,
          eventType: "order.placed",
          payload: {
            orderId: order.id,
            customerId: order.customerId,
            total: order.total,
            occurredAt: new Date().toISOString()
          }
        }
      });
    });
  }
}
```

**Outbox Publisher — lê e publica:**
```typescript
class OutboxPublisher {
  async run(): Promise<void> {
    while (true) {
      await this.processUnpublishedEvents();
      await sleep(1000);  // poll a cada 1s
    }
  }

  private async processUnpublishedEvents(): Promise<void> {
    // SKIP LOCKED garante que múltiplos publishers não processem o mesmo evento
    const events = await prisma.$queryRaw<OutboxEvent[]>`
      SELECT * FROM outbox_events
      WHERE published = false
      ORDER BY occurred_at
      LIMIT 100
      FOR UPDATE SKIP LOCKED
    `;

    for (const event of events) {
      await this.kafka.publish(event.eventType, event.payload);

      await prisma.outboxEvent.update({
        where: { id: event.id },
        data: { published: true, publishedAt: new Date() }
      });
    }
  }
}
```

### Abordagem com CDC (Debezium) — Mais Robusta

Em vez de polling, use **Change Data Capture** para capturar mudanças no WAL do PostgreSQL:

```
PostgreSQL WAL → Debezium → Kafka Connect → Kafka Topic
                             (lê outbox_events)
```

Configuração do Debezium (Kafka Connect):
```json
{
  "name": "outbox-connector",
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "database.hostname": "postgres",
    "database.dbname": "app",
    "table.include.list": "public.outbox_events",
    "transforms": "outbox",
    "transforms.outbox.type": "io.debezium.transforms.outbox.EventRouter",
    "transforms.outbox.table.field.event.type": "event_type",
    "transforms.outbox.table.field.event.key": "aggregate_id",
    "transforms.outbox.route.by.field": "event_type"
  }
}
```

**Vantagens do CDC sobre polling:**
- Latência ultra-baixa (< 100ms vs ~1s com polling)
- Sem carga extra no banco (lê WAL, não faz SELECT)
- Não precisa gerenciar o processo de polling

### Inbox Pattern (Complementar)

O Inbox Pattern resolve o problema no lado do **consumidor**: garantir processamento exatamente uma vez mesmo com at-least-once delivery do broker.

```typescript
class OrderEventConsumer {
  async handleOrderPlaced(event: OrderPlacedEvent): Promise<void> {
    await prisma.$transaction(async tx => {
      // Verifica se já processou — idempotência
      const exists = await tx.inboxEvent.findUnique({ where: { eventId: event.eventId } });
      if (exists) return;  // já processado, idempotente

      // Marca como recebido E processa na mesma transaction
      await tx.inboxEvent.create({ data: { eventId: event.eventId, processedAt: new Date() } });
      await tx.notification.create({ data: { orderId: event.orderId, type: "confirmation" } });
    });
  }
}
```

## Trade-offs

| Aspecto | Polling | CDC (Debezium) |
|---|---|---|
| Latência | ~1s | < 100ms |
| Complexidade | Baixa | Alta (Kafka Connect, conector) |
| Carga no banco | SELECT periódico | Leitura do WAL (menor impacto) |
| Garantias | At-least-once | At-least-once |
| Manutenção | Simples | Requer monitoramento do conector |

## Quando Usar

**Outbox é obrigatório quando:**
- Você publica eventos em broker E salva no banco no mesmo fluxo
- Consistência eventual é necessária mas perda de eventos é inaceitável
- Operações financeiras, pedidos, fluxos críticos de negócio

**Não precisar do Outbox:**
- Publicação de evento é best-effort (logs de acesso, analytics não-críticos)
- Você usa uma solução que já oferece transactional messaging nativamente (ex: AWS EventBridge Pipes + DynamoDB Streams)

## Conceitos Relacionados

[[event-driven-architecture]] · [[mensageria]] · [[cqrs]] · [[saga]] · [[distributed-locks-raft]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-13*
