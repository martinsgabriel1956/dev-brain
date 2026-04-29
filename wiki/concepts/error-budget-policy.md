---
type: concept
title: "Error Budget Policy"
aliases: ["error budget policy", "política de error budget"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sre, confiabilidade, operações, processo]
skill: tech-mentor-infra
status: stable
---

# Error Budget Policy

Conjunto de regras que mapeia o nível atual do [[concepts/error-budget]] para decisões de release e operação. Elimina negociação subjetiva entre Dev e Ops.

## Política

| Budget Restante | Ação |
|---|---|
| > 50% | Releases normais, experimentos e mudanças de risco moderado permitidas |
| 10% – 50% | Apenas features críticas; foco em reliability work; alertas automáticos para o time |
| < 10% | Freeze de features novas; apenas hotfixes e reliability fixes; post-mortem obrigatório de todos os incidentes recentes |
| 0% (esgotado) | Stop shipping; time foca 100% em estabilidade até budget se recuperar no próximo período |

## Por que funciona

Remove a tensão crônica Dev vs. Ops: a política é acordada com antecedência. Quando o budget zera, não é decisão de ninguém — é a política.

## Key Sources

- [[sources/sre-sli-slo-sla]]
- [[sources/sre-error-budget-incidents]]
