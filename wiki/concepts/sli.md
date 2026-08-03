---
type: concept
title: "SLI — Service Level Indicator"
aliases: ["service level indicator", "sli"]
date_created: 2026-04-22
date_updated: 2026-08-03
source_count: 2
tags: [sre, observabilidade, metricas, prometheus]
skill: tech-mentor-infra
status: stable
---

# SLI — Service Level Indicator

Métrica concreta que mede um aspecto da qualidade do serviço. Sempre um número entre 0 e 1 (ou porcentagem). É a entrada do [[concepts/slo]].

## Tipos Comuns

| Tipo | Fórmula |
|---|---|
| Disponibilidade | `requests_success / requests_total` |
| Latência | `requests_under_300ms / requests_total` |
| Freshness | `records_updated_in_last_hour / total_records` |
| Durabilidade | `bytes_successfully_retrieved / bytes_written` |

## Prometheus

```yaml
- record: sli:availability:rate5m
  expr: |
    sum(rate(http_requests_total{status=~"2.."}[5m]))
    /
    sum(rate(http_requests_total{status!~"4.."}[5m]))
```

Erros 4xx excluídos do denominador — são erro do cliente, não do serviço.

## A Cadeia SLI → SLO → SLA

Forma simples de lembrar a cadeia: o SLI é a métrica (ex.: proporção de respostas HTTP 200), o [[concepts/slo]] é a porcentagem/meta sobre essa métrica, e o [[concepts/sla]] é a camada contratual sobre a mesma promessa quando ela cruza a fronteira entre empresas.

## Key Sources

- [[sources/sre-sli-slo-sla]]
- [[sources/slo-sli-sla-exemplo-ecommerce]]
