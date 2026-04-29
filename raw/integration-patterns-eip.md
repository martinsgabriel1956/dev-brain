---
date: 2026-04-17
tags: [tech-mentor, arquitetura, principios, mensageria, integracao]
skill: tech-mentor-backend/references/messaging-patterns
level: avançado
---

# Integration Patterns (EIP)

## Contexto
*Enterprise Integration Patterns* (Hohpe & Woolf, 2003) é o catálogo de referência para sistemas que integram via mensageria. Três padrões são especialmente relevantes em arquitetura moderna: **Claim Check**, **Competing Consumers** e **Routing Slip**.

## Claim Check

**Problema:** mensagens grandes (PDFs, imagens, payloads > 1MB) sobrecarregam o broker. Kafka tem limite default de 1MB por mensagem; aumentar esse limite degrada performance.

**Solução:** armazene o payload grande em Object Storage (S3, GCS) e publique no broker apenas um **ticket** com a referência (claim check).

```
Producer                Broker             Consumer
   │                      │                   │
   │──payload(10MB)──►S3   │                   │
   │◄──── URL ────────────│                   │
   │──{ claimCheckUrl }──►│                   │
   │                      │──{ url }─────────►│
   │                      │                   │──GET url──►S3
   │                      │                   │◄─payload──────
```

```typescript
// Producer
async function publishWithClaimCheck(payload: Buffer, topic: string) {
  const key = `events/${randomUUID()}.json`;
  await s3.putObject({ Bucket: BUCKET, Key: key, Body: payload });

  await kafka.send({
    topic,
    messages: [{ value: JSON.stringify({ claimCheckKey: key }) }]
  });
}

// Consumer
async function consumeWithClaimCheck(message: KafkaMessage) {
  const { claimCheckKey } = JSON.parse(message.value!.toString());
  const response = await s3.getObject({ Bucket: BUCKET, Key: claimCheckKey });
  const payload = await response.Body!.transformToString();
  return JSON.parse(payload);
}
```

## Competing Consumers

**Problema:** um único consumer não consegue processar a fila na velocidade de publicação — throughput limitado.

**Solução:** múltiplos consumers competem pelas mesmas mensagens. O broker (ou DB com SKIP LOCKED) garante que cada mensagem é processada por apenas um consumer.

```
         ┌─────────────────────┐
Queue    │ msg1 msg2 msg3 msg4 │
         └─────────────────────┘
               │   │   │
           ┌───┘   │   └───┐
           ▼       ▼       ▼
      Consumer1 Consumer2 Consumer3
```

No Kafka, isso é implementado via **Consumer Groups**: partições são distribuídas entre consumers do mesmo grupo. Máximo de paralelismo = número de partições.

```typescript
// Kafka — consumer group com 3 instâncias processando em paralelo
const consumer = kafka.consumer({ groupId: "order-processor" });
await consumer.subscribe({ topic: "orders", fromBeginning: false });

await consumer.run({
  partitionsConsumedConcurrently: 3, // até 3 partições por instância
  eachMessage: async ({ message }) => {
    await processOrder(JSON.parse(message.value!.toString()));
  }
});
```

**Regra crítica:** mensagens dentro da mesma partição são ordenadas e processadas sequencialmente. Para ordering by entity (ex: todos os eventos do `orderId` na mesma partição), use o `orderId` como Kafka message key.

## Routing Slip

**Problema:** o caminho de processamento de uma mensagem varia conforme seu conteúdo — nem todas as mensagens passam pelos mesmos steps.

**Solução:** a mensagem carrega seu próprio itinerário (routing slip). Cada step lê o próximo destino do slip e encaminha após processar.

```
Message = {
  payload: { ... },
  routingSlip: ["validate", "enrich", "notify", "archive"]
}

validate → enrich → notify → archive → done
```

```typescript
type RoutingSlip = string[];

type Message<T> = {
  payload: T;
  routingSlip: RoutingSlip;
  currentStep: number;
};

async function process<T>(message: Message<T>, handlers: Record<string, (payload: T) => Promise<T>>) {
  const stepName = message.routingSlip[message.currentStep];
  if (!stepName) return message.payload; // fim do slip

  const handler = handlers[stepName];
  const updatedPayload = await handler(message.payload);

  return process(
    { ...message, payload: updatedPayload, currentStep: message.currentStep + 1 },
    handlers
  );
}

// Uso
const result = await process(
  {
    payload: order,
    routingSlip: ["validate", "enrich", "audit"],
    currentStep: 0
  },
  { validate, enrich, audit }
);
```

## Trade-offs Comparativos

| Pattern | Resolve | Custo |
|---|---|---|
| Claim Check | Mensagens grandes no broker | Latência extra por round-trip ao storage |
| Competing Consumers | Throughput limitado de processamento | Ordering dentro da partição deve ser considerado |
| Routing Slip | Fluxo variável sem orquestrador central | Slip corrompido = processamento errado; difícil de debugar |

## Conceitos Relacionados
[[kafka]] · [[rabbitmq]] · [[dlq-event-patterns]] · [[outbox-pattern]] · [[saga-pattern]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
