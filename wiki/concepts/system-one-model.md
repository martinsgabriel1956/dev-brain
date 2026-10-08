---
type: concept
title: "System One Model"
aliases: ["system 1 model", "modelo system one"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [ia, system-one-model, classificacao, decisao]
skill: tech-mentor-ai
status: draft
---

# System One Model

Categoria de modelo (nome inspirado no "System 1" de Kahneman, pensamento rápido) que **decide em vez de escrever**: recebe estado + [[wiki/concepts/perguntas-tipadas-choice-score-noul]] e devolve decisões tipadas com probabilidade e confiança, em paralelo, sem gerar texto token a token. Primeiro exemplar: [[wiki/entities/jev]] da [[wiki/entities/typesafe-ai]]. Treino: [[wiki/concepts/rlcd]].

## Contraste com LLM

| | LLM (gerativo) | System One |
|---|---|---|
| Saída | texto (JSON simulado) | valor tipado + probabilidades + confiança |
| Pós-processo | parse, validação, retry | nenhum |
| Latência/custo | alto (token a token) | baixo (paralelo) |
| Uso | raciocínio aberto, texto | classificar/ramificar: [[wiki/concepts/jev-para-ramificar-llm-para-ler]] |

Complementa, não substitui, o LLM; ver também [[wiki/concepts/cascade-pattern-llm]] e [[wiki/concepts/saida-estruturada-llm]] (que tenta forçar o schema no LLM; aqui o schema é nativo).

## Key sources
- [[wiki/sources/jev-typesafe-ai-system-one-model-decisoes-tipadas-codigo-fonte-tv]]
