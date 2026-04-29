---
type: source
title: "Multi-region & Global Load Balancing"
aliases: []
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/multi-region-global-lb.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-22
source_count: 0
tags: [multi-region, load-balancer, disponibilidade, sla, system-design]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Multi-region é a resposta para SLAs de 99,99%+ e latência global baixa, mas custa 2-3× mais que single-region. O padrão mais equilibrado é read-local/write-global. Active-Active exige gestão de conflitos de escrita. Route 53 failover depende de TTL (~60s); Global Accelerator usa Anycast e falha em ~30s. Antes de multi-region, garantir resiliência multi-AZ cobre 90% dos casos com 10% da complexidade.

## Claims Principais

| Claim | Confiança |
|---|---|
| SLA 99,99% = máximo 52 min de downtime/ano; single-region não garante isso | Alta |
| Multi-region custa 2-3× mais que single-region | Alta |
| Route 53 failover mínimo ~60s por dependência de TTL; Global Accelerator ~30s via Anycast | Alta |
| Read-local/write-global é o padrão mais equilibrado entre consistência e latência | Alta |
| Consistência forte cross-region exige consensus (Raft/Paxos) e adiciona latência intercontinental em cada write | Alta |
| Multi-AZ primeiro: 90% do benefício de resiliência com 10% da complexidade de multi-region | Alta |
| DNS TTL deve ser reduzido antes de um incidente, não durante — cache já está distribuído | Alta |

## Conceitos Abordados

- [[multi-region]]
- [[active-active-vs-active-passive]]
- [[global-load-balancer]]
- [[anycast]]
- [[read-local-write-global]]
- [[consistencia-de-dados]]
- [[failover]]
