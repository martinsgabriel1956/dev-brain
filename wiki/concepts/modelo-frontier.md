---
type: concept
title: "Modelos Frontier"
aliases: ["frontier models", "modelos de ponta", "modelos comerciais avancados"]
date_created: 2026-06-02
date_updated: 2026-07-24
source_count: 4
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
| Kimi K3 | Moonshot (open-weight, lançamento parcial) | 2,8T parâmetros, MoE 896/16 experts, até 75% economia de KV Cache — ver [[wiki/entities/moonshot-ai]] |
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

## Subclasse: Modelos Frontier de Cybersegurança (não-públicos)

Além dos modelos frontier de uso geral acima, surgiu em 2026 uma subclasse de modelos frontier especializados em cybersegurança ofensiva/defensiva — capazes de descobrir vulnerabilidades de software em escala industrial (falhas de décadas de idade em OpenBSD, FFmpeg, kernel Linux). Diferem dos modelos da tabela acima por não serem lançados ao público: Mitos e Fable 5 (Anthropic) e Mitos 5 foram restritos a um consórcio fechado (Glasswing) e depois formalmente bloqueados pelo governo dos EUA; o GPT 5.6 (OpenAI) seguiu o mesmo padrão de bloqueio. Japão (Sakana AI/Fugo) e China (360/Tulong Fang, Zhipu AI/GLM 5.2) já reivindicam capacidade equivalente. Ver [[wiki/sources/mitos-fable-5-bloqueio-governo-eua-cyberseguranca]].

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/kimi-k3-china-mercado-ia-open-source]] — Kimi K3, 2,8T parâmetros, lançamento parcial
- [[wiki/sources/mitos-fable-5-bloqueio-governo-eua-cyberseguranca]] — subclasse de modelos frontier de cybersegurança bloqueados por risco de segurança nacional (Mitos, Fable 5, GPT 5.6)
