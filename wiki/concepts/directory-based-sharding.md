---
type: concept
title: "Directory-Based Sharding"
aliases: ["sharding por diretório", "shard map"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [sharding, system-design]
skill: tech-mentor-system-design
status: draft
---

# Directory-Based Sharding

Tabela auxiliar (shard map) diz em que shard está cada chave. Prós: flexibilidade para realocar entidades pesadas. Contras: ponto único de falha e duas chamadas por operação (throughput dobrado). Caso de uso saudável: isolar celebridades em shard dedicado ([[wiki/concepts/hot-shard]]). Alternativa padrão: [[wiki/concepts/hash-based-sharding]]. Ver [[wiki/concepts/single-point-of-failure]].

## Key Sources

- [[wiki/sources/sharding-milhoes-de-escritas-partition-key-consistent-hashing-pedro-camaforte]]
