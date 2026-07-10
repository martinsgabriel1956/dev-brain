---
type: concept
title: "Rúbrica de Verificação (Agentes)"
aliases: ["rubrica", "critério de aprovação de agente", "rubric agentico"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 1
tags: [rubrica, verificador, planner-executor-critic, qualidade, agentes]
skill: tech-mentor-ai
status: draft
---

# Rúbrica de Verificação (Agentes)

Conjunto explícito de critérios, gerado junto com o prompt de uma subtarefa, que define quando essa subtarefa está "cumprida". É o contrato entre o [[wiki/concepts/planner-executor-critic|Planner]] que a criou e o Verificador/Critic que vai julgá-la — não é o executor que decide se terminou, é a rúbrica.

## Por Que Gerar a Rúbrica Junto com o Prompt

Se o critério de aceite só existir na cabeça de quem escreveu o prompt (o humano), o verificador não tem como julgar objetivamente. Ao fazer o Planner gerar a rúbrica no mesmo momento em que gera o prompt, o critério de sucesso fica explícito e é a mesma peça de informação enviada ao subagente executor e ao verificador — reduzindo ambiguidade entre "o que foi pedido" e "o que será cobrado".

## Como é Usada no Loop

1. Planner gera prompt + rúbrica para a subtarefa
2. Executor produz o resultado
3. Verificador recebe **a rúbrica** e o resultado — não o prompt original — e julga se cada exigência foi cumprida
4. Se reprovado, o verificador gera um follow-up específico apontando qual exigência da rúbrica não foi atendida (ex.: "reescreva o relatório incluindo uma tabela markdown com colunas")
5. O número de tentativas de follow-up antes de desistir é um limite determinístico definido por quem constrói o sistema — não pela LLM

## Diferença para Validação Ad-Hoc

Sem rúbrica, "verificar o resultado" vira um julgamento vago e sujeito a reinterpretação a cada rodada. Com rúbrica, o verificador tem uma lista fechada de exigências — mais próximo de um checklist testável do que de uma opinião do modelo.

## Key Sources

- [[wiki/sources/loop-engineering-planner-critic-grafo]]
