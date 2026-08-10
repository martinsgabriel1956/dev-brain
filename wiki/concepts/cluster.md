---
type: concept
title: "Cluster"
aliases: ["clusters", "compute cluster", "database cluster", "distributed cluster"]
date_created: 2026-05-05
date_updated: 2026-08-06
source_count: 3
tags: [cluster, distributed-systems, escalabilidade, alta-disponibilidade, infra]
skill: tech-mentor-infra
status: stable
---

# Cluster

Grupo de máquinas (nodes) que trabalham juntas e se apresentam como um sistema único para clients externos. Resolve três problemas centrais em sistemas distribuídos:

1. **Capacidade** — scale horizontal adicionando nodes
2. **Disponibilidade** — failover automático quando um node cai
3. **Latência geográfica** — nodes próximos de diferentes regiões

**Arquitetura base:**
```
Client → Load Balancer → [Node A | Node B | Node C]
                              ↕           ↕
                         [shared state / replication]
```

Um **control plane** (ou coordinator) decide onde cada workload roda. Clients falam com o cluster, não com uma máquina específica.

## Tipos Principais

| Tipo | Exemplos | Estratégia de distribuição |
|---|---|---|
| Compute | Kubernetes, ECS | Scheduler por CPU/memória disponível |
| Database | Postgres + Patroni, MySQL Group Replication | Primary escreve, réplicas lêem; failover automático |
| Cache | Redis Cluster | 16.384 hash slots divididos entre nodes |
| Search | Elasticsearch | Shards de índice paralelos |

## Quando Usar

**Usar quando:** carga não cabe em um único server, SLA > 99.9%, ou dado precisa estar em múltiplas regiões.

**Evitar quando:** workload pequeno e previsível (over-engineering), team sem maturidade operacional para estado distribuído, ou consistência forte é crítica e o sistema não tolera eventual consistency.

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Capacidade | Scale horizontal com commodity hardware | Complexidade operacional cresce |
| Disponibilidade | Failover automático | Estado distribuído difícil de manter consistente |
| Latência | Nodes geograficamente próximos | Network partition → dilema CAP |
| Custo | Usa hardware commodity | Mais máquinas = mais surface de falha |

## Cluster Ativo-Passivo vs. Ativo-Ativo

Um mesmo cluster (MySQL Cluster, Suse Cluster, Redhat Cluster) pode ser configurado em duas topologias com garantias bem diferentes: **ativo-passivo**, onde um nó primário serve tráfego e o(s) secundário(s) ficam em standby até um failover ser necessário — a base de [[wiki/concepts/alta-disponibilidade|HA]] —, ou **ativo-ativo**, onde todos os nós já servem tráfego em paralelo com dados replicados continuamente — a base de [[wiki/concepts/tolerancia-a-falha]]. Ver [[wiki/sources/ha-vs-ft-alta-disponibilidade-tolerancia-a-falha]] para a distinção completa e o trade-off de custo entre as duas.

## Key Sources

- [[sources/clusters]]
- [[wiki/sources/ha-vs-ft-alta-disponibilidade-tolerancia-a-falha]] — cluster ativo-passivo (HA) vs. ativo-ativo (Tolerância a Falha)
- [[wiki/sources/reacao-artigo-visual-algoritmos-load-balancing]] — arquitetura mínima de cluster (load balancer + N nodes intercambiáveis) usada como base para simular visualmente cada algoritmo de distribuição de carga
