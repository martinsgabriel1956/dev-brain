---
type: concept
title: "Go — Production e Observabilidade"
aliases: ["go graceful shutdown", "go health check", "go prometheus", "go otel", "go pprof"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [go, producao, graceful-shutdown, health-checks, prometheus, opentelemetry, pprof, docker]
skill: lang-systems
status: stable
---

# Go — Production e Observabilidade

Checklist de produção para serviços Go: graceful shutdown, health checks, métricas, tracing, profiling e Docker multi-stage.

## Graceful Shutdown

```go
quit := make(chan os.Signal, 1)
signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
<-quit

ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()
server.Shutdown(ctx) // drena conexões ativas, não aceita novas
```

Usar `Shutdown()` — não `Close()`. Timeout de 30s cobre requests em andamento.

## Health Checks

```go
// /health — liveness: processo está vivo?
// /ready  — readiness: pode receber tráfego? (DB conectado, dependências ok)
r.Get("/health", func(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)
})

r.Get("/ready", func(w http.ResponseWriter, r *http.Request) {
    if err := db.PingContext(r.Context()); err != nil {
        w.WriteHeader(http.StatusServiceUnavailable)
        return
    }
    w.WriteHeader(http.StatusOK)
})
```

K8s usa `/ready` para rolling deploys — crítico para [[zero-downtime-deploy]].

## Métricas com Prometheus

```go
var httpRequests = prometheus.NewCounterVec(
    prometheus.CounterOpts{Name: "http_requests_total"},
    []string{"method", "path", "status"},
)

func init() { prometheus.MustRegister(httpRequests) }
```

Expor `/metrics` e scrape com Prometheus + dashboards Grafana.

## Tracing com OpenTelemetry

```go
tp := sdktrace.NewTracerProvider(
    sdktrace.WithBatcher(exporter),
)
otel.SetTracerProvider(tp)

tracer := otel.Tracer("service-name")
ctx, span := tracer.Start(ctx, "operation-name")
defer span.End()
```

## pprof

```go
// Porta separada — nunca expor em :8080 em produção
go http.ListenAndServe(":6060", nil) // pprof registra handlers via import
import _ "net/http/pprof"
```

```bash
go tool pprof http://localhost:6060/debug/pprof/heap
go tool pprof http://localhost:6060/debug/pprof/goroutine
```

## Docker Multi-Stage

```dockerfile
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 go build -o server ./cmd/server

FROM scratch
COPY --from=builder /app/server /server
ENTRYPOINT ["/server"]
```

Binário < 20MB, sem shell, sem package manager — superfície de ataque mínima.

## Ver também

- [[observabilidade]] — três pilares: logs, métricas, traces
- [[zero-downtime-deploy]] — graceful shutdown no contexto de rolling deploy
- [[go-arquitetura]] — estrutura de projeto que viabiliza estes patterns

## Key Sources

- [[wiki/sources/go-producao]]
