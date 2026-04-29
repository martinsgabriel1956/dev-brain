---
type: source
title: "GraphQL"
aliases: ["graphql", "schema first", "dataloader", "n+1", "federation", "persisted queries"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/graphql.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [graphql, schema-first, dataloader, n-plus-1, federation, persisted-queries, depth-limiting, cursor-pagination]
skill: tech-mentor-backend
status: stable
---

## TL;DR

GraphQL permite que o cliente especifique exatamente os dados necessários. O problema clássico N+1 (100 orders = 100 queries de user) é resolvido com DataLoader (batching automático). Persisted Queries reduzem payload e previnem queries maliciosas. Federation v2 distribui o schema entre múltiplos serviços. Use quando: múltiplos clientes com necessidades de dados diferentes.

## Key Claims

**Claim:** DataLoader resolve o problema N+1 via batching automático por request.
**Evidence:** Sem DataLoader: 100 orders = 100 `findUser(id)`. Com DataLoader: acumula os 100 IDs no mesmo tick, faz 1 `findUsers(ids)`. O resultado é mapeado de volta por ID. DataLoader deve ser criado por request (não compartilhado entre requests).
**Confidence:** alta

**Claim:** Depth limiting é obrigatório para prevenir queries de denial-of-service.
**Evidence:** `{ user { orders { user { orders { user { ... } } } } } }` pode causar exponencial de queries. Depth limit de 5 bloqueia recursão excessiva. Também: query complexity analysis para limitar custo total.
**Confidence:** alta

**Claim:** GraphQL é pior que REST quando: API pública simples, contrato estável, caching de CDN necessário.
**Evidence:** REST com URL fixa: cacheável por CDN (GET /products/123 é sempre o mesmo). GraphQL POST: CDN não cacheia por padrão. REST: mais simples de versionar, melhor tooling de segurança perimetral. GraphQL vence para: BFF, múltiplos clientes, dados relacionados complexos.
**Confidence:** alta

**Claim:** Federation v2 permite que cada serviço possua seu subgraph — schema distribuído sem gateway monolítico.
**Evidence:** Products service define `Product`. Orders service extends `Product` com campo `orderHistory`. Apollo Router (ou equivalente) compõe os subgraphs em runtime. Cada time faz deploy do seu subgraph independentemente.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/graphql]]
- [[concepts/dataloader]]
- [[concepts/n-plus-one-problem]]
- [[concepts/graphql-federation]]
- [[concepts/persisted-queries]]
- [[concepts/cursor-pagination]]

## Open Questions

- Federation v2 e subgraph com schema incompatível — como gerenciar breaking changes em subgraphs independentes?
- GraphQL subscriptions em produção com muitos usuários simultâneos — WebSocket vs SSE?
