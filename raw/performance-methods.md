---
date: 2026-04-17
tags: [tech-mentor, infra, observabilidade, performance, use-method, red-method, four-golden-signals, k6, load-testing, flame-graph]
skill: tech-mentor-infra/references/observabilidade
level: intermediário
---

# Performance: USE Method, RED Method, Four Golden Signals e k6

## Contexto

Observar um sistema sem um framework de diagnóstico resulta em dashboards cheios de métricas sem hierarquia de investigação. USE, RED e Four Golden Signals são frameworks complementares: USE diagnostica recursos de infraestrutura, RED diagnostica serviços, e Four Golden Signals é o vocabulário do SRE do Google para alertas. k6 é a ferramenta de load testing que valida o sistema antes que o usuário o faça.

---

## USE Method — Diagnóstico de Recursos

Criado por Brendan Gregg para diagnosticar **recursos de infraestrutura** (CPU, memória, disco, rede, threads):

```
Para cada recurso, meça:
  U — Utilization: % do tempo que o recurso está ocupado
  S — Saturation:  fila ou backlog acumulando (sinal de sobrecarga)
  E — Errors:      operações que falharam

Recurso              | Utilization          | Saturation              | Errors
---------------------|----------------------|-------------------------|----------------------
CPU                  | % busy (top, vmstat) | run queue (>1/core)     | CPU exceptions
Memory               | % usado / total      | swap usage, OOM kills   | OOM errors
Disk I/O             | % busy (iostat)      | await time, queue depth | disk errors
Network interface    | throughput/bandwidth | packet drops, retransmit| CRC errors, collisions
Thread pool          | threads ativos/total | fila de work pendente   | rejected tasks
DB connection pool   | conns ativas/total   | conns em espera         | connection errors
```

```typescript
// Métricas USE expostas via Prometheus / OTel
import { metrics } from "@opentelemetry/api";

const meter = metrics.getMeter("infrastructure");

// U — Utilization: pool de conexões DB
const dbPoolUtilization = meter.createObservableGauge("db.pool.utilization", {
  description: "Proporção de conexões ativas / total"
});

dbPoolUtilization.addCallback(result => {
  const active = pool.activeConnections();
  const total = pool.totalConnections();
  result.observe(active / total, { "pool.name": "postgres-main" });
});

// S — Saturation: fila de tasks pendentes
const taskQueueDepth = meter.createObservableGauge("worker.queue.depth", {
  description: "Tasks aguardando processamento"
});

taskQueueDepth.addCallback(result => {
  result.observe(queue.size(), { "queue.name": "order-processor" });
});

// E — Errors: operações que falharam
const dbErrors = meter.createCounter("db.errors.total", {
  description: "Total de erros de banco de dados"
});

// Uso:
try {
  await query();
} catch (err) {
  dbErrors.add(1, { "error.type": "connection_refused", "db.name": "orders" });
  throw err;
}
```

---

## RED Method — Diagnóstico de Serviços

Criado por Tom Wilkie para **microsserviços e APIs** — perspectiva do consumidor do serviço:

```
Para cada serviço, meça:
  R — Rate:     requisições por segundo
  E — Errors:   % de requisições com erro (4xx, 5xx)
  D — Duration: distribuição de latência (p50, p95, p99)

Por que distribuição importa mais que média:
  Média:  p50=10ms, p99=2000ms → avg=50ms → média mente
  p99:    1% dos usuários espera 2s → inaceitável para SLO
  p999:   0.1% dos usuários (em 1M req/s = 1000 req/s com 2s latency)
```

```typescript
// RED metrics para uma API REST
import { trace, metrics, SpanStatusCode } from "@opentelemetry/api";

const meter = metrics.getMeter("api-service");

// R — Rate: counter de requests
const requestCounter = meter.createCounter("http.requests.total", {
  description: "Total de requisições HTTP"
});

// E — Errors: counter separado por código de status
const errorCounter = meter.createCounter("http.errors.total", {
  description: "Total de erros HTTP (4xx e 5xx)"
});

// D — Duration: histograma com buckets bem definidos
const requestDuration = meter.createHistogram("http.request.duration_ms", {
  description: "Duração das requisições em ms",
  unit: "ms",
  advice: {
    // Buckets: 5ms, 10ms, 25ms, 50ms, 100ms, 250ms, 500ms, 1s, 2.5s, 5s
    explicitBucketBoundaries: [5, 10, 25, 50, 100, 250, 500, 1000, 2500, 5000]
  }
});

// Middleware Express para coletar RED metrics
function redMetricsMiddleware(
  req: express.Request,
  res: express.Response,
  next: express.NextFunction
): void {
  const start = Date.now();
  const route = req.route?.path ?? req.path;

  requestCounter.add(1, {
    "http.method": req.method,
    "http.route": route
  });

  res.on("finish", () => {
    const duration = Date.now() - start;
    const labels = {
      "http.method": req.method,
      "http.route": route,
      "http.status_code": res.statusCode.toString()
    };

    requestDuration.record(duration, labels);

    if (res.statusCode >= 400) {
      errorCounter.add(1, labels);
    }
  });

  next();
}
```

---

## Four Golden Signals — Vocabulário SRE

Framework do Google SRE para alertas de produção. **Qualquer serviço user-facing deve monitorar os 4:**

```
1. Latency — quanto tempo leva para servir uma requisição
   → Separar latência de sucesso vs. de erro
   → Erro rápido não é problema de latência; sucesso lento é
   → Alertar em p99, não em média
   → SLO típico: p99 < 500ms

2. Traffic — quanto trabalho o sistema está fazendo
   → HTTP: requests/segundo por endpoint
   → Streaming: conexões ativas, bytes/s
   → DB: queries/segundo, transações/segundo
   → Baseline para detectar anomalias e capacity planning

3. Errors — taxa de requisições que falham
   → Erros explícitos: HTTP 5xx, exceções não tratadas
   → Erros implícitos: 200 OK com corpo de erro, dados incorretos
   → Erros de política: respostas acima do SLO de latência
   → SLO típico: < 0.1% de erros

4. Saturation — quão "cheio" está o serviço
   → % de utilização do recurso mais constrained
   → CPU, memória, disco, threads, conexões DB
   → Sistemas degradam antes de atingir 100% — alertar em 80%
   → Indicador leading: prediz problemas antes de acontecerem
```

```yaml
# Alertas Prometheus para Four Golden Signals
groups:
  - name: four_golden_signals
    rules:
      # Latency — p99 acima de 500ms por 5 minutos
      - alert: HighP99Latency
        expr: |
          histogram_quantile(0.99,
            rate(http_request_duration_ms_bucket[5m])
          ) > 500
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "p99 latency {{ $value }}ms acima do SLO"

      # Traffic — queda súbita de tráfego (possível falha upstream)
      - alert: TrafficDrop
        expr: |
          rate(http_requests_total[5m]) < 
          rate(http_requests_total[1h] offset 1d) * 0.5
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Tráfego caiu 50% vs. mesmo período ontem"

      # Errors — taxa de erro acima de 1%
      - alert: HighErrorRate
        expr: |
          rate(http_errors_total[5m]) / 
          rate(http_requests_total[5m]) > 0.01
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Taxa de erro {{ $value | humanizePercentage }}"

      # Saturation — pool de conexões acima de 80%
      - alert: DBPoolSaturation
        expr: db_pool_utilization > 0.8
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Pool de conexões em {{ $value | humanizePercentage }}"
```

---

## Flame Graph — Profiling de CPU

Flame graphs visualizam onde a CPU está sendo gasta — cada "chama" é uma função, largura = % do tempo total.

```typescript
// Node.js — Gerar flame graph com Clinic.js
// npm install -g clinic

// 1. Rodar o processo com profiling:
// clinic flame -- node app.js

// 2. Clinic gera um HTML interativo com o flame graph

// Alternativa: 0x (mais simples para produção)
// npm install -g 0x
// 0x app.js

// Análise manual com v8-profiler-node8
import v8Profiler from "v8-profiler-node8";
import fs from "fs";

async function captureProfile(durationMs: number): Promise<void> {
  v8Profiler.startProfiling("cpu-profile", true);

  await new Promise(resolve => setTimeout(resolve, durationMs));

  const profile = v8Profiler.stopProfiling("cpu-profile");

  await new Promise<void>((resolve, reject) => {
    profile.export((error, result) => {
      if (error) { reject(error); return; }
      fs.writeFileSync("profile.cpuprofile", result!);
      profile.delete();
      resolve();
    });
  });

  // Abrir o arquivo no Chrome DevTools → Performance → Load profile
  console.log({ message: "Profile salvo em profile.cpuprofile" });
}

// Como ler um flame graph:
// → Eixo X: % do tempo de CPU (largura = custo relativo)
// → Eixo Y: call stack (base = raiz, topo = leaf functions)
// → Hot paths: funções largas no topo (onde CPU gasta mais tempo)
// → Vermelho/laranja: candidatos a otimização
// → Idle/GC: indica pressão de memória ou await excessivo
```

---

## k6 — Load Testing

```javascript
// k6 — cenário completo de load test
// Rodar: k6 run load-test.js

import http from "k6/http";
import { check, sleep } from "k6";
import { Rate, Trend, Counter } from "k6/metrics";

// Métricas customizadas
const errorRate = new Rate("errors");
const orderDuration = new Trend("order_creation_duration");
const successfulOrders = new Counter("successful_orders");

export const options = {
  // Cenário: ramp up → pico → ramp down
  stages: [
    { duration: "2m", target: 50 },    // ramp up para 50 VUs
    { duration: "5m", target: 50 },    // manter 50 VUs por 5min (soak test)
    { duration: "2m", target: 200 },   // spike para 200 VUs
    { duration: "5m", target: 200 },   // manter pico
    { duration: "2m", target: 0 },     // ramp down
  ],

  // Thresholds — falha o teste se violar
  thresholds: {
    http_req_duration: [
      "p(95)<500",   // 95% das requests < 500ms
      "p(99)<1000"   // 99% das requests < 1s
    ],
    errors: ["rate<0.01"],               // erro < 1%
    http_req_failed: ["rate<0.05"],      // falha HTTP < 5%
    successful_orders: ["count>1000"]    // mínimo 1000 orders criadas
  }
};

// Cenário: criar order (fluxo completo)
export default function () {
  const BASE_URL = __ENV.BASE_URL ?? "http://localhost:3000";

  // 1. Login
  const loginRes = http.post(
    `${BASE_URL}/auth/login`,
    JSON.stringify({ email: "test@example.com", password: "Test@1234" }),
    { headers: { "Content-Type": "application/json" } }
  );

  check(loginRes, { "login 200": r => r.status === 200 });

  const token = loginRes.json("token") as string;

  // 2. Criar order
  const orderStart = Date.now();

  const orderRes = http.post(
    `${BASE_URL}/orders`,
    JSON.stringify({ productId: "prod-123", quantity: 1 }),
    {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`
      }
    }
  );

  orderDuration.add(Date.now() - orderStart);

  const orderSuccess = check(orderRes, {
    "order 201": r => r.status === 201,
    "order has id": r => r.json("data.id") !== undefined
  });

  if (orderSuccess) {
    successfulOrders.add(1);
  } else {
    errorRate.add(1);
  }

  sleep(1);  // 1s entre iterações por VU
}

// Tipos de teste com k6:
// Smoke test:      1 VU, 1 min — valida que o script roda
// Load test:       carga esperada normal — valida baseline
// Stress test:     acima do normal — encontra breaking point
// Spike test:      pico súbito — como o sistema reage a burst
// Soak test:       carga normal por horas — encontra memory leaks, degradação gradual
// Breakpoint test: aumenta até falhar — capacidade máxima real
```

---

## Trade-offs

| Framework | Diagnostica | Quando Usar |
|---|---|---|
| **USE Method** | Recursos (CPU, memória, disco, rede) | "Meu servidor está lento — onde está o bottleneck?" |
| **RED Method** | Serviços e APIs | "Meu microsserviço está com problema — qual endpoint?" |
| **Four Golden Signals** | Saúde geral user-facing | "Meu SLO está em risco? O usuário está sofrendo?" |
| **Flame Graph** | CPU hot paths no código | "Sei que está lento — qual função exatamente?" |
| **k6** | Capacidade e SLOs sob carga | "Meu sistema aguenta o traffic esperado?" |

## Quando Usar / Quando Evitar

**USE antes de RED:** quando a degradação parece vir de infraestrutura (CPU alta, swap, disco saturado). RED quando parece ser do código de serviço.

**Four Golden Signals para alertas:** não alerte em cada métrica possível — foque nos 4 sinais. Alerta em métrica de implementação (ex: "cache miss rate") é ruído; alerte no sintoma (latência, erro).

**k6 em CI:** adicione smoke test no pipeline (1 VU, 30s). Load test completo pré-deploy em staging.

**Evitar médias em SLOs:** p99 é o contrato real com o usuário. Média mascara outliers que causam churn.

## Conceitos Relacionados

[[otel-sdk]] · [[sre-sli-slo-sla]] · [[structured-logging]] · [[distributed-tracing]] · [[kafka]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-04-17*
