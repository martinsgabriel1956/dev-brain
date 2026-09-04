---
type: source
title: "Vector Clocks"
aliases: ["vector-clocks", "relogios-vetoriais"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/vector-clocks.md
source_url: ""
author: ""
date_published: "2026-04-17"
date_ingested: 2026-04-22
source_count: 0
tags: [sistemas-distribuidos, consistencia, causalidade, vector-clock]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Vector Clocks resolvem o rastreamento de causalidade em sistemas distribuídos sem relógio global. Cada nó mantém um vetor de contadores e ao receber mensagem faz merge tomando o máximo por posição. Permite detectar se dois eventos são causalmente relacionados (happened-before) ou concorrentes (conflito).

## Claims Principais

| Claim | Confiança |
|---|---|
| Wall clock timestamps não são suficientes para determinar causalidade em sistemas distribuídos | Alta |
| V1 happened-before V2 se V1[i] <= V2[i] para todo i e V1[j] < V2[j] para algum j | Alta |
| Eventos concorrentes (conflito) ocorrem quando nem V1 < V2 nem V2 < V1 | Alta |
| Merge de vector clocks toma o máximo de cada posição | Alta |
| DynamoDB e Riak usam vector clocks internamente | Alta |
| O vetor cresce O(N nós) — overhead significativo em clusters grandes | Alta |
| Last-Write-Wins (LWW) é a resolução mais simples mas descarta dados | Alta |
| CRDTs resolvem conflitos de vector clock matematicamente | Média |

## Conceitos Abordados

- [[vector-clock]]
- [[causal-consistency]]
- [[happened-before]]
- [[conflict-resolution]]
- [[crdt]]
- [[eventual-consistency]]
- [[wiki/concepts/last-write-wins]]
