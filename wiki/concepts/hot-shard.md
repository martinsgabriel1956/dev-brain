---
type: concept
title: "Hot Shard"
aliases: ["hotspot de shard", "problema da celebridade"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [sharding, hotspot, system-design]
skill: tech-mentor-system-design
status: draft
---

# Hot Shard

Shard que concentra tráfego desproporcional, mesmo com boa [[wiki/concepts/partition-key]] e hash. Causas: celebridade, post viral, range-based com usuários recentes, data como chave. Soluções: (1) **shard dedicado** para a entidade (roteado por [[wiki/concepts/directory-based-sharding]], hardware mais forte); (2) **partition key composta** (`id + N` ou `id + semana`) que subdivide o shard, ao custo de ler vários shards — mitigado com [[wiki/concepts/cache-layer]]. Ver [[wiki/concepts/sharding]], [[wiki/concepts/hotspot-analysis]].

## Key Sources

- [[wiki/sources/sharding-milhoes-de-escritas-partition-key-consistent-hashing-pedro-camaforte]]
