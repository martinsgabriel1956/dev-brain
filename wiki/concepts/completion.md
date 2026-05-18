---
type: concept
title: "Completion"
aliases: ["completions", "conclusão do modelo", "geração de texto"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 1
tags: [llm, prompt-engineering, completion, geração]
skill: tech-mentor-ai
status: stub
---

# Completion

## Definição

O texto gerado por um modelo de linguagem em resposta a um [[prompt-engineering|prompt]]. O modelo recebe o prompt e "continua escrevendo" — como uma pessoa que recebe o começo de uma frase e a completa.

## Mecanismo

Modelos [[autoregressive-language-model|autoregressivos]] geram completions token por token. Cada novo token é amostrado com base na probabilidade condicional dado o contexto anterior (prompt + tokens já gerados).

## Controle da Completion

- **[[hyperparameters-llm|Temperature]]** — quanto de aleatoriedade na amostragem. `0` = sempre o token mais provável (determinístico).
- **`max_tokens`** — limite máximo de tokens gerados.
- **`stop sequence`** — sequência que interrompe a geração. Útil para evitar que o modelo gere variações indesejadas.

## Fontes

- [[wiki/sources/microsoft-prompt-engineering-guide]]
