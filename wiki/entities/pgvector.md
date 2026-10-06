---
type: entity
title: "pgvector"
aliases: ["PG Vector", "PGVector"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [postgresql, pgvector, vector-store, rag, extensao]
skill: tech-mentor-ai
status: stub
---

# pgvector

Extensão do [[wiki/concepts/postgresql]] que adiciona tipo vetorial e busca por similaridade, permitindo usar o Postgres como [[wiki/concepts/vector-store]]. No demo roda no [[wiki/entities/neon-database]]; o [[wiki/entities/spring-ai]] cria a tabela `vector_store` (`id`, `content`, `metadata`, `embedding`).

## Key Sources

- [[wiki/sources/rag-spring-ai-microagente-recomendacao-michele-brito]]
- [[wiki/sources/rag-introducao-pipeline-completo]] — pgvector como opção viável que "aguenta bastante carga"
