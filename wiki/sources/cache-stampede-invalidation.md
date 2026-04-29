---
type: source
title: "Cache Stampede e Cache Invalidation"
aliases: []
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/cache-stampede-invalidation.md
source_url: ""
author: ""
date_published: "2026-04-17"
date_ingested: 2026-04-22
source_count: 0
tags: [cache, redis, performance, sistema-distribuido]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Referência focada em dois problemas avançados de cache: stampede (thundering herd) e invalidation. Apresenta três soluções para stampede — mutex lock, XFetch (Vattani et al.) e stale-while-revalidate — e três estratégias de invalidação: TTL-based, event-driven e versioned keys. A frase de Phil Karlton sobre cache invalidation ser um dos dois problemas mais difíceis em CS é contextualizada com soluções concretas.

## Claims Principais

| Claim | Confiança |
|---|---|
| Cache stampede: 500 requests simultâneos a um produto popular podem saturar o banco via cascata de timeouts e retries | Alta |
| Mutex lock usa SET NX EX para garantir exclusividade — lock de 5s é suficiente na maioria dos casos | Alta |
| XFetch recalcula o cache antes da expiração com probabilidade crescente (algoritmo de Vattani et al.) | Alta |
| Stale-while-revalidate retorna dado antigo imediatamente na expiração e revalida em background | Alta |
| Versioned keys eliminam o problema de invalidação — bump de versão torna todas as chaves antigas obsoletas | Alta |
| Event-driven invalidation requer SCAN para wildcards (redis.del com * não funciona diretamente) | Alta |

## Conceitos Abordados

- [[cache-stampede]]
- [[distributed-lock]]
- [[xfetch]]
- [[stale-while-revalidate]]
- [[cache-invalidation]]
- [[ttl]]
- [[versioned-keys]]
- [[graceful-degradation]]
