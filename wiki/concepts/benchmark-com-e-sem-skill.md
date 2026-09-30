---
type: concept
title: "Benchmark Com vs. Sem Skill"
aliases: ["with skill vs without skill", "delta de skill", "skill ablation"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [skills, evals, benchmark, haiku, opus, modelo, custo]
skill: tech-mentor-ai
status: draft
---

# Benchmark Com vs. Sem Skill

## TL;DR

Rodar o mesmo conjunto de prompts + asserções **com** e **sem** a skill, por modelo, e comparar o delta. Serve para decidir se a skill **merece existir** no projeto. Relato da fonte: skill de migração de banco de dados — **Opus 100/100 com ou sem skill** (skill dispensável); **Haiku ~90% com vs. ~50% sem** (delta ~40 pts) ([[wiki/sources/avaliacao-de-skills-skill-creator-description-e-benchmark]]).

## Estrutura da execução

- Pastas de iteração por modelo (Haiku, Opus), cada uma com `with_skill` / `without_skill`.
- Subagentes encadeados rodam os prompts em paralelo ([[wiki/concepts/subagentes]]).
- Benchmark consolida o que funcionou e falhou; relatório e sumário executivo em HTML com grades por asserção.

## Implicações

- **Skill como compensação de modelo fraco:** o valor cai à medida que o modelo melhora — reavaliar skills a cada troca de modelo. Liga-se a [[wiki/concepts/modelo-por-leverage-tarefa]] e [[wiki/concepts/roteamento-automatico-de-modelo]]: skill + modelo barato pode substituir modelo caro.
- **Custo de contexto de skills inúteis:** skill que não move o delta só ocupa espaço/roteamento ([[wiki/concepts/skills-agente]] — "Skill Que Atrapalha").

## Cautelas

Amostra e variância não informadas; um único domínio (migração de banco). Ver [[wiki/concepts/avaliacao-de-skills]].

## Key sources

- [[wiki/sources/avaliacao-de-skills-skill-creator-description-e-benchmark]]
