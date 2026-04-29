---
type: source
title: "Fase 1 — Fundamentos de Infraestrutura"
aliases: ["fundamentos infraestrutura", "dns load balancer cdn cache", "back of envelope", "latencia numeros"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/fase-1-fundamentos-infraestrutura.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [fundamentos, dns, load-balancer, cdn, cache, mensageria, back-of-envelope, latencia, infraestrutura]
skill: tech-mentor-infra
status: stable
---

## TL;DR

Fundamentos de infraestrutura: DNS (TTL, tipos de record), Load Balancer (L4 vs L7, algoritmos), CDN (edge cache, origem), Cache (hit/miss, eviction, invalidação), Banco de Dados (ACID, replicação, sharding), Mensageria (pub/sub, at-least-once). Números para ter na cabeça: RAM ~100ns, SSD ~100µs, rede cross-DC ~10ms. Back-of-envelope essencial para System Design.

## Key Claims

**Claim:** Conhecer os números de latência de memória é essencial para system design — diferença de 10000× entre RAM e rede.
**Evidence:** L1 cache: ~1ns. RAM: ~100ns. SSD: ~100µs (100.000ns). HDD: ~10ms. Rede mesma DC: ~0.5ms. Rede cross-DC: ~10ms. Implicação: ler 1MB da RAM leva ~250µs; via rede cross-DC leva ~10ms (40× mais lento). Decisões de cache, sharding e replicação devem ser orientadas por esses números.
**Confidence:** alta

**Claim:** Load Balancer L7 é obrigatório para roteamento por conteúdo — L4 só vê IP e porta.
**Evidence:** L4 (TCP): distribui por IP/porta, sem inspecionar payload. Mais rápido. L7 (HTTP): vê URL, headers, cookies. Habilita: roteamento por path (`/api` → backend, `/` → frontend), sticky sessions por cookie, terminação TLS, rate limiting por URL. ALB da AWS é L7; NLB é L4.
**Confidence:** alta

**Claim:** Cache invalidation é o problema mais difícil — TTL curto é mais seguro que cache manual.
**Evidence:** "There are only two hard things in Computer Science: cache invalidation and naming things." Cache com TTL: expira automaticamente — stale por tempo limitado. Cache manual invalidado por evento: implementação complexa, propensa a bugs, difícil de testar. Para leitura de dados que mudam raramente (configurações, catálogo), TTL de 5-60min é suficiente e seguro.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/dns]]
- [[concepts/load-balancer]]
- [[concepts/cdn]]
- [[concepts/cache]]
- [[concepts/back-of-envelope]]
- [[concepts/latency-numbers]]

## Open Questions

- Back-of-envelope para 10M usuários ativos: quais são os números base para CPU, memória e banco?
- CDN com conteúdo dinâmico personalizado por usuário — como usar edge cache sem vazar dados entre usuários?
