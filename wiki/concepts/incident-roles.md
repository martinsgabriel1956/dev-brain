---
type: concept
title: "Incident Roles"
aliases: ["papéis de incidente", "incident commander", "IC", "technical lead incidente"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sre, incidentes, operações, coordenação]
skill: tech-mentor-infra
status: stable
---

# Incident Roles

Papéis distintos durante um incidente. Separação é crítica: quando uma pessoa tenta coordenar E investigar ao mesmo tempo, perde visão de ambos.

## Papéis

**IC — Incident Commander**
Coordena a resposta. Delega investigação. Mantém comunicação entre papéis. Não investiga tecnicamente — quem coordena não mergulha no código.

**TL — Technical Lead**
Lidera a investigação técnica. Não coordena — foco total na causa raiz e mitigação. Reporta progresso ao IC.

**Comunicador**
Atualiza stakeholders externos (produto, C-level, clientes) e status page. Filtra ruído técnico para comunicação legível.

**Escriba**
Documenta a timeline em tempo real durante o incidente. Fonte primária para o [[concepts/blameless-post-mortem]] posterior. Se não houver escriba dedicado, o IC documenta minimamente no canal.

## Em Times Pequenos

Com equipe pequena, IC e Escriba podem ser a mesma pessoa. IC e TL nunca devem ser a mesma pessoa em SEV-1/SEV-2 — o custo cognitivo de coordenar + investigar simultaneamente aumenta MTTR significativamente.

## Key Sources

- [[sources/sre-error-budget-incidents]]
