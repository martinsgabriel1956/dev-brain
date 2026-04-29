---
type: concept
title: "SLA — Service Level Agreement"
aliases: ["service level agreement", "sla"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sre, contrato, confiabilidade]
skill: tech-mentor-infra
status: stable
---

# SLA — Service Level Agreement

Contrato externo com penalidades (créditos, multas). Derivado do [[concepts/slo]] com margem de segurança — sempre menos rigoroso que o SLO interno.

## Estrutura

```
SLO interno:  99.9% disponibilidade  ← operacional, critério para Error Budget
SLA externo:  99.5% disponibilidade  ← contratual, com créditos se violado

Margem de segurança: 0.4%
→ Se o SLO for violado, ainda há folga antes de violar o SLA e gerar multa
```

## Por que SLO ≠ SLA

SLO é ferramenta de decisão interna. SLA é compromisso legal com cliente. Gerir pelo SLA é tarde demais — o SLO funciona como alarme antecipado.

## Key Sources

- [[sources/sre-sli-slo-sla]]
