---
type: source
title: "Bancos Especializados — Graph, Time-Series, Vector, Embedded, Distribuído"
aliases: ["bancos especializados", "graph db", "neo4j", "time series", "influxdb", "vector db", "pgvector", "duckdb", "cockroachdb", "spanner"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/bancos-especializados.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [graph-db, neo4j, time-series, influxdb, timescaledb, vector-db, pgvector, duckdb, cockroachdb, spanner, embedded-db]
skill: tech-mentor-data
status: stable
---

## TL;DR

5 categorias de bancos especializados: Graph (Neo4j — relacionamentos N-hop), Time-Series (InfluxDB/TimescaleDB — queries por janela temporal), Vector (pgvector/Qdrant — similaridade semântica para RAG), Embedded (SQLite/DuckDB — in-process, zero infra), Distribuído (CockroachDB/Spanner — SQL com escala horizontal). Cada um resolve um padrão de acesso que PostgreSQL genérico resolve com dificuldade.

## Key Claims

**Claim:** Graph DB é o único que resolve queries de múltiplos hops de relacionamento eficientemente — RDBMS degrada exponencialmente.
**Evidence:** "Amigos de amigos que compraram produto X" em PostgreSQL: 3 JOINs self-referenciando tabela users. Em Neo4j: `MATCH (u:User)-[:FRIEND*1..3]->(friend)-[:BOUGHT]->(p:Product {name:"X"})`. Cada hop adicional no RDBMS multiplica o custo; no Graph DB é linear pelo número de nós visitados.
**Confidence:** alta

**Claim:** Time-Series DBs têm compressão e queries temporais nativas — PostgreSQL com TIMESTAMP não é suficiente para telemetria em escala.
**Evidence:** TimescaleDB: compressão automática de chunks antigos (10-100x). Queries de downsampling: `time_bucket('1h', time)` com índice nativo. InfluxDB: schema-less, ingestion >1M pontos/s. PostgreSQL TIMESTAMP requer índice manual, sem compressão temporal, sem funções de downsampling built-in.
**Confidence:** alta

**Claim:** pgvector é suficiente para RAG em produção até ~1M vetores — Qdrant/Weaviate para escalas maiores.
**Evidence:** pgvector: extensão PostgreSQL, vetores como coluna, índice HNSW ou IVFFlat. Queries `<->` (distância euclidiana), `<#>` (dot product), `<=>` (cosine). Vantagem: sem infra adicional, transações ACID, JOINs com dados relacionais. Qdrant/Pinecone: payloads maiores, filtering eficiente, escala horizontal nativa.
**Confidence:** alta

**Claim:** DuckDB é o SQLite para analytics — OLAP in-process sem servidor, queries colunares.
**Evidence:** DuckDB: execução colunar in-process, lê Parquet/CSV/Arrow diretamente, sem servidor. Ideal para data science local, ETL de médio volume, analytics em Lambda. SQLite é OLTP (row-store). DuckDB é OLAP (column-store). Não competem — servem padrões de acesso diferentes.
**Confidence:** alta

## Entities & Concepts Touched

- [[entities/neo4j]]
- [[entities/influxdb]]
- [[entities/timescaledb]]
- [[entities/pgvector]]
- [[entities/qdrant]]
- [[entities/duckdb]]
- [[entities/cockroachdb]]
- [[concepts/graph-db]]
- [[concepts/time-series-db]]
- [[concepts/vector-db]]

## Open Questions

- CockroachDB vs YugabyteDB em produção — qual tem melhor compatibilidade PostgreSQL para migrações?
- pgvector com HNSW vs IVFFlat — qual índice para qual tamanho de dataset?
