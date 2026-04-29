---
type: concept
title: "Ambient Mesh"
aliases: ["ambient mesh", "istio ambient", "ztunnel", "sidecarless mesh"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [service-mesh, istio, kubernetes, infraestrutura]
skill: tech-mentor-system-design
status: stable
---

# Ambient Mesh

Modo de operação do Istio (1.22+) que elimina o sidecar por pod, movendo o proxy para o nível do nó. Reduz overhead de memória significativamente em clusters grandes.

## Arquitetura

```
Sidecar:  Pod [app + envoy] → Pod [app + envoy]
Ambient:  Pod [app] → ztunnel (nó) → waypoint (namespace, L7) → Pod [app]
```

- **ztunnel** — proxy L4 no nível do nó; lida com mTLS e roteamento básico
- **waypoint proxy** — proxy L7 por namespace; apenas para namespaces que precisam de políticas avançadas (AuthorizationPolicy, fault injection)

## Ativação

```bash
istioctl install --set profile=ambient
kubectl label namespace production istio.io/dataplane-mode=ambient

# Waypoint apenas onde necessário
istioctl waypoint apply --namespace payments
```

## Vantagem vs Sidecar

- Sem overhead de container Envoy por pod (~200MB economizados por pod)
- Operação mais simples — sem gerenciar injeção de sidecar
- Deploy de aplicação mais rápido (sem wait de sidecar ready)

## Quando Preferir Sidecar

- Precisa de controle granular por pod (políticas diferentes dentro do mesmo namespace)
- Workloads críticos em produção — sidecar ainda é mais estável e maduro (2026)
- Debugging mais previsível — o sidecar é visível no pod

## Key Sources

- [[sources/service-mesh]]
