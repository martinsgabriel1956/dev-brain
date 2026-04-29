---
type: source
title: "Observabilidade"
aliases: ["observabilidade", "observability", "tres pilares", "metrics logs traces"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 0
tags: [observabilidade, metricas, logs, traces, prometheus, slo, alertas, red-method, opentelemetry]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-study/raw/observabilidade.md
source_url: ""
author: ""
date_published: 2026-03-27
date_ingested: 2026-04-22
---

# Observabilidade

## TL;DR

Três pilares complementares: métricas (o quê), traces (onde), logs (por quê). Alerte em sintomas (error rate > 1%), não em causas (CPU > 80%). Prioridade: logs estruturados com trace ID → métricas RED → SLO/Error Budget → distributed tracing.

## Key Claims

**Claim:** Os três pilares respondem perguntas diferentes e são complementares — nenhum substitui o outro.
**Evidence:** Métricas → "o quê está errado?" (error rate subiu 5%). Traces → "onde está errado?" (serviço de notificação lento). Logs → "por quê está errado?" (NullPointerException linha 234).
**Confidence:** alta

**Claim:** Alertar em sintomas (impacto no usuário), não em causas (utilização de recurso).
**Evidence:** CPU > 80% pode não impactar usuário. Error rate > 1% impacta agora. Alerta em causa gera alert fatigue sem ação clara; alerta em sintoma tem runbook óbvio.
**Confidence:** alta

**Claim:** Logs estruturados com trace ID são a prioridade de implementação — baixo custo, alto valor imediato.
**Evidence:** Log em texto livre é impossível de filtrar programaticamente. Log estruturado (JSON) permite query por userId, orderId, traceId. traceId correlaciona log com span no Jaeger/Tempo.
**Confidence:** alta

**Claim:** RED Method (Rate, Errors, Duration) cobre os alertas essenciais para qualquer serviço HTTP.
**Evidence:** Prometheus Counter para taxa/erros + Histogram para latência. PromQL: `histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))` para p99. Alertas essenciais: error rate > 1%, p99 > 2s, `up == 0`.
**Confidence:** alta

**Claim:** Prioridade de implementação: logs estruturados → métricas RED → SLO/Error Budget → distributed tracing.
**Evidence:** Distributed tracing só vale quando > 3 microsserviços. SLO/Error Budget requer métricas estáveis. Logs com trace ID funcionam mesmo com um único serviço.
**Confidence:** alta

## Stack Recomendada

```
Métricas: Prometheus + Grafana (self-hosted) ou Datadog (SaaS)
Logs:     Loki + Grafana ou Elasticsearch + Kibana
Traces:   Jaeger ou Grafana Tempo
Coleta:   OpenTelemetry (vendor-neutral)
```

## Concepts & Entities Touched

[[concepts/observabilidade]] · [[concepts/red-method]] · [[concepts/structured-logs]] · [[concepts/sli]] · [[concepts/slo]] · [[concepts/error-budget]] · [[concepts/blameless-post-mortem]]

## Open Questions

- OpenTelemetry auto-instrumentation vs manual — quando o overhead de configuração vale?
- Alert fatigue em times com muitos serviços — como calibrar thresholds sem perder sinal?
- Custo de storage de métricas/logs em escala — quando Datadog SaaS supera self-hosted?
