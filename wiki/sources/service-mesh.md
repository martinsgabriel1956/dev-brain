---
type: source
title: "Service Mesh (Istio, Linkerd, mTLS)"
aliases: ["service mesh", "istio", "linkerd", "mtls service mesh"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 0
tags: [service-mesh, istio, linkerd, mtls, sidecar, kubernetes, observabilidade, resiliencia]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-study/raw/service-mesh.md
source_url: ""
author: ""
date_published: 2026-03-29
date_ingested: 2026-04-22
---

# Service Mesh (Istio, Linkerd, mTLS)

## TL;DR

Service mesh move retry, timeout, circuit breaker, mTLS e tracing para a infraestrutura de rede via sidecar proxy — a aplicação não sabe que existe. Istio para traffic shaping avançado; Linkerd para mTLS + observabilidade com overhead mínimo. Menos de 10 serviços: provavelmente não justifica.

## Key Claims

**Claim:** Service mesh elimina duplicação de cross-cutting concerns (retry, mTLS, tracing) entre serviços — move para proxy sem alterar código da aplicação.
**Evidence:** Sidecar pattern: proxy container injetado em cada pod intercepta todo tráfego. Aplicação fala com localhost — proxy faz retry, mTLS, coleta métricas. `kubectl label namespace checkout istio-injection=enabled` é suficiente para ativar.
**Confidence:** alta

**Claim:** mTLS automático com Istio garante que pods comprometidos não consigam chamar serviços não autorizados — mesmo dentro do cluster.
**Evidence:** `PeerAuthentication mode: STRICT` rejeita plaintext. `AuthorizationPolicy` define quais service accounts podem chamar quais endpoints. Identidade via certificado SPIFFE baseado em Kubernetes Service Account.
**Confidence:** alta

**Claim:** Canary deploy, fault injection e retry/timeout são configuráveis via YAML sem alterar código.
**Evidence:** VirtualService define split de tráfego (90/10 por weight ou por header). Fault injection injeta delay (10%) e abort (5% retorna 503) para testar resiliência. Retry: `attempts: 3`, `perTryTimeout: 2s`, `retryOn: "5xx,reset,connect-failure"`.
**Confidence:** alta

**Claim:** Linkerd consome ~30MB por pod vs ~200MB do Istio (Envoy) — escolha depende de necessidade de traffic shaping avançado.
**Evidence:** Istio: Envoy proxy, rico em funcionalidades (canary, fault injection, mirror), alta complexidade operacional. Linkerd: proxy em Rust, leve, mTLS + observabilidade com dashboard built-in, complexidade baixa.
**Confidence:** alta

**Claim:** Ambient mesh (Istio 1.22+) elimina o sidecar movendo o proxy para o nível do nó (ztunnel), reduzindo overhead significativamente em clusters grandes.
**Evidence:** `istioctl install --set profile=ambient` + `kubectl label namespace istio.io/dataplane-mode=ambient`. Waypoint proxy (L7) apenas para namespaces que precisam de políticas avançadas. Sidecar ainda mais estável e com controle granular por pod.
**Confidence:** alta

**Claim:** Service mesh não justifica para menos de 10 serviços — API Gateway + libs de resiliência na aplicação resolvem 80% dos casos.
**Evidence:** Overhead operacional real: atualizações de proxy, debugging de tráfego no sidecar, curva de aprendizado de CRDs Istio. Alternativas: opossum (Node.js), resilience4j (Java) para circuit breaker/retry na aplicação.
**Confidence:** alta

## Concepts & Entities Touched

[[concepts/service-mesh]] · [[concepts/sidecar-pattern]] · [[concepts/mtls]] · [[concepts/fault-injection]] · [[concepts/ambient-mesh]] · [[concepts/circuit-breaker]] · [[concepts/canary-release]] · [[concepts/zero-downtime-deploy]]

## Open Questions

- Ambient mesh em produção já é estável o suficiente para workloads críticos (2026)?
- Como debugar quando o problema está no proxy Envoy e não na aplicação?
- Service mesh vale para sistemas com SLA interno relaxado (< 99.9%)?
