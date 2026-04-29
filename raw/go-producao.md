---
date: 2026-04-24
tags: [tech-mentor, lang-systems, go, producao, graceful-shutdown, observabilidade, docker, prometheus, opentelemetry]
skill: lang-systems/references/go
level: avançado
---

# Go — Production e Observabilidade

## Contexto
Go é a linguagem de escolha para infraestrutura de produção. Os primitivos de shutdown gracioso, health checks e observabilidade são todos resolvíveis com stdlib + libs leves. O resultado é binários pequenos, previsíveis e fáceis de operar.

---

## Graceful Shutdown

```go
func main() {
    srv := &http.Server{Addr: ":8080", Handler: router}

    // Canal para receber sinais do OS
    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)

    go func() {
        if err := srv.ListenAndServe(); !errors.Is(err, http.ErrServerClosed) {
            log.Fatalf("server error: %v", err)
        }
    }()

    <-quit // bloqueia até SIGINT/SIGTERM
    slog.Info("shutting down server...")

    // Contexto com timeout para terminar requests em voo
    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()

    if err := srv.Shutdown(ctx); err != nil {
        slog.Error("shutdown error", "err", err)
        os.Exit(1)
    }

    // Fechar outros recursos: DB, brokers, etc.
    db.Close()
    slog.Info("server stopped")
}
```

---

## Health Checks

```go
// /healthz — liveness: o processo está vivo?
// /readyz  — readiness: pronto para receber tráfego?

func healthzHandler(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)
    w.Write([]byte("ok"))
}

func readyzHandler(db *sql.DB) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        ctx, cancel := context.WithTimeout(r.Context(), 2*time.Second)
        defer cancel()

        if err := db.PingContext(ctx); err != nil {
            http.Error(w, "database unavailable", http.StatusServiceUnavailable)
            return
        }

        w.WriteHeader(http.StatusOK)
        json.NewEncoder(w).Encode(map[string]string{"status": "ready"})
    }
}
```

---

## Métricas com Prometheus

```go
import "github.com/prometheus/client_golang/prometheus"
import "github.com/prometheus/client_golang/prometheus/promauto"

var (
    requestsTotal = promauto.NewCounterVec(prometheus.CounterOpts{
        Name: "http_requests_total",
        Help: "Total de requisições HTTP",
    }, []string{"method", "path", "status"})

    requestDuration = promauto.NewHistogramVec(prometheus.HistogramOpts{
        Name:    "http_request_duration_seconds",
        Help:    "Duração das requisições HTTP",
        Buckets: prometheus.DefBuckets,
    }, []string{"method", "path"})
)

// Middleware de métricas
func metricsMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()
        rw := &responseWriter{ResponseWriter: w, status: 200}

        next.ServeHTTP(rw, r)

        duration := time.Since(start).Seconds()
        status := strconv.Itoa(rw.status)

        requestsTotal.WithLabelValues(r.Method, r.URL.Path, status).Inc()
        requestDuration.WithLabelValues(r.Method, r.URL.Path).Observe(duration)
    })
}

// Expor endpoint
mux.Handle("GET /metrics", promhttp.Handler())
```

---

## Tracing com OpenTelemetry

```go
import (
    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/trace"
)

// Setup (uma vez no main)
tp := initTracerProvider(ctx, serviceName, otlpEndpoint)
defer tp.Shutdown(ctx)
otel.SetTracerProvider(tp)

// Instrumentar handlers
tracer := otel.Tracer("myapp")

func getUserHandler(w http.ResponseWriter, r *http.Request) {
    ctx, span := tracer.Start(r.Context(), "getUserHandler")
    defer span.End()

    id := chi.URLParam(r, "id")
    span.SetAttributes(attribute.String("user.id", id))

    user, err := repo.FindByID(ctx, id) // ctx propagado
    if err != nil {
        span.RecordError(err)
        span.SetStatus(codes.Error, err.Error())
        http.Error(w, "error", 500)
        return
    }

    json.NewEncoder(w).Encode(user)
}
```

---

## Profiling com pprof

```go
import _ "net/http/pprof"

// Adicionar ao servidor de admin (nunca no servidor público)
go func() {
    log.Println(http.ListenAndServe("localhost:6060", nil))
}()
```

```bash
# CPU profile por 30s
go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30

# Heap
go tool pprof http://localhost:6060/debug/pprof/heap

# Goroutines ativas
curl http://localhost:6060/debug/pprof/goroutine?debug=1
```

---

## Docker Multi-Stage Build

```dockerfile
FROM golang:1.23-alpine AS builder
WORKDIR /app

# Layer de deps separada — cache no Docker
COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build \
    -ldflags="-w -s" \
    -o server ./cmd/server

# Imagem final — sem Go runtime, sem shell
FROM scratch
COPY --from=builder /app/server /server
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

EXPOSE 8080
ENTRYPOINT ["/server"]
```

`-ldflags="-w -s"` remove debug symbols e DWARF — reduz binário em ~30%.

---

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---------|----------|-------------|
| Graceful shutdown | Requests em voo terminam | Precisa de timeout para evitar hang infinito |
| pprof | Profiling em produção sem restart | Expor porta 6060 é risco de segurança |
| Imagem scratch | Mínima (~5MB), sem shell | Difícil debug — usar distroless como alternativa |
| OTel | Vendor-neutral | SDK adiciona latência mínima, mais deps |

## Quando Usar / Quando Evitar

**pprof em produção:** expor apenas em interface localhost ou rede interna. Nunca no endpoint público — revela detalhes da aplicação.

**scratch vs distroless:** scratch para máxima redução. `gcr.io/distroless/static` se precisar de debug básico (não tem shell mas tem algumas ferramentas).

## Conceitos Relacionados
[[go-concorrencia]] · [[go-arquitetura]] · [[opentelemetry]] · [[docker-multi-stage]] · [[cicd-pipeline]]

---
*Fonte: tech-mentor skill · lang-systems · 2026-04-24*
