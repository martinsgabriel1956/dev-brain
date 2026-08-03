---
type: concept
title: "Control Plane"
aliases: ["coordinator", "control plane", "cluster coordinator"]
date_created: 2026-05-05
date_updated: 2026-08-03
source_count: 2
tags: [control-plane, kubernetes, cluster, distributed-systems, infra]
skill: tech-mentor-infra
status: stub
---

# Control Plane

Componente central de um [[concepts/cluster]] responsável por decidir onde cada workload roda. Clients falam com o control plane, não com nodes individuais.

**No Kubernetes:** API Server + Scheduler + Controller Manager + etcd. O Scheduler avalia CPU/memória disponível por node e coloca pods onde há capacidade.

**Em databases:** o coordinator (ex: Patroni no Postgres) monitora o primary via heartbeat e promove uma réplica automaticamente em caso de falha.

**Em Redis Cluster:** não há coordinator centralizado — nodes usam gossip protocol para detectar falhas e eleger novo primary para um range de slots.

## Control Plane em Sharding de Aplicação

[[wiki/sources/large-scale-vs-complex-architecture]] descreve o mesmo conceito num nível diferente do cluster de infraestrutura: em [[wiki/concepts/large-scale-architecture]], o control plane é a camada de controladores que move um usuário de um [[wiki/concepts/sharding|shard]] para outro — distinta do software que atende o negócio/usuário final. A fonte observa que arquiteturas complexas (ver [[wiki/concepts/arquitetura-complexa]]) nem sempre têm essa camada de controle explícita, porque a complexidade ali vem de interdependência histórica, não de uma necessidade de coordenação por escala.

## Key Sources

- [[sources/clusters]]
- [[wiki/sources/large-scale-vs-complex-architecture]] — control plane como camada de coordenação de sharding em large scale architecture
