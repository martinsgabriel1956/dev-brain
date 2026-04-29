---
type: source
title: "Rate Limiting"
aliases: ["rate limit", "token bucket", "sliding window", "throttling", "throttle"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [rate-limiting, token-bucket, sliding-window, fixed-window, redis, lua, throttling, backend]
skill: tech-mentor-backend
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/rate-limiting.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# Rate Limiting

## TL;DR

Rate Limiting protege APIs de abuso e sobrecarga. Quatro algoritmos: Fixed Window (simples, boundary burst), Token Bucket (bursts controlados), Sliding Window Log (exato, memória O(N)), Sliding Window Counter (~90% precisão, O(1) memória). Escolha padrão: Sliding Window Counter para APIs. Implementação em Redis com Lua script para atomicidade. Hierarquia de limites: global → por IP → por usuário → por endpoint.

## Key Claims

| Claim | Evidência |
|---|---|
| Fixed Window tem boundary burst: 2x o limite nos segundos da virada | Vulnerabilidade conhecida |
| Sliding Window Counter é O(1) memória e ~90% preciso — melhor trade-off | Aproximação ponderada do log exato |
| Lua script no Redis garante atomicidade — sem race condition | Redis processa Lua atomicamente |
| Hierarquia de limites: global → por IP → por usuário → por endpoint | Defesa em profundidade |
| Token Bucket permite burst controlado — ideal para upload em lote | Tokens acumulam até o bucket |

## Conceitos

- [[concepts/rate-limiting]] — algoritmos e implementação
- [[concepts/idempotencia]] — cliente que respeita rate limit retenta com mesmo key
- [[concepts/cache-hot-path]] — Redis como storage dos contadores
- [[concepts/load-balancer]] — rate limiting pode ser feito no LB (ex: nginx)

## Key Sources

_Este é o documento primário._
