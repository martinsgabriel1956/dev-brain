---
date: 2026-03-27
tags: [tech-mentor, system-design, resiliencia, retry, backoff, jitter, idempotencia]
skill: tech-mentor-system-design/references/graceful-degradation.md
level: intermediário
---

# Retry com Backoff Exponencial

## Contexto

Retry parece trivial — "se falhou, tenta de novo". O problema é que retry ingênuo amplifica o problema: se 100 clientes tentam ao mesmo tempo, com o mesmo intervalo, eles criam uma avalanche que impede o serviço de se recuperar. Backoff exponencial + jitter é a solução.

## Como Funciona

### O Problema do Retry Ingênuo

```
Serviço B cai às 10:00:00

Sem backoff — todos os clientes tentam ao mesmo tempo:
10:00:01 → 1.000 requests simultâneos → falha
10:00:02 → 1.000 requests simultâneos → falha
→ Thundering herd: os retries impedem a recuperação
```

### Backoff Exponencial + Jitter

```
Sem jitter — todos sincronizados (ainda é thundering herd):
Cliente A: tentativa 2 → espera exatamente 200ms
Cliente B: tentativa 2 → espera exatamente 200ms
→ Spike coordenado

Com jitter — carga distribuída no tempo:
Cliente A: 200ms + 47ms de ruído  → tenta às .247
Cliente B: 200ms + 113ms de ruído → tenta às .313
→ Carga espalhada, serviço consegue se recuperar
```

### Quais Erros Retentar

```
✅ Retente (falhas transitórias):
  → 500, 502, 503, 504   — servidor/rede temporariamente indisponível
  → ECONNRESET, ETIMEDOUT — falha de rede

❌ Não retente (erros permanentes):
  → 400, 401, 403, 404, 422 — o mesmo request vai retornar o mesmo erro
```

## Código de Referência

### Implementação Completa

```typescript
type RetryOptions = {
  maxRetries?: number;
  baseDelayMs?: number;
  maxDelayMs?: number;
  shouldRetry?: (error: unknown) => boolean;
};

async function retryWithBackoff<T>(
  fn: () => Promise<T>,
  options: RetryOptions = {}
): Promise<T> {
  const {
    maxRetries = 3,
    baseDelayMs = 100,
    maxDelayMs = 5_000,
    shouldRetry = isTransientError
  } = options;

  let lastError: unknown;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (err) {
      lastError = err;

      if (!shouldRetry(err)) throw err;
      if (attempt === maxRetries) break;

      const exponential = baseDelayMs * Math.pow(2, attempt - 1);
      const jitter = Math.random() * baseDelayMs;
      const delay = Math.min(exponential + jitter, maxDelayMs);

      console.log({ message: "Retrying after failure", attempt, delayMs: Math.round(delay) });
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }

  throw lastError;
}

function isTransientError(err: unknown): boolean {
  if (!(err instanceof Error)) return false;
  if ("status" in err) {
    const status = (err as { status: number }).status;
    if (status >= 400 && status < 500) return false;
  }
  return true;
}
```

### Idempotência — Pré-requisito para Retry Seguro

```typescript
// ❌ Não idempotente — retry cria cobranças duplicadas
async function chargeCard(orderId: string, amountCents: number) {
  return stripe.charges.create({ amount: amountCents, currency: "brl" });
}

// ✅ Idempotente — chave garante que Stripe processa uma vez
async function chargeCard(orderId: string, amountCents: number) {
  return stripe.charges.create(
    { amount: amountCents, currency: "brl" },
    { idempotencyKey: `order-${orderId}` }
  );
}
```

### Retry em Mensageria

```typescript
// BullMQ — retry com backoff configurável
queue.add("charge", orderData, {
  attempts: 3,
  backoff: { type: "exponential", delay: 1_000 }
});

// SQS — retry nativo com DLQ após esgotar tentativas
const queueConfig = {
  VisibilityTimeout: 30,
  RedrivePolicy: {
    maxReceiveCount: 3,
    deadLetterTargetArn: dlqArn
  }
};
```

## Trade-offs

| Estratégia | Vantagem | Desvantagem |
|---|---|---|
| **Sem retry** | Zero complexidade | Falhas transitórias chegam ao usuário |
| **Retry imediato** | Simples | Thundering herd — amplifica o problema |
| **Backoff fixo** | Melhor que imediato | Clientes ainda sincronizados |
| **Backoff exponencial** | Reduz carga progressivamente | Aumenta latência percebida |
| **+ Jitter** | Distribui carga no tempo | Latência ligeiramente imprevisível |

## Quando Usar / Quando Evitar

**Sempre use retry com backoff em:**
- ✅ Chamadas HTTP para serviços externos (APIs de terceiros)
- ✅ Chamadas entre microserviços via rede
- ✅ Publicação de mensagens em broker (Kafka, SQS)

**Não use retry quando:**
- ❌ A operação não é idempotente e não tem idempotency key
- ❌ O erro é permanente (4xx de negócio)
- ❌ O serviço downstream está sabidamente com falha — use Circuit Breaker primeiro

**Parâmetros práticos:**
```
APIs internas:  maxRetries=3, baseDelay=100ms, maxDelay=2s
APIs externas:  maxRetries=2, baseDelay=500ms, maxDelay=5s
Jobs em fila:   maxRetries=5, backoff exponencial, DLQ após esgotar
```

## Conceitos Relacionados

[[fase-3-resiliencia]] · [[circuit-breaker]] · [[mensageria]] · [[graceful-degradation]] · [[rate-limiting]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
