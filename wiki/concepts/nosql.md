---
type: concept
title: "NoSQL"
aliases: ["not only sql", "bancos não relacionais"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [banco-de-dados, nosql, mongodb, redis, cassandra, system-design]
skill: tech-mentor-system-design
status: stable
---

# NoSQL

Categoria de bancos de dados que não seguem o modelo relacional. Cada tipo resolve um problema diferente.

| Tipo | Exemplos | Use para |
|---|---|---|
| **Document** | MongoDB, Firestore | Dados semi-estruturados, schema flexível |
| **Key-Value** | Redis, DynamoDB | Acesso por chave única, alta performance |
| **Wide-Column** | Cassandra, DynamoDB | Escrita massiva, série temporal, IoT |
| **Graph** | Neo4j, Neptune | Relacionamentos complexos |
| **Search** | Elasticsearch | Full-text search, faceted search |

## Quando Não Usar

- Dados financeiros ou transacionais → use relacional com [[concepts/acid]]
- Relacionamentos complexos entre entidades → JOINs relacionais são mais simples
- Quando você quer schema flexível mas já tem PostgreSQL → use `JSONB`

## Consistência

A maioria oferece consistência eventual. Para inventário crítico e saldos, isso é inaceitável. → [[concepts/relational-vs-nosql]]

## Key Sources

- [[sources/banco-de-dados]]
