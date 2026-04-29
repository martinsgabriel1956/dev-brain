---
type: source
title: "Read Replicas e Connection Pooling"
aliases: ["read replica", "pgbouncer", "connection pool", "rds proxy", "replicacao"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [read-replicas, connection-pooling, pgbouncer, rds-proxy, postgresql, prisma, banco-de-dados]
skill: tech-mentor-data
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/read-replicas-connection-pooling.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# Read Replicas e Connection Pooling

## TL;DR

Read Replicas escalam workloads read-heavy roteando queries SELECT para réplicas. Risco: replication lag — o padrão read-your-writes mitiga com flag Redis por N segundos. PgBouncer em transaction pooling reduz 1000 conexões de app para 25 conexões reais no PostgreSQL (que tem overhead de ~2–3GB com 1000 processos). Prisma tem suporte nativo a múltiplos datasources para routing automático.

## Key Claims

| Claim | Evidência |
|---|---|
| PostgreSQL cria 1 processo por conexão — 1000 conexões = 2–3GB só em overhead | Documentação PostgreSQL |
| PgBouncer em transaction pooling: 1000 clientes → 25 conexões reais | Proxy leve, event-driven |
| Replication lag cria inconsistência — leitura imediata após escrita pode retornar dado antigo | Solução: read-your-writes com flag Redis |
| RDS Proxy (AWS) é o PgBouncer gerenciado — sem operação manual | IAM auth, failover automático |
| Multi-replica: round-robin entre réplicas com fallback para primária em lag alto | Roteamento por latência ou health |

## Conceitos

- [[concepts/read-replicas]] — já existe no index
- [[concepts/connection-pooling]] — já existe no index
- [[concepts/read-your-writes]] — já existe no index
- [[concepts/postgresql]] — banco de referência
- [[concepts/db-sharding]] — quando réplicas não são suficientes

## Key Sources

_Este é o documento primário._
