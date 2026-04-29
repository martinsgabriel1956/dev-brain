---
type: source
title: "Case: URL Shortener"
aliases: ["url shortener design", "case url shortener", "bitly design"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, cases, url-shortener, hashing, cache, redirect, snowflake]
skill: tech-mentor-system-design
source_file: /home/gabriel-martins/Documentos/dev-study/raw/case-url-shortener.md
source_url: ""
author: "tech-mentor skill"
date_published: 2026-03-29
date_ingested: 2026-04-22
status: stable
---

# Case: URL Shortener

## TL;DR

Parece trivial mas força decisões reais: geração de IDs distribuídos (Snowflake > hash truncado), 301 vs 302 (analytics vs cache), estratégia de cache em camadas (Redis + hot cache local), e analytics fora do caminho crítico (Kafka async). Read:Write = 100:1, 95% resolve no cache.

## Key Claims

- **Snowflake ID + Base62 é a melhor opção** — distribuído, sem colisão garantida, sem coordenação central, ordenado por tempo. Hash truncado tem colisão. ID sequencial é enumerável. → [[concepts/snowflake-id]]
- **302 por padrão, 301 como opção** — 302 permite analytics preciso e destino mutável. 301 é opção explícita para quem não precisa de tracking. → [[concepts/http-redirect-301-302]]
- **95% dos redirects resolvem no cache** — power law: top 1% das URLs = 80% do tráfego. Redis 50GB resolve o volume relevante de 91TB de storage. → [[concepts/cache-hot-path]]
- **Hot cache local na API** — top 1.000 URLs = ~60% do tráfego. LRU in-memory por instância evita round-trip ao Redis para URLs virais. → [[concepts/cache-hot-path]]
- **Analytics async via Kafka** — analytics no caminho crítico do redirect adiciona latência. Kafka desacopla, ClickHouse agrega. Redis INCR com flush a cada 60s para contadores em tempo real. → [[concepts/analytics-pipeline]]
- **Base62 de 7 chars = 3,5 trilhões de combinações** — suficiente para 100M/dia por ~95 anos. → [[concepts/snowflake-id]]
- **PostgreSQL para storage principal** — 1.160 writes/s é comportável. ACID garante integridade. Sharding por short_code para escala a 1T URLs.

## Scale Numbers

```
Escritas: 100M/dia ÷ 86.400s   = 1.160 req/s
Leituras: 10B/dia ÷ 86.400s    = 115.740 req/s
Read:Write ratio                = 100:1
Storage 5 anos                  = ~91TB
Cache Redis necessário          = ~50GB (resolve 95% do tráfego)
Base62 7 chars                  = 62^7 = 3,5T combinações
```

## Entities

- [[entities/redis]]
- [[entities/kafka]]
- [[entities/postgresql]]
- [[entities/clickhouse]]

## Concepts

[[concepts/snowflake-id]] · [[concepts/http-redirect-301-302]] · [[concepts/cache-hot-path]] · [[concepts/analytics-pipeline]] · [[concepts/estimativas-back-of-envelope]] · [[concepts/distributed-lock]]

## Open Questions

- Rate limiting por IP no endpoint de redirect — como evitar falsos positivos em NATs compartilhados?
- ClickHouse vs DynamoDB para analytics de URL shortener em escala de 10B events/dia?

## Raw Quotes

> "Analytics não pode estar no caminho crítico do redirect — adiciona latência e cria acoplamento."

> "Top 1% das URLs = ~80% dos redirects. Storage barato, cache quente: Redis de 50GB resolve o volume relevante."

> "302 por padrão (analytics). Oferecer 301 como opção para quem não precisa de tracking."
