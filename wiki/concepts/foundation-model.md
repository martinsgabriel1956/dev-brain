---
type: concept
title: "Foundation Model"
aliases: ["modelo de fundação", "base model", "modelo base"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 1
tags: [llm, foundation-model, pré-treinamento, scaling]
skill: tech-mentor-ai
status: draft
---

# Foundation Model

## Definição

Modelo treinado em larga escala em dados não estruturados (geralmente web-scale) que serve como base para downstream tasks — seja via [[fine-tuning]], [[in-context-learning]] ou prompting direto.

O termo foi cunhado por Bommasani et al. (2021) em "On the Opportunities and Risks of Foundation Models" (Stanford), mas GPT-3 ([[wiki/sources/gpt3-language-models-are-few-shot-learners]]) é um dos primeiros exemplos paradigmáticos.

## Características

- **Escala**: treinado com ordens de magnitude mais compute do que modelos anteriores.
- **Generalidade**: capaz de realizar centenas de tarefas distintas sem retreinamento.
- **Emergência**: capacidades que não foram explicitamente treinadas aparecem em escalas suficientes (ex: aritmética, raciocínio analógico).
- **Adaptabilidade**: pode ser especializado via fine-tuning, RLHF ou ICL.

## Exemplos

- GPT-3, GPT-4 ([[wiki/entities/openai]])
- Claude (Anthropic)
- Gemini (Google)
- Llama (Meta) — open-weight

## Relação com [[scaling-laws]]

Foundation models existem porque [[scaling-laws]] tornaram previsível que modelos maiores seriam qualitativamente mais capazes — justificando o investimento de pré-treinamento.

## Fontes

- [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
- Bommasani et al. (2021) — "On the Opportunities and Risks of Foundation Models" [external]
