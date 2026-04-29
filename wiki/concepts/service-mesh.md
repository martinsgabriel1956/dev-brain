---
type: concept
title: "Service Mesh"
aliases: ["service mesh", "malha de serviços"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [service-mesh, kubernetes, microsservicos, infraestrutura, resiliencia, seguranca]
skill: tech-mentor-system-design
status: stable
---

# Service Mesh

Camada de infraestrutura que move cross-cutting concerns de rede (retry, timeout, circuit breaker, mTLS, tracing) para fora do código da aplicação. A aplicação não sabe que existe — ela fala com localhost, o proxy faz o trabalho.

## Problema que Resolve

Sem mesh: cada serviço implementa retry, mTLS e tracing — duplicado em cada linguagem, por cada time.
Com mesh: uma configuração YAML aplica a política para todos os serviços do namespace.

## Arquitetura

```
Sem mesh:  Serviço A (código + retry + mTLS + tracing) → Serviço B (idem)

Com mesh:  Serviço A (só código) → [Proxy A] ↔ [Proxy B] → Serviço B (só código)
                                        ↕              ↕
                                   Control Plane (Istiod)
```

Ver [[concepts/sidecar-pattern]] para o mecanismo de injeção de proxy.

## Istio vs Linkerd

| | Istio | Linkerd |
|---|---|---|
| Sidecar | Envoy (~200MB/pod) | linkerd-proxy em Rust (~30MB/pod) |
| mTLS | ✅ | ✅ |
| Traffic shaping | Rico (canary, fault injection, mirror) | Básico (split de tráfego) |
| Complexidade operacional | Alta | Baixa |
| Quando usar | Traffic shaping avançado necessário | mTLS + observabilidade sem overhead |

## Quando Usar / Evitar

```
< 10 serviços → API Gateway + libs (opossum, resilience4j) resolvem 80%
> 10 serviços, SREs dedicados → avaliar Linkerd primeiro, Istio se precisar de shaping avançado
Time pequeno sem expertise em K8s → evitar — overhead operacional é real
```

## Observabilidade Automática

Golden signals de rede (taxa de erro, latência P99) sem instrumentação na aplicação:

```promql
# Taxa de erro por serviço
sum(rate(istio_requests_total{destination_service_name="order-service",response_code=~"5.."}[5m]))
/
sum(rate(istio_requests_total{destination_service_name="order-service"}[5m]))
```

Kiali visualiza o service graph com taxas de erro por link e status mTLS em tempo real.

## Conceitos Relacionados

[[concepts/sidecar-pattern]] · [[concepts/mtls]] · [[concepts/fault-injection]] · [[concepts/ambient-mesh]] · [[concepts/circuit-breaker]] · [[concepts/canary-release]]

## Key Sources

- [[sources/service-mesh]]
