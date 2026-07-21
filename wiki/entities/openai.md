---
type: entity
title: "OpenAI"
aliases: ["Open AI"]
date_created: 2026-05-17
date_updated: 2026-07-21
source_count: 4
tags: [openai, organização, llm, ia]
skill: tech-mentor-ai
status: stable
---

# OpenAI

## Descrição

Organização de pesquisa em inteligência artificial fundada em 2015. Responsável pelo desenvolvimento da família GPT de modelos de linguagem e pelos produtos ChatGPT e API da OpenAI.

## Modelos Relevantes para a Wiki

- **GPT-2** (2019) — arquitetura base usada no GPT-3
- **GPT-3** (2020) — 175B parâmetros, formalizou [[in-context-learning]] e [[few-shot-learning]]
- **InstructGPT** (2022) — GPT-3 alinhado via RLHF / instruction tuning
- **GPT-4** (2023) — modelo multimodal, sem tamanho publicado

## Contribuições Teóricas Relevantes

- [[scaling-laws]] — Kaplan et al. (2020), pesquisadores da OpenAI
- [[in-context-learning]] — Brown et al. (2020) via GPT-3
- [[foundation-model]] — GPT-3 como exemplo paradigmático

## Modelos Adicionais

- **Codex** (2021) — modelo especializado em código, base do GitHub Copilot. Translada linguagem natural → código em mais de 12 linguagens.

## Tokenizador

Criadora do `tiktoken`, tokenizer BPE oficial da OpenAI (implementação JS: `js-tiktoken`). `o200k_base` é o tokenizer usado pelo GPT-4o — ver [[byte-pair-encoding]] e [[tokenizacao]].

## Competição com Open Source Chinês

Segundo [[wiki/sources/kimi-k3-china-mercado-ia-open-source]], o tamanho dos modelos frontier da OpenAI não é público — estimado em 5–10T parâmetros, deduzido pelo alto preço de inferência cobrado via API. A fonte especula (sem confirmação) que a OpenAI possa usar arquitetura [[wiki/concepts/mixture-of-experts|MoE]], por analogia com modelos open source chineses como o Kimi K3. Ver também [[wiki/concepts/corrida-preco-qualidade-llm]].

## Fontes

- [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
- [[wiki/sources/microsoft-prompt-engineering-guide]]
- [[wiki/sources/tokens-llm-fundamentos-typescript]]
- [[wiki/sources/html-vs-markdown-para-agentes-de-ia]] — Prompt Guidance da OpenAI recomenda Markdown estruturado (não HTML); mantém ferramenta própria de otimização de prompt por modelo
- [[wiki/sources/kimi-k3-china-mercado-ia-open-source]] — tamanho estimado (5-10T parâmetros) por dedução de preço; hipótese especulativa de arquitetura MoE
