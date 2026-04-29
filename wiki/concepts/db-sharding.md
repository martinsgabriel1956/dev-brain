---
type: concept
title: "DB Sharding"
aliases: ["sharding", "database sharding", "horizontal partitioning"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [sharding, escalabilidade, banco-de-dados, consistent-hashing, shard-key]
skill: tech-mentor-system-design
status: stub
---

# DB Sharding

Particionamento horizontal de um banco de dados em múltiplos nós independentes (shards) para ultrapassar os limites de uma única máquina.

**Três algoritmos:**
- **Range-based**: intervalo de valores por shard — range queries eficientes, mas hot spots em dados recentes.
- **Hash-based**: hash da shard key % N — distribuição uniforme, sem range queries, resharding move quase todos os dados.
- **Consistent hashing**: ring circular — resharding move apenas ~1/N dos dados. Usado por Redis Cluster (16.384 slots), Cassandra, DynamoDB.

**A decisão mais importante:** escolha da shard key — errar gera cross-shard queries (caras) ou hot spots.

**Considerar quando:** > ~10TB ou > ~100k QPS. Antes disso, read replicas + connection pooling resolvem.

## Key Sources

- [[sources/db-sharding]]
