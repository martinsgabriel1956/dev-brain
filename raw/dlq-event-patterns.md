---
date: 2026-04-16
tags: [tech-mentor, backend, mensageria, dlq, at-least-once, exactly-once, event-versioning]
skill: tech-mentor-backend/references/mensageria
level: avançado
---

# DLQ, At-Least-Once vs Exactly-Once e Event Versioning

## Contexto

Mensageria assíncrona introduz três problemas que precisam ser resolvidos explicitamente: o que fazer com mensagens que falham repetidamente (DLQ), quantas vezes uma mensagem pode ser processada (delivery semantics) e como evoluir o schema de eventos sem quebrar consumers (event versioning).

Ignorar qualquer um dos três é receita para perda silenciosa de dados, processamento duplicado ou deploys que quebram consumers em produção.

---

## DLQ — Dead Letter Queue

### O Problema

Sem DLQ, uma mensagem que falha em processamento bloqueia a fila inteira ou é descartada silenciosamente. Ambos os cenários são piores do que tratamento explícito.

### Implementação no Kafka

```typescript
import { Kafka, Consumer, EachMessagePayload } from "kafkajs";

const kafka = new Kafka({ clientId: "order-processor", brokers: ["kafka:9092"] });
const consumer = kafka.consumer({ groupId: "order-processor-group" });
const producer = kafka.producer();

const MAX_RETRIES = 3;
const DLQ_TOPIC = "orders.dlq";
const RETRY_TOPICS = [
  "orders.retry-1",  // delay: 30s
  "orders.retry-2",  // delay: 5min
  "orders.retry-3"   // delay: 30min
];

await consumer.subscribe({ topics: ["orders", ...RETRY_TOPICS] });

await consumer.run({
  eachMessage: async (payload: EachMessagePayload) => {
    const { topic, message } = payload;
    const retryCount = Number(message.headers?.["retry-count"] ?? 0);

    try {
      await processOrder(JSON.parse(message.value!.toString()));

    } catch (error) {
      if (retryCount >= MAX_RETRIES) {
        // Esgotou retries → DLQ com contexto completo
        await producer.send({
          topic: DLQ_TOPIC,
          messages: [{
            key: message.key,
            value: message.value,
            headers: {
              ...message.headers,
              "failed-topic": topic,
              "error-message": (error as Error).message,
              "error-at": new Date().toISOString(),
              "retry-count": String(retryCount)
            }
          }]
        });
        console.log({ message: "Message sent to DLQ", retryCount, error: (error as Error).message });

      } else {
        // Retry com backoff exponencial via tópico separado
        const nextRetryTopic = RETRY_TOPICS[retryCount];
        await producer.send({
          topic: nextRetryTopic,
          messages: [{
            key: message.key,
            value: message.value,
            headers: {
              ...message.headers,
              "retry-count": String(retryCount + 1),
              "original-topic": topic
            }
          }]
        });
      }
    }
  }
});
```

### Reprocessamento da DLQ

```typescript
// Consumer dedicado para reprocessar mensagens da DLQ após correção
const dlqConsumer = kafka.consumer({ groupId: "dlq-reprocessor" });
await dlqConsumer.subscribe({ topics: [DLQ_TOPIC] });

await dlqConsumer.run({
  eachMessage: async ({ message }) => {
    const originalTopic = message.headers?.["failed-topic"]?.toString();

    // Reenviar ao tópico original após correção do bug
    await producer.send({
      topic: originalTopic ?? "orders",
      messages: [{
        key: message.key,
        value: message.value,
        headers: { "reprocessed-from-dlq": "true" }
      }]
    });
  }
});
```

### DLQ no SQS

```typescript
// AWS SQS com DLQ configurada via redrive policy
// maxReceiveCount: após 3 tentativas, vai para DLQ automaticamente

// Terraform:
// resource "aws_sqs_queue" "orders_dlq" { name = "orders-dlq" }
// resource "aws_sqs_queue" "orders" {
//   redrive_policy = jsonencode({
//     deadLetterTargetArn = aws_sqs_queue.orders_dlq.arn
//     maxReceiveCount     = 3
//   })
// }

import { SQSClient, ReceiveMessageCommand, DeleteMessageCommand } from "@aws-sdk/client-sqs";

const sqs = new SQSClient({ region: "us-east-1" });

async function processMessages() {
  const response = await sqs.send(new ReceiveMessageCommand({
    QueueUrl: process.env.SQS_QUEUE_URL,
    MaxNumberOfMessages: 10,
    VisibilityTimeout: 30  // 30s para processar — se não deletar, volta à fila
  }));

  for (const msg of response.Messages ?? []) {
    try {
      await processOrder(JSON.parse(msg.Body!));
      // Sucesso → deletar da fila
      await sqs.send(new DeleteMessageCommand({
        QueueUrl: process.env.SQS_QUEUE_URL!,
        ReceiptHandle: msg.ReceiptHandle!
      }));
    } catch {
      // Não deletar → SQS recoloca na fila
      // Após maxReceiveCount tentativas → vai para DLQ automaticamente
      console.log({ message: "Processing failed, message will retry" });
    }
  }
}
```

---

## At-Least-Once vs Exactly-Once

### Delivery Semantics

| Semântica | O que garante | Quando usar |
|---|---|---|
| **At-most-once** | Entregue 0 ou 1 vez — pode perder | Telemetria, logs onde perda é ok |
| **At-least-once** | Entregue 1+ vezes — pode duplicar | Padrão seguro com idempotência no consumer |
| **Exactly-once** | Entregue exatamente 1 vez | Transações financeiras, muito caro |

### At-Least-Once com Idempotência (O Padrão Correto)

O jeito pragmático: garantir at-least-once na entrega + idempotência no processamento.

```typescript
// Consumer idempotente com Redis para deduplicação
import { createClient } from "redis";

const redis = createClient({ url: process.env.REDIS_URL });

async function processMessageIdempotently(messageId: string, payload: OrderPayload) {
  const dedupKey = `processed:order:${messageId}`;
  const TTL_SECONDS = 86400; // 24h — janela de deduplicação

  // SET NX: só executa se ainda não processou
  const isNew = await redis.set(dedupKey, "1", {
    NX: true,
    EX: TTL_SECONDS
  });

  if (!isNew) {
    console.log({ message: "Duplicate message, skipping", messageId });
    return; // Já processado — ignorar silenciosamente
  }

  // Processa (sabendo que nunca vai duplicar dentro da janela de TTL)
  await processOrder(payload);
}
```

### Exactly-Once no Kafka (Transações)

Kafka suporta exactly-once semantics (EOS) via transações — producer e consumer participam de uma transação atômica:

```typescript
const producer = kafka.producer({
  transactionalId: "order-processor-txn-1",  // ID único por instância
  maxInFlightRequests: 1,
  idempotent: true  // producer idempotente — requerido para EOS
});

await producer.connect();

// Dentro do consumer loop:
const transaction = await producer.transaction();
try {
  // Processar mensagem
  await processOrder(payload);

  // Publicar resultado + commit do offset na mesma transação
  await transaction.send({
    topic: "order-processed",
    messages: [{ value: JSON.stringify({ orderId, status: "processed" }) }]
  });

  // Offset só é commitado se a transação commitar
  await transaction.sendOffsets({
    consumerGroupId: "order-processor-group",
    topics: [{ topic: "orders", partitions: [{ partition, offset: String(offset + 1) }] }]
  });

  await transaction.commit();
} catch (error) {
  await transaction.abort();
  throw error;
}
```

**Custo do EOS:** latência 2-3x maior, complexidade operacional alta. Apenas para casos onde duplicata é inaceitável e idempotência no consumer não é viável.

---

## Event Versioning

### O Problema

Sistemas em produção evoluem. Um consumer em produção pode receber eventos publicados por uma versão antiga do producer (backward compatibility) ou por uma mais nova (forward compatibility).

### Estratégias

**1. Versão no tipo do evento (mais simples)**

```typescript
// Envelope com versão explícita
type OrderCreatedV1 = {
  version: 1;
  orderId: string;
  userId: string;
  total: number;
};

type OrderCreatedV2 = {
  version: 2;
  orderId: string;
  userId: string;
  total: number;
  currency: string;  // campo novo
  items: OrderItem[];  // campo novo
};

type OrderCreatedEvent = OrderCreatedV1 | OrderCreatedV2;

// Consumer — trata todas as versões
async function handleOrderCreated(event: OrderCreatedEvent) {
  if (event.version === 1) {
    return handleV1(event);
  }
  if (event.version === 2) {
    return handleV2(event);
  }
  console.log({ message: "Unknown event version", version: (event as { version: number }).version });
}
```

**2. Upcasting — converter versão antiga para nova no consumer**

```typescript
function upcastOrderCreated(raw: OrderCreatedV1 | OrderCreatedV2): OrderCreatedV2 {
  if (raw.version === 2) return raw;

  // Upcast V1 → V2 com defaults razoáveis
  return {
    version: 2,
    orderId: raw.orderId,
    userId: raw.userId,
    total: raw.total,
    currency: "BRL",  // default retroativo
    items: []  // sem dados históricos — default vazio
  };
}

// Consumer sempre trabalha com V2 — lógica simplificada
async function handleOrderCreated(raw: OrderCreatedV1 | OrderCreatedV2) {
  const event = upcastOrderCreated(raw);
  await processV2Order(event);
}
```

**3. Schema Registry com Avro — backward/forward compatibility**

```
Regras de compatibilidade no Schema Registry:

BACKWARD: consumer da versão nova pode ler eventos da versão antiga
  ✅ Adicionar campo opcional (union com null + default)
  ❌ Remover campo obrigatório
  ❌ Mudar tipo de campo

FORWARD: consumer da versão antiga pode ler eventos da versão nova
  ✅ Remover campo opcional
  ❌ Adicionar campo obrigatório
  ❌ Mudar tipo de campo

FULL: backward + forward — mais seguro, mais restritivo
```

```json
// Avro schema V2 com campo novo backward-compatible
{
  "type": "record",
  "name": "OrderCreated",
  "namespace": "com.empresa.orders",
  "fields": [
    { "name": "orderId", "type": "string" },
    { "name": "userId", "type": "string" },
    { "name": "total", "type": "double" },
    {
      "name": "currency",
      "type": ["null", "string"],
      "default": null  // campo novo como optional com default null → backward-compatible
    }
  ]
}
```

### Event Ordering — Particionamento como Solução

Kafka garante ordem *dentro de uma partição*. Para eventos que precisam de ordem (criação antes de cancelamento de um pedido), usar a mesma partition key:

```typescript
await producer.send({
  topic: "orders",
  messages: [{
    key: orderId,  // mesma key → mesma partição → ordem garantida
    value: JSON.stringify({ type: "OrderCreated", orderId, ... })
  }]
});

await producer.send({
  topic: "orders",
  messages: [{
    key: orderId,  // mesmo orderId → mesma partição → garante after criação
    value: JSON.stringify({ type: "OrderCancelled", orderId, ... })
  }]
});
```

**Armadilha:** partition keys com baixa cardinalidade (ex: status = "pending"/"completed") criam hot partitions — toda escrita vai para 1-2 partições. Usar IDs de alta cardinalidade.

## Conceitos Relacionados

[[kafka]] · [[rabbitmq]] · [[idempotencia]] · [[outbox-pattern]] · [[saga-pattern]] · [[cdc-debezium]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-16*
