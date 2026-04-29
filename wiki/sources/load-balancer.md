---
type: source
title: "Load Balancer"
aliases: ["load balancing", "l4 l7", "round robin", "least connections", "health check"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [load-balancer, l4, l7, round-robin, least-connections, health-check, alta-disponibilidade, infra]
skill: tech-mentor-infra
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/load-balancer.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# Load Balancer

## TL;DR

Load Balancer distribui tráfego entre instâncias para escalar horizontalmente e garantir disponibilidade. L4 opera na camada TCP (mais rápido, sem inspecionar conteúdo); L7 opera na camada HTTP (roteamento por path/header, SSL termination, cookie-based stickiness). Algoritmos: Round Robin, Least Connections, IP Hash, Weighted. Health check ativo é o coração do LB — sem ele, traffic vai para instâncias mortas.

## Key Claims

| Claim | Evidência |
|---|---|
| L7 permite roteamento inteligente: path, header, host-based | Essencial para microsserviços e canary releases |
| L4 é mais performático — não precisa inspecionar payload | Adequado para TCP genérico (banco, SMTP) |
| Health check ativo remove instâncias não-saudáveis automaticamente | Sem health check, LB distribui para instâncias caídas |
| LB em dois níveis em microsserviços: externo (L7 + SSL) + interno (service mesh) | Padrão com Istio/Envoy |
| Alta disponibilidade do LB: active-passive com VIP (Virtual IP) | LB não pode ser SPOF |

## Conceitos

- [[concepts/load-balancer]] — algoritmos e camadas
- [[concepts/service-discovery]] — como o LB sabe quais instâncias existem
- [[concepts/service-mesh]] — LB interno via sidecar
- [[concepts/canary-release]] — LB L7 roteia % do tráfego
- [[concepts/horizontal-vs-vertical-scaling]] — LB é pré-requisito para escala horizontal

## Key Sources

_Este é o documento primário._
