---
type: source
title: "Consistent Hashing"
aliases: ["consistent-hashing"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/consistent-hashing.md
source_url: ""
author: ""
date_published: "2026-04-14"
date_ingested: 2026-04-22
source_count: 0
tags: [distributed-systems, escala, sharding, cache, consistent-hashing]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Consistent Hashing resolve o problema de resharding em sistemas distribuídos: ao adicionar ou remover um nó, apenas K/N chaves precisam ser remapeadas (vs. quase todas no hash modulo simples). O ring hash com virtual nodes garante distribuição equilibrada entre nós físicos.

## Claims Principais

| Claim | Confiança |
|---|---|
| Hash modulo simples invalida quase todas as chaves ao mudar N | Alta |
| Consistent Hashing impacta apenas K/N chaves ao adicionar/remover nó | Alta |
| Virtual nodes resolvem a distribuição desigual sem eles | Alta |
| Redis Cluster usa 16384 hash slots distribuídos com consistent hashing | Alta |
| Cassandra usa consistent hashing para distribuir partições com fator de replicação | Alta |
| Sem virtual nodes, alguns nós podem receber muito mais carga que outros | Alta |
| Para range queries, range-based sharding é mais adequado | Alta |

## Conceitos Abordados

- [[consistent-hashing]]
- [[virtual-node]]
- [[hash-ring]]
- [[db-sharding]]
- [[redis-cluster]]
- [[resharding]]
