---
date: 2026-04-17
tags: [tech-mentor, backend, banco, redis, streams, redlock, eviction, pub-sub]
skill: tech-mentor-backend/references/banco
level: avançado
---

# Redis Avançado — Streams, Redlock, Eviction e Módulos

## Contexto

Redis vai além de cache key-value. Redis Streams é um log de eventos imutável com consumer groups — essencialmente Kafka leve sem broker externo. Redlock resolve distributed locking sem single point of failure. Eviction policies determinam o comportamento sob memória saturada. Entender essas camadas é essencial para usar Redis como infrastructure component, não apenas como cache.

---

## Redis Streams — Log de Eventos Persistente

Streams são append-only logs com consumer groups — cada mensagem é entregue a apenas um consumer no grupo (similar ao Kafka consumer groups).

```typescript
import { Redis } from "ioredis";

const redis = new Redis(process.env.REDIS_URL!);

// Produzir evento — XADD adiciona ao stream, retorna ID "timestamp-sequence"
async function publishEvent(streamKey: string, event: Record<string, string>): Promise<string> {
  // "*" = auto-gerar ID baseado em timestamp
  const eventId = await redis.xadd(streamKey, "*", ...Object.entries(event).flat());
  return eventId!;
}

// Consumer Group — criar grupo para processar eventos
async function createConsumerGroup(streamKey: string, groupName: string): Promise<void> {
  try {
    // "$" = só mensagens novas; "0" = desde o início do stream
    await redis.xgroup("CREATE", streamKey, groupName, "$", "MKSTREAM");
  } catch (err: unknown) {
    // BUSYGROUP = grupo já existe — ignorar
    if (err instanceof Error && !err.message.includes("BUSYGROUP")) throw err;
  }
}

// Consumer — ler e processar mensagens
async function consumeEvents(
  streamKey: string,
  groupName: string,
  consumerName: string,
  batchSize = 10
): Promise<void> {
  while (true) {
    // ">" = mensagens não entregues a nenhum consumer ainda
    const results = await redis.xreadgroup(
      "GROUP", groupName, consumerName,
      "COUNT", batchSize,
      "BLOCK", 5000,  // aguardar até 5s por novas mensagens
      "STREAMS", streamKey, ">"
    ) as [string, [string, string[]][]][] | null;

    if (!results) continue;  // timeout — sem mensagens novas

    for (const [, messages] of results) {
      for (const [messageId, fields] of messages) {
        // Converter array de fields para objeto
        const data: Record<string, string> = {};
        for (let i = 0; i < fields.length; i += 2) {
          data[fields[i]] = fields[i + 1];
        }

        try {
          await processEvent(data);
          // ACK — confirmar processamento para remover da PEL (Pending Entry List)
          await redis.xack(streamKey, groupName, messageId);
        } catch (error) {
          // Sem ACK = mensagem fica na PEL para reprocessamento
          console.log({ message: "Event processing failed", messageId, error });
        }
      }
    }
  }
}

async function processEvent(data: Record<string, string>): Promise<void> {
  console.log({ message: "Processing event", data });
}

// Reprocessar mensagens travadas (PEL com mais de 30s sem ACK)
async function reclaimStalePendingMessages(
  streamKey: string,
  groupName: string,
  consumerName: string,
  minIdleMs = 30_000
): Promise<void> {
  const pending = await redis.xautoclaim(
    streamKey, groupName, consumerName,
    minIdleMs, "0-0",  // desde o início da PEL
    "COUNT", "10"
  ) as [string, [string, string[]][], string[]];

  const [, messages] = pending;

  for (const [messageId, fields] of messages) {
    const data: Record<string, string> = {};
    for (let i = 0; i < fields.length; i += 2) {
      data[fields[i]] = fields[i + 1];
    }

    console.log({ message: "Reclaiming stale message", messageId });
    await processEvent(data);
    await redis.xack(streamKey, groupName, messageId);
  }
}

// Uso
await publishEvent("orders:events", { type: "order.created", orderId: "uuid", total: "149.90" });
await createConsumerGroup("orders:events", "order-processor");
// Em cada worker:
await consumeEvents("orders:events", "order-processor", `worker-${process.pid}`);
```

### Stream vs Pub/Sub vs List

```
Pub/Sub:  fire-and-forget, sem persistência, sem consumer groups → notificações efêmeras
List:     FIFO simples, sem replay, sem grupos → job queue simples com BLPOP/BRPOP
Streams:  log persistente, consumer groups, replay, PEL, ACK → event bus leve, audit log
```

---

## Redlock — Distributed Lock Sem SPOF

Um único Redis como lock é single point of failure. Redlock distribui o lock entre N instâncias independentes — require maioria (N/2 + 1) para adquirir.

```typescript
import Redlock, { Lock } from "redlock";
import { Redis } from "ioredis";

// 5 instâncias independentes (não replicas — cada uma tem seu próprio estado)
const redisNodes = [
  new Redis({ host: "redis-1", port: 6379 }),
  new Redis({ host: "redis-2", port: 6379 }),
  new Redis({ host: "redis-3", port: 6379 }),
  new Redis({ host: "redis-4", port: 6379 }),
  new Redis({ host: "redis-5", port: 6379 })
];

const redlock = new Redlock(redisNodes, {
  // Clock drift factor — compensar diferença entre clocks
  driftFactor: 0.01,
  // Tentativas de adquirir o lock
  retryCount: 3,
  retryDelay: 200,   // ms entre tentativas
  retryJitter: 100   // ms de jitter para evitar thundering herd
});

// Usar lock com auto-release via callback
async function processOrderExclusive(orderId: string): Promise<void> {
  const lockKey = `lock:order:${orderId}`;
  const lockTtl = 30_000;  // 30s — tempo máximo de processamento

  let lock: Lock;
  try {
    lock = await redlock.acquire([lockKey], lockTtl);
  } catch (err) {
    // Lock não adquirido — outro worker está processando
    throw new Error(`Could not acquire lock for order ${orderId}`);
  }

  try {
    await processOrder(orderId);

    // Estender lock se processamento demorar mais que esperado
    lock = await lock.extend(lockTtl);
  } finally {
    // Sempre liberar o lock ao terminar
    await lock.release();
  }
}

async function processOrder(orderId: string): Promise<void> {
  console.log({ message: "Processing order exclusively", orderId });
}

// Alternativa simples — Redis single node (sem Redlock) para casos não-críticos
async function simpleDistributedLock(
  redis: Redis,
  key: string,
  ttlMs: number
): Promise<{ acquired: boolean; release: () => Promise<void> }> {
  const lockId = crypto.randomUUID();
  // SET NX = só setar se não existir — atômico
  const acquired = await redis.set(key, lockId, "PX", ttlMs, "NX") === "OK";

  return {
    acquired,
    release: async () => {
      // Lua script — liberar APENAS se o lock ainda é nosso
      const script = `
        if redis.call("GET", KEYS[1]) == ARGV[1] then
          return redis.call("DEL", KEYS[1])
        else
          return 0
        end
      `;
      await redis.eval(script, 1, key, lockId);
    }
  };
}
```

---

## Eviction Policies — Comportamento sob Pressão de Memória

Quando Redis atinge `maxmemory`, a eviction policy determina o que descartar:

```
noeviction       → rejeitar escritas com erro (default) — bom para dados críticos
allkeys-lru      → descartar qualquer chave pela LRU — bom para cache puro
volatile-lru     → descartar apenas chaves com TTL, pela LRU — bom para cache + dados persistentes
allkeys-lfu      → LFU (Least Frequently Used) — melhor para distribuição não-uniforme (Zipf)
volatile-lfu     → LFU apenas em chaves com TTL
allkeys-random   → random — evitar (imprevisível)
volatile-random  → random apenas em chaves com TTL
volatile-ttl     → descartar chaves com TTL menor primeiro
```

```typescript
// Configuração recomendada para cache puro
// redis.conf:
// maxmemory 2gb
// maxmemory-policy allkeys-lru
// maxmemory-samples 10  (amostras para aproximar LRU — padrão 5, mais samples = mais preciso)

// Configuração para Redis com dados mistos (cache + dados persistentes sem TTL)
// maxmemory-policy volatile-lru
// → dados sem TTL (críticos) nunca são evictados
// → dados com TTL (cache) são evictados quando necessário

// Monitorar evictions para detectar saturação
async function getEvictionStats(redis: Redis): Promise<void> {
  const info = await redis.info("stats");
  const evictions = info.match(/evicted_keys:(\d+)/)?.[1];
  const hits = info.match(/keyspace_hits:(\d+)/)?.[1];
  const misses = info.match(/keyspace_misses:(\d+)/)?.[1];

  const hitRate = parseInt(hits ?? "0") / (parseInt(hits ?? "0") + parseInt(misses ?? "1"));

  console.log({
    evictedKeys: parseInt(evictions ?? "0"),
    hitRate: `${(hitRate * 100).toFixed(1)}%`
  });

  // Hit rate < 80% → cache muito pequeno ou TTLs muito curtos
  // evicted_keys crescendo → pressão de memória — aumentar maxmemory ou reduzir dados
}
```

---

## Pub/Sub — Broadcast em Tempo Real

```typescript
// Publisher
async function publishNotification(channel: string, payload: Record<string, unknown>): Promise<void> {
  const publisher = new Redis(process.env.REDIS_URL!);
  await publisher.publish(channel, JSON.stringify(payload));
  await publisher.quit();
}

// Subscriber — conexão dedicada (não pode fazer outros comandos)
async function subscribeToChannel(channel: string): Promise<void> {
  const subscriber = new Redis(process.env.REDIS_URL!);

  subscriber.on("message", (ch, message) => {
    if (ch !== channel) return;
    const payload = JSON.parse(message);
    console.log({ message: "Received notification", payload });
  });

  await subscriber.subscribe(channel);

  // Pattern subscribe — "notifications:*" captura qualquer canal com esse prefixo
  await subscriber.psubscribe("notifications:*");
  subscriber.on("pmessage", (pattern, ch, message) => {
    console.log({ pattern, channel: ch, message: JSON.parse(message) });
  });
}

// ATENÇÃO: Pub/Sub não tem persistência — se subscriber cair, perde mensagens
// Para entrega garantida: Redis Streams ou BullMQ
```

---

## Módulos Redis

```typescript
// RedisJSON — documentos JSON nativos com path queries
// Instalar: docker run redis/redis-stack

// Operações básicas
await redis.call("JSON.SET", "user:123", "$", JSON.stringify({ name: "Alice", age: 30 }));
const name = await redis.call("JSON.GET", "user:123", "$.name");  // ["Alice"]
await redis.call("JSON.NUMINCRBY", "user:123", "$.age", 1);       // incrementar campo numérico

// RediSearch — busca full-text e vetorial sobre JSON/Hash
// CREATE INDEX
await redis.call("FT.CREATE", "idx:users",
  "ON", "JSON",
  "PREFIX", "1", "user:",
  "SCHEMA",
  "$.name", "AS", "name", "TEXT", "WEIGHT", "5.0",
  "$.age", "AS", "age", "NUMERIC", "SORTABLE"
);

// SEARCH — busca com filtros
const results = await redis.call("FT.SEARCH", "idx:users",
  "@name:Alice @age:[25 +inf]",
  "LIMIT", "0", "10"
);

// RedisBloom — Bloom Filter para deduplicação
await redis.call("BF.RESERVE", "seen:emails", "0.01", "1000000");  // 1% false positive rate, 1M itens
const isSeen = await redis.call("BF.EXISTS", "seen:emails", "user@example.com");
await redis.call("BF.ADD", "seen:emails", "user@example.com");

// HyperLogLog — contagem aproximada de distintos com memória O(1)
await redis.pfadd("unique:visitors", "user-1", "user-2", "user-3");
const count = await redis.pfcount("unique:visitors");  // ~3 (99.81% precisão)
```

---

## Trade-offs

| Feature | Vantagem | Limitação |
|---|---|---|
| **Streams** | Persistente, consumer groups, replay | Sem compaction nativa (vs Kafka) |
| **Redlock** | Sem SPOF, fault-tolerant | Requer 5 instâncias; clock drift é risco real |
| **Pub/Sub** | Latência sub-ms, simples | Sem persistência — mensagens perdidas em crash |
| **allkeys-lru** | Cache puro simples | Pode evictar dados "quentes" recentemente acessados menos |
| **allkeys-lfu** | Melhor para Zipf distribution | Comportamento ruim em padrões de acesso uniformes |

## Quando Usar / Quando Evitar

**Redis Streams sobre Pub/Sub:** quando a entrega garantida importa — eventos de domínio, audit log, integração entre serviços com processamento assíncrono.

**Redis Streams sobre Kafka:** volumes < 1M msg/dia, equipes sem expertise em Kafka, infra simples.

**Redlock:** apenas quando o custo de lock duplicado é alto (processamento financeiro, charge). Para locks de baixo risco, single-node com SET NX é suficiente.

**volatile-lru sobre allkeys-lru:** quando Redis mistura cache (com TTL) e dados persistentes críticos (sem TTL) — evita que dados críticos sejam evictados.

**Evitar Pub/Sub:** qualquer cenário onde entrega garantida importa — usar Streams ou Kafka.

## Conceitos Relacionados

[[cache-strategies]] · [[distributed-locks]] · [[background-jobs]] · [[kafka]] · [[mongodb]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
