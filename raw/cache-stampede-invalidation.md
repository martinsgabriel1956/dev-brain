---
date: 2026-04-17
tags: [tech-mentor, cache, performance, redis, sistema-distribuido]
skill: tech-mentor-system-design/references/caching
level: avançado
---

# Cache Stampede e Cache Invalidation

## Cache Stampede (Thundering Herd)

### O Problema
Quando uma chave de cache expira, múltiplas requisições simultâneas percebem o cache miss **ao mesmo tempo** e todas disparam a query ao banco. O banco recebe N queries idênticas em vez de 1.

```
t=0: cache["product:123"] expira
t=1: 500 requisições simultâneas → todas veem cache miss
t=1: 500 queries ao PostgreSQL para o mesmo produto
t=2: banco sobrecarregado → latência aumenta → mais timeouts → mais retries → cascata
```

### Soluções

#### 1. Mutex Lock (mais simples)

```typescript
import { createClient } from "redis";

const redis = createClient();

async function getWithLock<T>(key: string, ttl: number, fetch: () => Promise<T>): Promise<T> {
  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);

  const lockKey = `lock:${key}`;
  const lockAcquired = await redis.set(lockKey, "1", { NX: true, EX: 5 }); // lock de 5s

  if (!lockAcquired) {
    // Outra instância está buscando — aguarda e tenta o cache de novo
    await new Promise(r => setTimeout(r, 100));
    return getWithLock(key, ttl, fetch); // recursão com retry
  }

  try {
    const data = await fetch();
    await redis.setEx(key, ttl, JSON.stringify(data));
    return data;
  } finally {
    await redis.del(lockKey); // libera o lock sempre
  }
}
```

#### 2. Probabilistic Early Expiration (melhor para alta carga)

Em vez de esperar expirar, recalcula o cache **antes** da expiração com probabilidade crescente conforme o TTL se aproxima. Zero locks, zero stampede.

```typescript
// XFetch algorithm (Vattani et al.)
async function getWithEarlyExpiry<T>(
  key: string,
  ttl: number,
  fetch: () => Promise<T>,
  beta = 1.0
): Promise<T> {
  const raw = await redis.get(`data:${key}`);
  const expiryRaw = await redis.get(`expiry:${key}`);

  if (raw && expiryRaw) {
    const expiry = parseFloat(expiryRaw);
    const delta = Date.now() / 1000 - (expiry - ttl); // tempo desde a criação
    const shouldRecompute = expiry - Date.now() / 1000 <= delta * beta * Math.log(Math.random());

    if (!shouldRecompute) return JSON.parse(raw);
  }

  // Recalcula e atualiza o cache
  const data = await fetch();
  const now = Date.now() / 1000;
  await Promise.all([
    redis.setEx(`data:${key}`, ttl, JSON.stringify(data)),
    redis.setEx(`expiry:${key}`, ttl, String(now + ttl))
  ]);
  return data;
}
```

#### 3. Request Collapsing (Stale-While-Revalidate)

Retorna o valor antigo (stale) imediatamente enquanto atualiza o cache em background.

```typescript
const cache = new Map<string, { data: unknown; expiresAt: number; refreshing: boolean }>();

async function getStaleWhileRevalidate<T>(key: string, ttl: number, fetch: () => Promise<T>): Promise<T> {
  const entry = cache.get(key);
  const isExpired = !entry || Date.now() > entry.expiresAt;

  if (!isExpired) return entry!.data as T;

  if (entry && !entry.refreshing) {
    // Retorna stale imediatamente, revalida em background
    entry.refreshing = true;
    fetch().then(data => {
      cache.set(key, { data, expiresAt: Date.now() + ttl * 1000, refreshing: false });
    }).catch(() => {
      if (entry) entry.refreshing = false;
    });
    return entry.data as T;
  }

  // Primeira vez — busca bloqueante
  const data = await fetch();
  cache.set(key, { data, expiresAt: Date.now() + ttl * 1000, refreshing: false });
  return data;
}
```

---

## Cache Invalidation

> *"Só há dois problemas difíceis em Ciência da Computação: invalidação de cache e nomear coisas."* — Phil Karlton

### Estratégias

#### TTL-Based (simples, eventual consistency)
```typescript
await redis.setEx(`product:${id}`, 300, JSON.stringify(product)); // expira em 5 min
// Aceita até 5 min de dado desatualizado
```

#### Event-Driven (consistência mais forte)
```typescript
// Ao atualizar produto, publica evento
await eventBus.publish("product.updated", { productId: id });

// Handler de cache invalida as chaves afetadas
eventBus.on("product.updated", async ({ productId }) => {
  await Promise.all([
    redis.del(`product:${productId}`),
    redis.del(`product-list:*`),         // precisa de SCAN para wildcards
    redis.del(`category:${product.categoryId}`)
  ]);
});
```

#### Versioned Keys (evita invalidação — muda a chave)
```typescript
// Em vez de invalidar, muda a versão da chave
const cacheVersion = await redis.get("product-cache-version") ?? "1";
const cacheKey = `product:${id}:v${cacheVersion}`;

// Para invalidar todo o cache de produtos: bump na versão
await redis.incr("product-cache-version");
// Todas as chaves antigas ficam órfãs e expiram pelo TTL
```

## Conceitos Relacionados
[[cache-strategies]] · [[redis-avancado]] · [[distributed-locks]] · [[graceful-degradation]] · [[rate-limiting]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
