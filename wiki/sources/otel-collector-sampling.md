---
type: source
title: "OTel Collector — Pipeline, Tail Sampling e Auto-instrumentation"
aliases: ["otel collector", "tail sampling", "head sampling", "auto instrumentation", "pyroscope", "continuous profiling"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/otel-collector-sampling.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [otel-collector, tail-sampling, auto-instrumentation, pyroscope, continuous-profiling, ebpf, opentelemetry]
skill: tech-mentor-infra
status: stable
---

## TL;DR

OTel Collector: gateway de observabilidade que recebe traces/métricas/logs e exporta para backends. Tail Sampling: decisão de sampling APÓS a request completar — retém 100% dos erros e spans lentos, descarta requests normais. Auto-instrumentation zero-code via OTel Operator em K8s. Continuous Profiling com Pyroscope/eBPF: correlaciona profiles com traces.

## Key Claims

**Claim:** Tail Sampling retém exatamente o que importa — erros, latência alta, 5% de requests normais.
**Evidence:** Head Sampling (probabilístico): 5% aleatório — pode descartar o único trace de um bug crítico. Tail Sampling: aguarda toda a request completar, avalia o resultado. Policy: 100% de spans com `status_code=ERROR`, 100% de spans com `duration > 500ms`, 5% dos demais. Decisão inteligente após conhecer o resultado real.
**Confidence:** alta

**Claim:** Auto-instrumentation K8s via OTel Operator injeta agente sem modificar o código da aplicação.
**Evidence:** OTel Operator: annotation `instrumentation.opentelemetry.io/inject-nodejs: "true"` no Deployment. Operator injeta init container que instala o agente antes do app iniciar. Captura automaticamente: HTTP, Express, database queries, cache calls — sem `require("@opentelemetry/sdk-node")` no código. Zero esforço para onboarding de novos serviços.
**Confidence:** alta

**Claim:** Continuous Profiling com Pyroscope/eBPF correlaciona CPU profiles com traces — identifica onde o CPU vai em requests específicas.
**Evidence:** Pyroscope: profiling contínuo com overhead < 1%. eBPF: sem agente no processo, profiling a nível de kernel. Integração com OTel: profile ID no trace span permite correlacionar "essa request específica gastou 80% do CPU em serialização JSON". Diagnóstico de performance em produção sem profiling on-demand que distorce o comportamento.
**Confidence:** alta

## Entities & Concepts Touched

- [[entities/otel-collector]]
- [[concepts/tail-sampling]]
- [[concepts/auto-instrumentation]]
- [[entities/pyroscope]]
- [[concepts/continuous-profiling]]
- [[concepts/ebpf]]
- [[concepts/opentelemetry]]

## Open Questions

- Tail Sampling em sistemas distribuídos: como garantir que spans de diferentes serviços da mesma trace cheguem ao mesmo Collector para a decisão?
- Continuous profiling com eBPF em K8s — compatibilidade com kernels de diferentes cloud providers?
