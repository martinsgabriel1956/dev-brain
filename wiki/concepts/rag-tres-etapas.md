---
type: concept
title: "RAG em três etapas (recuperar, aumentar, gerar)"
aliases: ["retrieve augment generate", "pipeline RAG de três etapas", "RAG"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [rag, retrieval, prompt, llm, pipeline]
skill: tech-mentor-ai
status: draft
---

# RAG em três etapas

Decomposição didática do RAG (geração aumentada por recuperação) em **Retrieval → Augmentation → Generation**:

1. **Recuperação:** a entrada vira embedding e a [[wiki/concepts/busca-semantica|busca por similaridade]] traz os top-K trechos do [[wiki/concepts/vector-store]] ([[wiki/concepts/recuperacao-com-filtro-de-metadados]]).
2. **Aumento:** monta-se o [[wiki/concepts/prompt-aumentado-rag|prompt aumentado]]: entrada + contexto recuperado + regras.
3. **Geração:** o LLM responde com base nesse prompt; reduz, mas não elimina, a [[wiki/concepts/alucinacao-llm|alucinação]].

Antes das três etapas existe a fase offline de [[wiki/concepts/indexacao-vetorial]] (chunking, embedding, gravação). Esta página cobre o desenho básico; técnicas de produção (re-ranking, HyDE, híbrida) estão em [[wiki/concepts/rag-arquitetura-avancada]] e [[wiki/concepts/hybrid-search]].

## Origem

Padrão "recuperar, então gerar" de [[wiki/entities/danqi-chen]] (2017); termo RAG de [[wiki/entities/patrick-lewis]] (2020), segundo a fonte (datas **[external, não verificado]**).

## Key Sources

- [[wiki/sources/rag-spring-ai-microagente-recomendacao-michele-brito]] — três etapas com implementação em Spring AI e uso dentro de um [[wiki/concepts/microagente]]
