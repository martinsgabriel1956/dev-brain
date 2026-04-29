---
type: source
title: "Cache"
aliases: []
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/cache.md
source_url: ""
author: ""
date_published: "2026-03-27"
date_ingested: 2026-04-22
source_count: 0
tags: [cache, redis, performance, system-design]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Cache guarda resultados de operações caras em armazenamento rápido (RAM) para evitar refazê-las. Redis é ~1000x mais rápido que banco em disco (100ns vs 100μs). Os três padrões fundamentais são Cache-Aside, Write-Through e Write-Behind. O trade-off central é consistência vs performance — stale data é o preço do cache.

## Claims Principais

| Claim | Confiança |
|---|---|
| Redis em RAM é ~1000x mais rápido que banco com I/O em disco | Alta |
| Cache-Aside é o padrão mais comum — popula só sob demanda | Alta |
| Write-Through garante consistência, mas dobra o custo de escrita | Alta |
| Write-Behind maximiza throughput de escrita com risco de perda de dados | Alta |
| Cache Stampede ocorre quando chave expira e N requests vão ao banco simultaneamente | Alta |
| Cache Penetration acontece com requests para chaves que nunca existem | Alta |
| Cache Avalanche ocorre quando muitas chaves expiram ao mesmo tempo — TTL com jitter é a solução | Alta |
| Redis Cluster usa 16.384 slots via CRC16(key) % 16384 para roteamento | Alta |
| Hash tags `{user:1}` garantem que chaves relacionadas ficam no mesmo shard | Alta |
| Cache não ajuda com dados únicos por request, dados com alta mutabilidade ou consistência forte obrigatória | Alta |

## Conceitos Abordados

- [[cache-aside]]
- [[write-through]]
- [[write-behind]]
- [[cache-stampede]]
- [[cache-penetration]]
- [[cache-avalanche]]
- [[ttl]]
- [[redis-cluster]]
- [[eviction-policy]]
- [[distributed-lock]]
