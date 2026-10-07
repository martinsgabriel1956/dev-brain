---
type: concept
title: "Channel Router: Prioridade, Preferência e Custo"
aliases: ["roteador de canal", "fallback de canal", "cost-aware routing"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [system-design, custo, notificacao, fallback]
skill: tech-mentor-system-design
status: draft
---

# Channel Router: Prioridade, Preferência e Custo

Componente (pode ser uma classe/[[wiki/concepts/facade-pattern|facade]]) que centraliza a decisão de canal por prioridade + preferência do usuário + custo. Fallback: push primeiro (grátis), e-mail depois (barato), SMS por último (10–500× mais caro `[external não verificado]`), reservado a falhas ou notificações críticas. Resolve o requisito *cost-aware*. Ver [[wiki/concepts/palavras-do-enunciado-mudam-a-arquitetura]], [[wiki/concepts/finops]], [[wiki/concepts/notification-system]], [[wiki/concepts/mobile-push-notifications]].

## Key sources
- [[wiki/sources/desafio-sistema-notificacao-system-design-reprova-senior-ana]]
