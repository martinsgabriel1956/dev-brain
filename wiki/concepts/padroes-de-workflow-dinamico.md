---
type: concept
title: "Padrões de Workflow Dinâmico"
aliases: ["fan-out-and-synthesize", "adversarial verification", "verificação adversária", "classify-and-act", "generate-and-filter", "tournament", "loop until done"]
date_created: 2026-11-10
date_updated: 2026-11-10
source_count: 1
tags: [dynamic-workflow, padroes, orquestracao, agentes, anthropic]
skill: tech-mentor-ai
status: stub
---

# Padrões de Workflow Dinâmico

Seis padrões nomeados por Thariq Shihipar e Sid Bidasaria em ["A harness for every task"](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code) (02/06/2026) `[external]`, para organizar [[wiki/concepts/dynamic-workflow|workflows dinâmicos]]. O artigo não foi ingerido; só os nomes foram lidos para esta página.

- Classify-and-act
- Fan-out-and-synthesize
- Adversarial verification
- Generate-and-filter
- Tournament
- Loop until done

## Origem

[[wiki/entities/ronald-hulk]] os apresenta em [[wiki/sources/dynamic-workflows-langgraph-engenharia-reversa-ronald-hulk]] como derivados dos padrões de ["Building Effective Agents"](https://www.anthropic.com/engineering/building-effective-agents) (19/12/2024) `[external]`: prompt chaining, routing, parallelization, orchestrator-workers e evaluator-optimizer. A correspondência abaixo é inferência desta wiki, e nem o vídeo nem o trecho lido a fazem par a par.

| Padrão de 2024 | Padrão próximo de 2026 |
|---|---|
| Routing | Classify-and-act |
| Parallelization, orchestrator-workers | Fan-out-and-synthesize |
| Evaluator-optimizer | Adversarial verification, loop until done |

## Como o autor descreve o uso

- **Fan-out e síntese:** o planner divide o problema em subagentes (funil, marketing, tempo de fechamento) e um nó final consolida.
- **Verificação adversária:** outro agente testa se a resposta ou a hipótese faz sentido. Ver [[wiki/concepts/planner-executor-critic]].
- **Classify:** na versão dele, um comando explícito faz o papel do classificador.
- **Loop until done:** na versão dele, retry em caso de falha.

## Key Sources

- [[wiki/sources/dynamic-workflows-langgraph-engenharia-reversa-ronald-hulk]]
