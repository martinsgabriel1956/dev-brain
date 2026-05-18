---
type: concept
title: "Context Window"
aliases: ["janela de contexto", "context length", "token limit"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 1
tags: [llm, context-window, tokens, prompt-engineering]
skill: tech-mentor-ai
status: stable
---

# Context Window

## Definição

Tamanho máximo de tokens que um modelo de linguagem pode processar em uma única chamada — incluindo o prompt de entrada **e** o completion gerado. Tokens que ultrapassam esse limite são descartados ou causam erro.

## Implicações para Prompt Engineering

- Prompts grandes (com histórico, exemplos, schemas) consomem tokens rapidamente.
- Para aplicações conversacionais, usar **janela deslizante (rolling window)**: manter apenas os N últimos pares input/output no contexto.
- Quanto maior o prompt, maior a latência e o custo por chamada.

## Implicações para Produção

- **Latência:** prompts maiores = respostas mais lentas. Fine-tuning pode reduzir a necessidade de prompts longos.
- **Custo:** tokens de input e output são cobrados separadamente na maioria das APIs.
- **Lost-in-the-Middle:** em contextos muito longos, modelos tendem a ignorar informações no meio — prefira informações críticas no início ou no fim.

## Evolução Histórica

| Modelo | Context Window |
|---|---|
| GPT-3 (2020) | 4.096 tokens |
| GPT-4 Turbo (2023) | 128.000 tokens |
| Gemini 1.5 Pro (2024) | 1.000.000 tokens |
| Llama 4 Scout (2025) | 10.000.000 tokens |

## Relação com Outros Conceitos

- [[prompt-engineering]] — o contexto é o espaço onde o prompt vive
- [[hyperparameters-llm]] — `max_tokens` controla o tamanho do completion
- [[in-context-learning]] — exemplos few-shot consomem tokens do context window

## Fontes

- [[wiki/sources/microsoft-prompt-engineering-guide]]
