---
type: source
title: "Clusters — Fundamentos"
aliases: ["cluster", "compute cluster", "database cluster", "cache cluster"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 0
tags: [cluster, distributed-systems, kubernetes, redis-cluster, elasticsearch, infra, escalabilidade, alta-disponibilidade]
skill: tech-mentor-infra
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/clusters.md
source_url:
author:
date_published: 2026-05-05
date_ingested: 2026-05-05
---

# Clusters — Fundamentos

## TL;DR

Cluster é um grupo de máquinas (nodes) que se apresentam como um sistema único. Resolve três problemas centrais: capacidade (scale horizontal), disponibilidade (failover automático) e latência geográfica (nodes distribuídos). Um control plane decide onde cada workload roda; clients falam com o cluster, não com uma máquina específica. Cada tipo de cluster tem uma estratégia própria de distribuição de estado: pods (Kubernetes), primary/replica (databases), hash slots (Redis), shards (Elasticsearch).

## Key Claims

| Claim | Evidência |
|---|---|
| Compute clusters (K8s) usam scheduler baseado em CPU/memória disponível | Scheduler decide placement de pods; node com menos recurso recebe menos pods |
| Database clusters (Patroni) têm um primary para escrita e réplicas para leitura | Se primary cai, uma réplica assume — failover automático |
| Redis Cluster divide keyspace em 16.384 hash slots distribuídos entre nodes | Cada node é responsável por um range de slots — mesma lógica do consistent hashing |
| Elasticsearch distribui índices em shards paralelos | Queries rodam em paralelo, aumentando throughput de busca |
| Network partition força dilema CAP | Nodes geograficamente distribuídos ganham latência mas perdem consistência forte |
| Cluster é over-engineering quando workload é pequeno e previsível | Antes de cluster: right-sizing, read replicas, connection pooling |

## Conceitos

- [[concepts/cluster]] — fundamento: o que é, tipos, trade-offs
- [[concepts/control-plane]] — coordenador central que decide placement de workloads
- [[concepts/redis-cluster]] — hash slots, gossip protocol, failover
- [[concepts/db-sharding]] — consistent hashing, shard key, resharding
- [[concepts/load-balancer]] — entry point do cluster para clients externos
- [[concepts/cap-theorem]] — dilema inevitável em sistemas distribuídos com network partition

## Open Questions

- Como funciona o processo de resharding em Redis Cluster sem downtime?
- Qual o custo operacional real de um cluster Postgres com Patroni vs RDS Multi-AZ?

## Key Sources

_Este é o documento primário._
