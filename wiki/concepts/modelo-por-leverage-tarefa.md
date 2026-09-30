---
type: concept
title: "Alocação de Modelo por Alavancagem da Tarefa"
aliases: ["model routing by leverage", "leverage-based model selection", "alavancagem de tarefa"]
date_created: 2026-07-21
date_updated: 2026-09-29
source_count: 3
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

## Terceiro Eixo: Velocidade

[[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] amplia essa heurística com um eixo que a formulação original (só alavancagem → custo) não cobria explicitamente: **velocidade**, tratada separadamente de inteligência e de custo. Um bug fix simples e bem definido pode ter baixa alavancagem (não justifica o modelo mais forte) mas alta urgência de velocidade (não pode esperar a latência de um modelo grande) — nesse caso a recomendação não é o modelo mais barato genérico, mas o modelo mais rápido disponível (ex.: Gemini Flash), mesmo que não seja o mais barato por token. Ou seja, a matriz de decisão completa cruza três variáveis — inteligência, velocidade, custo — não duas.

## Relação com Outros Conceitos

- [[wiki/concepts/subagentes]] — a etapa de implementação pode ser paralelizada entre vários subagentes rodando o modelo mais leve
- [[wiki/concepts/worktree-paralelismo]] — paralelismo a nível de file system para as mesmas tarefas de implementação, quando independentes o suficiente para branches separados

## Skill Como Alternativa a Modelo Mais Caro

No benchmark de [[wiki/sources/avaliacao-de-skills-skill-creator-description-e-benchmark]], uma skill elevou o Haiku de ~50% para ~90% na tarefa testada, enquanto o Opus atingiu 100% sem ela — indício de que skill + modelo menor é uma alavanca de custo, e que a necessidade da skill deve ser reavaliada ao trocar de modelo ([[wiki/concepts/benchmark-com-e-sem-skill]]). Evidência de um único caso, sem amostra informada.

## Key Sources

- [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]]
- [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] — adiciona velocidade como terceiro eixo de decisão, além de alavancagem/custo
- [[wiki/sources/avaliacao-de-skills-skill-creator-description-e-benchmark]] — skill eleva Haiku de ~50% a ~90%; Opus dispensa a skill
