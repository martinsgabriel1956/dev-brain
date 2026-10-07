---
type: concept
title: "API é Consequência, Não Ponto de Partida"
aliases: ["progresso falso", "não comece pela API"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [system-design, entrevistas, anti-pattern]
skill: tech-mentor-system-design
status: draft
---

# API é Consequência, Não Ponto de Partida

Em entrevista de system design, desenhar endpoints primeiro é *progresso falso*: parece avanço (rota, código), mas sem requisitos nem entidades faltam `user ID`, prioridade, etc. A API decorre das decisões de arquitetura. Ordem: [[wiki/concepts/requisitos-funcionais-e-nao-funcionais|requisitos]] → [[wiki/concepts/entidades-de-primeira-classe-system-design|entidades]] (≤3 min) → [[wiki/concepts/high-level-design]] → API se sobrar tempo. Ver [[wiki/concepts/entrevista-system-design]], [[wiki/concepts/notification-system]]. Causa de fundo: o sênior extrapola etapas por saber demais; ver [[wiki/concepts/pensar-em-voz-alta-na-entrevista]].

## Key sources
- [[wiki/sources/desafio-sistema-notificacao-system-design-reprova-senior-ana]]
