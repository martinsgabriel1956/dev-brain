---
date: 2026-03-27
tags: [tech-mentor, system-design, deploy, observabilidade, metricas, logs, slo, alertas, prometheus]
skill: tech-mentor-system-design/references/performance-profiling.md
level: intermediário
---

# Observabilidade

## Contexto

Observabilidade é a capacidade de entender o estado interno de um sistema a partir de suas saídas externas. Sem ela, você descobre o problema quando o usuário reclama. Os três pilares são complementares — cada um responde uma pergunta diferente:

```
Métricas → "O QUÊ está errado?" (error rate subiu 5%)
Traces   → "ONDE está errado?" (serviço de notificação está lento)
Logs     → "POR QUÊ está errado?" (NullPointerException na linha 234)
```

## Como Funciona

### SLO, SLA e Error Budget

```
SLA → Contrato com o cliente: "garantimos 99.9% de disponibilidade"
SLO → Meta interna: "queremos 99.95%" (mais restritivo que o SLA)
SLI → A métrica que mede o SLO: % de requests com status < 500

Error Budget = 100% - SLO
  SLO 99.9% → budget = 0.1% = 43,2 minutos/mês de downtime permitido

Se o budget acabou:
  → Congela novos deploys até o próximo período
  → Foco total em confiabilidade, não em features
```

### Regra de Alertas

```
Alerte em SINTOMAS (usuário impactado), não em causas (CPU alto)

❌ CPU > 80%        → pode não impactar usuário
✅ Error rate > 1%  → usuário está sendo impactado agora
```

## Código de Referência

### Métricas — RED Method com Prometheus

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

app.get("/metrics", async (req, res) => {
  res.set("Content-Type", register.contentType);
  res.send(await register.metrics());
});
```

```promql
# Error rate dos últimos 5 minutos
sum(rate(http_requests_total{status_code=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))

# p99 de latência
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))
```

### Logs Estruturados

```typescript
// ❌ Texto livre — impossível filtrar programaticamente
console.log(`User ${userId} placed order ${orderId}`);

// ✅ Estruturado — cada campo é pesquisável
console.log({
  message: "Order placed",
  userId,
  orderId,
  amountCents: amount,
  traceId: getTraceId(),   // correlaciona com o trace no Jaeger
  spanId: getSpanId(),
  timestamp: new Date().toISOString()
});

// Níveis:
// ERROR → falha que impacta usuário, requer ação imediata
// WARN  → inesperado mas recuperável (fallback ativado)
// INFO  → eventos de negócio relevantes
// DEBUG → diagnóstico técnico — NUNCA em produção
```

### Alertas — Os Essenciais

```yaml
# 1. Error rate alto
- alert: HighErrorRate
  expr: |
    sum(rate(http_requests_total{status_code=~"5.."}[5m]))
    /
    sum(rate(http_requests_total[5m])) > 0.01
  for: 2m  # precisa durar 2 minutos (evita flapping)
  annotations:
    runbook: "https://wiki.empresa.com/runbooks/high-error-rate"

# 2. Latência alta (p99)
- alert: HighLatency
  expr: histogram_quantile(0.99, rate(http_duration_bucket[5m])) > 2

# 3. Serviço indisponível
- alert: ServiceDown
  expr: up{job="api"} == 0
  for: 1m

# 4. Error budget quase esgotado (burn rate alto)
- alert: ErrorBudgetBurnRateHigh
  expr: |
    (1 - job:slo_availability:ratio_rate1h) > 14.4 * (1 - 0.999)
  annotations:
    summary: "Consuming error budget 14.4x faster than allowed"
```

## Trade-offs

| Aspecto | Sem Observabilidade | Com Observabilidade |
|---|---|---|
| **Detecção** | Usuário reclama primeiro | Alerta antes do usuário perceber |
| **Debug** | Horas reproduzindo localmente | Minutos com logs + traces |
| **Deploys** | "Torce para não quebrar" | Monitora métricas em tempo real |
| **SLA** | Estimado | Medido e rastreável |
| **Custo** | Zero setup | Storage de métricas/logs (crescente) |
| **Alert fatigue** | Não tem alertas | Precisa calibrar para não virar ruído |

## Quando Usar / Quando Evitar

**Stack recomendada:**
```
Métricas: Prometheus + Grafana (self-hosted) ou Datadog (SaaS)
Logs:     Loki + Grafana ou Elasticsearch + Kibana
Traces:   Jaeger ou Grafana Tempo
Coleta:   OpenTelemetry (vendor-neutral)
```

**Prioridade de implementação:**
1. Logs estruturados com trace ID — baixo custo, alto valor
2. Métricas RED por endpoint — alertas úteis
3. SLO + Error Budget — alinha eng e produto
4. Distributed tracing — quando microserviços forem > 3

## Conceitos Relacionados

[[fase-4-deploy-operacoes]] · [[distributed-tracing]] · [[cicd-pipeline]] · [[circuit-breaker]] · [[numeros-de-latencia]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
