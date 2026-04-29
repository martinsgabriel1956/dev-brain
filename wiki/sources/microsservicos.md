---
type: source
title: "Microsserviços"
aliases: ["microsservicos", "microservices", "decomposicao por dominio", "service mesh", "bounded context"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/microsservicos.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [microsservicos, decomposicao, autonomia-deploy, circuit-breaker, service-discovery, distributed-monolith, strangler-fig]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Microsserviços são serviços independentes com autonomia de deploy, dados isolados, e domínio coeso. Decomposição correta: por Bounded Context (DDD), não por camada técnica. Resiliência obrigatória: Circuit Breaker + Retry. O anti-pattern mais comum: Distributed Monolith (microsserviços com banco compartilhado ou chamadas síncronas em cascata).

## Key Claims

**Claim:** Decomposição por Bounded Context é o critério correto — não por camada técnica.
**Evidence:** "Serviço de dados" + "Serviço de API" = Distributed Monolith técnico. "Orders Service" + "Payments Service" = microsserviços por domínio. Cada domínio tem dados isolados, linguagem própria, deploy independente.
**Confidence:** alta

**Claim:** Microsserviços só fazem sentido para times grandes com domínios distintos — não para startups.
**Evidence:** Overhead de microsserviços: service discovery, distributed tracing, networking, eventual consistency, deploy complexo. Para time de < 5 devs: Monolito Modular com mesma qualidade de código, 10× menos complexidade operacional.
**Confidence:** alta

**Claim:** Padrões de resiliência são obrigatórios — falhas parciais são o estado normal em microsserviços.
**Evidence:** Payments Service down 5min/mês = 99.99% uptime. Payments + Orders + Inventory encadeados = (99.99%)³ = 99.97% = ~2h downtime/mês. Circuit Breaker + Fallback previne propagação de falha.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/microsservicos]]
- [[concepts/bounded-context]]
- [[concepts/distributed-monolith]]
- [[concepts/circuit-breaker]]
- [[concepts/service-discovery]]
- [[concepts/strangler-fig]]
- [[concepts/conways-law]]

## Open Questions

- Dados compartilhados entre serviços (ex: catálogo de produtos usado por Orders e Inventory) — como evitar duplicação vs acoplamento?
- Service mesh (Istio) vs library-level resilience (Hystrix/Resilience4j) — quando cada abordagem é melhor?
