---
type: source
title: "Números de Latência"
aliases: ["latency numbers every programmer should know"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/numeros-de-latencia.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-22
source_count: 0
tags: [latencia, performance, back-of-envelope, system-design]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

RAM é 1000× mais rápida que SSD; SSD é 100× mais rápido que HDD. Redis ~0.1ms, PostgreSQL com índice 1-10ms, cross-region 130-250ms. Cada hop de rede no mesmo DC custa ~0.5ms — 10 microserviços no mesmo AZ somam ~5ms só em overhead de rede. Esses números guiam decisões de cache, mensageria e posicionamento geográfico de serviços.

## Claims Principais

| Claim | Confiança |
|---|---|
| RAM ~100ns, SSD random ~150μs, HDD seek ~10ms — diferença de 3 ordens de grandeza | Alta |
| Redis ~0.1ms, PostgreSQL com índice 1-10ms, cross-region 130-250ms | Alta |
| Cada hop de rede no mesmo DC custa ~0.5ms | Alta |
| 1ms = limite para UX "instantâneo"; 100ms = usuário percebe lentidão; 1s = abandono | Alta |
| Redis suporta ~100.000 ops/s; Kafka ~1.000.000 msgs/s por broker | Alta |
| Soma de latências síncronas > SLA é o sinal para mover operações para fora do critical path via mensageria | Alta |

## Conceitos Abordados

- [[latencia]]
- [[hierarquia-de-memoria]]
- [[back-of-envelope]]
- [[cache]]
- [[mensageria]]
- [[critical-path]]
