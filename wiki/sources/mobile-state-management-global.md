---
type: source
title: "State Management Global — Mobile (Zustand, Redux, Riverpod, Bloc)"
aliases: ["mobile state global", "zustand mobile", "redux mobile", "riverpod flutter", "bloc flutter"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-state-management-global.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, state-management, zustand, redux, riverpod, bloc, global-state]
skill: tech-mentor-mobile
status: stable
---

# State Management Global — Mobile

## TL;DR

Estado global apenas para o que é verdadeiramente compartilhado: autenticação, carrinho, configurações de tema. React Native: Zustand (simples, sem boilerplate) ou Redux Toolkit (apps complexos com DevTools). Flutter: Riverpod (recomendado, typesafe) ou Bloc (events/states explícitos). Nunca colocar server state em estado global — usar TanStack Query / Riverpod FutureProvider.

## Claims Principais

| Claim | Confiança |
|---|---|
| Server state não pertence ao estado global — TanStack Query gerencia cache e sync | Alta |
| Zustand tem zero boilerplate vs Redux — preferível para a maioria dos casos RN | Alta |
| Riverpod é type-safe e testável sem context — Bloc para fluxos com eventos complexos | Alta |
| Estado global excessivo = acoplamento — preferir composição de estados locais | Alta |

## Conceitos Abordados

- [[mobile-state-management-global]] · [[mobile-state-management-local]] · [[mobile-chamadas-http]] · [[mobile-navegacao]]
