---
type: source
title: "Orquestração Multi-agente"
aliases: ["multi-agent", "orquestracao agentes", "supervisor pattern", "swarm"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/agentes-orquestracao.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [agentes, multi-agente, orquestracao, supervisor-pattern, handoff, swarm, langgraph, temporal, durable-execution]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Multi-agente faz sentido quando a task tem paralelismo real ou requer especialistas distintos. Os 4 padrões principais: Supervisor (orquestrador delega), Handoff (transferência de contexto), Swarm (paralelo + agregação), Planner-Executor-Critic (loop reflexivo). LangGraph gerencia estado como grafo. Temporal/Inngest para durabilidade.

## Key Claims

**Claim:** Multi-agente só vale quando há paralelismo real ou especialistas distintos.
**Evidence:** Um agente geral com 20 tools é melhor que 5 agentes de 4 tools cada se as tasks forem sequenciais. O overhead de comunicação entre agentes (context passing, latência) custa mais do que economiza se não houver paralelismo real.
**Confidence:** alta

**Claim:** Supervisor Pattern é o mais seguro para orquestração controlada.
**Evidence:** Orquestrador central mantém estado global, delega sub-tasks, valida resultados antes de prosseguir. Trade-off: bottleneck no orquestrador, mas controle total sobre fluxo e rollback.
**Confidence:** alta

**Claim:** LangGraph representa estado de agente como grafo — nodes são passos, edges são transições condicionais.
**Evidence:** Permite loops, branches e human-in-the-loop nativos. State é tipado e persistido automaticamente entre execuções (checkpointing). Vantagem sobre chains lineares: fluxos não-lineares sem código de controle manual.
**Confidence:** alta

**Claim:** Durable Execution (Temporal/Inngest) resolve agentes long-running com garantia de at-least-once.
**Evidence:** Workflows são gravados step a step. Crash no meio → retoma do último passo completado. Temporal: open source, complexo de operar. Inngest: managed, mais simples, menos controle.
**Confidence:** alta

**Claim:** Error boundaries categorizados são essenciais — cada categoria tem estratégia distinta.
**Evidence:** tool_error → retry com backoff. parsing_error → retry com instrução mais explícita. context_overflow → compressão. infinite_loop → human review. budget_exceeded / safety_violation → stop imediato.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/supervisor-pattern]]
- [[concepts/handoff-pattern]]
- [[concepts/swarm-pattern]]
- [[wiki/concepts/planner-executor-critic]]
- [[wiki/concepts/langgraph]]
- [[concepts/durable-execution]]
- [[entities/temporal]]
- [[concepts/error-boundary-agents]]
- [[concepts/checkpointing-agents]]

> Nota de lint (2026-07-10): `planner-executor-critic` e `langgraph` foram criados em `wiki/concepts/` durante a ingestão de [[wiki/sources/loop-engineering-planner-critic-grafo]] — links acima corrigidos para o path atual. `supervisor-pattern`, `handoff-pattern`, `swarm-pattern`, `durable-execution`, `error-boundary-agents` e `checkpointing-agents` permanecem como links quebrados (nunca criados), fora do escopo desta ingestão.

## Open Questions

- Como passar contexto entre agentes no Handoff Pattern sem vazar informação sensível?
- Qual o overhead real de latência do LangGraph vs scaffolding manual?
