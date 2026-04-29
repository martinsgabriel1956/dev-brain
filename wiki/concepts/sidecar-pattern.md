---
type: concept
title: "Sidecar Pattern"
aliases: ["sidecar", "sidecar proxy", "sidecar container"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [kubernetes, service-mesh, arquitetura, infraestrutura]
skill: tech-mentor-system-design
status: stable
---

# Sidecar Pattern

Container auxiliar injetado em cada pod que intercepta todo o tráfego de rede da aplicação principal. A aplicação não sabe que existe — fala com localhost, o sidecar faz retry, mTLS, coleta métricas.

## Como Funciona

O proxy intercepta tráfego de saída (outbound) e de entrada (inbound). Do ponto de vista da aplicação: ela conecta em localhost na porta normal. O sidecar redireciona via iptables antes que o pacote saia do pod.

```bash
# Istio: habilitar injeção automática na namespace
kubectl label namespace checkout istio-injection=enabled

# Pod com sidecar aparece como 2/2
kubectl get pods -n checkout
# NAME                READY   STATUS
# checkout-api-xxx    2/2     Running   ← app + istio-proxy
```

## Vantagens

- Cross-cutting concerns (retry, mTLS, tracing) sem alterar código da aplicação
- Políticas aplicadas uniformemente independente da linguagem do serviço
- Atualização de política sem redeploy da aplicação

## Desvantagem

- Overhead de memória: Envoy ~200MB por pod, linkerd-proxy ~30MB
- Latência adicional por hop (microsegundos — raramente perceptível)
- Debugging mais complexo: problema na app ou no proxy?

## Alternativa: Ambient Mesh

[[concepts/ambient-mesh]] — proxy no nível do nó (ztunnel) elimina o sidecar por pod. Istio 1.22+.

## Key Sources

- [[sources/service-mesh]]
