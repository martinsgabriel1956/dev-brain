---
type: concept
title: "Blast Radius"
aliases: ["raio de explosão", "failure blast radius"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [resiliencia, blast-radius, system-design, isolamento]
skill: tech-mentor-system-design
status: stub
---

# Blast Radius

Extensão do impacto quando um componente falha. Quanto menor o blast radius, mais contida a falha.

## Sem Isolamento

```
Pool compartilhado de 100 threads:
Serviço B (lento): usa 10 → 20 → 50 → 80 → 100 threads
Serviço C (normal): quer 10 threads → não tem → falha
Serviço D (crítico): quer 5 threads → não tem → falha
→ blast radius: 1 serviço lento derrubou 3
```

## Como Reduzir

- [[concepts/bulkhead]] — pools separados por downstream
- [[concepts/circuit-breaker]] — corta falhas antes de cascatear
- Filas assíncronas — desacopla produtor de consumidor

## Key Sources

- [[sources/bulkhead]]
