---
date: 2026-03-27
tags: [tech-mentor, system-design, infraestrutura, mensageria, kafka, rabbitmq, sqs, eda]
skill: tech-mentor-system-design/references/eda-overview.md
level: fundamento
---

# Mensageria

## Contexto

Mensageria é comunicação **assíncrona** entre serviços através de um intermediário (broker). Em vez de serviço A chamar serviço B diretamente e esperar a resposta, A publica uma mensagem e continua — B processa quando puder. A mudança central: produtor e consumidor são desacoplados no tempo e no espaço. Não precisam estar online ao mesmo tempo, não precisam se conhecer.

## Como Funciona

### Sync vs Async — O Problema que Mensageria Resolve

```
Sync (REST/gRPC):
Order → [HTTP] → Payment → [HTTP] → Inventory → [HTTP] → Notification
                                                              ↑
                              se isso cair, o pedido falha inteiro

Async (Mensageria):
Order → publica "order.created" → Broker
                                      ├── Payment consome (quando puder)
                                      ├── Inventory consome (quando puder)
                                      └── Notification consome (quando puder)
                     se Notification cair, a mensagem fica na fila
```

Com sync, a latência soma — 3 chamadas de 100ms = 300ms mínimo. Com async, o Order responde ao cliente em ~10ms e o restante acontece em paralelo.

### Queue vs Stream — A Distinção Fundamental

| Característica | Queue (fila) | Stream |
|---|---|---|
| **Semântica** | Cada mensagem é consumida **uma vez** | Cada consumer lê **seu próprio offset** |
| **Retenção** | Mensagem some após consumo | Mensagem fica por TTL configurado |
| **Replay** | Impossível | Possível — reprocessar eventos passados |
| **Consumidores** | Compete pelo item (um ganha) | Todos recebem (pub/sub) |
| **Exemplo** | RabbitMQ, SQS | Kafka, Kinesis |

- **Queue**: processamento de job único (enviar email, processar pagamento) — só um worker deve executar
- **Stream**: eventos de negócio (pedido criado, usuário ativado) — múltiplos serviços precisam reagir

### Os Três Grandes Brokers

**Kafka** — stream distribuído, alta throughput:
```
Producer → Topic (particionado) → Consumer Groups
                                        ├── Group A: Payment service (offset próprio)
                                        └── Group B: Analytics service (offset próprio)

Retenção default: 7 dias → replay de eventos possível
Throughput: milhões de mensagens/segundo
```

**RabbitMQ** — queue clássica, roteamento flexível:
```
Producer → Exchange → Binding Rules → Queue → Consumer
              │
              ├── Direct exchange:  routing key exata
              ├── Topic exchange:   wildcard (order.*)
              └── Fanout exchange:  broadcast para todas as queues
```

**SQS** — queue gerenciada AWS, zero operação:
```
Standard Queue:  at-least-once, ordem não garantida → mais barato
FIFO Queue:      exactly-once, ordem garantida → 300 TPS limit
```

## Código de Referência

### Dead Letter Queue (DLQ)

```typescript
// SQS — após 3 tentativas falhas, vai para a DLQ automaticamente
const queueConfig = {
  RedrivePolicy: {
    maxReceiveCount: 3,
    deadLetterTargetArn: dlqArn
  }
};

async function processMessage(message: SQSMessage) {
  try {
    await processOrder(JSON.parse(message.Body));
    await sqs.deleteMessage({ ReceiptHandle: message.ReceiptHandle });
  } catch (err) {
    // Não deleta → visibilidade timeout expira → SQS reentrega
    // Após maxReceiveCount, vai para DLQ automaticamente
    console.log({ message: "Message processing failed", error: err.message });
  }
}
```

### Outbox Pattern — Garantia de Publicação

```typescript
// ❌ Problema: transação commita mas publicação falha → evento perdido
await db.$transaction(async tx => {
  const order = await tx.order.create({ data });
  await kafka.publish("order.created", order); // pode falhar aqui
});

// ✅ Outbox: salva evento na mesma transação, worker publica depois
await db.$transaction(async tx => {
  const order = await tx.order.create({ data });
  await tx.outbox.create({
    data: { topic: "order.created", payload: JSON.stringify(order) }
  });
});

// Worker separado (CDC ou polling) lê outbox e publica no broker
async function outboxWorker() {
  const events = await db.outbox.findMany({ where: { publishedAt: null } });
  for (const event of events) {
    await kafka.publish(event.topic, JSON.parse(event.payload));
    await db.outbox.update({
      where: { id: event.id },
      data: { publishedAt: new Date() }
    });
  }
}
```

### Idempotência — Consumer Seguro para At-least-once

```typescript
async function processOrderPayment(event: OrderCreatedEvent) {
  // Idempotency key — se já processou, ignora
  const existing = await db.payment.findUnique({
    where: { orderId: event.orderId }
  });
  if (existing) return; // já processado → seguro ignorar

  await db.payment.create({ data: { orderId: event.orderId } });
}
```

### Event-Carried State Transfer

```typescript
// ❌ Event Notification — consumer precisa buscar o dado
{ event: "user.updated", userId: "123" }
// Consumer faz GET /users/123 → acoplamento + latência extra

// ✅ Event-Carried State Transfer — dado no próprio evento
{
  event: "user.updated",
  userId: "123",
  name: "Gabriel",
  email: "gabriel@email.com",
  updatedAt: "2026-03-27T10:00:00Z"
}
// Consumer tem tudo que precisa — sem lookup extra
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| **Desacoplamento** | Serviços evoluem independentemente | Fluxo distribuído difícil de debugar |
| **Resiliência** | Buffer contra picos, sem cascata de falhas | Eventual consistency — dado não é imediato |
| **Throughput** | Paralelo nativo, processa em batch | Latência de entrega maior que sync |
| **Kafka** | Replay, alta throughput, durável | Operação complexa, custo em cluster pequeno |
| **SQS** | Zero ops, custo baixo, HA automático | Sem replay, FIFO limitado a 300 TPS |
| **RabbitMQ** | Roteamento flexível, protocolo AMQP | State em memória por default, mais infra |

### Garantias de Entrega

| Garantia | Significado | Implicação |
|---|---|---|
| **At-most-once** | Pode perder, nunca duplica | Log de métricas — perda tolerável |
| **At-least-once** | Nunca perde, pode duplicar | Padrão — consumer precisa ser idempotente |
| **Exactly-once** | Nunca perde, nunca duplica | Kafka transactions / SQS FIFO — mais caro |

## Quando Usar / Quando Evitar

**Use mensageria quando:**
- ✅ Múltiplos serviços precisam reagir ao mesmo evento (fan-out)
- ✅ Processamento pode ser deferido (envio de email, geração de relatório)
- ✅ Workload com picos — broker absorve burst sem derrubar o consumer
- ✅ Integração com sistemas lentos ou instáveis

**Evite quando:**
- ❌ Precisa da resposta imediata para continuar o fluxo — use RPC/REST
- ❌ Sistema pequeno com 2-3 serviços — complexidade não compensa
- ❌ Transação distribuída com rollback automático — mensageria não tem 2PC

## Conceitos Relacionados

[[fase-1-fundamentos-infraestrutura]] · [[banco-de-dados]] · [[cache]] · [[event-sourcing]] · [[cqrs]] · [[outbox-pattern]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
