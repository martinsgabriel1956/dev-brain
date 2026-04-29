---
type: concept
title: "Error Budget"
aliases: ["error budget", "budget de erros"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sre, confiabilidade, operações, prometheus]
skill: tech-mentor-infra
status: stable
---

# Error Budget

Quantidade de falha permitida antes de violar o [[concepts/slo]]. Governa a decisão de velocidade vs. estabilidade de forma objetiva e sem negociação subjetiva.

## Cálculo

```
SLO: 99.9% de disponibilidade em 30 dias
30 dias = 43.200 minutos
Error Budget = 0.1% × 43.200 = 43.2 minutos de indisponibilidade permitida

Incidente: 15 minutos de downtime
→ Error Budget restante: 28.2 minutos (34.7% consumido)
```

## Alerting por Burn Rate (Prometheus)

Burn rate é mais eficaz que threshold absoluto — detecta esgotamento antecipado.

```yaml
- alert: ErrorBudgetFastBurn
  expr: |
    (
      1 - sum(rate(http_requests_total{status=~"2.."}[1h]))
          / sum(rate(http_requests_total{status!~"4.."}[1h]))
    ) > (14 * 0.001)
  for: 2m
  labels:
    severity: critical

- alert: ErrorBudgetSlowBurn
  expr: |
    (
      1 - sum(rate(http_requests_total{status=~"2.."}[6h]))
          / sum(rate(http_requests_total{status!~"4.."}[6h]))
    ) > (6 * 0.001)
  for: 15m
  labels:
    severity: warning
```

FastBurn: > 14× a taxa normal em 1h → critical. SlowBurn: > 6× em 6h → warning.

Ver política de decisão em [[concepts/error-budget-policy]].

## Key Sources

- [[sources/sre-sli-slo-sla]]
- [[sources/sre-error-budget-incidents]]
