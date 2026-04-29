---
date: 2026-04-17
tags: [tech-mentor, infra, observabilidade, opentelemetry, otel, tracing, typescript, collector]
skill: tech-mentor-infra/references/observabilidade
level: intermediário
---

# OpenTelemetry — SDK TypeScript, Collector Pipeline e Tail Sampling

## Contexto

OpenTelemetry é o padrão de instrumentação unificado para traces, métricas e logs — agnóstico de vendor (Datadog, Jaeger, Grafana, Honeycomb). O SDK instrumenta o código; o Collector é o gateway que recebe, processa e exporta para o backend. Tail Sampling permite decidir DEPOIS da request completa se o trace vale armazenar, baseado no resultado real (erro, latência).

---

## SDK TypeScript — Instrumentação

### Setup do SDK (inicializar ANTES de qualquer import do app)

```typescript
// tracing.ts — deve ser o primeiro arquivo carregado
// Node: --require ./tracing.js ou import antes de tudo

import { NodeSDK } from "@opentelemetry/sdk-node";
import { Resource } from "@opentelemetry/resources";
import { SEMRESATTRS_SERVICE_NAME, SEMRESATTRS_SERVICE_VERSION } from "@opentelemetry/semantic-conventions";
import { OTLPTraceExporter } from "@opentelemetry/exporter-trace-otlp-http";
import { OTLPMetricExporter } from "@opentelemetry/exporter-metrics-otlp-http";
import { PeriodicExportingMetricReader } from "@opentelemetry/sdk-metrics";
import { BatchSpanProcessor } from "@opentelemetry/sdk-trace-base";
import { getNodeAutoInstrumentations } from "@opentelemetry/auto-instrumentations-node";

const sdk = new NodeSDK({
  resource: new Resource({
    [SEMRESATTRS_SERVICE_NAME]: process.env.SERVICE_NAME ?? "unknown-service",
    [SEMRESATTRS_SERVICE_VERSION]: process.env.SERVICE_VERSION ?? "0.0.0",
    "deployment.environment": process.env.NODE_ENV ?? "development"
  }),

  // Exportar para OTel Collector (que encaminha para Jaeger/Tempo/Datadog)
  spanProcessor: new BatchSpanProcessor(
    new OTLPTraceExporter({
      url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT ?? "http://localhost:4318/v1/traces"
    }),
    {
      maxQueueSize: 2048,
      scheduledDelayMillis: 5000,   // flush a cada 5s
      exportTimeoutMillis: 30000
    }
  ),

  metricReader: new PeriodicExportingMetricReader({
    exporter: new OTLPMetricExporter({
      url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT ?? "http://localhost:4318/v1/metrics"
    }),
    exportIntervalMillis: 30000   // exportar métricas a cada 30s
  }),

  // Auto-instrumentação: HTTP, Express, Prisma, Redis, gRPC, etc
  instrumentations: [
    getNodeAutoInstrumentations({
      "@opentelemetry/instrumentation-http": {
        // Não criar span para health checks
        ignoreIncomingRequestHook: req => req.url === "/health"
      },
      "@opentelemetry/instrumentation-fs": { enabled: false }  // muito verboso
    })
  ]
});

sdk.start();

process.on("SIGTERM", async () => {
  await sdk.shutdown();
  process.exit(0);
});
```

### Instrumentação Manual — Spans e Atributos

```typescript
import { trace, context, SpanStatusCode, SpanKind } from "@opentelemetry/api";

const tracer = trace.getTracer("order-service", "1.0.0");

// Span manual para operação de negócio
async function createOrder(userId: string, items: OrderItem[]): Promise<Order> {
  return tracer.startActiveSpan(
    "order.create",
    {
      kind: SpanKind.INTERNAL,
      attributes: {
        "order.user_id": userId,
        "order.item_count": items.length,
        "order.total_value": items.reduce((sum, i) => sum + i.price * i.quantity, 0)
      }
    },
    async span => {
      try {
        // Operação filha — span filho é criado automaticamente dentro do contexto ativo
        const validatedItems = await validateInventory(items);

        // Adicionar atributos depois de calcular
        span.setAttribute("order.validated", true);

        const order = await prisma.order.create({
          data: { userId, items: { create: validatedItems } }
        });

        span.setAttribute("order.id", order.id);
        span.setStatus({ code: SpanStatusCode.OK });

        return order;
      } catch (error) {
        // Registrar erro no span
        span.recordException(error as Error);
        span.setStatus({
          code: SpanStatusCode.ERROR,
          message: (error as Error).message
        });
        throw error;
      } finally {
        span.end();
      }
    }
  );
}

// Propagar contexto manualmente (ex: entre workers/filas)
import { propagation, ROOT_CONTEXT } from "@opentelemetry/api";

// Producer — serializar contexto na mensagem
async function enqueueJob(jobData: Record<string, unknown>): Promise<void> {
  const carrier: Record<string, string> = {};
  propagation.inject(context.active(), carrier);

  await queue.add("process-job", {
    ...jobData,
    _otelContext: carrier  // traceparent + tracestate headers
  });
}

// Consumer — restaurar contexto da mensagem
async function processJob(job: { data: Record<string, unknown> }): Promise<void> {
  const carrier = job.data._otelContext as Record<string, string> ?? {};
  const parentContext = propagation.extract(ROOT_CONTEXT, carrier);

  // Iniciar span filho dentro do contexto propagado
  return context.with(parentContext, () =>
    tracer.startActiveSpan("job.process", async span => {
      try {
        await doWork(job.data);
        span.setStatus({ code: SpanStatusCode.OK });
      } finally {
        span.end();
      }
    })
  );
}

// Métricas customizadas
import { metrics } from "@opentelemetry/api";

const meter = metrics.getMeter("order-service");

const orderCounter = meter.createCounter("orders.created", {
  description: "Total de orders criadas"
});

const orderValueHistogram = meter.createHistogram("orders.value", {
  description: "Distribuição de valores de orders",
  unit: "BRL",
  advice: { explicitBucketBoundaries: [10, 50, 100, 500, 1000, 5000] }
});

const activeConnectionsGauge = meter.createUpDownCounter("db.connections.active", {
  description: "Conexões ativas com o banco"
});

// Uso nas operações
orderCounter.add(1, { "order.status": "created", "user.segment": "premium" });
orderValueHistogram.record(order.total, { "payment.method": "credit_card" });
```

---

## OTel Collector — Pipeline de Observabilidade

```yaml
# otel-collector.yaml
receivers:
  otlp:
    protocols:
      http:
        endpoint: 0.0.0.0:4318
      grpc:
        endpoint: 0.0.0.0:4317

  # Receber métricas do Prometheus (scrape)
  prometheus:
    config:
      scrape_configs:
        - job_name: "app-metrics"
          scrape_interval: 30s
          static_configs:
            - targets: ["app:9090"]

  # Receber logs do host
  filelog:
    include: ["/var/log/app/*.json"]
    operators:
      - type: json_parser
        timestamp:
          parse_from: attributes.timestamp
          layout: "%Y-%m-%dT%H:%M:%S.%LZ"

processors:
  # Batch — agrupar antes de exportar (reduz custo de rede)
  batch:
    timeout: 5s
    send_batch_size: 1024
    send_batch_max_size: 2048

  # Resource detection — adicionar metadados do ambiente
  resourcedetection:
    detectors: [env, system, docker, k8snode]

  # Memory limiter — evitar OOM no Collector
  memory_limiter:
    limit_mib: 512
    spike_limit_mib: 128
    check_interval: 5s

  # Sampling baseado em head (probabilístico)
  probabilistic_sampler:
    sampling_percentage: 10  # 10% de todos os traces

  # Filtrar spans desnecessários
  filter:
    traces:
      span:
        - 'attributes["http.target"] == "/health"'
        - 'attributes["http.target"] == "/metrics"'

  # Adicionar atributos a todos os traces
  attributes:
    actions:
      - key: "env"
        value: "production"
        action: insert

exporters:
  # Jaeger
  otlp/jaeger:
    endpoint: "jaeger:4317"
    tls:
      insecure: true

  # Grafana Tempo
  otlp/tempo:
    endpoint: "tempo:4317"
    tls:
      insecure: true

  # Datadog
  datadog:
    api:
      key: ${DATADOG_API_KEY}

  # Prometheus (métricas)
  prometheus:
    endpoint: "0.0.0.0:9090"

  # Loki (logs)
  loki:
    endpoint: "http://loki:3100/loki/api/v1/push"

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter, resourcedetection, batch, filter]
      exporters: [otlp/tempo, datadog]

    metrics:
      receivers: [otlp, prometheus]
      processors: [memory_limiter, resourcedetection, batch]
      exporters: [prometheus]

    logs:
      receivers: [otlp, filelog]
      processors: [memory_limiter, batch]
      exporters: [loki]
```

---

## Tail Sampling — Decisão Após a Requisição Completa

Head sampling decide no início da request se vai amostrar. Tail sampling decide DEPOIS — pode guardar 100% de erros e 5% de traces normais:

```yaml
# Tail Sampling Processor — requer OTel Collector contrib
processors:
  tail_sampling:
    decision_wait: 10s           # aguardar até 10s pelos spans filhos
    num_traces: 100000           # traces em memória simultaneamente
    expected_new_traces_per_sec: 100

    policies:
      # Sempre guardar traces com erro
      - name: errors-policy
        type: status_code
        status_code:
          status_codes: [ERROR]

      # Sempre guardar traces lentos (> 2s)
      - name: latency-policy
        type: latency
        latency:
          threshold_ms: 2000

      # Guardar traces de endpoints críticos
      - name: critical-endpoints
        type: string_attribute
        string_attribute:
          key: "http.target"
          values: ["/api/payment", "/api/checkout"]
          enabled_regex_matching: false

      # Amostrar 5% do restante
      - name: probabilistic-base
        type: probabilistic
        probabilistic:
          sampling_percentage: 5

      # Combinar políticas: error OU latência OU 5% do resto
      - name: composite-policy
        type: composite
        composite:
          max_total_spans_per_second: 1000
          policy_order: [errors-policy, latency-policy, critical-endpoints, probabilistic-base]
          rate_allocation:
            - policy: errors-policy
              percent: 40
            - policy: latency-policy
              percent: 30
            - policy: probabilistic-base
              percent: 30
```

---

## Auto-Instrumentação vs Manual

```
Auto-instrumentação (zero-code):
  → HTTP/Express, Prisma, Redis, gRPC, AWS SDK, MongoDB
  → Span criado automaticamente por cada request/query
  → Sem mudança de código
  → Ativar via getNodeAutoInstrumentations()

Manual (custom spans):
  → Lógica de negócio — "criar pedido", "calcular frete", "validar cupom"
  → Adicionar atributos de domínio: orderId, userId, valor, número de itens
  → Eventos de estado: span.addEvent("inventory.validated")
  → Use quando: operações que cruzam múltiplas queries/requests, regras de negócio

Regra prática: auto para infraestrutura, manual para negócio.
```

---

## Trade-offs

| Abordagem | Overhead | Completude | Operação |
|---|---|---|---|
| **Head Sampling** | Baixo | Perde erros raros | Simples |
| **Tail Sampling** | Alto (memória no Collector) | Guarda o que importa | Complexo |
| **100% (sem sampling)** | Alto | Completo | Caro (storage) |
| **Auto-instrução** | Mínimo | Infra apenas | Zero |
| **Manual** | Baixo | Negócio + infra | Médio |

## Quando Usar / Quando Evitar

**Tail Sampling:** sistemas de produção com volume > 1k req/s onde custo de storage importa — permite 100% de cobertura de erros com custo controlado.

**Head Sampling:** sistemas menores, debug temporário, ambientes de desenvolvimento.

**Collector vs SDK direto para backend:** sempre usar Collector em produção — centraliza configuração de sampling, permite trocar backend sem redeployar apps.

**Continuous Profiling (Pyroscope):** complemento ao tracing — enquanto traces mostram "qual request foi lento", profiling mostra "qual linha de código consome mais CPU" em nível de fleet.

## Conceitos Relacionados

[[sre-sli-slo-sla]] · [[structured-logging]] · [[distributed-tracing]] · [[kafka]] · [[background-jobs]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-04-17*
