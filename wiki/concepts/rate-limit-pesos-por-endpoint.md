---
type: concept
title: "Pesos por Endpoint no Rate Limit"
aliases: ["rate limit por custo", "weighted token bucket"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [rate-limiting, token-bucket, custo-por-operacao]
skill: tech-mentor-backend
status: draft
---

# Pesos por Endpoint no Rate Limit

No [[wiki/concepts/token-bucket]] contabilizado por endpoint, cada operação consome um número de tokens proporcional ao seu custo: GET simples = 1, endpoint pesado = 10 (ou ~1000 num balde maior) ([[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]]). Protege recursos caros sem exigir taxa uniforme e sem mudar o código da API.

**Caso do autor:** ~10 clientes sincronizavam dados em segundo plano (endpoint de diff, caro em CPU/memória), alguns em paralelo, degradando outros endpoints e o portal usado por milhares de pessoas. Solução: 10.000 tokens/h por cliente; portal = 1 token, sincronização ≈ 1000. Picos contidos sem mexer na API; clientes ajustaram processos ao receber [[wiki/concepts/http-429-too-many-requests]] (efeito pedagógico). Relato único, sem métricas.

Une regra de negócio (contrato) e proteção técnica. `[skill: tech-mentor-backend]`: limites por tier e por custo de operação. Ver [[wiki/concepts/rate-limiting]], [[wiki/concepts/api-gateway]].

## Key Sources

- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]]
