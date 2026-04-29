---
type: source
title: "Temporal — Durable Execution e Workflow Orchestration"
aliases: ["temporal", "durable execution", "temporal workflow", "temporal activities", "temporal signals", "workflow orchestration"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/temporal.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [temporal, durable-execution, workflow-orchestration, sagas, activities, signals, workflow-versioning]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Temporal: Durable Execution — workflows são funções que persistem estado automaticamente, sobrevivem a crashes e reiniciam de onde pararam. Workflow define o fluxo; Activities fazem o I/O (chamadas externas, banco). Signals para input externo durante execução. Queries para estado atual. Versionamento de workflows para mudanças em workflows em execução. Melhor para: Sagas complexas, processos de negócio de longa duração (horas/dias).

## Key Claims

**Claim:** Temporal persiste o histórico de execução — workflow sobrevive a crash do worker e continua de onde parou.
**Evidence:** Worker crash durante `step 3 de 10`: sem Temporal, o processo recomeça do zero ou fica em estado indefinido. Com Temporal: event history persiste no Temporal Server. Worker novo conecta, replaya o histórico (replay é determinístico), retoma em `step 4`. Sem perda de progresso, sem lógica de checkpoint manual.
**Confidence:** alta

**Claim:** Activities são os únicos pontos de I/O — Workflow deve ser determinístico e livre de side effects.
**Evidence:** Regra: nenhum I/O no Workflow (sem HTTP calls, sem banco, sem `Date.now()`, sem `Math.random()`). Tudo isso em Activities. Razão: Workflow é replayado pelo Temporal para reconstruir estado. Se `Date.now()` retorna valores diferentes no replay, o replay diverge do original → erro de non-determinism. Activities têm retry automático configurável.
**Confidence:** alta

**Claim:** Signals permitem input externo em workflows em execução — sem polling.
**Evidence:** Workflow de aprovação: workflow aguarda em `await workflow.condition(() => approved)`. Aprovador envia Signal `approve` via API. Temporal entrega o Signal ao workflow, que sai do `await`. Alternativa sem Signal: polling de banco por status de aprovação — mais lento, acoplado ao banco.
**Confidence:** alta

## Entities & Concepts Touched

- [[entities/temporal]]
- [[concepts/durable-execution]]
- [[concepts/workflow-orchestration]]
- [[concepts/saga-pattern]]
- [[concepts/activities-temporal]]
- [[concepts/signals-temporal]]

## Open Questions

- Temporal Cloud vs self-hosted — quando o custo operacional de self-hosted justifica vs o pricing do cloud?
- Workflow versioning com Temporal — como lidar com workflows de longa duração (semanas) que precisam de mudança de lógica urgente?
