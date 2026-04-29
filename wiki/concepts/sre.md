---
type: concept
title: "SRE — Site Reliability Engineering"
aliases: ["site reliability engineering", "sre"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sre, confiabilidade, operações, devops]
skill: tech-mentor-infra
status: stable
---

# SRE — Site Reliability Engineering

Disciplina que trata confiabilidade de sistemas como problema de engenharia. Framework central: definir o que significa "suficientemente confiável" ([[concepts/slo]]), medir se você está lá ([[concepts/sli]]), e usar a folga disponível ([[concepts/error-budget]]) para tomar decisões de velocidade vs. estabilidade.

## Por que importa

Sem esse framework, a discussão de confiabilidade fica na base de "o sistema tá caindo?" — reativa, sem critério de decisão, com tensão crônica entre Dev e Ops.

## Componentes

- [[concepts/sli]] — métrica concreta (o que medir)
- [[concepts/slo]] — meta interna (qual o target)
- [[concepts/sla]] — contrato externo (com penalidade)
- [[concepts/error-budget]] — folga operacional (governa velocidade vs. estabilidade)
- [[concepts/error-budget-policy]] — regras de decisão por nível de budget
- [[concepts/blameless-post-mortem]] — cultura de aprendizado sem blame

## Key Sources

- [[sources/sre-sli-slo-sla]]
