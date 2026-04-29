---
date: 2026-04-17
tags: [tech-mentor, performance, profiling, observabilidade, sre]
skill: tech-mentor-infra/references/observability
level: avançado
---

# Flame Graph, USE Method, RED Method e Four Golden Signals

## Flame Graph — CPU Profiling

### Contexto
Flame graphs visualizam onde o CPU passa o tempo durante a execução. O eixo X representa tempo acumulado (largura = % de CPU), o eixo Y representa a call stack. Cada retângulo é um frame de função — quanto mais largo, mais CPU consumiu.

Criado por Brendan Gregg, são a forma mais eficiente de identificar **hot paths** em código de produção.

```
▲ (topo = leaf functions — onde o CPU realmente estava)
│  processPayment  ████████████████
│  validateCard    ████  └─ bcrypt.hash ████████████████
│  db.query        ████████
│  serialize       ████
└─────────────────────────────────────────────► (base = onde a execução começou)
```

**Leitura:** procure os retângulos largos no topo da stack — são as funções que mais consomem CPU e que você pode otimizar.

### Node.js — Clinic.js e 0x

```bash
# Clinic.js — ferrramenta completa de diagnóstico Node
npm install -g clinic

# Flame graph do processo sob carga
clinic flame -- node server.js

# Doctor — detecta event loop lag, memory leaks, I/O issues
clinic doctor -- node server.js

# 0x — flame graph mais simples e rápido
npm install -g 0x
0x server.js
```

### Go — pprof

```go
import _ "net/http/pprof"

// Servidor de profiling (NÃO expor em produção sem auth)
go func() {
    http.ListenAndServe("localhost:6060", nil)
}()
```

```bash
# Coletar CPU profile por 30 segundos
go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30

# Dentro do pprof:
(pprof) web         # abre flame graph no browser
(pprof) top 10      # top 10 funções por CPU
(pprof) list funcName  # código da função com anotações
```

---

## USE Method — Diagnóstico de Recursos

Framework de Brendan Gregg para diagnosticar **gargalos de infraestrutura**. Para cada recurso físico, verifique:

- **U**tilization: qual % do recurso está sendo usado?
- **S**aturation: há filas aguardando o recurso?
- **E**rrors: há erros acontecendo?

```
Recurso         | Utilization          | Saturation           | Errors
----------------|----------------------|----------------------|------------------
CPU             | top, mpstat          | load average > cores | dmesg, perf
Memória         | free -m              | swap usage           | OOM killer logs
Disco           | iostat %util         | await time           | dmesg I/O errors
Rede            | ifstat, sar -n DEV   | dropped packets      | netstat -s
PostgreSQL conn | pg_stat_activity     | pg_stat_bgwriter     | pg_log
```

**Diagnóstico rápido via USE:**
1. CPU util > 80% por período sustentado? → Escala horizontal ou otimiza código
2. Load average > número de cores? → Saturação de CPU → processos esperando scheduler
3. Swap em uso? → Memória saturada → application em paging → latência alta

---

## RED Method — Diagnóstico de Serviços

Para **serviços** (APIs, microsserviços), o USE não se aplica diretamente. O RED Method foca no ponto de vista do request:

- **R**ate: quantas requisições por segundo?
- **E**rrors: qual a taxa de erro?
- **D**uration: qual a latência (p50, p95, p99)?

```typescript
// Instrumentação RED com OpenTelemetry
import { metrics } from "@opentelemetry/api";

const meter = metrics.getMeter("orders-service");

const requestCounter = meter.createCounter("http_requests_total", {
  description: "Total HTTP requests"
});

const requestDuration = meter.createHistogram("http_request_duration_seconds", {
  description: "HTTP request duration",
  boundaries: [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5]
});

app.use((req, res, next) => {
  const start = Date.now();

  res.on("finish", () => {
    const labels = { method: req.method, route: req.route?.path, status: String(res.statusCode) };
    requestCounter.add(1, labels);
    requestDuration.record((Date.now() - start) / 1000, labels);
  });

  next();
});
```

---

## Four Golden Signals (Google SRE)

Expandem o RED Method com um quarto sinal voltado à infraestrutura:

| Signal | Definição | Métrica típica |
|---|---|---|
| **Latency** | Tempo para atender requisições — separar sucesso de erro | p99 < 200ms |
| **Traffic** | Volume de carga no sistema | Requests/s, queries/s |
| **Errors** | Taxa de requisições falhando | HTTP 5xx rate < 0.1% |
| **Saturation** | Quão "cheio" está o sistema | CPU > 80%, queue depth > N |

**Regra prática:** se você só pode monitorar 4 coisas, monitore essas. Os alertas mais valiosos saem dos Golden Signals, não de métricas de baixo nível.

```yaml
# Alertas Prometheus baseados nos Golden Signals
groups:
  - name: golden-signals
    rules:
      - alert: HighLatency
        expr: histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m])) > 0.5
        for: 5m
        labels: { severity: warning }

      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.01
        for: 2m
        labels: { severity: critical }

      - alert: HighSaturation
        expr: rate(cpu_usage_seconds_total[5m]) > 0.8
        for: 10m
        labels: { severity: warning }
```

## Conceitos Relacionados
[[observabilidade]] · [[sre-sli-slo-sla]] · [[otel-sdk]] · [[performance-methods]] · [[distributed-tracing]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-04-17*
