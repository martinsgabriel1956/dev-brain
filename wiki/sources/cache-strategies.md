---
type: source
title: "Estratégias de Cache — Cache-Aside, Write-Through, Write-Behind e Cache Stampede"
aliases: []
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/cache-strategies.md
source_url: ""
author: ""
date_published: "2026-04-16"
date_ingested: 2026-04-22
source_count: 0
tags: [cache, redis, cache-aside, write-through, cache-stampede, system-design]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Aprofundamento nas estratégias de cache com exemplos TypeScript completos. Cache-Aside é o padrão default para leituras. Write-Through para consistência forte. Write-Behind para throughput máximo de escrita. Cache Stampede tem três soluções principais: mutex lock, probabilistic early expiration (XFetch) e stale-while-revalidate. Invalidação pode ser TTL, write-through, event-driven (CDC) ou versioned keys.

## Claims Principais

| Claim | Confiança |
|---|---|
| Cache-Aside tem 100% de miss rate no cold start | Alta |
| Write-Through pode usar best-effort no cache update — banco é a fonte de verdade | Alta |
| Write-Behind deve ser usado apenas para dados onde perda eventual é aceitável (analytics, contadores) | Alta |
| Cache Stampede: chave popular expira → N requests simultâneos saturam o banco | Alta |
| Mutex lock (SET NX EX) garante que só um worker busca o dado no banco | Alta |
| XFetch (probabilistic early expiration) evita stampede sem locks — probabilidade crescente de recompute próximo da expiração | Alta |
| Stale-while-revalidate retorna dado stale imediatamente e atualiza em background | Alta |
| Invalidação event-driven via CDC (Debezium + Kafka) oferece consistência mais forte | Média |
| Versioned keys nunca invalidam — incrementa versão e deixa chaves antigas expirar pelo TTL | Alta |

## Conceitos Abordados

- [[cache-aside]]
- [[write-through]]
- [[write-behind]]
- [[cache-stampede]]
- [[stale-while-revalidate]]
- [[xfetch]]
- [[distributed-lock]]
- [[cache-invalidation]]
- [[ttl]]
- [[cdc-debezium]]
