---
type: concept
title: "Observabilidade"
aliases: ["observabilidade", "observability", "três pilares", "metrics logs traces"]
date_created: 2026-04-22
date_updated: 2026-07-21
source_count: 7
tags: [observabilidade, metricas, logs, traces, prometheus, sre, infraestrutura]
skill: tech-mentor-system-design
status: stable
---

# Observabilidade

Capacidade de entender o estado interno de um sistema a partir de suas saídas externas. Sem ela, o problema é descoberto quando o usuário reclama.

## Os Três Pilares

```
Métricas → "O QUÊ está errado?" (error rate subiu 5%)
Traces   → "ONDE está errado?" (serviço de notificação lento)
Logs     → "POR QUÊ está errado?" (NullPointerException linha 234)
```

Pilares são complementares — nenhum substitui o outro.

## Regra de Alertas

Alerte em **sintomas** (usuário impactado), não em causas (utilização de recurso):

```
❌ CPU > 80%        → pode não impactar usuário
✅ Error rate > 1%  → usuário está sendo impactado agora
```

## RED Method — Métricas Essenciais

**R**ate · **E**rrors · **D**uration — cobre os alertas essenciais de qualquer serviço HTTP.

```typescript
import { Counter, Histogram, register } from "prom-client";

const httpRequests = new Counter({
  name: "http_requests_total",
  help: "Total HTTP requests",
  labelNames: ["method", "route", "status_code"]
});

const httpDuration = new Histogram({
  name: "http_request_duration_seconds",
  help: "HTTP request duration",
  labelNames: ["method", "route"],
  buckets: [0.01, 0.05, 0.1, 0.3, 0.5, 1, 2, 5]
});

app.use((req, res, next) => {
  const end = httpDuration.startTimer({ method: req.method, route: req.route?.path });
  res.on("finish", () => {
    httpRequests.inc({
      method: req.method,
      route: req.route?.path ?? "unknown",
      status_code: res.statusCode
    });
    end();
  });
  next();
});
```

```promql
# Error rate últimos 5 minutos
sum(rate(http_requests_total{status_code=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))

# p99 de latência
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))
```

## Logs Estruturados

```typescript
// ❌ Texto livre — impossível filtrar programaticamente
console.log(`User ${userId} placed order ${orderId}`);

// ✅ Estruturado — cada campo pesquisável, trace ID correlaciona com Jaeger
console.log({
  message: "Order placed",
  userId,
  orderId,
  amountCents: amount,
  traceId: getTraceId(),
  spanId: getSpanId(),
  timestamp: new Date().toISOString()
});
```

Níveis: `ERROR` (impacta usuário) · `WARN` (inesperado mas recuperável) · `INFO` (evento de negócio) · `DEBUG` (nunca em produção)

## Alertas Essenciais (Prometheus)

```yaml
- alert: HighErrorRate
  expr: |
    sum(rate(http_requests_total{status_code=~"5.."}[5m]))
    / sum(rate(http_requests_total[5m])) > 0.01
  for: 2m
  annotations:
    runbook: "https://wiki.empresa.com/runbooks/high-error-rate"

- alert: HighLatency
  expr: histogram_quantile(0.99, rate(http_duration_bucket[5m])) > 2

- alert: ServiceDown
  expr: up{job="api"} == 0
  for: 1m

- alert: ErrorBudgetBurnRateHigh
  expr: (1 - job:slo_availability:ratio_rate1h) > 14.4 * (1 - 0.999)
```

## Prioridade de Implementação

1. **Logs estruturados com trace ID** — baixo custo, alto valor imediato
2. **Métricas RED por endpoint** — alertas úteis desde o primeiro serviço
3. **SLO + Error Budget** — alinha engenharia e produto
4. **Distributed tracing** — quando microsserviços forem > 3

## Stack Recomendada

```
Métricas: Prometheus + Grafana (self-hosted) ou Datadog (SaaS)
Logs:     Loki + Grafana ou Elasticsearch + Kibana
Traces:   Jaeger ou Grafana Tempo
Coleta:   OpenTelemetry (vendor-neutral)
```

## Erro comum de arquitetura: pular o Collector

Boa prática de produção com [[wiki/concepts/distributed-tracing|OpenTelemetry]]: a aplicação nunca deve enviar telemetria direto para Prometheus/Loki/Tempo — ela envia para o **OpenTelemetry Collector**, que centraliza formatação e roteamento e distribui para cada backend especializado. Mandar o dado direto da aplicação pro backend final (pulando o Collector) é apontado como o erro mais comum ao montar essa stack.

## De coleta a correlação automática

A prioridade de implementação acima (logs → métricas RED → SLO → tracing) é sobre **coletar** dados. Uma vez coletados e centralizados, um agente de IA com acesso via MCP aos backends (ex. Grafana MCP → Prometheus/Loki/Tempo) consegue correlacionar os três pilares automaticamente e produzir relatórios de causa raiz que antes exigiam investigação manual de dias ou semanas. Ver [[wiki/concepts/investigacao-de-incidentes-com-ia-e-mcp]]. O ouro continua nos dados — a IA acelera a correlação, não substitui a coleta.

## Relacionado

[[concepts/sli]] · [[concepts/slo]] · [[concepts/error-budget]] · [[concepts/blameless-post-mortem]] · [[concepts/circuit-breaker]] · [[concepts/service-mesh]] · [[wiki/concepts/investigacao-de-incidentes-com-ia-e-mcp]]

## Key Sources

- [[sources/observabilidade]]
- [[wiki/sources/diferenciais-portfolio-backend-junior]]
- [[sources/5-principios-programador]]
- [[sources/roadmap-dev-senior-2026]] — pilar 4: ler o sistema como sistema vivo (logs, métricas)
- [[wiki/sources/10-conceitos-fundamentais-backend]] — observabilidade como "meta-conceito" nº 1: o que amarra cache, fila, banco e autenticação no mundo real; logs = o que aconteceu, métricas = está crescendo?, traces = onde o tempo foi gasto
- [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]] — arquitetura do Collector como ponto único de roteamento; correlação automática de telemetria via agente de IA + MCP
- [[wiki/sources/impacto-ia-mercado-frontend]] — observabilidade como um dos itens que menos mudou com IA, citado como marcador de maturidade de plataforma que blinda orgs do impacto de mercado
