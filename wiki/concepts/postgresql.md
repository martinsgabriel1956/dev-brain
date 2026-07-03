---
type: concept
title: "PostgreSQL"
aliases: ["postgres", "pg"]
date_created: 2026-04-22
date_updated: 2026-07-03
source_count: 3
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

## Backend as a Service Ainda é Postgres

Supabase é um exemplo de BaaS que expõe Postgres via API REST/realtime. Chamar a API não elimina SQL — por baixo, o motor continua sendo Postgres executando SQL. Ver [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]].

## JSONB como Ponte para NoSQL

A coluna `JSONB` indexável é o motivo prático de muita gente não precisar de uma infraestrutura poliglota: cobre boa parte do caso de uso que levaria alguém a adotar um banco não relacional para dado semi-estruturado. Ver [[wiki/concepts/relational-vs-nosql]] e [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]].

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
- [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]]
