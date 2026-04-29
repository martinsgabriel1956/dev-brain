---
type: concept
title: "Incident Lifecycle"
aliases: ["ciclo de vida de incidente", "incident response", "resposta a incidente"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sre, incidentes, operações, on-call]
skill: tech-mentor-infra
status: stable
---

# Incident Lifecycle

Fluxo estruturado de resposta a incidente — da detecção à resolução e aprendizado. Previsibilidade no processo reduz tempo de resolução sob stress.

## Fluxo

```
1. Alerta → on-call recebe page
2. Acknowledge em < 5min
3. Avalia severidade → declara incidente se SEV-2+
4. Abre canal dedicado (#incident-YYYY-MM-DD-HH)
5. Assume IC (ou escalona para quem assume)
6. Investigação → mitigação (mitigação ≠ causa raiz — ok parar aqui)
7. Resolve → comunica resolução para stakeholders
8. Abre post-mortem em 24-48h
```

## Princípio Central

**Mitigação antes de causa raiz.** Rollback em 10 minutos é melhor que investigar 2 horas para encontrar a causa enquanto usuários são impactados. A causa raiz vai para o [[concepts/blameless-post-mortem]].

## Papéis

Ver [[concepts/incident-roles]] — IC, TL, Comunicador, Escriba são papéis distintos que não devem se misturar.

## Severidade

Ver [[concepts/incident-severity]] — define tempo de resposta e escalonamento.

## Key Sources

- [[sources/sre-error-budget-incidents]]
