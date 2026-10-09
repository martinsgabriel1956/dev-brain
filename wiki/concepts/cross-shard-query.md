---
type: concept
title: "Cross-Shard Query"
aliases: ["query entre shards", "scatter-gather"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [sharding, system-design]
skill: tech-mentor-system-design
status: draft
---

# Cross-Shard Query

Consulta que precisa de vários shards (ex.: top 10 posts globais: top 10 por shard, agrega, reordena). Deve ser exceção; se for frequente, a [[wiki/concepts/partition-key]] está errada ou sharding não serve. Mitigações: [[wiki/concepts/cache-layer]] com TTL (ex.: 5 min — troca frescor por latência) e [[wiki/concepts/desnormalizacao]]. Para escritas atômicas entre shards: [[wiki/concepts/saga-pattern]] / [[wiki/concepts/two-phase-commit]].

## Key Sources

- [[wiki/sources/sharding-milhoes-de-escritas-partition-key-consistent-hashing-pedro-camaforte]]
