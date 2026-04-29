---
date: 2026-03-27
tags: [tech-mentor, system-design, infraestrutura, cache, redis, performance]
skill: tech-mentor-system-design/references/system-design-cache-lock-queue.md
level: fundamento
---

# Cache

## Contexto

Cache guarda o resultado de operações caras em armazenamento rápido para não refazê-las. É a ferramenta de performance mais impactante — um banco respondendo em 10ms pode virar 0.1ms com cache na frente. A diferença existe porque banco faz I/O em disco (100μs) e Redis fica inteiramente em RAM (100ns) — 1000x mais rápido.

## Como Funciona

### Os Três Padrões Fundamentais

**Cache-Aside** (lazy loading — o mais comum):

```typescript
async function getUser(id: string): Promise<User> {
  const cached = await redis.get(`user:${id}`);
  if (cached) return JSON.parse(cached);

  const user = await db.user.findUnique({ where: { id } });
  if (!user) throw new NotFoundError();

  await redis.set(`user:${id}`, JSON.stringify(user), "EX", 300);
  return user;
}
```

Cache só é populado quando há demanda — dados raramente acessados não ocupam memória. A aplicação gerencia explicitamente.

**Write-Through** — escreve no cache e no banco na mesma operação:

```typescript
async function updateUser(id: string, data: UpdateUserDTO): Promise<User> {
  const user = await db.user.update({ where: { id }, data });
  await redis.set(`user:${id}`, JSON.stringify(user), "EX", 300);
  return user;
}
```

Cache sempre tem o dado mais recente. Custo: toda escrita passa pelo cache.

**Write-Behind** — escreve no cache, persiste no banco de forma assíncrona:

```
App → Cache → retorna para o cliente
         ↓
     [async worker]
         ↓
      Banco de dados
```

Write mais rápido. Risco: se o cache cair antes de persistir, os dados se perdem.

## Código de Referência

### Invalidação

**TTL:**
```typescript
redis.set(`user:${id}`, data, "EX", 300); // expira em 5 minutos
```

**Invalidação explícita:**
```typescript
async function updateUser(id: string, data: UpdateUserDTO) {
  await db.user.update({ where: { id }, data });
  await redis.del(`user:${id}`);
}
```

**Cache Tags — invalida grupos de chaves:**
```typescript
// Popular com tag
await redis.set(`user:${id}:profile`, profileData, "EX", 300);
await redis.sadd(`tag:user:${id}`, `user:${id}:profile`, `user:${id}:settings`);

// Invalidar tudo relacionado
async function invalidateUser(id: string) {
  const keys = await redis.smembers(`tag:user:${id}`);
  if (keys.length) await redis.del(...keys);
  await redis.del(`tag:user:${id}`);
}
```

### Problemas Clássicos e Soluções

**Cache Stampede (Thundering Herd)** — chave expira, N requests vão ao banco ao mesmo tempo:
```typescript
// Cache lock — só um processo busca no banco
async function getUserWithLock(id: string): Promise<User> {
  const cached = await redis.get(`user:${id}`);
  if (cached) return JSON.parse(cached);

  const lock = await redis.set(`lock:user:${id}`, "1", "EX", 5, "NX");
  if (!lock) {
    await sleep(50);
    return getUserWithLock(id); // tenta o cache de novo
  }

  try {
    const user = await db.user.findUnique({ where: { id } });
    await redis.set(`user:${id}`, JSON.stringify(user), "EX", 300);
    return user;
  } finally {
    await redis.del(`lock:user:${id}`);
  }
}
```

**Cache Penetration** — requests para chave que nunca existe, todas passam pelo banco:
```typescript
// Cacheia "not found" com TTL curto
const user = await db.user.findUnique({ where: { id } });
const value = user ? JSON.stringify(user) : "NULL";
await redis.set(`user:${id}`, value, "EX", user ? 300 : 30);
```

**Cache Avalanche** — muitas chaves expiram ao mesmo tempo:
```typescript
// TTL com jitter (variação aleatória)
const ttl = 300 + Math.floor(Math.random() * 60); // 300-360s
await redis.set(key, value, "EX", ttl);
```

### Redis Cluster — Escala Horizontal

```
Client → Cluster-aware client
              ↓
     Slot routing (16.384 slots)
              ↓
┌──────────┬──────────┬──────────┐
│ Shard 1  │ Shard 2  │ Shard 3  │
│ Primary  │ Primary  │ Primary  │
│ Replica  │ Replica  │ Replica  │
└──────────┴──────────┴──────────┘

Slot = CRC16(key) % 16384 → mesma key sempre no mesmo shard
```

**Hash tags** — chaves relacionadas no mesmo shard:
```
{user:1}:profile  →  mesmo slot  →  MGET e transactions funcionam
{user:1}:settings →  mesmo slot
```

Configuração:
```
maxmemory 4gb
maxmemory-policy allkeys-lru
```

## Trade-offs

| Padrão | Vantagem | Desvantagem |
|---|---|---|
| **Cache-Aside** | Só cacheia o que é lido | Thundering herd no miss |
| **Write-Through** | Consistência forte | Overhead em escritas de dados raramente lidos |
| **Write-Behind** | Write mais rápido | Risco de perda de dados |

| Política de Eviction | Use quando |
|---|---|
| `LRU` | Maioria dos casos |
| `LFU` | Hot/cold data bem definido |
| `noeviction` | Não pode perder dado — retorna erro quando cheio |

## Quando Usar / Quando Evitar

**Cache não ajuda com:**
- Dado sempre único por request (relatório personalizado) — hit rate zero
- Dado que muda a cada request — TTL seria 0s
- Consistência forte obrigatória — transações financeiras, inventário crítico

**Stale data** é o trade-off fundamental de cache: consistência vs performance. Aceite stale quando possível — se o usuário pode ver o perfil com 5 minutos de delay, TTL de 5 min está OK.

## Conceitos Relacionados

[[fase-1-fundamentos-infraestrutura]] · [[cdn]] · [[redis]] · [[banco-de-dados]] · [[distributed-lock]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
