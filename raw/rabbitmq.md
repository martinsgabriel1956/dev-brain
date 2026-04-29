---
date: 2026-04-14
tags: [tech-mentor, backend, mensageria, rabbitmq, filas]
skill: tech-mentor-backend/references/mensageria
level: intermediário
---

# RabbitMQ

## Contexto

RabbitMQ é um message broker baseado no protocolo AMQP (Advanced Message Queuing Protocol). Diferente do Kafka, que é um log distribuído, o RabbitMQ é um broker tradicional orientado a filas: mensagens são roteadas, consumidas e removidas.

É a escolha certa quando você precisa de roteamento flexível, baixa latência, e semântica de "processar uma vez e remover" — em contraste com o modelo de log persistente do Kafka.

## Como Funciona

### Topologia

```
Producer → Exchange → Binding → Queue → Consumer
```

**Exchange:** recebe mensagens dos producers e as roteia para filas baseado em regras.

**Queue:** buffer persistente de mensagens esperando consumo.

**Binding:** regra que liga uma exchange a uma fila (com routing key ou pattern).

### Tipos de Exchange

```
Direct Exchange — roteamento exato por routing key
  Producer publica com key="order.created"
  Binding: key="order.created" → Queue "order-processor"
  → Apenas essa fila recebe

Fanout Exchange — broadcast para todas as filas ligadas
  Producer publica (sem key)
  Bindings: → Queue A, Queue B, Queue C
  → Todas as filas recebem a mesma mensagem (pub/sub)

Topic Exchange — roteamento com wildcards
  Routing key format: "entity.event.source"
  * = exatamente uma palavra
  # = zero ou mais palavras

  key="order.created.web"  → faz match com "order.#" e "*.created.*"
  key="payment.failed"     → faz match com "payment.#" e "#.failed"

Headers Exchange — roteamento por headers AMQP (raro na prática)
```

```typescript
import amqplib from "amqplib";

const connection = await amqplib.connect("amqp://localhost");
const channel = await connection.createChannel();

// Topic Exchange para roteamento flexível
await channel.assertExchange("events", "topic", { durable: true });

// Filas com bindings diferentes
await channel.assertQueue("order-processor", { durable: true });
await channel.assertQueue("notification-sender", { durable: true });
await channel.assertQueue("audit-logger", { durable: true });

// Order processor: apenas eventos de order
channel.bindQueue("order-processor", "events", "order.#");

// Notification: created events de qualquer entidade
channel.bindQueue("notification-sender", "events", "*.created");

// Audit: tudo
channel.bindQueue("audit-logger", "events", "#");

// Producer — publica com routing key específica
await channel.publish(
  "events",
  "order.created",
  Buffer.from(JSON.stringify({ orderId: "abc", total: 100 })),
  { persistent: true } // sobrevive a restart do broker
);
```

### Consumer com Ack Manual

```typescript
await channel.consume("order-processor", async msg => {
  if (!msg) return;

  try {
    const order = JSON.parse(msg.content.toString());
    await processOrder(order);

    // Ack: remove a mensagem da fila
    channel.ack(msg);

  } catch (error) {
    console.log({ message: "Processing failed", error });

    // nack com requeue=false → vai para DLX em vez de re-enfileirar
    channel.nack(msg, false, false);
  }
}, { noAck: false }); // noAck: false = ack manual obrigatório

// Prefetch: quantas mensagens o consumer pode ter "em mãos" sem ack
// Limita paralelismo e evita que um consumer engole a fila inteira
channel.prefetch(10);
```

### DLX — Dead Letter Exchange

Mensagens que falham vão para uma exchange especial de DLX, permitindo análise e reprocessamento:

```typescript
// Fila principal com DLX configurado
await channel.assertQueue("order-processor", {
  durable: true,
  arguments: {
    "x-dead-letter-exchange": "events.dlx",
    "x-dead-letter-routing-key": "order.failed",
    "x-message-ttl": 30000  // opcional: expira mensagem após 30s → vai para DLX
  }
});

// DLX Exchange e fila de quarentena
await channel.assertExchange("events.dlx", "topic", { durable: true });
await channel.assertQueue("dead-letters", { durable: true });
channel.bindQueue("dead-letters", "events.dlx", "#");

// Consumer de DLQ para inspeção e reprocessamento manual
await channel.consume("dead-letters", msg => {
  if (!msg) return;
  const headers = msg.properties.headers;
  console.log({
    message: "Dead letter received",
    originalQueue: headers["x-death"]?.[0]?.queue,
    reason: headers["x-death"]?.[0]?.reason,
    count: headers["x-death"]?.[0]?.count
  });
  channel.ack(msg);
});
```

### Quorum Queues — Alta Disponibilidade

Classic queues com mirroring foram depreciadas. Quorum queues usam Raft para replicação:

```typescript
await channel.assertQueue("orders-ha", {
  durable: true,
  arguments: {
    "x-queue-type": "quorum",  // Raft-based, alta disponibilidade
    "x-delivery-limit": 3      // máximo de tentativas antes de DLX
  }
});
```

## Trade-offs com Kafka

| Aspecto | RabbitMQ | Kafka |
|---|---|---|
| **Semântica** | Fila — consome e remove | Log — persiste, replayable |
| **Roteamento** | Flexível (exchanges, bindings) | Simples (topic + partition key) |
| **Múltiplos consumers** | Competing consumers (cada msg para 1) | Consumer groups independentes (cada msg para N grupos) |
| **Replay** | Não — mensagem consumida é removida | Sim — qualquer offset |
| **Throughput** | ~100k msg/s | Milhões/s |
| **Latência** | Sub-milissegundo | Milissegundos |
| **Operação** | Moderada | Alta (ZooKeeper/KRaft, partitions) |
| **Casos de uso** | Tasks, RPC, roteamento complexo | Streaming, CDC, event log, auditoria |

## Quando Usar / Quando Evitar

**Usar RabbitMQ quando:**
- Precisar de roteamento flexível (topic/fanout/direct em um só broker)
- Latência muito baixa é crítica (sub-ms)
- Padrão de task queue (worker consome, processa, ack, remove)
- RPC assíncrono (reply-to queue pattern)
- Volume moderado (< 100k msg/s)

**Usar Kafka quando:**
- Múltiplos sistemas independentes precisam consumir o mesmo evento
- Replay e auditoria são necessários
- Throughput > 100k msg/s
- Integração com CDC, data pipeline ou streaming

**Usar SQS/SNS quando:**
- AWS e você quer zero operação de broker
- Não precisa de roteamento complexo

## Conceitos Relacionados

[[kafka]] · [[event-driven-architecture]] · [[outbox-pattern]] · [[saga-pattern]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-14*
