---
date: 2026-05-05
tags: [tech-mentor, infra, distributed-systems]
skill: tech-mentor-infra/references/clusters
level: fundamento
---

# Clusters

## Contexto
Cluster é um grupo de máquinas (nodes) que trabalham juntas e se apresentam como um sistema único para quem está de fora. Resolve três problemas centrais em sistemas distribuídos: capacidade, disponibilidade e latência geográfica.

## Como Funciona
Um **control plane** (ou coordinator) decide onde cada workload roda. Os clients falam com o cluster, não com uma máquina específica.

```
Client → Load Balancer → [Node A | Node B | Node C]
                              ↕           ↕
                         [shared state / replication]
```

## Tipos Comuns

**Compute clusters** (Kubernetes, ECS): distribuem containers/pods entre nodes. O scheduler decide onde cada pod roda baseado em CPU/memória disponível.

**Database clusters** (Postgres + Patroni, MySQL Group Replication): um node é o primary (escreve), os outros são replicas (lêem). Se o primary cai, uma replica assume.

**Cache clusters** (Redis Cluster): divide o keyspace em 16.384 slots distribuídos entre nodes. Cada node é responsável por um range de slots.

**Search clusters** (Elasticsearch): divide índices em shards distribuídos. Queries rodam em paralelo em múltiplos nodes.

## Código de Referência

```yaml
# Kubernetes — listar nodes do cluster
# kubectl get nodes

# Redis Cluster — habilitar no redis.conf
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Capacidade | Scale horizontal adicionando nodes | Complexidade operacional cresce |
| Disponibilidade | Failover automático | Estado distribuído difícil de manter consistente |
| Latência | Nodes geograficamente distribuídos | Network partition → dilema CAP |
| Custo | Usa hardware commodity | Mais máquinas = mais custo e surface de falha |

## Quando Usar / Quando Evitar

**Usar quando:**
- Um único server não aguenta a carga (CPU, memória, I/O)
- SLA exige alta disponibilidade (uptime > 99.9%)
- Dado precisa estar próximo de múltiplas regiões

**Evitar quando:**
- Workload é pequeno e previsível — over-engineering caro
- Time não tem maturidade operacional para gerenciar estado distribuído
- Consistência forte é crítica e o sistema não tolera eventual consistency

## Conceitos Relacionados
[[cap-theorem]] · [[kubernetes]] · [[redis-cluster]] · [[replicacao]] · [[load-balancer]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-05-05*
