---
type: source
title: "Design System Mobile — Tokens, Componentes Agnósticos, Figma-to-Code"
aliases: ["mobile design system", "design tokens mobile", "figma to code mobile"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-design-system.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, design-system, tokens, componentes, figma, dark-mode]
skill: tech-mentor-mobile
status: stable
---

# Design System Mobile

## TL;DR

Design system mobile é a fonte única de verdade entre Figma e código. Arquitetura: tokens no centro (cores, espaçamento, tipografia), componentes primitivos em cima (Button, Input, Text), componentes compostos no topo (ProductCard, CheckoutForm). Tokens garantem dark mode, theming e resizing sem tocar componentes. Sem design system, cada dev reinventa padding — inconsistência que usuários percebem.

## Claims Principais

| Claim | Confiança |
|---|---|
| Tokens como fonte única de verdade — dark mode é troca de token, não de componente | Alta |
| Figma Variables → Style Dictionary → tokens em código (JSON → Kotlin/Swift/TS) | Alta |
| Componentes primitivos sem lógica de negócio — reusáveis em qualquer contexto | Alta |
| Design system sem govenance morre — precisa de processo de contribution e versionamento | Alta |

## Conceitos Abordados

- [[mobile-design-system]] · [[mobile-cross-platform-decision]] · [[mobile-feature-flags]]
