---
type: concept
title: "Output vs. Outcome (métricas de produtividade)"
aliases: ["output vs outcome", "metricas de output", "metricas de outcome", "volume vs valor"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_count: 1
tags: [engineering-metrics, ia-produtividade, dora, space, goodharts-law]
skill: tech-mentor-leadership
status: draft
---

# Output vs. Outcome

**TL;DR:** Métricas de **output** medem o que o time devolve (linhas, commits, PRs, velocidade, volume); métricas de **outcome** medem o efeito no mundo (bugs em produção, incidentes, tempo de ciclo, facilidade de mudar o sistema). A IA é o tipo de ferramenta que **infla output independente de qualidade** — por isso medir output é enganoso justamente quando se usa IA.

## Por que a distinção importa mais com IA

Se você mede volume, a IA vai fazer o número subir — e a percepção acompanha: 95% dos devs se sentem mais produtivos, mesmo produzindo código de qualidade menor. É [[wiki/concepts/goodharts-law]] em ação: a métrica de atividade vira alvo e perde significado. No vocabulário do SPACE (ver [[wiki/concepts/dora-metrics]]), **Activity** sozinha é gamificável; o que vale é **Performance/outcome**.

## As perguntas de outcome que revelam a verdade

1. **Bug rate pós-deploy** — se a IA aumenta produtividade *e* qualidade, bugs após o deploy têm que **cair**. Se sobem, há problema.
2. **Ciclo de code review** — se o último PR levou mais de uma semana para mergear, o gargalo é o **processo**, não a pessoa; adicionar mais PRs piora. Ver [[wiki/concepts/paradoxo-da-aceleracao]].
3. **Facilidade de mudar o codebase** — o sistema **como um todo** (não só o módulo tocado) está mais fácil ou mais difícil de mudar?

## A pergunta-raiz

> Você está usando IA para escrever **mais** código ou **melhor** código?

São escolhas diferentes que produzem resultados diferentes — e as métricas de output não distinguem uma da outra.

## Conceitos Relacionados

[[wiki/concepts/goodharts-law]] · [[wiki/concepts/dora-metrics]] · [[wiki/concepts/paradoxo-da-aceleracao]] · [[wiki/concepts/roi-de-ia]] · [[wiki/concepts/code-review]]

## Key Sources

- [[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]]
