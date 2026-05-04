---
type: concept
title: "Mental Alignment"
aliases: ["alinhamento mental", "sincronização de modelo mental", "team alignment"]
date_created: 2026-05-04
date_updated: 2026-05-04
source_count: 1
tags: [coding-agents, workflow, team, code-review]
skill: tech-mentor-ai
status: draft
---

# Mental Alignment

O real propósito do code review: manter todos no time com o mesmo modelo mental de como o codebase está mudando e por quê. Não é só sobre encontrar bugs — é sobre **sincronização cognitiva**.

## Por Que Importa em Times com IA

Quando um time usa coding agents e entrega 2–3x mais código, o problema não é mais "o código está correto?" — é "alguém além da pessoa que promoveu entende o que foi entregue?"

Sem mental alignment:
- Decisões de arquitetura tomadas implicitamente por agentes
- Tech debt que ninguém sabe que existe
- Risco de [[concepts/comprehension-debt]] em escala — toda a equipe, não só uma pessoa

## Planos como Ferramenta de Alinhamento

No [[concepts/rpi-workflow]], os planos gerados na fase de plan servem como veículo de mental alignment: um líder técnico pode ler o plano (não o código) e manter entendimento de como o sistema está evoluindo. Isso escala bem — ler 200 linhas de plano é viável diariamente; ler 2.000 linhas de código gerado, não.

## Threads de Agente em PRs

Incluir as threads de interação com o agente no PR (os prompts usados, as decisões tomadas, os resultados de build) leva o revisor numa jornada que um diff normal no GitHub não consegue:

- Não só "aqui está o que mudou"
- Mas "aqui está o raciocínio, a ordem das mudanças, e a evidência de que funciona"

## Relação com Comprehension Debt

[[concepts/comprehension-debt]] é o que acontece quando o mental alignment falha em nível individual — o dev para de entender o próprio código que entregou. Mental alignment é a versão coletiva do mesmo problema — o time para de entender o codebase como um todo.

## Key Sources

- [[sources/context-engineering-avancado-para-coding-agents]]
