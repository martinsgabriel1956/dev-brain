---
type: concept
title: "Cache Stampede"
aliases: ["cache stampede", "cache stampede prevention", "dog-piling", "thundering herd cache"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [cache-stampede, thundering-herd, cache, probabilistic-expiration, request-coalescing]
skill: tech-mentor-system-design
status: stable
---

## Definição

Cache stampede (também chamado dog-piling) é quando múltiplos callers detectam um cache miss simultaneamente e todos vão ao origin (banco, API) ao mesmo tempo para reconstruir o dado.

É uma instância específica do [[concepts/thundering-herd]] aplicada a caches.

## Cenário

```
Cache TTL = 10 minutos
10.000 usuários ativos

10:00:00 — cache expira
10:00:00 — 10.000 requests detectam miss simultaneamente
10:00:00 — 10.000 queries no banco ao mesmo tempo
10:00:00 — banco passa de 200 req/s para 10.000 req/s
10:00:01 — banco timeout / OOM / restart
```

## Técnicas de prevenção

### Probabilistic Early Expiration

Em vez de expirar no TTL exato, cada caller calcula com probabilidade crescente se deve revalidar antes do TTL.

```typescript
function shouldRevalidate(ttlRemaining: number, delta: number, beta = 1): boolean {
  // XFetch algorithm: probabilidade cresce conforme TTL diminui
  const rand = -delta * beta * Math.log(Math.random());
  return rand >= ttlRemaining;
}

async function getWithProbabilisticExpiry(key: string) {
  const cached = await redis.get(key);
  if (!cached) return rebuild(key);

  const { value, computedAt, ttl } = JSON.parse(cached);
  const delta = Date.now() - computedAt; // tempo de rebuild estimado
  const ttlRemaining = ttl - (Date.now() - computedAt);

  if (shouldRevalidate(ttlRemaining, delta)) {
    // revalida antes do TTL — apenas um caller estatisticamente
    return rebuild(key);
  }

  return value;
}
```

### Request Coalescing (Single Rebuilder)

Apenas um caller reconstrói o cache. Os outros aguardam o resultado.

```typescript
const rebuilding = new Map<string, Promise<unknown>>();

async function getWithCoalescing(key: string) {
  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);

  // já tem um rebuild em andamento para esta key?
  if (rebuilding.has(key)) {
    return rebuilding.get(key);
  }

  const promise = rebuild(key).then(value => {
    redis.setex(key, TTL, JSON.stringify(value));
    rebuilding.delete(key);
    return value;
  });

  rebuilding.set(key, promise);
  return promise;
}
```

### Stale-While-Revalidate

Servir o dado stale enquanto o rebuild acontece em background.

```typescript
async function getStaleWhileRevalidate(key: string) {
  const cached = await redis.get(key);

  if (cached) {
    const { value, expiresAt } = JSON.parse(cached);

    if (Date.now() > expiresAt) {
      // stale — rebuild em background, serve o stale agora
      rebuild(key).then(fresh => redis.setex(key, TTL, JSON.stringify({
        value: fresh,
        expiresAt: Date.now() + TTL * 1000
      })));
    }

    return value;
  }

  return rebuild(key);
}
```

## Relação com outros conceitos

- [[concepts/thundering-herd]] — cache stampede é uma instância de thundering herd
- [[concepts/cache-hot-path]] — cache em camadas reduz a probabilidade de stampede no layer mais baixo
- [[concepts/back-pressure]] — back pressure controla fluxo produtor→consumidor; stampede é o inverso

## Key Sources

- [[sources/conceitos-que-ninguem-ensina]]
