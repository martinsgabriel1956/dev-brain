---
type: concept
title: "PostgreSQL"
aliases: ["postgres", "pg"]
date_created: 2026-04-22
date_updated: 2026-07-27
source_count: 4
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

## Processo por Conexão, Não Thread

Diferença arquitetural fundamental frente ao [[wiki/concepts/mysql|MySQL]]: o Postgres usa um **processo do sistema operacional** (fork) para cada conexão, não uma thread. Isolamento melhor — um processo travando não derruba os outros — mas custo maior: manter centenas de conexões IDLE consome recurso real mesmo sem query rodando. É por isso que [[wiki/concepts/connection-pooling|PgBouncer]] é considerado obrigatório em produção, e não apenas uma otimização — ele multiplexa milhares de conexões de aplicação em algumas centenas de conexões reais no banco (limite prático direto costuma ficar em 500–2.000).

## Postgres vs MySQL em Cargas Analíticas

Benchmarks independentes citados mostram Postgres até 50% mais rápido que MySQL em cargas com CTEs e agregações pesadas — uma das razões pelas quais equipes migram de MySQL para Postgres quando os relatórios/joins complexos começam a pesar. PostGIS (geoespacial) e pgvector (busca vetorial para IA) reforçam o mesmo padrão do JSONB: extensão nativa cobrindo o que levaria a adotar um banco especializado à parte.

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
- [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]]
- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]] — arquitetura processo-por-conexão, PgBouncer como padrão, e comparação de performance analítica com MySQL
