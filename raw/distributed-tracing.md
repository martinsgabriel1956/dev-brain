---
date: 2026-03-27
tags: [tech-mentor, system-design, resiliencia, distributed-tracing, opentelemetry, observabilidade, jaeger]
skill: tech-mentor-system-design/references/distributed-systems-advanced.md
level: intermediário
---

# Distributed Tracing

## Contexto

Em um sistema com múltiplos microserviços, quando uma request demora 2 segundos, onde perdeu esse tempo? Sem tracing, você busca logs em N sistemas e correlaciona manualmente. Com tracing, você abre o Jaeger, busca o trace ID e vê o gráfico completo em 10 segundos. Distributed tracing é a ferramenta de observabilidade que conecta todas as peças.

## Como Funciona

### Conceitos Fundamentais

```
Trace — representa uma request completa de ponta a ponta:
  trace_id: 4bf92f3577b34da6a3ce929d0e0e4736

  Span — uma operação individual dentro do trace:
  ┌─────────────────────────────────────────────────┐ 2.300ms
  │ API Gateway                                     │
  │  ┌───────────────────────────────────────────┐  │
  │  │ Order Service (45ms)                      │  │
  │  │  ┌─────────────────────────────────────┐  │  │
  │  │  │ PostgreSQL query (12ms)              │  │  │
  │  │  └─────────────────────────────────────┘  │  │
  │  └───────────────────────────────────────────┘  │
  │  ┌───────────────────────────────────────────┐  │
  │  │ Payment Service (80ms)                    │  │
  │  └───────────────────────────────────────────┘  │
  │  ┌───────────────────────────────────────────┐  │
  │  │ Notification Service (1.800ms) ← gargalo  │  │
  │  └───────────────────────────────────────────┘  │
  └─────────────────────────────────────────────────┘
```

### W3C Trace Context — O Padrão

```
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
             ↑   ↑                                ↑               ↑
          versão  trace-id (16 bytes)          parent-span-id   flags (sampled)
```

O trace ID nasce no primeiro serviço e é propagado via headers HTTP para todos os downstream. Cada serviço cria seu próprio span com o mesmo trace ID.

## Código de Referência

### Setup OpenTelemetry — Node.js

```typescript
// tracing.ts — SEMPRE o primeiro import da aplicação
import { NodeSDK } from "@opentelemetry/sdk-node";
import { OTLPTraceExporter } from "@opentelemetry/exporter-trace-otlp-http";
import { HttpInstrumentation } from "@opentelemetry/instrumentation-http";
import { PgInstrumentation } from "@opentelemetry/instrumentation-pg";
import { Resource } from "@opentelemetry/resources";
import { SEMRESATTRS_SERVICE_NAME } from "@opentelemetry/semantic-conventions";

const sdk = new NodeSDK({
  resource: new Resource({
    [SEMRESATTRS_SERVICE_NAME]: "order-service"
  }),
  traceExporter: new OTLPTraceExporter({
    url: "http://otel-collector:4318/v1/traces"
  }),
  instrumentations: [
    new HttpInstrumentation(),  // propaga traceparent em todo axios/fetch automaticamente
    new PgInstrumentation()     // spans automáticos para queries PostgreSQL
  ]
});

sdk.start();
// Com isso: axios, fetch, pg geram spans e propagam context sem mudar o código de negócio
```

### Spans Customizados — Contexto de Negócio

```typescript
import { trace, SpanStatusCode, context } from "@opentelemetry/api";

const tracer = trace.getTracer("order-service");

async function processOrder(orderId: string) {
  const span = tracer.startSpan("processOrder");

  return context.with(trace.setSpan(context.active(), span), async () => {
    try {
      span.setAttribute("order.id", orderId);
      span.setAttribute("order.source", "web");

      const order = await orderRepository.findById(orderId);
      span.setAttribute("order.total_cents", order.totalCents);

      const result = await chargePayment(order);
      span.setStatus({ code: SpanStatusCode.OK });
      return result;
    } catch (err) {
      span.recordException(err as Error);
      span.setStatus({ code: SpanStatusCode.ERROR, message: (err as Error).message });
      throw err;
    } finally {
      span.end(); // SEMPRE no finally — span nunca pode ficar aberto
    }
  });
}
```

### Propagação em Mensageria

HTTP propaga automaticamente. Mensageria precisa de propagação manual.

```typescript
import { context, propagation, trace, SpanStatusCode } from "@opentelemetry/api";

// PRODUTOR — injeta trace context nos headers da mensagem
async function publishOrderCreated(order: Order) {
  const carrier: Record<string, string> = {};
  propagation.inject(context.active(), carrier);

  await kafka.producer().send({
    topic: "order.created",
    messages: [{ key: order.id, value: JSON.stringify(order), headers: carrier }]
  });
}

// CONSUMIDOR — extrai trace context e continua o trace original
async function handleOrderCreated(message: KafkaMessage) {
  const carrier = Object.fromEntries(
    Object.entries(message.headers ?? {}).map(([k, v]) => [k, v?.toString() ?? ""])
  );
  const parentContext = propagation.extract(context.active(), carrier);

  return context.with(parentContext, async () => {
    const span = trace.getTracer("inventory-service").startSpan("handleOrderCreated");
    try {
      await reserveStock(JSON.parse(message.value!.toString()));
      span.setStatus({ code: SpanStatusCode.OK });
    } catch (err) {
      span.recordException(err as Error);
      span.setStatus({ code: SpanStatusCode.ERROR });
      throw err;
    } finally {
      span.end();
    }
  });
}
// Resultado: Jaeger conecta o span do produtor → Kafka → span do consumidor no mesmo trace
```

### Correlação Traces + Logs

```typescript
import { trace } from "@opentelemetry/api";

function getTraceContext() {
  const span = trace.getActiveSpan();
  if (!span) return {};
  const { traceId, spanId } = span.spanContext();
  return { traceId, spanId };
}

// Todo log carrega o trace ID — clique no log, abra o trace
console.log({
  message: "Order processed",
  orderId: "ord_123",
  ...getTraceContext()
});
```

### Sampling — Não Rastreie Tudo

```typescript
import { ParentBasedSampler, TraceIdRatioBased } from "@opentelemetry/sdk-trace-base";

// 10% das requests novas são rastreadas
// Requests com trace ID propagado do upstream sempre são rastreadas
const sampler = new ParentBasedSampler({
  root: new TraceIdRatioBased(0.1)
});
```

## Trade-offs

| Aspecto | Sem Tracing | Com Tracing |
|---|---|---|
| **Debug de latência** | Manual — busca em N logs separados | Visual — gráfico de spans com timing |
| **Root cause** | Horas para identificar | Segundos |
| **Overhead** | Zero | 1–3% CPU com sampling adequado |
| **Custo de storage** | Zero | Alto se 100% sampling em alta carga |
| **Complexidade** | Zero | Setup + instrumentação + backend |

## Quando Usar / Quando Evitar

**Obrigatório quando:**
- ✅ Mais de 2–3 serviços em uma cadeia de request
- ✅ SLA de latência para o usuário final
- ✅ Você passou mais de 30 min debugando uma lentidão intermitente

**Não é necessário quando:**
- ❌ Monolito — logging estruturado + APM são suficientes
- ❌ Sistema simples sem dependências externas relevantes

**Stack recomendada:**
```
OpenTelemetry SDK → OTel Collector → Jaeger (self-hosted) ou Grafana Tempo
                                   → correlaciona com Loki (logs) e Prometheus (métricas)
```

## Conceitos Relacionados

[[fase-3-resiliencia]] · [[circuit-breaker]] · [[mensageria]] · [[numeros-de-latencia]] · [[load-balancer]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
