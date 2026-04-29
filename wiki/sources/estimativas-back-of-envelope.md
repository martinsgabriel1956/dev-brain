---
type: source
title: "Estimativas Back-of-Envelope"
aliases: ["back-of-envelope estimation", "capacity estimation"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/estimativas-back-of-envelope.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-22
source_count: 0
tags: [estimativas, capacidade, entrevista, system-design, qps, storage]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Framework de 4 passos: (1) clarificar escopo — DAU, read/write ratio, pico vs média; (2) estimar QPS; (3) estimar storage; (4) estimar bandwidth. O objetivo é ordem de grandeza para evitar over/under-engineering. Tabela de referência: startup <1k QPS = monolito+PG; >100k QPS = microsserviços+cell-based.

## Claims Principais

| Claim | Confiança |
|---|---|
| O objetivo de estimativas back-of-envelope é ordem de grandeza, não precisão | Alta |
| QPS médio = requisições/dia ÷ 86.400; pico = média × 5-10× | Alta |
| 1 tweet ≈ 1KB com índices e overhead — base para cálculo de storage | Alta |
| Cache com 80% hit rate reduz carga no banco em 5× | Alta |
| >100k QPS requer arquitetura microsserviços + cell-based | Média |
| Short URL de 7 chars base62 = 62^7 = 3.5 trilhões de URLs únicas | Alta |
| Replicação 3× multiplica storage necessário por 3 | Alta |

## Conceitos Abordados

- [[back-of-envelope]]
- [[qps]]
- [[capacity-planning]]
- [[db-sharding]]
- [[cache]]
- [[consistent-hashing]]
- [[rate-limiting]]
