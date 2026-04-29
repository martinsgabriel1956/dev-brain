---
date: 2026-04-17
tags: [tech-mentor, mensageria, eventos, ordering, saga, process-manager]
skill: tech-mentor-backend/references/messaging
level: avançado
---

# Event Ordering e Long-Running Processes

## Event Ordering

### O Problema
Em sistemas com múltiplos producers e brokers particionados, eventos de uma mesma entidade podem chegar fora de ordem: `OrderShipped` chega antes de `OrderCreated`.

### Particionamento como Solução

No Kafka, mensagens com a mesma **key** sempre vão para a mesma partição, garantindo ordering dentro daquela entidade.

```typescript
// Producer — sempre usar orderId como key
await producer.send({
  topic: "orders",
  messages: [{
    key: order.id,           // garante que todos os eventos do mesmo pedido
    value: JSON.stringify(event) // vão para a mesma partição, em ordem
  }]
});
```

**Limitação:** ordering é garantida *por partição*, não entre entidades diferentes. Se você precisa ordenar eventos de `Order` com eventos de `Payment` (entidades diferentes), particionamento não resolve.

### Sequence Numbers

Para ordering além de partições, use sequence numbers no próprio evento:

```typescript
type DomainEvent = {
  aggregateId: string;
  aggregateVersion: number;  // sequence number por aggregate
  eventType: string;
  payload: unknown;
  occurredAt: string;
};

// Consumer detecta gap na sequência
class OrderEventConsumer {
  private expectedVersions = new Map<string, number>();

  async handle(event: DomainEvent) {
    const expected = this.expectedVersions.get(event.aggregateId) ?? 0;
    
    if (event.aggregateVersion !== expected + 1) {
      // Evento chegou fora de ordem — buffer e aguarda o evento faltante
      await this.bufferOutOfOrder(event);
      return;
    }

    await this.processEvent(event);
    this.expectedVersions.set(event.aggregateId, event.aggregateVersion);
    await this.drainBuffer(event.aggregateId);
  }
}
```

---

## Long-Running Processes

### O Problema
Processos de negócio que envolvem múltiplos serviços ao longo do tempo (minutos, horas, dias) precisam de estado persistido entre etapas. Exemplo: "checkout → pagamento → antifraude → fulfillment → notificação".

### Process Manager (Saga com State Machine)

Diferente de uma Saga simples (sem estado central), o **Process Manager** mantém estado explícito de onde o processo está.

```typescript
type CheckoutProcessState =
  | "awaiting_payment"
  | "payment_processing"
  | "fraud_check"
  | "fulfillment"
  | "completed"
  | "failed";

type CheckoutProcess = {
  id: string;
  orderId: string;
  state: CheckoutProcessState;
  startedAt: Date;
  lastUpdatedAt: Date;
  compensations: string[]; // ações de rollback executadas
};

class CheckoutProcessManager {
  async on(event: DomainEvent) {
    const process = await this.processRepo.findByOrderId(event.orderId);

    switch (event.type) {
      case "OrderCreated":
        await this.start(event.orderId);
        await this.commandBus.send({ type: "InitiatePayment", orderId: event.orderId });
        break;

      case "PaymentSucceeded":
        if (process?.state !== "payment_processing") return; // idempotência
        await this.transition(process.id, "fraud_check");
        await this.commandBus.send({ type: "RunFraudCheck", orderId: event.orderId });
        break;

      case "FraudCheckPassed":
        await this.transition(process.id, "fulfillment");
        await this.commandBus.send({ type: "StartFulfillment", orderId: event.orderId });
        break;

      case "PaymentFailed":
      case "FraudCheckFailed":
        await this.transition(process.id, "failed");
        await this.compensate(process!);
        break;
    }
  }

  private async compensate(process: CheckoutProcess) {
    // Executa compensações em ordem inversa
    if (process.compensations.includes("payment")) {
      await this.commandBus.send({ type: "RefundPayment", orderId: process.orderId });
    }
  }
}
```

### Timeout e Prazo de Expiração

Long-running processes precisam lidar com timeout — o que acontece se `PaymentSucceeded` nunca chega?

```typescript
// Ao iniciar o processo, agendar um timeout
class CheckoutProcessManager {
  private async start(orderId: string) {
    const process = await this.processRepo.create({
      orderId,
      state: "awaiting_payment",
      startedAt: new Date()
    });

    // Scheduler agenda evento de timeout para daqui 30 minutos
    await this.scheduler.schedule({
      at: new Date(Date.now() + 30 * 60 * 1000),
      event: { type: "CheckoutTimeout", processId: process.id }
    });
  }

  async on(event: { type: "CheckoutTimeout"; processId: string }) {
    const process = await this.processRepo.findById(event.processId);
    if (process?.state === "completed" || process?.state === "failed") return; // já terminou

    await this.transition(process!.id, "failed");
    await this.compensate(process!);
  }
}
```

### Process Manager vs. Saga

| Aspecto | Saga (Choreography) | Process Manager |
|---|---|---|
| Estado | Implícito (nos eventos) | Explícito (na tabela) |
| Visibilidade | Difícil — precisa juntar eventos | Fácil — query direta no estado |
| Timeout | Complexo de implementar | Natural — agendar evento de expiração |
| Complexidade | Baixa inicialmente | Maior — requer state machine |
| Quando usar | 2-3 steps simples | 4+ steps, timeout, compensação complexa |

## Conceitos Relacionados
[[saga-pattern]] · [[kafka]] · [[event-sourcing]] · [[temporal]] · [[idempotencia]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
