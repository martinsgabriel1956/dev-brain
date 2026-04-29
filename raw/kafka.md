---
date: 2026-04-14
tags: [tech-mentor, backend, mensageria, kafka, streaming]
skill: tech-mentor-backend/references/mensageria
level: avançado
---

# Apache Kafka

## Contexto

Kafka é um log distribuído, imutável e ordenado. Não é uma fila tradicional — é um sistema de streaming onde os eventos ficam armazenados por tempo configurável e múltiplos consumidores independentes podem lê-los a partir de qualquer posição.

Criado no LinkedIn em 2011 para processar trilhões de eventos por dia. Hoje é a espinha dorsal de pipelines de dados e sistemas event-driven em grande escala.

## Como Funciona

### Modelo Mental Fundamental

Pense em Kafka como um **commit log de banco de dados**, mas como sistema de primeira classe:
- Eventos são escritos no final do log (append-only)
- Consumidores controlam sua própria posição de leitura (offset)
- O log pode ser relido quantas vezes quiser

```
Offset:  0        1        2        3        4
         │        │        │        │        │
         ▼        ▼        ▼        ▼        ▼
Topic: [order.created][order.paid][order.shipped][order.delivered][order.created]

Consumer A: lendo offset 3
Consumer B: lendo offset 1  ← independente de A
```

### Topologia

```
Producer → Topic → Partition → Consumer Group → Consumer
```

**Topic:** stream lógico de eventos de um tipo (ex: `orders`, `payments`).

**Partition:** unidade de paralelismo e ordenação. Dentro de uma partition, a ordem é garantida. Entre partitions, não.

```
Topic "orders" com 3 partitions:
  Partition 0: [order#1, order#4, order#7]
  Partition 1: [order#2, order#5, order#8]
  Partition 2: [order#3, order#6, order#9]
```

**Partition Key:** determina em qual partition o evento vai. Eventos com a mesma chave vão para a mesma partition — garantindo ordenação por entidade.

```typescript
// Produzindo com partition key = orderId
await producer.send({
  topic: "orders",
  messages: [{
    key: order.id,   // mesma order sempre vai para a mesma partition
    value: JSON.stringify(order)
  }]
});
```

**Consumer Group:** grupo de consumidores que divide as partitions entre si. Cada partition é atribuída a exatamente um consumidor do grupo.

```
Consumer Group "order-processor" com 3 consumers:
  Consumer 1 → Partition 0
  Consumer 2 → Partition 1
  Consumer 3 → Partition 2
  (paralelismo máximo = número de partitions)
```

**Replicação:** cada partition tem N réplicas em brokers diferentes. Um líder (leader) recebe escritas; os seguidores (ISR - In-Sync Replicas) replicam. Se o líder cai, um ISR assume.

### Configurações Críticas de Produtor

```typescript
const producer = kafka.producer({
  // Quantas réplicas devem confirmar antes de responder "escrito"
  // acks: 0 = fire-and-forget (sem garantia)
  // acks: 1 = apenas líder confirmou (pode perder se líder cai antes de replicar)
  // acks: "all" = todas as ISRs confirmaram (mais seguro)
  acks: "all",

  // Retry automático em falha transitória
  retry: { retries: 5, initialRetryTime: 300 }
});
```

### Configurações Críticas de Consumidor

```typescript
const consumer = kafka.consumer({
  groupId: "order-processor",

  // Onde começar a ler quando não há offset commitado para o grupo
  // "earliest" = do início do log
  // "latest" = somente mensagens novas
  fromBeginning: true
});

await consumer.run({
  // autoCommit: false = você controla quando comita o offset
  // Importante para garantia de processamento (at-least-once)
  eachMessage: async ({ topic, partition, message }) => {
    const order = JSON.parse(message.value.toString());
    await processOrder(order);
    // offset só é comitado quando processOrder resolve
  }
});
```

### DLQ (Dead Letter Queue)

Mensagens que falham repetidamente não devem bloquear o consumo. Mova para um tópico de DLQ para análise posterior.

```typescript
async function processWithDLQ(message: KafkaMessage) {
  try {
    await processOrder(JSON.parse(message.value.toString()));
  } catch (error) {
    console.log({ message: "Moving to DLQ", error, offset: message.offset });
    await producer.send({
      topic: "orders.dlq",
      messages: [{
        key: message.key,
        value: message.value,
        headers: {
          "original-topic": "orders",
          "error": error.message,
          "failed-at": new Date().toISOString()
        }
      }]
    });
  }
}
```

### Schema Registry

Sem Schema Registry, qualquer producer pode quebrar todos os consumers mudando o formato do evento.

```typescript
// Com Schema Registry + Avro: compatibilidade verificada no publish
const { SchemaRegistry } = require("@kafkajs/confluent-schema-registry");

const registry = new SchemaRegistry({ host: "http://schema-registry:8081" });

// Schema evolution: BACKWARD_COMPATIBLE = novo schema lê eventos antigos
// Campo novo deve ter default value
const schemaId = await registry.register({
  type: SchemaType.AVRO,
  schema: JSON.stringify({
    type: "record",
    name: "Order",
    fields: [
      { name: "id", type: "string" },
      { name: "userId", type: "string" },
      { name: "total", type: "double" },
      { name: "currency", type: "string", default: "BRL" } // novo campo com default
    ]
  })
}, { compatibility: "BACKWARD" });
```

### Consumer Groups e Rebalanceamento

Quando um consumer entra ou sai do grupo, ocorre um **rebalanceamento**: as partitions são redistribuídas. Durante o rebalance, o consumo para brevemente.

```typescript
consumer.on(consumer.events.GROUP_JOIN, ({ payload }) => {
  console.log({ message: "Rebalance completed", memberAssignment: payload.memberAssignment });
});
```

Para minimizar rebalances: use `CooperativeStickyAssignor` (rebalance incremental) e configure `session.timeout.ms` adequadamente.

## Trade-offs

| Aspecto | Kafka | RabbitMQ | SQS |
|---|---|---|---|
| **Throughput** | Muito alto (milhões/s) | Alto (100k/s) | Alto (gerenciado) |
| **Retenção** | Configurável (dias/semanas) | Até consumir | 14 dias |
| **Replay** | Sim — qualquer offset | Não | Não |
| **Ordenação** | Por partition | Por fila | Apenas FIFO queue |
| **Múltiplos consumers** | Sim (consumer groups independentes) | Não (competing consumers) | Não |
| **Operação** | Alta complexidade (Zookeeper/KRaft, brokers) | Moderada | Zero (gerenciado) |
| **Latência** | Baixa (ms) | Muito baixa (sub-ms) | Baixa (ms) |

## Quando Usar / Quando Evitar

**Usar Kafka quando:**
- Throughput alto (> 100k eventos/s)
- Múltiplos sistemas independentes precisam consumir o mesmo evento
- Replay de eventos é necessário (auditoria, reprocessamento, Event Sourcing)
- Pipeline de dados com transformações encadeadas (Kafka Streams, Flink)
- CDC (Change Data Capture) com Debezium

**Evitar Kafka quando:**
- Sistema pequeno com < 10k mensagens/dia → SQS ou BullMQ são suficientes e muito mais simples
- Precisar de RPC (request-response) → use gRPC ou REST
- Time sem experiência em operações distribuídas → custo operacional é alto
- Mensagens precisam expirar com TTL dinâmico por mensagem → RabbitMQ é mais flexível

## Conceitos Relacionados

[[outbox-pattern]] · [[event-sourcing]] · [[cqrs]] · [[event-driven-architecture]] · [[schema-registry]] · [[cdc]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-14*
