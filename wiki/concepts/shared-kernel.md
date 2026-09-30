---
type: concept
title: "Shared Kernel"
aliases: ["kernel compartilhado", "shared kernel"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [ddd, context-map, shared-kernel, integracao]
skill: tech-mentor-backend
status: stub
---

# Shared Kernel

## TL;DR

Padrão de integração entre bounded contexts em que um subconjunto do modelo é **compartilhado de forma controlada** entre dois contextos ([[wiki/sources/bounded-context-contextos-delimitados-bernardo-lobato]]). Ver [[wiki/concepts/context-map]]. Risco (da skill [skill: tech-mentor-backend]): o kernel crescer e virar acoplamento implícito; alterações sem aviso aos outros times quebram silenciosamente.

Ver também a discussão de limites do Shared Kernel em [[wiki/concepts/ddd]] (claim de [[wiki/sources/tres-tipos-de-modulos-arquitetura-modular-valdemar-neto]], não verificado).

## Key Sources

- [[wiki/sources/bounded-context-contextos-delimitados-bernardo-lobato]] — citado como uma das estratégias de comunicação entre contextos (uma linha)
