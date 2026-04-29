---
date: 2026-03-27
tags: [tech-mentor, system-design, escalabilidade, event-sourcing, cqrs, ddd, auditoria]
skill: tech-mentor-system-design/references/event-sourcing-cqrs.md
level: intermediário
---

# Event Sourcing

## Contexto

Em bancos tradicionais você armazena o estado atual. Em Event Sourcing você armazena a sequência de eventos que levou ao estado atual. O estado é uma consequência — sempre derivável dos eventos. O banco nunca perde informação: toda mudança é um fato imutável registrado com timestamp. Trabalha em conjunto com CQRS — o write model usa Event Sourcing, as projeções alimentam o read model.

## Como Funciona

### O Modelo Mental

```
Traditional (state-based):
  orders: { id: 1, status: "shipped", total: 250 }
  → UPDATE orders SET status = "shipped" WHERE id = 1
  → O que aconteceu antes? Perdido para sempre.

Event Sourcing (event-based):
  events:
    { orderId: 1, type: "OrderCreated",      data: { items, total: 250 }, at: t1 }
    { orderId: 1, type: "PaymentConfirmed",  data: { txId: "tx_abc" },    at: t2 }
    { orderId: 1, type: "OrderShipped",      data: { tracking: "BR123" }, at: t3 }

  Estado atual = replay de todos os eventos
```

### Aggregate, Command, Event

O `when` é separado do `apply`: ao reconstruir do histórico, só chama `when` — sem reemitir eventos.

```typescript
class Order {
  private id: string;
  private status: OrderStatus;
  private items: OrderItem[];
  private events: DomainEvent[] = [];

  static create(id: string, items: OrderItem[]): Order {
    const order = new Order();
    order.apply(new OrderCreatedEvent(id, items));
    return order;
  }

  ship(trackingCode: string): void {
    if (this.status !== OrderStatus.PAID) {
      throw new Error("Cannot ship unpaid order");
    }
    this.apply(new OrderShippedEvent(this.id, trackingCode));
  }

  cancel(reason: string): void {
    if (this.status === OrderStatus.SHIPPED) {
      throw new Error("Cannot cancel shipped order");
    }
    this.apply(new OrderCancelledEvent(this.id, reason));
  }

  private apply(event: DomainEvent): void {
    this.when(event);
    this.events.push(event);
  }

  // Puro — só muda estado, sem side effects
  private when(event: DomainEvent): void {
    switch (event.type) {
      case "OrderCreated":
        this.id = event.orderId;
        this.items = event.items;
        this.status = OrderStatus.PENDING;
        break;
      case "PaymentConfirmed":
        this.status = OrderStatus.PAID;
        break;
      case "OrderShipped":
        this.status = OrderStatus.SHIPPED;
        break;
      case "OrderCancelled":
        this.status = OrderStatus.CANCELLED;
        break;
    }
  }

  static reconstitute(events: DomainEvent[]): Order {
    const order = new Order();
    for (const event of events) order.when(event);
    return order;
  }

  getUncommittedEvents(): DomainEvent[] { return [...this.events]; }
  clearUncommittedEvents(): void { this.events = []; }
}
```

## Código de Referência

### Event Store — Schema PostgreSQL

```sql
CREATE TABLE event_streams (
  stream_id VARCHAR(255) PRIMARY KEY,
  version   BIGINT NOT NULL DEFAULT 0
);

CREATE TABLE events (
  id          BIGSERIAL PRIMARY KEY,
  stream_id   VARCHAR(255) NOT NULL REFERENCES event_streams(stream_id),
  version     BIGINT NOT NULL,
  type        VARCHAR(255) NOT NULL,
  data        JSONB NOT NULL,
  metadata    JSONB,
  occurred_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  UNIQUE(stream_id, version)  -- optimistic locking nativo
);

CREATE INDEX idx_events_stream ON events(stream_id, version);
```

```typescript
// Append com optimistic concurrency
async function appendToStream(
  streamId: string,
  events: DomainEvent[],
  expectedVersion: number
) {
  await db.$transaction(async tx => {
    const { version } = await tx.eventStream.findFirst({
      where: { streamId }
    }) ?? { version: -1 };

    if (version !== expectedVersion) {
      throw new ConcurrencyError(`Expected ${expectedVersion}, got ${version}`);
    }

    for (let i = 0; i < events.length; i++) {
      await tx.event.create({
        data: {
          streamId,
          version: expectedVersion + i + 1,
          type: events[i].type,
          data: events[i],
          occurredAt: new Date()
        }
      });
    }

    await tx.eventStream.upsert({
      where: { streamId },
      create: { streamId, version: expectedVersion + events.length },
      update: { version: expectedVersion + events.length }
    });
  });
}
```

### Snapshots — Performance com Aggregates Grandes

```typescript
async function loadOrder(orderId: string): Promise<Order> {
  const snapshot = await snapshotStore.getLatest(orderId);

  if (snapshot) {
    const order = Order.fromSnapshot(snapshot.state);
    const newEvents = await eventStore.readFromStream(
      `order-${orderId}`,
      snapshot.version + 1
    );
    for (const event of newEvents) order.when(event);
    return order;
  }

  const allEvents = await eventStore.readFromStream(`order-${orderId}`);
  return Order.reconstitute(allEvents);
}

async function saveOrder(order: Order): Promise<void> {
  const events = order.getUncommittedEvents();
  await eventStore.appendToStream(`order-${order.id}`, events, order.version);

  // Snapshot a cada 50 eventos
  if (order.version % 50 === 0) {
    await snapshotStore.save({
      aggregateId: order.id,
      version: order.version,
      state: order.toSnapshot()
    });
  }

  order.clearUncommittedEvents();
}
```

### Projeções — Read Model a partir de Eventos

```typescript
class OrderProjection {
  async run(): Promise<void> {
    const checkpoint = await this.getCheckpoint("order-projection");
    const events = this.eventStore.subscribeFromPosition(checkpoint);

    for await (const event of events) {
      await db.$transaction(async tx => {
        await this.processEvent(event, tx);
        await this.saveCheckpoint("order-projection", event.position, tx);
      });
    }
  }
}
// Rebuild: trunca a tabela, zera o checkpoint, reprocessa tudo do início
```

### Time-Travel — Estado em qualquer ponto no tempo

```typescript
async function getOrderStateAt(orderId: string, asOf: Date): Promise<OrderState> {
  const events = await db.event.findMany({
    where: { streamId: `order-${orderId}`, occurredAt: { lte: asOf } },
    orderBy: { version: "asc" }
  });
  return events.reduce(applyEvent, initialOrderState);
}
// Impossível com bancos tradicionais — o UPDATE sobrescreve o passado
```

### Event Schema Migration — Upcasting

```typescript
// Nunca modifique eventos já persistidos — upcast só na leitura
class OrderPlacedUpcaster {
  canUpcast(event: StoredEvent): boolean {
    return event.type === "OrderPlaced" && (!event.version || event.version < 2);
  }

  upcast(event: StoredEvent): StoredEvent {
    return {
      ...event,
      version: 2,
      customerId: `usr_${event.customerId}`,
      totalCents: Math.round(event.total * 100),
      total: undefined
    };
  }
}
// Upcasters encadeados: v1→v2→v3 — nunca salte versões
```

## Trade-offs

| Aspecto | State-based | Event Sourcing |
|---|---|---|
| **Audit log** | Não nativo — requer triggers | Completo por design |
| **Time-travel** | Impossível sem CDC | Nativo |
| **Replay/rebuild** | Impossível | Qualquer projeção pode ser reconstruída |
| **Complexidade** | Baixa | Alta — aggregate, eventstore, projeções |
| **Queries ad-hoc** | Fácil com SQL | Requer projeções pré-construídas |
| **Debug** | Difícil rastrear o porquê | Stream de eventos = história completa |

## Quando Usar / Quando Evitar

**Use Event Sourcing quando:**
- ✅ Auditoria completa é obrigatória (financeiro, compliance, saúde)
- ✅ Time-travel: "qual era o estado do contrato em X?"
- ✅ Múltiplas projeções do mesmo dado (relatório, API, analytics)
- ✅ Domínio rico em eventos de negócio (pedido, contrato, conta bancária)

**Evite quando:**
- ❌ CRUD simples — cadastro de usuário, configurações
- ❌ Time sem experiência em DDD — complexidade alta
- ❌ Queries ad-hoc complexas (OLAP) — não é banco analítico
- ❌ Não precisa de auditoria — complexidade não compensa

## Conceitos Relacionados

[[fase-2-escalabilidade]] · [[cqrs]] · [[mensageria]] · [[banco-de-dados]] · [[outbox-pattern]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
