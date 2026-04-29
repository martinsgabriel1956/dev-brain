---
type: concept
title: "Distributed Tracing"
aliases: ["tracing distribuído", "opentelemetry", "spans", "trace context"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [distributed-tracing, observabilidade, opentelemetry, jaeger, spans, w3c-trace-context]
skill: tech-mentor-infra
status: stub
---

# Distributed Tracing

Técnica de observabilidade que registra o caminho completo de um request por múltiplos serviços, mostrando latência por etapa.

**Conceitos:** Trace (fluxo completo end-to-end) → Spans (unidade de trabalho com duração) → traceparent (W3C padrão de propagação entre serviços).

**Padrão de instrumentação:** OpenTelemetry SDK → OTel Collector → Jaeger ou Grafana Tempo.

**HttpInstrumentation** propaga `traceparent` automaticamente em todo axios/fetch — sem mudar código de negócio.

**Sampling obrigatório:** não rastreie 100% das requests. Overhead ~5%; usar tail-based sampling.

**Quando usar:** > 2–3 serviços em cadeia. Abaixo disso, APM + logs estruturados são suficientes.

## Key Sources

- [[sources/distributed-tracing]]
