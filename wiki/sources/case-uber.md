---
type: source
title: "Case: Ride-sharing (Uber)"
aliases: ["uber system design", "ride sharing design", "case uber"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, cases, uber, geolocalização, matching, geohash, redis, kafka]
skill: tech-mentor-system-design
source_file: /home/gabriel-martins/Documentos/dev-study/raw/case-uber.md
source_url: ""
author: "tech-mentor skill"
date_published: 2026-03-29
date_ingested: 2026-04-22
status: stable
---

# Case: Ride-sharing (Uber)

## TL;DR

Dois problemas hard juntos: geolocalização em tempo real com escrita intensa (1.25M writes/s) + matching em <1s. Solução central: Redis GEO para posições voláteis, Geohash para busca por prefixo evitando 5M cálculos de distância, distributed lock (SET NX) para race condition no match, Kafka para tracking e surge pricing desacoplados do caminho crítico.

## Key Claims

- **Redis GEO para localização de motoristas** — 1.25M writes/s, dados voláteis, busca geoespacial nativa. PostGIS não aguenta o write throughput. → [[concepts/redis-geo]]
- **Geohash evita cálculo de distância para 5M** — busca por prefixo na célula do passageiro + 8 adjacentes. Células próximas = prefixo compartilhado. → [[concepts/geohash]]
- **Pipeline de matching em 5 etapas** — GEOSEARCH → ETA real (Routing Service) → ranking por score → oferta via WebSocket → accept/reject com fallback e expansão de raio. → [[concepts/ride-matching-pipeline]]
- **Distributed lock com Redis SET NX** — evita race condition onde dois passageiros recebem oferta do mesmo motorista simultaneamente. → [[concepts/distributed-lock]]
- **Surge pricing desacoplado** — Kafka stream agrega demanda por geohash em janela de 5min, Redis cache o multiplier com TTL 30s. Não bloqueia caminho crítico do match. → [[concepts/surge-pricing]]
- **Tracking via WebSocket + Kafka** — motorista → WebSocket → Location Service → Kafka topic `ride.{id}.location` → passageiro via WebSocket. → [[concepts/realtime-tracking]]
- **Geohash boundary problem** — dois pontos a 100m podem ter prefixos diferentes em células adjacentes. Solução: buscar célula + 8 adjacentes sempre. → [[concepts/geohash]]
- **Redis cai: dados efêmeros** — perda de posição tolerável pois motoristas reenviam a cada 4s. Degradação de UX, não de correção.

## Scale Numbers

```
5M motoristas × 1 update/4s    = 1.25M writes/s
1M corridas/hora (pico)        = 278 matches/s
278 matches × 10 ETA calls     = 2.780 routing req/s
Kafka location stream          = ~60MB/s (1.25M msg/s × 50 bytes)
Redis GEO memory (5M drivers)  = ~350MB
```

## Entities

- [[entities/uber]]
- [[entities/redis]]
- [[entities/kafka]]
- [[entities/osrm]]

## Concepts

[[concepts/geohash]] · [[concepts/redis-geo]] · [[concepts/ride-matching-pipeline]] · [[concepts/distributed-lock]] · [[concepts/surge-pricing]] · [[concepts/realtime-tracking]] · [[concepts/estimativas-back-of-envelope]] · [[concepts/circuit-breaker]]

## Open Questions

- Como coordenar canary de algoritmo de matching sem afetar SLA de <1s?
- Geohash boundary problem em fronteiras de países/fusos — impacto operacional?

## Raw Quotes

> "Busca por raio via latitude/longitude bruta requer calcular distância para cada um dos 5M motoristas — inviável."

> "Dados de localização são efêmeros — em 4s, todos os motoristas reenviam posição."

> "Distância euclidiana ≠ ETA real (trânsito, ruas de mão única)."
