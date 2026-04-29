---
type: source
title: "Performance: USE Method, RED Method, Four Golden Signals e k6"
aliases: ["performance methods", "use method", "red method", "four golden signals", "k6", "load testing", "latency p95 p99"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/performance-methods.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [performance, use-method, red-method, four-golden-signals, k6, load-testing, flame-graph, slo, latency]
skill: tech-mentor-infra
status: stable
---

## TL;DR

3 frameworks diagnósticos: USE (Utilization/Saturation/Errors — para recursos), RED (Rate/Errors/Duration — para serviços), Four Golden Signals (Google SRE — Latency/Traffic/Errors/Saturation). k6 para load testing com thresholds como SLOs. Flame Graph para CPU profiling. p95/p99 são as métricas corretas — p50 esconde outliers que afetam 5-1% dos usuários.

## Key Claims

**Claim:** p95/p99 são as métricas corretas para SLOs — p50 esconde problemas que afetam usuários reais.
**Evidence:** p50 = 100ms, p95 = 800ms, p99 = 2000ms. p50 parece ótimo — mas 5% dos usuários esperam 800ms e 1% espera 2s. Para SLO de "99% das requests < 500ms": p99 = 500ms. k6: `http_req_duration["p(95)"] < 500` como threshold. Alertar em p95 > 500ms em produção.
**Confidence:** alta

**Claim:** k6 permite definir SLOs como thresholds no teste — falha automaticamente em CI se performance degradar.
**Evidence:** `thresholds: { "http_req_duration": ["p(95)<500", "p(99)<1000"], "http_req_failed": ["rate<0.01"] }`. Script de load test commited no repo. CI roda k6 contra staging antes de cada deploy. Se p95 piora, pipeline falha. Performance regression detectada antes de chegar em produção.
**Confidence:** alta

**Claim:** USE Method é disciplinado para diagnóstico de infra — percorre todos os recursos antes de concluir.
**Evidence:** Processo: para cada recurso (CPU, memória, disco I/O, rede, connections de banco): medir Utilization (%), Saturation (fila), Errors. Diagnóstico sistemático evita pular para conclusão prematura. CPU 70% utilização sem saturation = ok. CPU 70% + saturation alta = gargalo iminente. Diferença crítica ignorada sem USE.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/use-method]]
- [[concepts/red-method]]
- [[concepts/four-golden-signals]]
- [[entities/k6]]
- [[concepts/load-testing]]
- [[concepts/flame-graph]]
- [[concepts/slo]]
- [[concepts/latency-percentiles]]

## Open Questions

- k6 com complex auth flows (OAuth2 com token refresh) — como manter tokens válidos durante load test de longa duração?
- Four Golden Signals em gRPC streaming — como medir duration em streams bidirecionais contínuos?
