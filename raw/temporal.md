---
date: 2026-04-14
tags: [tech-mentor, backend, mensageria, temporal, workflows, durable-execution]
skill: tech-mentor-backend/references/mensageria
level: avançado
---

# Temporal — Durable Execution e Workflow Orchestration

## Contexto

Temporal resolve o problema de **processos de longa duração** que precisam sobreviver a falhas, restarts e deploys. É um runtime de "durable execution": o código do workflow é executado como se nunca houvesse falhas — o Temporal garante que cada passo seja completado, mesmo que o worker caia no meio.

Comparado a Saga manual com Kafka: Temporal elimina o boilerplate de compensação, retry, state management e deduplicação. A lógica de negócio fica clara; o Temporal cuida da infraestrutura de confiabilidade.

## Como Funciona

### Modelo Mental

O Temporal persiste o **histórico de execução** do workflow. Se o worker cai, ao reiniciar ele **replaya** o histórico até o ponto onde parou e continua de onde estava — sem re-executar o que já foi feito.

```
Workflow: ProcessOrderWorkflow

Passo 1: ReserveInventory()    ← executado e persistido
Passo 2: ChargePayment()       ← executado e persistido
Passo 3: SendConfirmation()    ← worker cai aqui ↓
              [worker reinicia]
              [Temporal replaya passos 1 e 2 no histórico]
              [re-executa SendConfirmation()]
Passo 4: NotifyWarehouse()     ← continua normalmente
```

### Workflow e Activities

```typescript
import { defineWorkflow, defineActivity, proxyActivities, sleep } from "@temporalio/workflow";
import type * as activities from "./activities";

// Activities: unidades de trabalho que podem falhar e ser retentadas
// Cada activity é executada fora do worker e tem retry automático
const { reserveInventory, chargePayment, sendConfirmation, notifyWarehouse } = proxyActivities<typeof activities>({
  startToCloseTimeout: "30s",  // máximo para completar
  retry: {
    maximumAttempts: 3,
    initialInterval: "1s",
    backoffCoefficient: 2      // 1s, 2s, 4s
  }
});

// Workflow: orquestração determinística dos steps
export async function processOrderWorkflow(orderId: string): Promise<void> {
  // Todos os passos são duráveis — sobrevivem a falhas do worker
  await reserveInventory(orderId);
  await chargePayment(orderId);
  await sendConfirmation(orderId);
  await notifyWarehouse(orderId);
}

// Workflow com sleep durável — funciona por dias/semanas
export async function subscriptionRenewalWorkflow(subscriptionId: string): Promise<void> {
  while (true) {
    await chargeSubscription(subscriptionId);
    await sleep("30 days"); // sleep durável — worker pode reiniciar no meio
    await checkSubscriptionStatus(subscriptionId);
  }
}
```

```typescript
// activities.ts — I/O real, chamadas externas, banco de dados
export async function reserveInventory(orderId: string): Promise<void> {
  await prisma.inventory.update({
    where: { orderId },
    data: { status: "reserved" }
  });
}

export async function chargePayment(orderId: string): Promise<void> {
  const order = await prisma.order.findUniqueOrThrow({ where: { id: orderId } });
  await stripe.paymentIntents.confirm(order.paymentIntentId);
}
```

### Signals e Queries

**Signals:** permitem que código externo envie dados para um workflow em execução.

```typescript
// Workflow aguarda aprovação humana via Signal
import { defineSignal, setHandler, condition } from "@temporalio/workflow";

const approvalSignal = defineSignal<[{ approved: boolean; reason: string }]>("approval");

export async function expenseApprovalWorkflow(expenseId: string): Promise<string> {
  let approved = false;
  let reason = "";

  setHandler(approvalSignal, ({ approved: a, reason: r }) => {
    approved = a;
    reason = r;
  });

  // Aguarda signal por até 7 dias
  const received = await condition(() => approved !== undefined, "7 days");

  if (!received) {
    await cancelExpense(expenseId);
    return "expired";
  }

  if (!approved) {
    await rejectExpense(expenseId, reason);
    return "rejected";
  }

  await processExpense(expenseId);
  return "approved";
}

// Enviar signal de outro serviço
const handle = client.workflow.getHandle(workflowId);
await handle.signal(approvalSignal, { approved: true, reason: "Within budget" });
```

**Queries:** leitura síncrona do estado atual de um workflow.

```typescript
import { defineQuery, setHandler } from "@temporalio/workflow";

const statusQuery = defineQuery<{ step: string; completedAt?: Date }>("status");

export async function processOrderWorkflow(orderId: string) {
  let currentStep = "starting";
  setHandler(statusQuery, () => ({ step: currentStep }));

  currentStep = "reserving";
  await reserveInventory(orderId);

  currentStep = "charging";
  await chargePayment(orderId);

  currentStep = "completed";
}

// Query do cliente
const status = await handle.query(statusQuery);
console.log(status.step); // "charging"
```

### Compensação — Saga com Temporal

Temporal simplifica drasticamente o padrão Saga — a lógica de compensação fica no próprio workflow:

```typescript
export async function bookTripWorkflow(tripId: string): Promise<void> {
  let flightBooked = false;
  let hotelBooked = false;

  try {
    await bookFlight(tripId);
    flightBooked = true;

    await bookHotel(tripId);
    hotelBooked = true;

    await bookCar(tripId);

  } catch (error) {
    // Compensação em ordem inversa
    if (hotelBooked) await cancelHotel(tripId);
    if (flightBooked) await cancelFlight(tripId);
    throw error;
  }
}
```

### Versionamento de Workflows

Workflows de longa duração precisam lidar com deploys de nova versão enquanto instâncias antigas ainda estão rodando:

```typescript
import { patched } from "@temporalio/workflow";

export async function processOrderWorkflow(orderId: string) {
  await reserveInventory(orderId);
  await chargePayment(orderId);

  // patched() permite adicionar novo comportamento sem quebrar instâncias antigas
  if (patched("send-sms-confirmation")) {
    await sendSmsConfirmation(orderId); // novo step na v2
  }

  await sendEmailConfirmation(orderId);
}
```

## Trade-offs

| Aspecto | Temporal | Saga Manual (Kafka) | Step Functions (AWS) |
|---|---|---|---|
| **Código** | Workflow legível, linear | Handlers espalhados + state machine | YAML/JSON de definição |
| **Estado** | Gerenciado automaticamente | Você gerencia no banco | Gerenciado pela AWS |
| **Durabilidade** | Event sourcing interno automático | Outbox Pattern manual | Gerenciada pela AWS |
| **Observabilidade** | UI nativa com histórico completo | Rastreamento manual | CloudWatch |
| **Operação** | Auto-hosted ou Temporal Cloud | Kafka + consumers | Serverless |
| **Vendor lock** | Temporal (open-source) | Neutro | AWS |
| **Custo** | Infrastructure + Temporal Cloud | Kafka infrastructure | Por state transition |

## Quando Usar / Quando Evitar

**Usar Temporal quando:**
- Workflows de longa duração (minutos a dias — onboarding, aprovação, cobrança)
- Muitos passos com compensação complexa — o Saga manual fica inviável
- Precisar de sleep durável, retries automáticos e visibilidade do estado
- Time quer focar em lógica de negócio, não em infraestrutura de confiabilidade

**Considerar alternativas quando:**
- Fluxo simples de 2-3 steps — Saga manual ou BullMQ são suficientes
- Você já está 100% no AWS — Step Functions tem menos overhead operacional
- Time pequeno sem capacidade de operar um cluster Temporal

## Conceitos Relacionados

[[saga-pattern]] · [[kafka]] · [[rabbitmq]] · [[outbox-pattern]] · [[idempotencia]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-14*
