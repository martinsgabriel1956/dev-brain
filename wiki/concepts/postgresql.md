---
type: concept
title: "PostgreSQL"
aliases: ["postgres", "pg"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [banco-de-dados, postgresql, relacional, jsonb, vetorial]
skill: tech-mentor-system-design
status: stable
---

# PostgreSQL

Banco relacional open-source. Default para a maioria dos casos — migre só quando claramente não serve.

## Capacidades Além do Básico

| Feature | Substitui |
|---|---|
| `JSONB` | MongoDB para dados semi-estruturados |
| Full-text search nativo | Elasticsearch para casos simples |
| `pg_vector` extension | Pinecone/Weaviate para busca vetorial em IA |
| Timescaledb extension | InfluxDB para série temporal |

## Regra de Ouro

Não migre para NoSQL por performance antes de:
1. Criar os [[concepts/database-index]] corretos
2. Resolver [[concepts/n-plus-one]] queries
3. Configurar [[concepts/connection-pooling]] com PgBouncer
4. Avaliar [[concepts/read-replicas]] para reads

## Key Sources

- [[sources/banco-de-dados]]
