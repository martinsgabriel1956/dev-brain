---
type: source
title: "Flame Graph, USE Method, RED Method e Four Golden Signals"
aliases: ["flame graph", "use method", "red method", "four golden signals", "cpu profiling", "pprof", "clinic.js"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/flame-graph-profiling.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [flame-graph, profiling, use-method, red-method, four-golden-signals, pprof, clinic-js, sre, observabilidade]
skill: tech-mentor-infra
status: stable
---

## TL;DR

4 frameworks de diagnóstico: Flame Graph (onde o CPU passa o tempo), USE Method (Utilization/Saturation/Errors — para recursos de infra), RED Method (Rate/Errors/Duration — para serviços), Four Golden Signals (Latency/Traffic/Errors/Saturation — Google SRE). Ferramentas: pprof (Go), Clinic.js/0x (Node.js). Use USE para diagnóstico de infra; RED/Golden Signals para alertas de SLO.

## Key Claims

**Claim:** Flame Graph mostra exatamente onde o CPU está sendo gasto — sem flame graph, otimização é adivinhação.
**Evidence:** Flame Graph: eixo X = tempo de CPU acumulado, eixo Y = call stack. Plateau largo = função que consome muito CPU. Identificar o plateau mais largo e otimizar essa função tem impacto imediato. Sem profiling: otimizar por intuição frequentemente melhora código que não é o gargalo real.
**Confidence:** alta

**Claim:** USE Method é o framework correto para diagnosticar problemas de infra — analisa recursos, não serviços.
**Evidence:** USE: para cada recurso (CPU, memória, disco, rede): Utilization (% utilizado), Saturation (fila de espera), Errors (erros do recurso). CPU 100% utilização + alta saturation = CPU bound. Memória alta + swap = memory bound. Disciplinado: percorre todos os recursos antes de concluir o diagnóstico.
**Confidence:** alta

**Claim:** Four Golden Signals (Google SRE) são a base mínima para alertas de serviço — Latency, Traffic, Errors, Saturation.
**Evidence:** Latency (p50/p95/p99 de requisições). Traffic (req/s). Errors (taxa de erro %). Saturation (% de capacidade). Alerta em Latency p95 > 500ms e Error rate > 1% cobre 90% dos incidentes. RED Method (Rate, Errors, Duration) é a versão mais simples — mesmos princípios, nomenclatura diferente.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/flame-graph]]
- [[concepts/use-method]]
- [[concepts/red-method]]
- [[concepts/four-golden-signals]]
- [[concepts/cpu-profiling]]
- [[entities/pprof]]
- [[entities/clinic-js]]
- [[concepts/sre]]

## Open Questions

- Flame Graph em produção com alta carga — como coletar CPU profile sem impacto perceptível?
- Continuous profiling (Pyroscope, Parca) em microserviços — como correlacionar profiles com traces?
