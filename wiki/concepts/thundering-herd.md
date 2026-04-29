---
type: concept
title: "Thundering Herd"
aliases: ["thundering herd", "retry storm", "cache stampede"]
date_created: 2026-04-22
date_updated: 2026-04-23
source_count: 2
tags: [resiliencia, distribuidos, retry, cache, performance]
skill: tech-mentor-system-design
status: stable
---

# Thundering Herd

Fenômeno onde múltiplos clientes disparam requests simultâneos para o mesmo recurso, amplificando a carga no exato momento em que o sistema está mais vulnerável — geralmente durante recuperação de uma falha.

## Causas Comuns

- **Retry ingênuo:** todos os clientes falham ao mesmo tempo e retentam no mesmo instante
- **Cache stampede:** cache expira → todos os clientes tentam popular o cache simultaneamente → banco sobrecarregado
- **Backoff sem jitter:** intervalo fixo sincroniza clientes mesmo com delay

## Solução por Causa

| Causa | Solução |
|---|---|
| Retry simultâneo | [[concepts/retry-backoff]] — backoff exponencial + jitter |
| Cache stampede | Cache lock (apenas um reconstrói), probabilistic early expiration |
| Reconexão de WebSocket | Jitter no reconnect delay |

## Por que é Perigoso

O sistema em recuperação recebe carga máxima no pior momento — exatamente quando precisa de folga para estabilizar. Thundering herd pode transformar uma falha transitória de 10s em downtime de minutos.

## Key Sources

- [[sources/retry-backoff]]
- [[sources/conceitos-que-ninguem-ensina]]
