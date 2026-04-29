---
type: source
title: "Layouts Responsivos — Mobile"
aliases: ["mobile layouts", "flexbox mobile", "responsive mobile", "safe area"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-layouts-responsivos.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, layouts, flexbox, responsive, safe-area, WindowSizeClass, LayoutBuilder]
skill: tech-mentor-mobile
status: stable
---

# Layouts Responsivos — Mobile

## TL;DR

Flexbox (RN), ConstraintLayout/LayoutBuilder (Android/Flutter), Auto Layout (iOS). SafeArea obrigatório em todas as plataformas — notch, dynamic island, nav bar, home indicator. WindowSizeClass (Android) e `horizontalSizeClass` (iOS) para tablets/foldables. Evitar tamanhos hardcoded — usar percentagens, `Expanded`/`Flexible` (Flutter) ou constraints relativos.

## Claims Principais

| Claim | Confiança |
|---|---|
| SafeArea/`safeAreaInsets` obrigatório — sem ele o conteúdo fica atrás do notch/home indicator | Alta |
| WindowSizeClass (Android) classifica Compact/Medium/Expanded — breakpoints oficiais do Google | Alta |
| Flexbox RN usa `flexDirection: 'column'` por padrão (oposto ao CSS) | Alta |
| LayoutBuilder (Flutter) obtém constraints do pai — preferível a MediaQuery para componentes | Alta |

## Conceitos Abordados

- [[mobile-layouts-responsivos]] · [[mobile-navegacao]] · [[mobile-performance-listas]] · [[mobile-design-system]]
