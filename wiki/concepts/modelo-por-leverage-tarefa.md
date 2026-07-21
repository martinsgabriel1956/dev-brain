---
type: concept
title: "Alocação de Modelo por Alavancagem da Tarefa"
aliases: ["model routing by leverage", "leverage-based model selection", "alavancagem de tarefa"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [claude-code, model-routing, agentes, custo, arquitetura-de-agentes]
skill: tech-mentor-ai
status: draft
---

# Alocação de Modelo por Alavancagem da Tarefa

## TL;DR

Heurística de custo/benefício para escolher qual modelo usar em cada etapa de um workflow agêntico: quanto maior o impacto (alavancagem) de uma decisão — planejamento, arquitetura — mais justificado é usar o modelo mais forte e caro disponível; quanto mais rotineira e mecânica a tarefa, mais adequado é um modelo mais leve e barato.

## O Raciocínio

Um erro de planejamento ou de decisão arquitetural se propaga para todo o trabalho subsequente — o custo de errar é alto, então vale pagar mais (tempo, tokens, latência) por um modelo mais capaz nessa etapa. Já uma tarefa de implementação mecânica, bem especificada por uma spec clara, tem risco menor e não precisa do mesmo nível de raciocínio.

## Workflow Sugerido

```
Modelo forte (ex.: Fable)     → planejamento, spec, decisões de arquitetura
Modelo intermediário (ex.: Opus) → quebra da spec em tarefas menores
Modelo mais leve (ex.: Sonnet) → implementação das tarefas, possivelmente
                                   em múltiplos subagentes paralelos
```

## Relação com Outros Conceitos

- [[wiki/concepts/subagentes]] — a etapa de implementação pode ser paralelizada entre vários subagentes rodando o modelo mais leve
- [[wiki/concepts/worktree-paralelismo]] — paralelismo a nível de file system para as mesmas tarefas de implementação, quando independentes o suficiente para branches separados

## Key Sources

- [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]]
