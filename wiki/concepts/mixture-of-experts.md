---
type: concept
title: "Mixture of Experts (MoE)"
aliases: ["MoE", "mixture of experts", "mistura de especialistas"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 1
tags: [moe, arquitetura, llm, open-source, custo]
skill: tech-mentor-ai
status: stub
---

# Mixture of Experts (MoE)

Arquitetura de rede neural onde o modelo é composto por múltiplas redes "especialistas" e um mecanismo de roteamento que, para cada token, ativa apenas um subconjunto dos especialistas. Resultado: modelo com capacidade total alta, mas custo de inferência menor que um transformer denso equivalente.

## Por que Importa para Devs

MoE é a principal razão pela qual modelos open source chineses (Qwen, GLM, Kimi K2.6) conseguem oferecer preços muito menores que modelos frontier como Opus ou GPT-5.5:
- Menos parâmetros ativados por inferência → menos VRAM necessária → custo operacional menor
- Permite modelos com parâmetros totais grandes mas custo de inferência de modelos menores

Modelos comerciais (Anthropic, OpenAI) não adotam MoE publicamente em seus modelos principais, o que contribui para o custo mais alto.

## Qualidade vs Custo

MoE não significa pior qualidade. Em 2025–2026, modelos MoE open source passaram de "praticamente inutilizáveis" para "suficientes para muitas tarefas profissionais". A diferença está no tipo de tarefa:
- Tarefas complexas/novas: modelos densos (Opus, GPT-5.5) ainda levam vantagem
- Tarefas bem especificadas com bom contexto: MoE open source entrega resultado comparável por fração do preço

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
