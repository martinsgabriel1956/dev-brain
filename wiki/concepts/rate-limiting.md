---
type: concept
title: "Rate Limiting"
aliases: ["throttling", "rate limit", "token bucket", "sliding window"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [rate-limiting, token-bucket, sliding-window, redis, throttling, protecao-api]
skill: tech-mentor-backend
status: stub
---

# Rate Limiting

Mecanismo de controle que limita a frequência de requests para proteger APIs de abuso e sobrecarga.

**Quatro algoritmos:**
| Algoritmo | Precisão | Memória | Bursts |
|---|---|---|---|
| Fixed Window | Média — boundary burst | O(1) | Sim |
| Token Bucket | Alta | O(1) | Controlado |
| Sliding Window Log | Exata | O(N) | Não |
| Sliding Window Counter | ~90% | O(1) | Não |

**Escolha padrão:** Sliding Window Counter para APIs gerais. Token Bucket quando bursts controlados são desejados (upload em lote).

**Implementação:** Redis + Lua script (atomicidade). Hierarquia: global → por IP → por usuário → por endpoint.

## Key Sources

- [[sources/rate-limiting]]
