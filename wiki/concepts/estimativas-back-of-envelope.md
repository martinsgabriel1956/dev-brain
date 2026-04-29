---
type: concept
title: "Estimativas Back-of-Envelope"
aliases: ["back of envelope", "estimativas de escala", "capacity estimation"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, estimativas, entrevista, escala, capacity-planning]
skill: tech-mentor-system-design
status: stub
---

# Estimativas Back-of-Envelope

Cálculos rápidos de escala para validar decisões arquiteturais e identificar gargalos antes de desenhar o sistema.

## Template

```
Usuários ativos × frequência de ação = requests/s
Requests/s × tamanho médio = bandwidth
Requests/s × latência = concorrência (Little's Law → [[concepts/littles-law]])
Storage = volume × retenção × fator de replicação
```

## Exemplo Uber

```
5M motoristas × 1 update/4s    = 1.25M writes/s  → Redis, não PostgreSQL
1M corridas/hora (pico)        = 278 matches/s
278 matches × 10 ETA calls     = 2.780 routing/s  → 1-2 nós OSRM
Kafka: 1.25M msg × 50 bytes    = 60MB/s           → 10 partitions ok
Redis GEO: 5M × 70 bytes       = 350MB            → cabe em 1 instância
```

## Por que Fazer em Entrevista

Mostra que a escolha de tecnologia é baseada em números, não em preferência. "Redis porque é mais rápido" é fraco. "Redis porque PostgreSQL não suporta 1.25M writes/s" é arquitetura.

## Key Sources

- [[sources/case-uber]]
