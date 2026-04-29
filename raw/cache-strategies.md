---
date: 2026-04-16
tags: [tech-mentor, system-design, cache, redis, cache-aside, write-through, cache-stampede]
skill: tech-mentor-system-design/references/distributed-systems
level: intermediário
---

# Estratégias de Cache — Cache-Aside, Write-Through, Write-Behind e Cache Stampede

## Contexto

Cache resolve dois problemas: latência (dados longe do caller) e throughput (banco não aguenta a carga de leitura). A estratégia de leitura define quando popular o cache (lazy vs eager). A estratégia de escrita define quando invalidar ou atualizar (write-through vs write-behind vs invalidation). Misturar estratégias erradas causa inconsistência silenciosa ou stale data por tempo indefinido.

---

## Cache-Aside (Lazy Loading) — O Padrão Mais Comum

O caller é responsável por ler o cache, fazer miss, ir ao banco e popular o cache.

```typescript
const CACHE_TTL_SECONDS = 3600;  // 1 hora

async function getUserById(userId: string): Promise<User | null> {
  const cacheKey = `user:${userId}`;

  // 1. Tentar cache primeiro
  const cached = await redis.get(cacheKey);
  if (cached) {
    return JSON.parse(cached) as User;
  }

  // 2. Cache miss — ir ao banco
  const user = await prisma.user.findUnique({ where: { id: userId } });

  if (user) {
    // 3. Popular cache para próximas leituras
    await redis.setex(cacheKey, CACHE_TTL_SECONDS, JSON.stringify(user));
  }

  return user;
}

// Invalidação na escrita
async function updateUser(userId: string, data: UpdateUserData): Promise<User> {
  const user = await prisma.user.update({ where: { id: userId }, data });

  // Invalidar cache — próxima leitura fará cache miss e popula com dado novo
  await redis.del(`user:${userId}`);

  return user;
}
```

**Características:** o cache só contém dados que foram lidos ao menos uma vez. Cold start tem 100% de miss rate. Inconsistência pode ocorrer se o banco for atualizado diretamente sem invalidar o cache.

---

## Write-Through — Escrita Sincronizada

Toda escrita vai simultaneamente ao cache e ao banco. Leitura sempre encontra cache quente (se o dado foi escrito recentemente).

```typescript
async function createOrder(data: CreateOrderData): Promise<Order> {
  // 1. Escrever no banco
  const order = await prisma.order.create({ data });

  // 2. Escrever no cache imediatamente
  const cacheKey = `order:${order.id}`;
  await redis.setex(cacheKey, 3600, JSON.stringify(order));

  return order;
}

async function updateOrderStatus(orderId: string, status: OrderStatus): Promise<Order> {
  // 1. Atualizar banco
  const order = await prisma.order.update({
    where: { id: orderId },
    data: { status }
  });

  // 2. Atualizar cache com dado novo — sem precisar invalidar
  const cacheKey = `order:${orderId}`;
  await redis.setex(cacheKey, 3600, JSON.stringify(order));

  return order;
}

async function getOrderById(orderId: string): Promise<Order | null> {
  const cacheKey = `order:${orderId}`;

  const cached = await redis.get(cacheKey);
  if (cached) return JSON.parse(cached) as Order;

  // Miss apenas para dados que nunca foram escritos pelo caminho correto
  const order = await prisma.order.findUnique({ where: { id: orderId } });
  if (order) await redis.setex(cacheKey, 3600, JSON.stringify(order));

  return order;
}
```

**Problema:** escrita dupla — banco + cache em cada operação. Se o cache estiver down, a escrita no cache falha mas o banco foi atualizado → inconsistência. Solução: usar pipeline com retry ou tratar falha no cache como non-blocking.

```typescript
// Escrita não-bloqueante no cache — banco é a fonte de verdade
async function updateUserSafe(userId: string, data: UpdateUserData): Promise<User> {
  const user = await prisma.user.update({ where: { id: userId }, data });

  // Cache update é best-effort — falha silenciosa aceitável aqui
  redis.setex(`user:${userId}`, 3600, JSON.stringify(user)).catch(err => {
    console.log({ message: "Cache update failed (non-critical)", userId, error: err.message });
  });

  return user;
}
```

---

## Write-Behind (Write-Back) — Escrita Assíncrona

Escreve primeiro no cache, retorna sucesso ao caller, e persiste no banco de forma assíncrona. Maximiza throughput de escrita, mas há risco de perda de dados se o cache morrer antes da persistência.

```typescript
import { Queue } from "bullmq";

const persistQueue = new Queue("cache-persist", { connection });

async function updateMetrics(userId: string, delta: Partial<UserMetrics>): Promise<void> {
  const cacheKey = `metrics:${userId}`;

  // 1. Atualizar cache imediatamente (HINCRBY para counters)
  await redis.hincrby(cacheKey, "pageViews", delta.pageViews ?? 0);
  await redis.hincrby(cacheKey, "loginCount", delta.loginCount ?? 0);
  await redis.expire(cacheKey, 3600);

  // 2. Enfileirar persistência assíncrona no banco
  await persistQueue.add(
    "persist-metrics",
    { userId, delta },
    {
      // Deduplicar — se já há job para este userId, não duplicar
      jobId: `metrics-${userId}`,
      delay: 5000  // agregar escritas por 5s antes de persistir
    }
  );
}

// Worker que persiste no banco
const persistWorker = new Worker("cache-persist", async job => {
  const { userId, delta } = job.data;

  await prisma.userMetrics.upsert({
    where: { userId },
    create: { userId, ...delta },
    update: {
      pageViews: { increment: delta.pageViews ?? 0 },
      loginCount: { increment: delta.loginCount ?? 0 }
    }
  });
}, { connection });
```

**Risco real:** Redis restart antes da persistência = perda de dados. Usar apenas para dados onde perda eventual é aceitável (contadores aproximados, analytics, métricas não-críticas).

---

## Cache Stampede — O Problema do Cache Quente que Esfriou

Quando um cache quente expira, múltiplas requests simultâneas fazem cache miss e vão ao banco ao mesmo tempo. Em alta carga, isso pode derrubar o banco.

```
Cache TTL expira: key "product:123"
1000 requests simultâneas → todas fazem cache miss
1000 queries ao banco ao mesmo tempo → banco saturado → latência explode
```

### Solução 1 — Mutex Lock (Sem Thundering Herd)

```typescript
const LOCK_TTL_SECONDS = 10;
const STALE_TTL_SECONDS = 60;  // manter dado stale enquanto outro worker recalcula

async function getProductWithLock(productId: string): Promise<Product | null> {
  const cacheKey = `product:${productId}`;
  const lockKey = `lock:product:${productId}`;

  // 1. Tentar cache primeiro
  const cached = await redis.get(cacheKey);
  if (cached) return JSON.parse(cached) as Product;

  // 2. Cache miss — tentar adquirir lock
  const lockAcquired = await redis.set(lockKey, "1", { NX: true, EX: LOCK_TTL_SECONDS });

  if (lockAcquired) {
    // 3. Sou o único worker buscando este dado agora
    try {
      const product = await prisma.product.findUnique({ where: { id: productId } });
      if (product) {
        await redis.setex(cacheKey, 3600, JSON.stringify(product));
      }
      return product;
    } finally {
      await redis.del(lockKey);
    }
  } else {
    // 4. Outro worker já está buscando — aguardar e tentar o cache novamente
    await new Promise(resolve => setTimeout(resolve, 100));
    const retried = await redis.get(cacheKey);
    return retried ? JSON.parse(retried) as Product : null;
  }
}
```

### Solução 2 — Probabilistic Early Expiration (Sem Lock)

Expirar o cache cedo de forma probabilística — quanto mais próximo da expiração, maior a chance de recalcular. Elegante, sem coordenação.

```typescript
// Algoritmo: XFetch (optimal probabilistic cache stampede prevention)
// P(recalcular) = -β * gap * ln(rand)
// gap = tempo_atual - (expira_em - ttl)

async function getWithEarlyExpiration<T>(
  key: string,
  fetch: () => Promise<T>,
  ttlSeconds: number,
  beta = 1.0  // controla agressividade do early expiration
): Promise<T> {
  const dataKey = `data:${key}`;
  const metaKey = `meta:${key}`;

  const [rawData, rawMeta] = await Promise.all([
    redis.get(dataKey),
    redis.get(metaKey)
  ]);

  if (rawData && rawMeta) {
    const meta = JSON.parse(rawMeta) as { delta: number; expiresAt: number };
    const now = Date.now() / 1000;

    // Calcular se deve recalcular antecipadamente
    const gap = now - (meta.expiresAt - ttlSeconds);
    const shouldRecompute = gap > -beta * meta.delta * Math.log(Math.random());

    if (!shouldRecompute) {
      return JSON.parse(rawData) as T;
    }

    // Probabilisticamente, recalcula antes de expirar
    console.log({ message: "Probabilistic early cache recompute", key });
  }

  // Buscar dado e medir tempo de fetch (para calibrar beta)
  const fetchStart = Date.now();
  const data = await fetch();
  const delta = (Date.now() - fetchStart) / 1000;  // em segundos

  const expiresAt = Date.now() / 1000 + ttlSeconds;

  await Promise.all([
    redis.setex(dataKey, ttlSeconds, JSON.stringify(data)),
    redis.setex(metaKey, ttlSeconds, JSON.stringify({ delta, expiresAt }))
  ]);

  return data;
}

// Uso
const product = await getWithEarlyExpiration(
  `product:${productId}`,
  () => prisma.product.findUniqueOrThrow({ where: { id: productId } }),
  3600
);
```

### Solução 3 — Stale-While-Revalidate

Retornar dado stale imediatamente e atualizar em background:

```typescript
type CacheEntry<T> = {
  data: T;
  expiresAt: number;  // timestamp de expiração do fresh
  staleUntil: number; // timestamp de expiração do stale
};

async function getStaleWhileRevalidate<T>(
  key: string,
  fetch: () => Promise<T>,
  freshSeconds: number,   // tempo com dado fresh
  staleSeconds: number    // tempo extra com dado stale (enquanto revalida)
): Promise<T> {
  const raw = await redis.get(key);

  if (raw) {
    const entry = JSON.parse(raw) as CacheEntry<T>;
    const now = Date.now() / 1000;

    if (now < entry.expiresAt) {
      // Dado fresh — retornar diretamente
      return entry.data;
    }

    if (now < entry.staleUntil) {
      // Dado stale mas ainda aceitável — retornar e revalidar em background
      setImmediate(async () => {
        const fresh = await fetch();
        const newEntry: CacheEntry<T> = {
          data: fresh,
          expiresAt: Date.now() / 1000 + freshSeconds,
          staleUntil: Date.now() / 1000 + freshSeconds + staleSeconds
        };
        await redis.setex(key, freshSeconds + staleSeconds, JSON.stringify(newEntry));
      });
      return entry.data;
    }
  }

  // Cache miss completo — buscar e popular
  const data = await fetch();
  const entry: CacheEntry<T> = {
    data,
    expiresAt: Date.now() / 1000 + freshSeconds,
    staleUntil: Date.now() / 1000 + freshSeconds + staleSeconds
  };
  await redis.setex(key, freshSeconds + staleSeconds, JSON.stringify(entry));
  return data;
}
```

---

## Cache Invalidation — Estratégias

```typescript
// 1. TTL-based — o mais simples, aceitar staleness até o TTL
await redis.setex(key, 3600, value);

// 2. Write-through invalidation — invalidar na escrita
await redis.del(`product:${productId}`);
await prisma.product.update({ where: { id: productId }, data });

// 3. Event-driven — invalidar via evento do banco (CDC)
// Debezium captura UPDATE no products table → publica no Kafka
// Consumer do Kafka invalida a cache key correspondente
async function onProductUpdated(event: ProductUpdatedEvent) {
  await redis.del(`product:${event.after.id}`);
  // Se categoria mudou, invalidar cache de listagem também
  if (event.before.categoryId !== event.after.categoryId) {
    await redis.del(`products:category:${event.before.categoryId}`);
    await redis.del(`products:category:${event.after.categoryId}`);
  }
}

// 4. Versioned keys — nunca invalidar, sempre criar nova key
function buildVersionedKey(entityId: string, version: number): string {
  return `product:${entityId}:v${version}`;
}
// Ao atualizar: incrementar versão e deixar a antiga expirar
```

---

## Trade-offs

| Estratégia | Consistência | Performance de Leitura | Performance de Escrita | Complexidade |
|---|---|---|---|---|
| **Cache-Aside** | Eventual (TTL) | Alta (hit) | Normal | Baixa |
| **Write-Through** | Forte | Alta | Dobrado | Média |
| **Write-Behind** | Eventual | Alta | Muito alta | Alta |
| **Read-Through** | Eventual (TTL) | Alta | Normal | Média (lógica no cache) |

## Quando Usar / Quando Evitar

**Cache-Aside:** padrão default. Dados de leitura intensiva com atualizações moderadas. Perfis de usuário, produtos, configurações.

**Write-Through:** dados financeiros, pedidos — onde leitura após escrita deve ser sempre consistente. Custo: escrita dupla.

**Write-Behind:** contadores de alta frequência (views, likes, analytics), dados onde perda de alguns updates é aceitável. Não usar para dados transacionais.

**Cache Stampede Prevention:** obrigatório em qualquer cache com TTL de itens populares. Escolher entre mutex (menor carga no banco, latência sob stampede) ou early expiration (zero lock, melhor para requests muito rápidos).

**Stale-While-Revalidate:** APIs de leitura onde latência P50 importa mais que freshness. Padrão do HTTP `Cache-Control: stale-while-revalidate`.

## Conceitos Relacionados

[[redis]] · [[read-replicas-connection-pooling]] · [[distributed-locks]] · [[cdc-debezium]] · [[consistent-hashing]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-16*
