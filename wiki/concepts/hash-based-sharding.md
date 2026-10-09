---
type: concept
title: "Hash-Based Sharding"
aliases: ["sharding por hash"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [sharding, system-design, hashing]
skill: tech-mentor-system-design
status: draft
---

# Hash-Based Sharding

`shard = hash(partition_key) % N`. Hash determinístico e pseudo-aleatório → distribuição uniforme, sem hot shards por padrão de acesso. Fraqueza: mudar N remapeia quase todas as chaves; mitigação padrão é [[wiki/concepts/consistent-hashing]] com [[wiki/concepts/virtual-node]]. Sem range queries eficientes. Ver [[wiki/concepts/hashing]], [[wiki/concepts/partition-key]].

## Key Sources

- [[wiki/sources/sharding-milhoes-de-escritas-partition-key-consistent-hashing-pedro-camaforte]]
