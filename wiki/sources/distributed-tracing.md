---
type: source
title: "Distributed Tracing"
aliases: ["opentelemetry", "jaeger", "tracing", "spans", "trace context"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [distributed-tracing, opentelemetry, jaeger, observabilidade, spans, w3c-trace-context, system-design]
skill: tech-mentor-infra
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/distributed-tracing.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# Distributed Tracing

## TL;DR

Distributed Tracing mostra o caminho completo de um request por múltiplos serviços, com latência por etapa. Conceitos fundamentais: Trace (fluxo completo), Span (unidade de trabalho), traceparent (W3C padrão de propagação). OpenTelemetry é o padrão de instrumentação; Jaeger ou Grafana Tempo são backends. Stack recomendada: OTel SDK → OTel Collector → Jaeger + Loki + Prometheus correlacionados.

## Key Claims

| Claim | Evidência |
|---|---|
| traceparent é o padrão W3C para propagação cross-service | W3C Trace Context spec |
| HttpInstrumentation do OTel propaga context automaticamente | axios/fetch não precisam ser modificados |
| Sampling é obrigatório — não rastreie 100% das requests | Overhead de ~5% com tail sampling |
| Spans customizados adicionam contexto de negócio | orderId, userId, além dos spans de infra |
| Tracing é obrigatório quando há > 2–3 serviços em cadeia | Abaixo disso, APM + logs estruturados são suficientes |

## Conceitos

- [[concepts/distributed-tracing]] — spans, traces, propagação
- [[concepts/observabilidade]] — três pilares: métricas, traces, logs
- [[concepts/opentelemetry]] — padrão de instrumentação
- [[concepts/outbox-pattern]] — propagação de trace em mensageria assíncrona

## Key Sources

_Este é o documento primário._
