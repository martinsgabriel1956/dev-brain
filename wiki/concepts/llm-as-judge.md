---
type: concept
title: "LLM-as-a-Judge"
aliases: ["llm as judge", "LLM como juiz", "juiz de IA"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 1
tags: [evals, llm, avaliacao, agentes, code-review]
skill: tech-mentor-ai
status: stub
---

# LLM-as-a-Judge

Usar um LLM para avaliar/classificar a saída de outro (ou de si mesmo). Na fonte, aparece como o **segundo classificador** que confere se a mudança precisa do número de revisores humanos que o primeiro atribuiu ([[wiki/concepts/classificador-de-risco-de-revisao-humana]]) e como a etapa de verificação de achados ([[wiki/concepts/consenso-multiagente-em-code-review]]) em [[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]].

Para uso em evals de produção (G-Eval, RAGAS, golden dataset), ver a referência `production-evals.md` da skill [skill: tech-mentor-ai] e [[wiki/concepts/evals-llm]], [[wiki/concepts/golden-dataset]].

## Pendências

- Viés do juiz (mesmo modelo/família do autor), calibração e custo — sem tratamento dedicado no wiki ainda.

## Key sources

- [[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]]
