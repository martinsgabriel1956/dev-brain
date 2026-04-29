---
type: source
title: "Animações Performáticas — Reanimated 3, Compose Animated, Flutter Implicit Animations"
aliases: ["mobile animacoes", "reanimated 3", "compose animation", "flutter animations"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-animacoes-performaticas.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, animacoes, reanimated, compose, flutter, ui-thread, jank]
skill: tech-mentor-mobile
status: stable
---

# Animações Performáticas — Mobile

## TL;DR

Animações performáticas rodam na UI thread — nunca no JS thread (RN) ou na thread principal de negócio. React Native usa Reanimated 3 com worklets; Android Compose usa `animate*AsState` e `AnimatedVisibility`; Flutter usa `ImplicitlyAnimatedWidget` e `AnimationController`. Jank (frames > 16ms) é perceptível imediatamente — profiling com Perfetto/Instruments antes de otimizar.

## Claims Principais

| Claim | Confiança |
|---|---|
| Reanimated 3 worklets rodam na UI thread — elimina bridge RN no loop de animação | Alta |
| Compose `animate*AsState` é declarativo — framework gera interpolação automaticamente | Alta |
| Flutter `ImplicitlyAnimatedWidget` para animações simples; `AnimationController` para controle fino | Alta |
| Animações CSS/`Animated` (RN) são suficientes para simples — Reanimated só para gestos e animações complexas | Alta |

## Conceitos Abordados

- [[mobile-animacoes-performaticas]] · [[mobile-performance-listas]] · [[mobile-profiling]]
