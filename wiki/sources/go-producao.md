---
type: source
title: "Go — Production e Observabilidade"
aliases: ["go graceful shutdown", "go prometheus", "go opentelemetry", "go pprof", "go docker"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/go-producao.md
source_url: ""
author: "lang-systems skill"
date_published: 2026-04-24
date_ingested: 2026-04-24
source_count: 0
tags: [go, producao, graceful-shutdown, health-checks, prometheus, opentelemetry, pprof, docker]
skill: lang-systems
status: stable
---

# Go — Production e Observabilidade

## TL;DR

Graceful shutdown em Go: capturar SIGTERM/SIGINT com `os.Signal`, chamar `http.Server.Shutdown(ctx)` com timeout. Health checks: `/health` (liveness) e `/ready` (readiness — DB, dependências). Métricas com `prometheus/client_golang`. Tracing com OpenTelemetry SDK. pprof exposto em porta separada para profiling em produção. Docker multi-stage build produz binários < 20MB.

## Claims Principais

| Claim | Confiança |
|---|---|
| Graceful shutdown deve usar `server.Shutdown()` — não `server.Close()` | Alta |
| `/ready` distingue "processo vivo" de "pronto para tráfego" — crítico em rolling deploys | Alta |
| pprof em porta separada (não :8080) evita exposição acidental em produção | Alta |
| Docker multi-stage: `golang:1.22-alpine` para build → `scratch` ou `alpine` para runtime | Alta |
| `otel.SetTracerProvider` global deve ser inicializado antes de qualquer handler | Alta |

## Conceitos Abordados

- [[go-producao]] · [[go-arquitetura]] · [[go-ecossistema]] · [[observabilidade]] · [[zero-downtime-deploy]]
