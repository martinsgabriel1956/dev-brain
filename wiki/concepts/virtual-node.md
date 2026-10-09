---
type: concept
title: "Virtual Node"
aliases: ["vnode", "vnodes"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [sharding, consistent-hashing]
skill: tech-mentor-system-design
status: draft
---

# Virtual Node

No [[wiki/concepts/consistent-hashing]], cada shard físico ocupa vários pontos do anel. Ao adicionar um nó, ele recebe um pouco de dados de cada nó existente em vez de metade de um só, evitando shards cheios ao lado de shards pela metade. Fonte apenas cita o conceito; detalhes ficam para estudo futuro.

## Key Sources

- [[wiki/sources/sharding-milhoes-de-escritas-partition-key-consistent-hashing-pedro-camaforte]]
