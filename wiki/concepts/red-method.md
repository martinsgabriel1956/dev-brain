---
type: concept
title: "RED Method"
aliases: ["red method", "rate errors duration", "golden signals"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [observabilidade, metricas, prometheus, sre]
skill: tech-mentor-system-design
status: stable
---

# RED Method

**R**ate · **E**rrors · **D**uration — três métricas que cobrem os alertas essenciais de qualquer serviço HTTP. Complemento do USE Method (Utilization, Saturation, Errors) que foca em recursos de infra.

| Métrica | O que mede | Tipo Prometheus |
|---|---|---|
| Rate | Requests por segundo | Counter |
| Errors | Taxa de erros (5xx) | Counter |
| Duration | Latência (p50, p99) | Histogram |

## Por que Histogram para Latência

Histogram permite calcular percentis via PromQL (`histogram_quantile`) — média é enganosa em distribuições com cauda longa. p99 revela o pior caso que 1% dos usuários experimenta.

## Relação com [[concepts/sli]]

Rate e Errors alimentam diretamente o SLI de disponibilidade. Duration alimenta o SLI de latência. RED Method é a instrumentação mínima para ter SLOs rastreáveis.

## Key Sources

- [[sources/observabilidade]]
