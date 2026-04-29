---
type: source
title: "DB Sharding"
aliases: ["sharding", "database sharding", "consistent hashing db"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [sharding, consistent-hashing, shard-key, escalabilidade, banco-de-dados, system-design]
skill: tech-mentor-system-design
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/db-sharding.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# DB Sharding

## TL;DR

Sharding divide horizontalmente os dados de um banco em múltiplos nós para ultrapassar os limites de escala de uma única máquina. Três algoritmos: range-based (hot spots), hash-based (sem range queries), consistent hashing (resharding eficiente). A escolha do shard key é a decisão mais importante — errar significa cross-shard queries ou hot spots. Considerar sharding apenas acima de ~10TB ou ~100k QPS.

## Key Claims

| Claim | Evidência |
|---|---|
| Consistent hashing move apenas ~1/N dos dados ao resharding | Ring circular: adicionar nó E manda só a fatia entre ele e o vizinho |
| Range-based causa hot spots em dados recentes | Dados novos sempre no último shard |
| Cross-shard JOINs são caros ou impossíveis | Exigem Saga/2PC ou redesign do schema |
| Redis Cluster usa 16.384 slots de consistent hashing | Documentação Redis Cluster |
| Resharding usa dual-write + backfill | Escreve nos dois schemas durante a migração |

## Conceitos

- [[concepts/db-sharding]] — particionamento horizontal
- [[concepts/consistent-hashing]] — ring circular, resharding eficiente
- [[concepts/shard-key]] — a decisão mais importante
- [[concepts/cross-shard-operations]] — JOINs e transações entre shards
- [[concepts/saga-pattern]] — alternativa ao 2PC em operações cross-shard

## Open Questions

- Qual é o limiar prático para migrar de particionamento lógico (PostgreSQL schemas) para sharding físico?

## Key Sources

_Este é o documento primário._
