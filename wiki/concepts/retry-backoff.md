---
type: concept
title: "Retry com Backoff Exponencial e Jitter"
aliases: ["retry backoff", "exponential backoff", "jitter retry", "retry pattern"]
date_created: 2026-04-22
date_updated: 2026-08-14
source_count: 3
tags: [resiliencia, retry, backoff, jitter, thundering-herd, network, idempotencia]
skill: tech-mentor-system-design
status: stable
---

# Retry com Backoff Exponencial e Jitter

Padrão de resiliência para falhas transitórias de rede. Retry ingênuo (imediato ou intervalo fixo) amplifica o problema via [[concepts/thundering-herd]]. Backoff exponencial + jitter distribui a carga no tempo.

## O Problema

```
Sem backoff: 1000 clientes retentam ao mesmo tempo →
spike coordenado → serviço não consegue se recuperar

Sem jitter: backoff exponencial mas todos esperam exatamente 200ms →
ainda é spike, apenas deslocado
```

## Fórmula

```
delay = min(baseDelay × 2^(attempt-1) + random(baseDelay), maxDelay)
```

## Implementação

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

## O que Retentar

```
✅ 500, 502, 503, 504, ECONNRESET, ETIMEDOUT  — transitório
❌ 400, 401, 403, 404, 422                    — permanente, retry inútil
```

## Em Mensageria

```typescript
// BullMQ
queue.add("charge", orderData, {
  attempts: 3,
  backoff: { type: "exponential", delay: 1_000 }
});

// SQS com DLQ
const queueConfig = {
  VisibilityTimeout: 30,
  RedrivePolicy: { maxReceiveCount: 3, deadLetterTargetArn: dlqArn }
};
```

## Parâmetros Práticos

| Contexto | maxRetries | baseDelay | maxDelay |
|---|---|---|---|
| APIs internas | 3 | 100ms | 2s |
| APIs externas | 2 | 500ms | 5s |
| Jobs em fila | 5 | exponencial | DLQ |

## Pré-requisito: Idempotência

Retry só é seguro se a operação for idempotente. Ver [[concepts/idempotencia]].

Um timeout no cliente não diz *por que* a resposta não chegou — a operação pode ter falhado antes do servidor, estar em andamento, ou já ter sido concluída com a resposta perdida no caminho de volta. O cliente não consegue diferenciar esses três casos olhando só para o relógio, e é exatamente essa ambiguidade que torna o retry necessário e a idempotência obrigatória: o objetivo não é evitar o retry, é garantir que retentar não produza um efeito de negócio duplicado.

## Quando NÃO usar

- Operação não idempotente sem idempotency key
- Serviço downstream sabidamente em falha → usar [[concepts/circuit-breaker]] primeiro
- Erro permanente (4xx de negócio)

## Key Sources

- [[sources/retry-backoff]]
- [[wiki/sources/idempotencia-pagamentos-retry-sistemas-distribuidos]] — por que o timeout sozinho não distingue falha, processamento em andamento e sucesso com resposta perdida; teste que corta a resposta depois do efeito e antes da confirmação
- [[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]] — retry agressivo entre produtor e fila pode adicionar ainda mais pressão a um sistema já sobrecarregado, agravando [[wiki/concepts/back-pressure]] em vez de mitigá-lo
