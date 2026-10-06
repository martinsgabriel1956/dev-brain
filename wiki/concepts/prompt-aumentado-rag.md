---
type: concept
title: "Prompt aumentado (etapa de aumento do RAG)"
aliases: ["prompt enriquecido", "augmentation", "enriquecimento de prompt"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [rag, prompt, contexto, politicas, llm]
skill: tech-mentor-ai
status: draft
---

# Prompt aumentado

Segunda etapa do [[wiki/concepts/rag-tres-etapas|RAG]]: junta três coisas numa única `String` enviada ao LLM:

1. a **entrada** que disparou o fluxo (ex.: a order criada);
2. o **contexto recuperado** (listas de documentos: catálogo e histórico);
3. **regras e políticas** pré-definidas (ex.: só recomendar tours da mesma região; não repetir tour já comprado).

No código da fonte, a montagem fica em método isolado, separado da recuperação e da chamada ao LLM.

## Observação

As regras vivem **no prompt**: o LLM pode descumpri-las, e nada valida a saída no exemplo (**inferência minha**; ver [[wiki/concepts/prompt-engineering]] e [[wiki/concepts/alucinacao-llm]]). Quanto maior o contexto, maior o risco de [[wiki/concepts/degradacao-de-contexto]]; ver [[wiki/concepts/janela-de-contexto]].

## Key Sources

- [[wiki/sources/rag-spring-ai-microagente-recomendacao-michele-brito]]
