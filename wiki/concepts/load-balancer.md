---
type: concept
title: "Load Balancer"
aliases: ["lb", "load balancing", "l4", "l7", "round robin"]
date_created: 2026-04-23
date_updated: 2026-05-05
source_count: 2
tags: [load-balancer, l4, l7, round-robin, health-check, alta-disponibilidade, infra]
skill: tech-mentor-infra
status: stub
---

# Load Balancer

Componente que distribui tráfego entre múltiplas instâncias de um serviço para escalar horizontalmente e garantir disponibilidade.

**L4 vs L7:**
- **L4 (TCP/UDP):** mais rápido, sem inspecionar conteúdo. Para TCP genérico (banco, SMTP).
- **L7 (HTTP):** roteamento por path/header/host, SSL termination, cookie stickiness. Essencial para microsserviços e canary.

**Algoritmos:** Round Robin, Least Connections, IP Hash (stickiness), Weighted.

**Health check ativo:** coração do LB — remove instâncias não-saudáveis. Sem health check, o LB distribui para instâncias caídas.

**Alta disponibilidade:** LB não pode ser SPOF — active-passive com VIP (Virtual IP).

**Em microsserviços:** dois níveis — externo (L7 + SSL) + interno (service mesh/Envoy).

## Key Sources

- [[sources/load-balancer]]
- [[sources/clusters]]
