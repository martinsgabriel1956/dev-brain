---
type: source
title: "Service Discovery"
aliases: ["service discovery", "client-side discovery", "server-side discovery", "consul", "kubernetes dns"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 0
tags: [sistemas-distribuidos, networking, microsservicos, kubernetes, consul, dns]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-study/raw/service-discovery.md
source_url: ""
author: ""
date_published: 2026-04-17
date_ingested: 2026-04-22
---

# Service Discovery

## TL;DR

Em ambientes dinâmicos (K8s, ECS, auto-scaling), IPs mudam — service discovery é o mecanismo para serviços se encontrarem. No Kubernetes: DNS-based é o padrão (zero overhead). Fora do K8s ou multi-cloud: Consul. Client-side quando precisa de controle fino de LB; server-side quando quer clientes simples.

## Key Claims

**Claim:** Client-side discovery dá controle total ao cliente sobre balanceamento, mas acoplando lógica de discovery em cada cliente.
**Evidence:** Cliente consulta Service Registry (Consul/Eureka) → recebe lista de instâncias → aplica round-robin/circuit breaker/affinity. Trade-off: poder vs acoplamento — mudança de estratégia de LB requer atualização de todos os clientes.
**Confidence:** alta

**Claim:** Server-side discovery simplifica clientes ao custo de um hop extra e ponto crítico no load balancer.
**Evidence:** Cliente envia request para LB (Envoy/Kong) → LB consulta registry e roteia. Mudança de estratégia transparente para clientes. LB vira SPOF se não houver HA.
**Confidence:** alta

**Claim:** No Kubernetes, DNS-based discovery é o padrão — cada Service recebe nome DNS estável sem lógica de discovery no cliente.
**Evidence:** `http://order-service.production.svc.cluster.local` — kube-dns resolve para ClusterIP, kube-proxy distribui entre pods via iptables/IPVS. Zero código de discovery na aplicação.
**Confidence:** alta

**Claim:** Consul é a escolha para ambientes fora do K8s ou multi-cloud — health check integrado com deregistro automático.
**Evidence:** `deregisterCriticalServiceAfter: "30s"` remove instâncias doentes automaticamente. `consul.health.service({ passing: true })` retorna apenas instâncias saudáveis. Registro/deregistro via SIGTERM handler.
**Confidence:** alta

## Concepts & Entities Touched

[[concepts/service-discovery]] · [[concepts/service-mesh]] · [[concepts/sidecar-pattern]]

## Open Questions

- Consul vs etcd para service discovery em multi-cloud — quando cada um?
- DNS negative caching no K8s — como evitar que falhas de lookup sejam cacheadas?
- Service discovery para workers assíncronos (sem HTTP) — qual o padrão?
