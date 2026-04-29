---
type: concept
title: "Little's Law"
aliases: ["lei de little", "littles law", "dimensionamento de concorrência"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, performance, concorrencia, dimensionamento, littles-law]
skill: tech-mentor-system-design
status: stub
---

# Little's Law

Fórmula para dimensionar concorrência ideal de um sistema.

```
L = λ × W

L = número médio de requisições em andamento (concorrência)
λ = throughput (req/s)
W = latência média (segundos)
```

## Exemplo Prático

```
Payment service: 50 req/s, latência média 200ms
L = 50 × 0.2 = 10 threads
Com margem de segurança 2×: pool de 20
```

## Aplicação

Use para dimensionar [[concepts/bulkhead]] pools. Pool menor que L = fila crescente sob carga normal. Pool muito maior = recursos desperdiçados.

## Margem de Segurança

Aplique 2× como piso. Picos de tráfego, GC pauses e latência p99 > média justificam margem maior.

## Key Sources

- [[sources/bulkhead]]
