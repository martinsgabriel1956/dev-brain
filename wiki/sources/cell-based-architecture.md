---
type: source
title: "Cell-Based Architecture"
aliases: ["cell based architecture", "cell architecture", "blast radius", "tenant isolation", "shard architecture"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/cell-based-architecture.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [cell-based-architecture, blast-radius, tenant-isolation, sharding, availability, resilience, multi-tenant]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Cell-Based Architecture particiona o sistema em células funcionalmente completas e independentes — cada célula serve um subconjunto de usuários ou tenants. Falha em uma célula não afeta as demais (blast radius containment). Adotada por Amazon, Slack, Discord, Shopify. Trade-off: complexidade operacional alta, justificada apenas para sistemas com SLAs críticos e escala >1M usuários.

## Key Claims

**Claim:** Cell-Based Architecture resolve blast radius — falha em uma célula não derruba o sistema inteiro.
**Evidence:** Arquitetura global única: bug de deploy atinge 100% dos usuários. Com células: deploy em célula 1 de 10 → afeta apenas 10% dos usuários. Rollback isolado por célula. Amazon usa internamente; Slack particionou por workspace — incidente em uma célula não afeta outras.
**Confidence:** alta

**Claim:** Cada célula é funcionalmente completa — tem seu próprio banco, cache, serviços e broker.
**Evidence:** Célula não compartilha recursos com outras células. Usuário A vai sempre para Célula 1 (por hash do ID). Célula 1 tem: PostgreSQL A, Redis A, serviços A. Sem dependências entre células em runtime. Complexidade: roteamento de entrada (cell router) + sincronização de dados entre células quando necessário.
**Confidence:** alta

**Claim:** Cell-Based é adequado apenas para sistemas com alta escala e SLAs críticos — complexidade operacional alta.
**Evidence:** Custo: cada célula = infra completa duplicada (N células = N× custo base). Operação: deploys devem ser coordenados por célula, monitoramento por célula. Para sistemas com <100k usuários ou SLA de 99.9%, microserviços com múltiplas AZs é suficiente. Cell-based justifica para 99.99%+ e >1M usuários.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/cell-based-architecture]]
- [[concepts/blast-radius]]
- [[concepts/tenant-isolation]]
- [[concepts/sharding]]
- [[concepts/availability-zones]]

## Open Questions

- Cell routing com migração de usuários entre células — como fazer sem downtime e sem perda de dados?
- Cell-based vs multi-region — quando cada abordagem resolve melhor o problema de blast radius?
