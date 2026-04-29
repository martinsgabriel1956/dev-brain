---
type: source
title: "K8s Networking — CNI, Cilium, NetworkPolicy, Gateway API"
aliases: ["k8s networking", "cilium", "network policy", "gateway api", "ingress", "cni"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/k8s-networking.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [kubernetes, networking, cni, cilium, ebpf, network-policy, gateway-api, ingress, micro-segmentacao, canary]
skill: tech-mentor-infra
status: stable
---

## TL;DR

K8s networking tem 3 regras: Pod-to-Pod sem NAT, Node-to-Pod sem NAT, Pod vê seu próprio IP. CNI implementa essas regras — Cilium usa eBPF (mais performático, sem kube-proxy). NetworkPolicy implementa micro-segmentação (default deny-all + allow-list). Gateway API substitui Ingress com suporte nativo a canary e traffic splitting.

## Key Claims

**Claim:** Default deny-all + allow-list explícito é o único modelo de NetworkPolicy seguro.
**Evidence:** Sem NetworkPolicy, todo pod alcança todo pod — flat network. Um pod comprometido tem acesso a todos os outros serviços e bancos. Default deny-all no namespace + allow-list específico por serviço = blast radius controlado.
**Confidence:** alta

**Claim:** Gateway API supera Ingress para roteamento avançado — suporte nativo a canary, header-based routing, traffic splitting.
**Evidence:** Ingress: configuração via annotations não tipadas, sem suporte nativo a canary. Gateway API: HTTPRoute com `weight` para traffic splitting (90/10 canary). Separação de responsabilidades: infra gerencia Gateway, produto gerencia HTTPRoute.
**Confidence:** alta

**Claim:** Cilium com eBPF elimina kube-proxy — menor latência e melhor observabilidade.
**Evidence:** kube-proxy usa iptables O(n) para roteamento. Cilium usa eBPF O(1) — hash map em kernel space. Hubble (UI) oferece L7 visibility nativamente. 30% menos latência em clusters com muitos serviços.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/cni-kubernetes]]
- [[concepts/cilium]]
- [[concepts/ebpf]]
- [[concepts/network-policy]]
- [[concepts/gateway-api]]
- [[concepts/zero-trust]]

## Open Questions

- NetworkPolicy com Cilium CiliumNetworkPolicy (L7) vs K8s NetworkPolicy (L3/L4) — quando ir além do L4?
- Gateway API e cert-manager — como automatizar rotação de certificados TLS sem downtime?
