---
date: 2026-04-17
tags: [tech-mentor, observabilidade, opentelemetry, otel, tracing, sampling]
skill: tech-mentor-infra/references/observability
level: avançado
---

# OTel Collector — Pipeline, Tail Sampling e Auto-instrumentation

## OTel Collector — Arquitetura

O Collector é um proxy de telemetria. Recebe dados de múltiplas fontes, processa e exporta para múltiplos destinos — desacoplando a aplicação do backend de observabilidade.

```
┌──────────────────────────────────────────────┐
│              OTel Collector                   │
│                                               │
│  Receivers   →   Processors   →   Exporters  │
│                                               │
│  otlp         batch            jaeger         │
│  prometheus   filter           tempo          │
│  kafka        resource         prometheus     │
│  hostmetrics  tail_sampling    otlp           │
└──────────────────────────────────────────────┘
```

```yaml
# otel-collector-config.yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318
  hostmetrics:
    scrapers:
      cpu: {}
      memory: {}
      disk: {}

processors:
  batch:
    timeout: 1s
    send_batch_size: 1024

  # Remove dados sensíveis antes de exportar
  attributes:
    actions:
      - key: http.request.header.authorization
        action: delete
      - key: db.statement
        action: hash    # anonimiza queries com dados sensíveis

  # Adiciona resource attributes comuns
  resource:
    attributes:
      - key: deployment.environment
        value: production
        action: upsert

exporters:
  otlp/tempo:
    endpoint: http://tempo:4317
    tls:
      insecure: true
  prometheusremotewrite:
    endpoint: http://mimir:9009/api/v1/push
  loki:
    endpoint: http://loki:3100/loki/api/v1/push

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch, attributes, resource]
      exporters: [otlp/tempo]
    metrics:
      receivers: [otlp, hostmetrics]
      processors: [batch, resource]
      exporters: [prometheusremotewrite]
    logs:
      receivers: [otlp]
      processors: [batch, resource]
      exporters: [loki]
```

---

## Tail Sampling — Decisão Inteligente de Sampling

**Head sampling** decide aleatoriamente ao iniciar o trace (ex: amostrar 10%). O problema: descarta traces de erros e alta latência junto com os de sucesso.

**Tail sampling** aguarda o trace completar, examina o resultado e então decide se salva. Implementado no Collector.

```yaml
processors:
  tail_sampling:
    decision_wait: 10s     # aguarda 10s para o trace completar
    num_traces: 100000     # buffer de traces em memória
    expected_new_traces_per_sec: 1000
    policies:
      # SEMPRE salvar erros
      - name: errors-policy
        type: status_code
        status_code: { status_codes: [ERROR] }

      # SEMPRE salvar traces lentos (p99 > 500ms)
      - name: slow-traces
        type: latency
        latency: { threshold_ms: 500 }

      # Salvar 1% dos traces de sucesso (sampling aleatório para baseline)
      - name: random-baseline
        type: probabilistic
        probabilistic: { sampling_percentage: 1 }

      # Salvar 100% dos traces de operações críticas
      - name: payment-traces
        type: string_attribute
        string_attribute:
          key: rpc.method
          values: ["ProcessPayment", "RefundPayment"]
```

**Resultado:** 100% de visibilidade em erros e lentidão, com baixo custo de armazenamento para traces normais.

---

## Auto-instrumentation — Zero-code Observability

Instrumentação automática sem modificar o código da aplicação — via agente ou init container no K8s.

### Node.js

```typescript
// Adicionar ao início do processo — ANTES de qualquer import
// --require @opentelemetry/auto-instrumentations-node/register

// Variáveis de ambiente configuram tudo:
// OTEL_SERVICE_NAME=order-api
// OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4318
// OTEL_TRACES_SAMPLER=parentbased_traceidratio
// OTEL_TRACES_SAMPLER_ARG=0.1
```

```bash
node --require @opentelemetry/auto-instrumentations-node/register server.js
```

Instrumenta automaticamente: http/https, Express/Fastify, PostgreSQL, Redis, MongoDB, gRPC, fetch/axios.

### K8s — Operador de Instrumentação

```yaml
# OpenTelemetry Operator injeta o agente via init container
apiVersion: opentelemetry.io/v1alpha1
kind: Instrumentation
metadata:
  name: nodejs-instrumentation
  namespace: production
spec:
  exporter:
    endpoint: http://otel-collector:4317
  propagators: [tracecontext, baggage, b3]
  sampler:
    type: parentbased_traceidratio
    argument: "0.1"
  nodejs:
    image: ghcr.io/open-telemetry/opentelemetry-operator/autoinstrumentation-nodejs:latest

---
# No Deployment: anotar para injetar automaticamente
metadata:
  annotations:
    instrumentation.opentelemetry.io/inject-nodejs: "true"
```

---

## Continuous Profiling — Pyroscope e eBPF

Profiling contínuo coleta CPU/memory profiles em produção sem impacto perceptível.

```typescript
// Pyroscope SDK — Node.js
import Pyroscope from "@pyroscope/nodejs";

Pyroscope.init({
  serverAddress: "http://pyroscope:4040",
  appName: "order-api",
  tags: { environment: "production", version: process.env.APP_VERSION }
});

Pyroscope.start();
```

```yaml
# Pyroscope como DaemonSet — eBPF profiling zero-code
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: pyroscope-agent
spec:
  template:
    spec:
      hostPID: true   # acesso aos processos do node
      containers:
        - name: pyroscope
          image: grafana/pyroscope:latest
          securityContext:
            privileged: true   # necessário para eBPF
```

## Conceitos Relacionados
[[otel-sdk]] · [[distributed-tracing]] · [[sre-sli-slo-sla]] · [[flame-graph-profiling]] · [[observabilidade]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-04-17*
