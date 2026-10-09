---
type: concept
title: "Partition Key"
aliases: ["chave de partição", "shard key"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [sharding, system-design, partition-key]
skill: tech-mentor-system-design
status: draft
---

# Partition Key

Coluna que comanda a distribuição dos dados entre os shards; primeira coisa a declarar numa entrevista de [[wiki/concepts/sharding]]. Três propriedades: **alta cardinalidade** (`is_premium` limita a 2 shards; um ID não), **distribuição equilibrada** (país: Vaticano vs Brasil) e **alinhamento com as queries** (dados consultados juntos moram no mesmo shard — `user_id` no Instagram, `order_id` no e-commerce). Más escolhas: plano free/pago (baixa cardinalidade e desigual), data do evento (o shard do ano corrente esquenta). Pode ser composta para aliviar [[wiki/concepts/hot-shard]]. Mesma ideia de shard key em [[wiki/concepts/db-sharding]]; chave errada gera [[wiki/concepts/cross-shard-query]] frequentes.

## Key Sources

- [[wiki/sources/sharding-milhoes-de-escritas-partition-key-consistent-hashing-pedro-camaforte]]
