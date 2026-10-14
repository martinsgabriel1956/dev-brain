---
type: concept
title: "Vector store"
aliases: ["embedding store", "banco vetorial", "base vetorial", "vector database"]
date_created: 2026-10-06
date_updated: 2026-10-14
source_count: 2
tags: [rag, vector-store, embeddings, banco-de-dados, similaridade]
skill: tech-mentor-ai
status: draft
---

# Vector store

Base que guarda **embeddings** junto ao conteúdo e metadados e responde a consultas por **similaridade** (vizinhos mais próximos), não por igualdade como SQL. Opções citadas: [[wiki/entities/pgvector]] (extensão do [[wiki/concepts/postgresql]]) e Pinecone.

## Estrutura de um registro

`id`, `content` (texto), `metadata`, `embedding`. É o mesmo desenho do tipo `Document` do [[wiki/entities/spring-ai]] e da tabela `vector_store` que ele cria por padrão. Ver também [[wiki/concepts/chunking]].

## Uso

- Escrita: [[wiki/concepts/indexacao-vetorial]].
- Leitura: [[wiki/concepts/recuperacao-com-filtro-de-metadados]] (query + topK + filtro). Ver [[wiki/concepts/top-k-retrieval]].

Comparação de bancos e tuning (HNSW, multi-tenancy): [[wiki/concepts/rag-arquitetura-avancada]].

## Key Sources

- [[wiki/sources/rag-spring-ai-microagente-recomendacao-michele-brito]]

## Adição (2026-10-14)

Com embeddings multimodais um item pode ter mais de um vetor (imagem, metadados); mais dimensões, mais armazenamento: [[wiki/concepts/reducao-de-dimensoes-de-embedding]].

- [[wiki/sources/gemini-embedding-2-embedding-multimodal-google]] — vários vetores por item (imagem + metadados) e custo de armazenar 3072 dimensões
