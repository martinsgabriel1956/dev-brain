---
type: concept
title: "SLO — Service Level Objective"
aliases: ["service level objective", "slo"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sre, confiabilidade, operações]
skill: tech-mentor-infra
status: stable
---

# SLO — Service Level Objective

Meta interna de confiabilidade — threshold do [[concepts/sli]] que o time se compromete a manter. É a fonte da verdade para decisões operacionais (não o [[concepts/sla]]).

## Exemplos

```
Disponibilidade: "99.9% dos requests bem-sucedidos em janela de 30 dias"
Latência:        "99% dos requests atendidos em < 300ms em janela de 30 dias"
Freshness:       "95% dos dados da dashboard atualizados em < 5 minutos"
```

## Escolhendo o SLO Correto

- Muito alto (99.99%) → pressão constante, zero margem para manutenção
- Muito baixo (95%) → usuários insatisfeitos
- **Regra:** comece com o que você já entrega hoje, meça 30 dias, depois decida o target

SLO interno é sempre mais rigoroso que o [[concepts/sla]] externo — a diferença é a margem de segurança antes de gerar penalidade contratual.

## Relação com Error Budget

`Error Budget = 1 - SLO`. SLO de 99.9% em 30 dias = 43.2 minutos de indisponibilidade permitida. Ver [[concepts/error-budget]].

## Key Sources

- [[sources/sre-sli-slo-sla]]
