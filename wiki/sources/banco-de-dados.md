---
type: source
title: "Banco de Dados"
aliases: ["databases", "banco de dados fundamentos"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [banco-de-dados, postgresql, acid, nosql, read-replicas, connection-pooling, n-plus-one, system-design]
skill: tech-mentor-system-design
source_file: /home/gabriel-martins/Documentos/dev-study/raw/banco-de-dados.md
source_url: ""
author: "tech-mentor skill"
date_published: 2026-03-27
date_ingested: 2026-04-22
status: stable
---

# Banco de Dados

## TL;DR

Banco de dados persiste estado. PostgreSQL é o default — migre só quando ele claramente não serve. As decisões de índice, transação, réplica e pooling têm impacto direto em consistência, escalabilidade e custo.

## Key Claims

- **ACID é a fundação do relacional** — Atomicity, Consistency, Isolation, Durability. Dado commitado sobrevive a falha via WAL. → [[concepts/acid]]
- **NoSQL não substitui relacional, complementa** — cada tipo resolve um problema específico: Document para schema flexível, Key-Value para acesso por chave, Wide-Column para escrita massiva, Graph para relacionamentos complexos. → [[concepts/nosql]]
- **Índice tem custo de escrita** — cada `INSERT`/`UPDATE`/`DELETE` atualiza todos os índices. 15 índices = 15x mais trabalho por escrita. → [[concepts/database-index]]
- **Transações são obrigatórias para operações dependentes** — dois updates dependentes sem `$transaction` podem resultar em estado inválido. → [[concepts/database-transactions]]
- **Read replicas para workload read-heavy** — roteamento explícito read→réplica, write→primário. Read-your-writes via flag no Redis. → [[concepts/read-replicas]] [[concepts/read-your-writes]]
- **PgBouncer elimina overhead de conexões** — 50 pods × 20 conexões = 1000 → PgBouncer → 20 conexões reais. `pool_mode = transaction` é o recomendado. → [[concepts/connection-pooling]]
- **N+1 é o bug de performance mais comum** — 1 query + N queries em loop; solução é JOIN via `include`. → [[concepts/n-plus-one]]
- **PostgreSQL faz mais do que parece** — JSONB, full-text search, pg_vector (busca vetorial IA), Timescaledb (série temporal). → [[concepts/postgresql]]

## Entities

- [[entities/postgresql]]
- [[entities/pgbouncer]]
- [[entities/mongodb]]
- [[entities/redis]]
- [[entities/prisma]]

## Concepts

[[concepts/acid]] · [[concepts/nosql]] · [[concepts/database-index]] · [[concepts/database-transactions]] · [[concepts/read-replicas]] · [[concepts/read-your-writes]] · [[concepts/connection-pooling]] · [[concepts/n-plus-one]] · [[concepts/postgresql]] · [[concepts/relational-vs-nosql]]

## Open Questions

- Quando exatamente pg_vector compete com Pinecone/Weaviate em produção?
- Qual o threshold de reads/writes para justificar read replica vs escalar vertical?

## Raw Quotes

> "Use PostgreSQL como padrão e só migre para outro banco quando ele claramente não serve para o caso."

> "50 pods × 20 conexões = 1000 conexões → PgBouncer → 20 conexões reais no PostgreSQL"

> "Read replicas não substituem queries lentas — otimize os índices primeiro"
