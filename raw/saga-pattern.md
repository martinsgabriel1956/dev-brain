---
date: 2026-04-13
tags: [tech-mentor, backend, saga, distributed-transactions, choreography, orchestration]
skill: tech-mentor-backend/references/distributed-systems
level: avançado
---

# Saga Pattern

## Contexto

Em sistemas distribuídos, não existe 2PC (Two-Phase Commit) eficiente entre serviços independentes. A Saga é o padrão para **gerenciar transações distribuídas** garantindo consistência eventual via sequência de transações locais com **compensações** em caso de falha.

O conceito central: cada etapa tem uma **transação local** (que funciona) e uma **transação compensatória** (que desfaz o efeito em caso de falha posterior).

## As Duas Abordagens

### Choreography (Coreografia)

Cada serviço reage a eventos e publica novos eventos. Sem coordenador central.

```
OrderService → [order.placed]  → PaymentService → [payment.processed] → InventoryService
                                                                              │
OrderService ← [order.cancelled] ← PaymentService ← [payment.refunded] ←────┘
              (compensação)        (compensação)    (compensation trigger)
```

**Implementação:**
```typescript
// PaymentService — reage a order.placed
class PaymentConsumer {
  async handleOrderPlaced(event: OrderPlacedEvent): Promise<void> {
    try {
      const charge = await this.stripeAdapter.charge(event.total, event.paymentMethod);
      await this.eventBus.publish("payment.processed", {
        orderId: event.orderId,
        transactionId: charge.id
      });
    } catch (error) {
      // Falha → publica evento de compensação
      await this.eventBus.publish("payment.failed", {
        orderId: event.orderId,
        reason: error.message
      });
    }
  }
}

// OrderService — reage a payment.failed e compensa
class OrderCompensationConsumer {
  async handlePaymentFailed(event: PaymentFailedEvent): Promise<void> {
    await this.orderService.cancel(event.orderId, "Payment failed");
    await this.eventBus.publish("order.cancelled", { orderId: event.orderId });
  }
}
```

### Orchestration (Orquestração)

Um coordenador central (Saga Orchestrator) emite comandos e aguarda respostas. Tem visão completa do fluxo.

```
                     ┌─────────────────────────┐
                     │    Order Saga            │
                     │    (Orchestrator)        │
                     └──────────┬──────────────┘
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
    [charge.command]  [reserve.command]    [notify.command]
          │                     │                     │
    PaymentService       InventoryService    NotificationService
          │                     │                     │
    [charged.reply]  [reserved.reply]       [notified.reply]
```

**Implementação com state machine:**
```typescript
type SagaState = "PENDING" | "PAYMENT_PROCESSING" | "INVENTORY_RESERVING" | "COMPLETED" | "COMPENSATING" | "FAILED";

class PlaceOrderSaga {
  private state: SagaState = "PENDING";
  private completedSteps: string[] = [];

  async start(orderId: string): Promise<void> {
    this.state = "PAYMENT_PROCESSING";

    // Emite comando para Payment Service
    await this.commandBus.send("payment.charge.command", {
      sagaId: this.sagaId,
      orderId,
      amount: this.order.total
    });
  }

  async handlePaymentCharged(reply: PaymentChargedReply): Promise<void> {
    this.completedSteps.push("payment");
    this.state = "INVENTORY_RESERVING";

    await this.commandBus.send("inventory.reserve.command", {
      sagaId: this.sagaId,
      orderId: reply.orderId,
      items: this.order.items
    });
  }

  async handleInventoryReserveFailed(reply: ReserveFailedReply): Promise<void> {
    this.state = "COMPENSATING";

    // Compensa etapas concluídas na ordem inversa
    if (this.completedSteps.includes("payment")) {
      await this.commandBus.send("payment.refund.command", {
        sagaId: this.sagaId,
        transactionId: reply.transactionId
      });
    }
  }

  async handlePaymentRefunded(): Promise<void> {
    this.state = "FAILED";
    await this.orderRepository.cancel(this.order.id, "Inventory unavailable");
  }
}
```

**Persistência do estado da Saga (obrigatório):**
```sql
CREATE TABLE sagas (
  id          UUID PRIMARY KEY,
  type        VARCHAR(100) NOT NULL,
  state       VARCHAR(100) NOT NULL,
  payload     JSONB NOT NULL,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

## Comparação Choreography vs Orchestration

| Aspecto | Choreography | Orchestration |
|---|---|---|
| Visibilidade do fluxo | Difícil — distribuído em eventos | Clara — centralizada no orchestrator |
| Acoplamento | Baixo (eventos) | Moderado (orchestrator conhece todos) |
| Debugging | Complexo — rastrear eventos no broker | Mais fácil — estado no banco do orchestrator |
| Testabilidade | Difícil — precisa de todos os serviços | Mais fácil — orchestrator testável isoladamente |
| Single Point of Failure | Não tem | O orchestrator pode ser |
| Quando usar | Fluxos simples, poucos passos | Fluxos complexos, muitas compensações |

## Compensações — Regras Críticas

```
Transações compensatórias devem ser:
1. Idempotentes — podem ser chamadas múltiplas vezes
2. Sem retry infinito — eventual dead letter queue
3. Em ordem inversa da execução original

Compensação NÃO é rollback:
- Você não desfaz — você compensa
- "Estornar pagamento" vs "não cobrar"
- Dados gerados (IDs, timestamps) permanecem
```

### Dead Letter Queue para Sagas Travadas

```typescript
class SagaMonitor {
  // Verifica sagas presas em estado intermediário por muito tempo
  async checkStuckSagas(): Promise<void> {
    const stuckSagas = await prisma.saga.findMany({
      where: {
        state: { notIn: ["COMPLETED", "FAILED"] },
        updatedAt: { lt: new Date(Date.now() - 30 * 60 * 1000) }  // 30min sem atualizar
      }
    });

    for (const saga of stuckSagas) {
      await this.alerting.warn({
        message: "Saga stuck",
        sagaId: saga.id,
        state: saga.state,
        duration: Date.now() - saga.updatedAt.getTime()
      });
    }
  }
}
```

## Temporal — Durable Execution para Sagas

O Temporal é a abordagem moderna para orquestração de sagas — o estado da saga sobrevive a crashes do processo automaticamente:

```typescript
import { defineWorkflow, proxyActivities } from "@temporalio/workflow";

const activities = proxyActivities<{
  chargePayment(orderId: string, amount: number): Promise<string>;
  refundPayment(transactionId: string): Promise<void>;
  reserveInventory(orderId: string, items: OrderItem[]): Promise<void>;
  releaseInventory(orderId: string): Promise<void>;
}>({ startToCloseTimeout: "1 minute" });

export const placeOrderWorkflow = defineWorkflow(async (orderId: string): Promise<void> => {
  const transactionId = await activities.chargePayment(orderId, order.total);

  try {
    await activities.reserveInventory(orderId, order.items);
  } catch (error) {
    // Temporal garante que esta compensação será executada mesmo após crash
    await activities.refundPayment(transactionId);
    throw error;
  }
});
```

## Conceitos Relacionados

[[event-driven-architecture]] · [[outbox-pattern]] · [[circuit-breaker]] · [[distributed-locks-raft]] · [[mensageria]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-13*
