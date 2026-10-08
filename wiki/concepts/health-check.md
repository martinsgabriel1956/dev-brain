---
type: concept
title: "Health Check"
aliases: ["healthcheck", "verificação de saúde", "/health"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [health-check, load-balancer, alta-disponibilidade, infra]
skill: tech-mentor-infra
status: stub
---

# Health Check

Sondagem periódica que o [[wiki/concepts/load-balancer]] faz em cada instância (tipicamente uma rota `/health` que responde "healthy"). Quem não responde é marcado como morto e sai do rodízio; quando volta a responder, reentra. Configura-se quantas falhas consecutivas marcam como morto e quantos sucessos marcam como vivo. Sem ele, o LB mandaria requisições a servidores caídos (500/404) e o cliente sofreria. Complementar com logs e alertas ([[wiki/concepts/observabilidade]]) para a equipe saber da queda. Base da [[wiki/concepts/alta-disponibilidade]].

## Key sources

- [[wiki/sources/load-balancer-como-funciona-algoritmos-health-check-nginx-haproxy]]
