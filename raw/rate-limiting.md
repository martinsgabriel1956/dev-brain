---
date: 2026-04-16
tags: [tech-mentor, backend, apis, rate-limiting, redis, algoritmos, token-bucket]
skill: tech-mentor-backend/references/apis
level: intermediário
---

# Rate Limiting — Token Bucket, Leaky Bucket e Sliding Window

## Contexto

Rate limiting protege APIs de abuso, garante fairness entre consumers e previne cascata de falhas. A escolha do algoritmo afeta diretamente o comportamento observado pelo cliente: o Token Bucket permite bursts controlados, o Leaky Bucket suaviza o tráfego, o Fixed Window é simples mas tem boundary exploits, e o Sliding Window elimina o exploit com custo moderado.

Em sistemas distribuídos, o estado do rate limiter precisa estar em Redis (não in-memory), ou workers diferentes terão contadores independentes.

---

## Fixed Window Counter — O Mais Simples

```typescript
// Divide o tempo em janelas fixas (ex: 1 minuto)
// Problema: burst no boundary — 100 req nos últimos 100ms + 100 req nos primeiros 100ms
// = 200 req em 200ms, mas ambas as janelas mostram 100 req (dentro do limite)

async function fixedWindowRateLimit(
  identifier: string,
  limit: number,
  windowSeconds: number
): Promise<{ allowed: boolean; remaining: number; resetAt: number }> {
  const now = Math.floor(Date.now() / 1000);
  const windowStart = Math.floor(now / windowSeconds) * windowSeconds;
  const key = `ratelimit:fixed:${identifier}:${windowStart}`;

  const current = await redis.incr(key);

  if (current === 1) {
    // Primeiro request na janela — definir TTL
    await redis.expire(key, windowSeconds);
  }

  return {
    allowed: current <= limit,
    remaining: Math.max(0, limit - current),
    resetAt: windowStart + windowSeconds
  };
}
```

---

## Sliding Window Log — Preciso mas Caro

```typescript
// Mantém timestamp de cada request — sem o boundary exploit do Fixed Window
// Problema: memória proporcional ao número de requests (não ao limite)
// Impraticável para limites altos (ex: 10000 req/min por usuário)

async function slidingWindowLogRateLimit(
  identifier: string,
  limit: number,
  windowMs: number
): Promise<{ allowed: boolean; remaining: number }> {
  const now = Date.now();
  const windowStart = now - windowMs;
  const key = `ratelimit:log:${identifier}`;

  // Operação atômica com pipeline
  const pipeline = redis.pipeline();
  pipeline.zremrangebyscore(key, 0, windowStart);  // remover requests antigos
  pipeline.zadd(key, now, `${now}-${Math.random()}`);  // adicionar request atual
  pipeline.zcard(key);  // contar requests na janela
  pipeline.expire(key, Math.ceil(windowMs / 1000));

  const results = await pipeline.exec();
  const count = results![2][1] as number;

  return {
    allowed: count <= limit,
    remaining: Math.max(0, limit - count)
  };
}
```

---

## Sliding Window Counter — O Equilíbrio

Aproximação do sliding window usando dois contadores (janela atual + anterior). Memória O(1), precisão ~99%.

```typescript
// Fórmula: peso_anterior = (tempo_restante_na_janela_anterior / tamanho_janela)
// count_efetivo = count_anterior * peso_anterior + count_atual

async function slidingWindowCounterRateLimit(
  identifier: string,
  limit: number,
  windowSeconds: number
): Promise<{ allowed: boolean; remaining: number; resetAt: number }> {
  const now = Date.now() / 1000;  // em segundos com decimais
  const currentWindow = Math.floor(now / windowSeconds);
  const previousWindow = currentWindow - 1;

  const currentKey = `ratelimit:sw:${identifier}:${currentWindow}`;
  const previousKey = `ratelimit:sw:${identifier}:${previousWindow}`;

  // Ler ambas as janelas em paralelo
  const [currentCount, previousCount] = await Promise.all([
    redis.get(currentKey).then(v => parseInt(v ?? "0")),
    redis.get(previousKey).then(v => parseInt(v ?? "0"))
  ]);

  // Calcular peso da janela anterior
  const elapsedInCurrentWindow = now % windowSeconds;
  const previousWeight = (windowSeconds - elapsedInCurrentWindow) / windowSeconds;

  const estimatedCount = Math.floor(previousCount * previousWeight) + currentCount;

  if (estimatedCount >= limit) {
    return {
      allowed: false,
      remaining: 0,
      resetAt: (currentWindow + 1) * windowSeconds
    };
  }

  // Incrementar janela atual
  await redis.pipeline()
    .incr(currentKey)
    .expire(currentKey, windowSeconds * 2)  // manter por 2 janelas
    .exec();

  return {
    allowed: true,
    remaining: limit - estimatedCount - 1,
    resetAt: (currentWindow + 1) * windowSeconds
  };
}
```

---

## Token Bucket — Bursts Controlados

Cada consumer tem um "balde" com capacidade máxima de tokens. Tokens são adicionados a uma taxa constante. Cada request consome um token. Permite burst até a capacidade do balde.

```typescript
// Implementação com Lua script — atomicidade garantida no Redis
const TOKEN_BUCKET_SCRIPT = `
local key = KEYS[1]
local capacity = tonumber(ARGV[1])
local refill_rate = tonumber(ARGV[2])   -- tokens por segundo
local now = tonumber(ARGV[3])           -- timestamp em ms
local requested = tonumber(ARGV[4])     -- tokens necessários (geralmente 1)

-- Ler estado atual do bucket
local data = redis.call("HMGET", key, "tokens", "last_refill")
local tokens = tonumber(data[1]) or capacity
local last_refill = tonumber(data[2]) or now

-- Calcular tokens ganhos desde última refill
local elapsed_seconds = (now - last_refill) / 1000
local new_tokens = elapsed_seconds * refill_rate
tokens = math.min(capacity, tokens + new_tokens)

-- Tentar consumir tokens
if tokens >= requested then
  tokens = tokens - requested
  redis.call("HMSET", key, "tokens", tokens, "last_refill", now)
  redis.call("EXPIRE", key, 3600)
  return {1, math.floor(tokens)}  -- {allowed, remaining}
else
  redis.call("HMSET", key, "tokens", tokens, "last_refill", now)
  redis.call("EXPIRE", key, 3600)
  return {0, math.floor(tokens)}  -- {not_allowed, remaining}
end
`;

async function tokenBucketRateLimit(
  identifier: string,
  capacity: number,
  refillRate: number,  // tokens por segundo
  requested = 1
): Promise<{ allowed: boolean; remaining: number }> {
  const key = `ratelimit:token:${identifier}`;
  const now = Date.now();

  const [allowed, remaining] = await redis.eval(
    TOKEN_BUCKET_SCRIPT,
    1,
    key,
    capacity,
    refillRate,
    now,
    requested
  ) as [number, number];

  return { allowed: allowed === 1, remaining };
}

// Uso: 100 tokens de capacidade, 10 tokens/segundo de refill
// Permite burst de até 100 requests, depois limita a 10/s
await tokenBucketRateLimit(`user:${userId}`, 100, 10);
```

---

## Leaky Bucket — Saída Suavizada

Processa requests a uma taxa constante independente do padrão de entrada. Requests acima da capacidade são descartados (ou enfileirados). Usado em sistemas de billing, APIs externas com rate limit estrito.

```typescript
// Leaky bucket como fila — processa 1 request por intervalo fixo
// Na prática, implementado como FIFO com worker de velocidade constante

async function leakyBucketRateLimit(
  identifier: string,
  capacity: number,  // tamanho máximo da fila
  leakRateMs: number  // intervalo entre processamentos em ms
): Promise<{ allowed: boolean; queuePosition: number }> {
  const key = `ratelimit:leaky:${identifier}`;
  const now = Date.now();

  const script = `
    local key = KEYS[1]
    local capacity = tonumber(ARGV[1])
    local leak_rate = tonumber(ARGV[2])
    local now = tonumber(ARGV[3])

    -- Calcular quantos itens "vazaram" desde o último acesso
    local last_leak = tonumber(redis.call("HGET", key, "last_leak") or now)
    local queue_size = tonumber(redis.call("HGET", key, "queue_size") or 0)

    local elapsed = now - last_leak
    local leaked = math.floor(elapsed / leak_rate)
    queue_size = math.max(0, queue_size - leaked)

    if leaked > 0 then
      redis.call("HSET", key, "last_leak", now)
    end

    if queue_size >= capacity then
      redis.call("EXPIRE", key, 3600)
      return {0, queue_size}
    end

    queue_size = queue_size + 1
    redis.call("HMSET", key, "queue_size", queue_size, "last_leak", last_leak)
    redis.call("EXPIRE", key, 3600)
    return {1, queue_size}
  `;

  const [allowed, queuePosition] = await redis.eval(
    script, 1, key, capacity, leakRateMs, now
  ) as [number, number];

  return { allowed: allowed === 1, queuePosition };
}
```

---

## Middleware Express com Headers de Rate Limit

```typescript
import type { Request, Response, NextFunction } from "express";

type RateLimitConfig = {
  limit: number;
  windowSeconds: number;
  keyExtractor?: (req: Request) => string;  // default: IP
};

function rateLimitMiddleware(config: RateLimitConfig) {
  const { limit, windowSeconds, keyExtractor } = config;

  return async (req: Request, res: Response, next: NextFunction) => {
    const identifier = keyExtractor
      ? keyExtractor(req)
      : req.ip ?? "unknown";

    const result = await slidingWindowCounterRateLimit(identifier, limit, windowSeconds);

    // Headers padrão de rate limit (RFC 6585 + draft RateLimit header)
    res.setHeader("X-RateLimit-Limit", limit);
    res.setHeader("X-RateLimit-Remaining", result.remaining);
    res.setHeader("X-RateLimit-Reset", result.resetAt);

    if (!result.allowed) {
      res.setHeader("Retry-After", Math.ceil(result.resetAt - Date.now() / 1000));
      return res.status(429).json({
        error: {
          code: "RATE_LIMIT_EXCEEDED",
          message: "Too many requests. Please retry after the reset time.",
          retryAfter: result.resetAt
        }
      });
    }

    next();
  };
}

// Aplicar por rota com configurações diferentes
app.use("/api/auth", rateLimitMiddleware({ limit: 10, windowSeconds: 60 }));  // strict para auth
app.use("/api", rateLimitMiddleware({
  limit: 1000,
  windowSeconds: 60,
  keyExtractor: req => req.headers["authorization"] ?? req.ip ?? "unknown"  // por token
}));
```

---

## Rate Limiting Distribuído com Lua Atômico

O Lua script no Redis executa atomicamente — sem race conditions entre leitura e escrita de contadores em múltiplos workers.

```typescript
// Estratégia de key para diferentes granularidades
function buildRateLimitKey(identifier: string, resource: string, window: string): string {
  return `ratelimit:${resource}:${identifier}:${window}`;
}

// Múltiplos limites em camadas
async function multiLayerRateLimit(userId: string): Promise<boolean> {
  const [perSecond, perMinute, perHour] = await Promise.all([
    slidingWindowCounterRateLimit(`user:${userId}`, 10, 1),     // 10/s
    slidingWindowCounterRateLimit(`user:${userId}`, 300, 60),   // 300/min
    slidingWindowCounterRateLimit(`user:${userId}`, 5000, 3600) // 5000/h
  ]);

  return perSecond.allowed && perMinute.allowed && perHour.allowed;
}
```

---

## Trade-offs

| Algoritmo | Burst | Memória | Precisão | Complexidade |
|---|---|---|---|---|
| **Fixed Window** | Alto (boundary exploit) | O(1) | Baixa | Simples |
| **Sliding Window Log** | Não | O(requests) | Alta | Média |
| **Sliding Window Counter** | Não | O(1) | ~99% | Média |
| **Token Bucket** | Sim (controlado) | O(1) | Alta | Alta |
| **Leaky Bucket** | Não (saída uniforme) | O(1) | Alta | Alta |

## Quando Usar / Quando Evitar

**Fixed Window:** métricas internas, dashboards, casos onde precisão não é crítica.

**Sliding Window Counter:** rate limiting de API pública — melhor custo-benefício entre precisão e memória.

**Token Bucket:** APIs que devem tolerar burst legítimo (upload de arquivo, importação em batch).

**Leaky Bucket:** proteção de sistemas downstream com throughput fixo (APIs externas com limite estrito por segundo).

**Evitar in-memory em ambiente com múltiplos workers:** cada worker terá seu próprio contador — o limite real será `limit × workers`.

## Conceitos Relacionados

[[rest-openapi]] · [[distributed-locks]] · [[redis]] · [[webhook]] · [[graceful-degradation]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-16*
