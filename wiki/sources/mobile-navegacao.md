---
type: source
title: "Navegação Mobile — Stack, Tab, Drawer, Deep Links"
aliases: ["mobile navegacao", "react navigation", "navigation compose", "flutter navigator"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-navegacao.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, navegacao, stack, tab, drawer, react-navigation, navigation-compose, flutter]
skill: tech-mentor-mobile
status: stable
---

# Navegação Mobile

## TL;DR

React Navigation (RN) é o padrão — Stack, Tab, Drawer compostos. Navigation Compose (Android) com rotas tipadas em Kotlin. Flutter usa Navigator 2.0 (GoRouter) para deep links com estado. Padrão: Tab navigation no root, Stack dentro de cada tab. Estado de navegação não é estado de UI — não colocar em Zustand/Redux.

## Claims Principais

| Claim | Confiança |
|---|---|
| React Navigation 6+ suporta tipagem TypeScript para parâmetros de rota | Alta |
| Navigation Compose rotas tipadas (Kotlin Serializable) eliminam string magic | Alta |
| GoRouter (Flutter) unifica Navigator 2.0 e deep links — obrigatório para apps com links | Alta |
| Tab no root + Stack dentro de cada tab = padrão de navegação iOS/Android | Alta |
| Estado de navegação não pertence ao estado global da aplicação | Alta |

## Conceitos Abordados

- [[mobile-navegacao]] · [[mobile-deep-links]] · [[mobile-state-management-global]] · [[mobile-layouts-responsivos]]
