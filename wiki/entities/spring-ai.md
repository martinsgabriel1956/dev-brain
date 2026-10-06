---
type: entity
title: "Spring AI"
aliases: ["Spring AI project"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [java, spring, spring-ai, rag, llm, framework]
skill: tech-mentor-ai
status: stub
---

# Spring AI

Projeto do ecossistema [[wiki/entities/spring-boot]] para integrar IA em aplicações Java. Peças usadas no demo de [[wiki/sources/rag-spring-ai-microagente-recomendacao-michele-brito]]:

- **`VectorStore`**: abstração sobre bases vetoriais ([[wiki/entities/pgvector]]); `add` grava e a busca por similaridade recebe query, topK e filtro ([[wiki/concepts/vector-store]]).
- **`Document`**: id, conteúdo, metadados, embedding.
- **Modelos de embedding**: chamados automaticamente ao gravar/consultar (starter do Google/Gemini no exemplo).
- **`ChatClient`**: fluxo `prompt → user → call → content` sobre vários LLMs.

Versões no exemplo: Spring Boot 4, Java 25. Detalhes de API só pela narração **[external, não verificado: https://docs.spring.io/spring-ai/reference/]**.

## Key Sources

- [[wiki/sources/rag-spring-ai-microagente-recomendacao-michele-brito]]
