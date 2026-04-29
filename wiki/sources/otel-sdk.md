---
type: source
title: "OpenTelemetry — SDK TypeScript, Collector Pipeline e Tail Sampling"
aliases: ["opentelemetry", "otel sdk", "distributed tracing", "spans", "otlp", "structured logging otel"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/otel-sdk.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [opentelemetry, otel-sdk, distributed-tracing, spans, metrics, otlp, auto-instrumentation, typescript]
skill: tech-mentor-infra
status: stable
---

## TL;DR

OpenTelemetry: padrão unificado para traces, métricas e logs — vendor-agnostic. SDK TypeScript inicializa ANTES de qualquer import. Auto-instrumentation cobre HTTP, Express, Prisma, Redis automaticamente. Instrumentação manual para lógica de negócio crítica (`tracer.startActiveSpan`). Tail Sampling no Collector: retém 100% dos erros, descarta requests normais. Exporta para Jaeger, Grafana Tempo, Datadog.

## Key Claims

**Claim:** SDK deve ser inicializado antes de qualquer import do app — ordem de import determina se auto-instrumentation funciona.
**Evidence:** `require("tracing")` antes de `require("express")`. Se Express for importado antes do SDK, o auto-patcher não consegue interceptar a criação do servidor. Node.js: `--require ./tracing.js` no start command. Falha silenciosa: app funciona mas sem traces dos requests HTTP.
**Confidence:** alta

**Claim:** Instrumentação automática cobre 80% dos casos — instrumentação manual para lógica de negócio.
**Evidence:** `getNodeAutoInstrumentations()`: HTTP, Express, gRPC, Redis, PostgreSQL, MongoDB, GraphQL — sem código adicional. Lacuna: lógica de negócio custom, chamadas a serviços sem biblioteca instrumentada, processamento de filas interno. Para esses casos: `tracer.startActiveSpan("processOrder", span => { ... span.end() })`.
**Confidence:** alta

**Claim:** Attributes semânticos no span são o que torna traces pesquisáveis — sem eles, trace é inútil para debugging.
**Evidence:** Span sem attributes: "processOrder levou 500ms" — não diz nada. Com `span.setAttribute("order.id", orderId)`, `span.setAttribute("user.id", userId)`, `span.setAttribute("payment.method", method)`: trace searchable por cliente, produto, método de pagamento. Padrão: OTel Semantic Conventions para evitar nomes inconsistentes.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/opentelemetry]]
- [[concepts/distributed-tracing]]
- [[concepts/spans]]
- [[concepts/otlp]]
- [[concepts/auto-instrumentation]]
- [[entities/jaeger]]
- [[entities/grafana-tempo]]

## Open Questions

- OTel context propagation em sistemas com queues (SQS, Kafka) — como propagar trace context entre produtor e consumidor?
- OTel metrics vs Prometheus — quando migrar métricas existentes para OTel sem duplicar instrumentação?
