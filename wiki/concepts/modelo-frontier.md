---
type: concept
title: "Modelos Frontier"
aliases: ["frontier models", "modelos de ponta", "modelos comerciais avancados"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 2
tags: [modelos, frontier, llm, openai, anthropic, google]
skill: tech-mentor-ai
status: draft
---

# Modelos Frontier

Os modelos de linguagem mais capazes disponíveis no mercado em um dado momento — geralmente comerciais e fechados, com bilhões de parâmetros e treinamento proprietário em escala massiva. São o padrão de referência para tarefas de codificação profissional.

## Modelos Frontier para Codificação (2026)

| Modelo | Provider | Destaque |
|---|---|---|
| Opus 4.7 | Anthropic | Top em design/frontend; preferido para review |
| GPT-5.5 | OpenAI | Melhor reasoning para tarefas novas/complexas |
| GPT-5.4 | OpenAI | Melhor custo-benefício que 5.5 para muitas tarefas |
| Gemini 3.1 | Google | Puxou contexto de 1M tokens; forte em multimodal |
| Kimi K2.6 | Moonshot (open-weight) | Resultado comparável a frontier por fração do preço |
| GLM 5.1 | Zhipu AI (open-weight) | MoE barato e eficiente |
| Qwen 3.6 | Alibaba (open-weight) | MoE; muito bom para código |

## Comerciais vs Open-Weight

**Comerciais** (Anthropic, OpenAI, Google): modelo fechado, treinamento opaco, API com compliance enterprise, custo mais alto.

**Open-weight** (Kimi, Qwen, GLM): pesos disponíveis publicamente, treinamento baseado em MoE (mais barato de rodar), preços de API muito menores. Em 2025–2026, passaram de "praticamente inúteis" para "suficientes para muitas tarefas profissionais".

## Como o GPT chegou ao nível de codificação

A OpenAI pegou o modelo O3 (alto reasoning), fez fine-tuning específico para código, e o resultado foi excelente. As versões 5.1, 5.2, 5.3, 5.4, 5.5 evoluíram sobre essa base. Não é um modelo novo — é o mesmo base com melhorias incrementais de fine-tuning e RLHF.

## Degradação e Custo

Ver [[wiki/concepts/degradacao-de-contexto]] para como a qualidade dos modelos frontier cai após ~400k tokens.

Ver [[wiki/sources/formacao-ia-devs-aula-03-llm]] para tabela de preços por token.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
