---
date: 2026-04-17
tags: [tech-mentor, mensageria, nats, streaming, backend]
skill: tech-mentor-backend/references/messaging
level: intermediário
---

# NATS e NATS JetStream

## Contexto
**NATS** é um sistema de mensageria leve, de alto throughput e baixíssima latência, escrito em Go. O core NATS é pub/sub at-most-once — sem persistência. **JetStream** é a extensão de streaming persistente que adiciona at-least-once e exactly-once delivery, consumers duráveis e KV Store.

Onde se posiciona: mais simples que Kafka (sem partições complexas), mais rápido que RabbitMQ em pub/sub puro, com footprint mínimo (~20MB). Comum em edge computing, IoT, e sistemas que precisam de mensageria sem a complexidade operacional do Kafka.

## NATS Core — Pub/Sub

```typescript
import { connect, StringCodec } from "nats";

const nc = await connect({ servers: "nats://localhost:4222" });
const sc = StringCodec();

// Publisher
await nc.publish("orders.created", sc.encode(JSON.stringify({ orderId: "123" })));

// Subscriber — at-most-once (sem ACK, sem persistência)
const sub = nc.subscribe("orders.*");
for await (const msg of sub) {
  const data = JSON.parse(sc.decode(msg.data));
  console.log({ message: "Received", subject: msg.subject, data });
}

// Request-Reply — padrão RPC sobre NATS
const response = await nc.request("user.lookup", sc.encode("user-123"), { timeout: 3000 });
const user = JSON.parse(sc.decode(response.data));
```

**Subjects** usam hierarquia com wildcards:
- `orders.created` — subject específico
- `orders.*` — qualquer sub-nível único (`orders.created`, `orders.updated`)
- `orders.>` — qualquer sub-nível profundo (`orders.created`, `orders.us.east.created`)

## JetStream — Streaming Persistente

```typescript
import { connect, StringCodec, AckPolicy, DeliverPolicy } from "nats";

const nc = await connect({ servers: "nats://localhost:4222" });
const js = nc.jetstream();
const jsm = await nc.jetstreamManager();
const sc = StringCodec();

// Criar Stream (equivalente ao tópico Kafka)
await jsm.streams.add({
  name: "ORDERS",
  subjects: ["orders.>"],
  max_age: 7 * 24 * 60 * 60 * 1e9, // 7 dias em nanosegundos
  storage: "file",  // ou "memory"
  num_replicas: 3
});

// Publicar com garantia de entrega
const pubAck = await js.publish("orders.created", sc.encode(JSON.stringify({ orderId: "456" })));
console.log({ message: "Published", stream: pubAck.stream, seq: pubAck.seq });

// Consumer durável — at-least-once com ACK manual
const consumer = await js.consumers.get("ORDERS", "order-processor");
// ou criar:
await jsm.consumers.add("ORDERS", {
  durable_name: "order-processor",
  ack_policy: AckPolicy.Explicit,   // ACK manual
  deliver_policy: DeliverPolicy.All // desde o início
});

const messages = await consumer.fetch({ max_messages: 10 });
for await (const msg of messages) {
  try {
    const order = JSON.parse(sc.decode(msg.data));
    await processOrder(order);
    msg.ack();                   // confirma processamento
  } catch (err) {
    msg.nak();                   // recoloca na fila para reprocessar
    // ou: msg.term() para descartar permanentemente
  }
}
```

## KV Store — Redis-like sobre JetStream

```typescript
// KV Store persistente e replicado
const kv = await js.views.kv("user-sessions", {
  ttl: 30 * 60 * 1e9,  // 30 minutos
  replicas: 3
});

await kv.put("session:abc123", sc.encode(JSON.stringify({ userId: "1", role: "admin" })));

const entry = await kv.get("session:abc123");
const session = JSON.parse(sc.decode(entry!.value));

// Watch para mudanças em tempo real
const watcher = await kv.watch({ key: "session:*" });
for await (const entry of watcher) {
  console.log({ message: "Session changed", key: entry.key, op: entry.operation });
}
```

## Comparativo NATS vs. Kafka vs. RabbitMQ

| Aspecto | NATS Core | NATS JetStream | Kafka | RabbitMQ |
|---|---|---|---|---|
| Persistência | Não | Sim | Sim | Sim |
| Throughput | ~10M msg/s | ~1M msg/s | ~1M msg/s | ~100k msg/s |
| Latência | < 1ms | 1-5ms | 5-15ms | 1-5ms |
| Complexidade operacional | Muito baixa | Baixa | Alta | Média |
| Particionamento | Não | Não (por consumer) | Sim (explícito) | Não |
| Footprint | 20MB | 20MB | JVM + ZK/KRaft | ~150MB |
| Casos de uso | IoT, edge, microserviços | Streaming leve | Big data, event log | Routing complexo |

## Quando Usar / Quando Evitar

**Usar quando:**
- Precisa de mensageria leve sem overhead operacional do Kafka
- Edge computing, IoT, ou sistemas embarcados
- Request-reply (RPC) entre microsserviços — NATS tem suporte nativo
- KV distribuído simples sem Redis

**Evitar quando:**
- Precisa de particionamento explícito por chave (ordering garantida por entidade) → Kafka
- Routing complexo com exchanges e bindings → RabbitMQ
- Ecosistema já usa Kafka — migrar por conta do NATS raramente vale

## Conceitos Relacionados
[[kafka]] · [[rabbitmq]] · [[dlq-event-patterns]] · [[background-jobs]] · [[redis-avancado]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
