---
type: concept
title: "Avaliação de Skills"
aliases: ["skill evals", "evaluation de skills", "testar skills"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [skills, evals, skill-creator, qualidade, harness, llm]
skill: tech-mentor-ai
status: draft
---

# Avaliação de Skills

## TL;DR

Aplicar a lógica de [[wiki/concepts/llm-evals-testing|evals]] a uma [[wiki/concepts/skills-agente|skill]]: medir, com dados, (a) se ela **é acionada** quando deveria ([[wiki/concepts/otimizacao-de-descricao-de-skill]]) e (b) se ela **melhora o resultado** frente à ausência dela ([[wiki/concepts/benchmark-com-e-sem-skill]]). Sem isso, a fonte alerta para a "falsa sensação" de saber criar uma skill decente ([[wiki/concepts/pilares-de-desenvolvimento-com-ia]]).

## Duas dimensões

| Dimensão | Pergunta | Mecanismo relatado |
|---|---|---|
| Acionamento | O harness carrega a skill nas queries certas (e não nas erradas)? | Loop de description com queries *should trigger* |
| Qualidade | A skill melhora a saída? Em qual modelo? | Execução com/sem skill, asserções por caso, relatório de grades |

## Eixos de variação

O resultado depende de client (harness), modelo, provedor e dataset — a mesma skill pode ser essencial num modelo e dispensável em outro ([[wiki/sources/avaliacao-de-skills-skill-creator-description-e-benchmark]]).

## Ciclo de melhoria

Rodar → ler o relatório item a item → entender *por que* falhou → ajustar `SKILL.md`/referências → rodar de novo. A skill melhora "progressivamente todos os dias". É a versão manual do que [[wiki/concepts/closed-loop-skill-learning]] automatiza.

## Ferramenta

[[wiki/entities/skill-creator]] (Anthropic). Scripts locais verificados: `run_loop.py`, `improve_description.py`, `run_eval.py`, `aggregate_benchmark.py`, `generate_report.py` [skill: skill-creator — verificado no diretório da skill].

## Limites e cautelas

- Sem número de amostra/variância na fonte; tratar percentuais como ilustrativos.
- Gates de eval em CI (golden dataset) são a prática de produção [skill: tech-mentor-ai — `production-evals.md`]; a fonte não os mostra.

## Key sources

- [[wiki/sources/avaliacao-de-skills-skill-creator-description-e-benchmark]]
