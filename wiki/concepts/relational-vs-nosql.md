---
type: concept
title: "Relacional vs NoSQL"
aliases: ["sql vs nosql", "relational vs document", "escolha de banco"]
date_created: 2026-04-22
date_updated: 2026-07-03
source_count: 2
tags: [banco-de-dados, nosql, postgresql, system-design, trade-offs]
skill: tech-mentor-system-design
status: stable
---

# Relacional vs NoSQL

Não existe escolha universal. Cada tipo resolve um problema diferente.

## Trade-offs

| Aspecto | Relacional | NoSQL |
|---|---|---|
| **Consistência** | [[concepts/acid]] completo | Eventual (geralmente) |
| **Queries** | JOINs complexos, agregações | Simples, por chave |
| **Escala de escrita** | Vertical (um primário) | Horizontal nativo |
| **Schema** | Rígido — segurança + integridade | Flexível — agilidade |

## Decisão

- Financeiro, multi-entidade, transações → **Relacional** ([[concepts/postgresql]])
- Dados semi-estruturados, schema muda muito → **Document** (MongoDB)
- Cache, sessão, acesso por chave → **Key-Value** (Redis)
- Escrita massiva, IoT, série temporal → **Wide-Column** (Cassandra)
- Relacionamentos complexos → **Graph** (Neo4j)
- Full-text search → **Search** (Elasticsearch)

## Antes de Migrar

[[concepts/postgresql]] consegue JSONB, full-text search básico, pg_vector e Timescaledb. Avalie extensões antes de adicionar complexidade operacional.

## Eixo Diferente: SQL Embutido no Código vs. Modelo de Dados

Essa comparação (relacional vs. NoSQL) é frequentemente confundida com uma discussão diferente: se a aplicação deve escrever SQL diretamente no código ou abstrair isso via [[wiki/concepts/orm]]/[[wiki/concepts/domain-specific-language]]. São eixos ortogonais — você pode usar SQL cru ou um ORM tanto num banco relacional quanto (via camadas de tradução) sobre um BaaS documental. Ver [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]].

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
