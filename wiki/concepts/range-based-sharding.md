---
type: concept
title: "Range-Based Sharding"
aliases: ["sharding por faixa"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [sharding, system-design]
skill: tech-mentor-system-design
status: draft
---

# Range-Based Sharding

Distribui por faixas da chave (A–I/J–R/S–Z, ou `user_id` 0–1M/1M–2M). Limites: alfabeto finito e nomes desiguais; faixas iniciais ficam concentradas num shard (e vazias nas demais); usuários recentes são mais ativos → hot shard no último intervalo. Não é o padrão de mercado; ver [[wiki/concepts/hash-based-sharding]] e [[wiki/concepts/hot-shard]].

## Key Sources

- [[wiki/sources/sharding-milhoes-de-escritas-partition-key-consistent-hashing-pedro-camaforte]]
