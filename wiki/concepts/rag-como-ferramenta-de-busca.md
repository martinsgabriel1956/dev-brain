---
type: concept
title: "RAG como Ferramenta de Busca"
aliases: ["RAG é um problema de busca", "retrieval como tool", "agentic RAG (visão prática)"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [rag, tool-use, retrieval, agentes]
skill: tech-mentor-ai
status: draft
---

# RAG como Ferramenta de Busca

Enquadramento em que RAG é, acima de tudo, um **problema de busca**. Depois que as LLMs passaram a chamar ferramentas de forma consistente ([[wiki/concepts/tool-call]], [[wiki/concepts/tool-use-agents]]), o retrieval virou uma **tool**: o agente a chama, ela consulta o banco e devolve chunks, e a LLM responde.

## Consequências

- Retrieval é **uma etapa** (o R); o agente gera depois.
- O agente pode **refazer a pergunta** e buscar de novo, mas as chamadas devem ter **limite** para evitar loop.
- A qualidade da resposta depende mais da qualidade da busca ([[wiki/concepts/hybrid-search]], [[wiki/concepts/top-k-retrieval]]) do que do modelo.
- Para o pipeline completo (ingestão, chunking, metadados), ver [[wiki/concepts/rag-arquitetura-avancada]] e [[wiki/sources/rag-introducao-pipeline-completo]].

## Key sources

- [[wiki/sources/rag-busca-hibrida-semantica-e-textual-ronald-hulk]]
