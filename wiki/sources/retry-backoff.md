---
type: source
title: "Retry com Backoff Exponencial"
aliases: ["retry backoff", "exponential backoff", "jitter", "thundering herd"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 0
tags: [resiliencia, retry, backoff, jitter, idempotencia, thundering-herd, mensageria]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-study/raw/retry-backoff.md
source_url: ""
author: ""
date_published: 2026-03-27
date_ingested: 2026-04-22
---

# Retry com Backoff Exponencial

## TL;DR

Retry ingênuo amplifica falhas — 1000 clientes retentando no mesmo instante criam thundering herd que impede recuperação. Backoff exponencial + jitter distribui a carga no tempo. Pré-requisito para retry seguro: idempotência.

## Key Claims

**Claim:** Retry sem jitter cria thundering herd — clientes sincronizados tentam no mesmo instante, amplificando a carga no serviço em recuperação.
**Evidence:** Sem jitter: todos os clientes esperam exatamente 200ms → spike coordenado → serviço não consegue se recuperar. Com jitter: `delay = min(exponential + random(baseDelay), maxDelay)` → carga distribuída no tempo → janelas de recuperação entre picos.
**Confidence:** alta

**Claim:** Apenas erros transitórios devem ser retentados — erros permanentes (4xx de negócio) vão retornar o mesmo resultado independente do número de tentativas.
**Evidence:** ✅ Retente: 500/502/503/504, ECONNRESET, ETIMEDOUT. ❌ Não retente: 400/401/403/404/422 — o mesmo request retorna o mesmo erro.
**Confidence:** alta

**Claim:** Idempotência é pré-requisito para retry seguro — sem ela, retry pode criar cobranças duplicadas ou efeitos colaterais múltiplos.
**Evidence:** `stripe.charges.create` sem idempotency key = cobrança duplicada em cada retry. Com `idempotencyKey: order-${orderId}` = Stripe processa exatamente uma vez, retries seguros.
**Confidence:** alta

**Claim:** Circuit breaker deve ser ativado antes de retry quando o serviço downstream está sabidamente com falha.
**Evidence:** Retry contra serviço em falha total consome threads e aumenta latência do chamador. Circuit breaker abre imediatamente, fail-fast sem tentar — retry só faz sentido para falhas transitórias pontuais.
**Confidence:** alta

## Parâmetros Práticos

```
APIs internas:  maxRetries=3, baseDelay=100ms, maxDelay=2s
APIs externas:  maxRetries=2, baseDelay=500ms, maxDelay=5s
Jobs em fila:   maxRetries=5, backoff exponencial, DLQ após esgotar
```

## Concepts & Entities Touched

[[concepts/retry-backoff]] · [[concepts/idempotencia]] · [[concepts/thundering-herd]] · [[concepts/circuit-breaker]] · [[concepts/graceful-degradation]]

## Open Questions

- Retry com backoff em streaming (SSE, WebSocket) — qual o padrão de reconnect?
- Como expor retry count nas métricas sem aumentar cardinalidade do Prometheus?
- Jitter full vs decorrelated jitter — diferença prática em alta concorrência?
