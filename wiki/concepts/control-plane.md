---
type: concept
title: "Control Plane"
aliases: ["coordinator", "control plane", "cluster coordinator"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [control-plane, kubernetes, cluster, distributed-systems, infra]
skill: tech-mentor-infra
status: stub
---

# Control Plane

Componente central de um [[concepts/cluster]] responsável por decidir onde cada workload roda. Clients falam com o control plane, não com nodes individuais.

**No Kubernetes:** API Server + Scheduler + Controller Manager + etcd. O Scheduler avalia CPU/memória disponível por node e coloca pods onde há capacidade.

**Em databases:** o coordinator (ex: Patroni no Postgres) monitora o primary via heartbeat e promove uma réplica automaticamente em caso de falha.

**Em Redis Cluster:** não há coordinator centralizado — nodes usam gossip protocol para detectar falhas e eleger novo primary para um range de slots.

## Key Sources

- [[sources/clusters]]
