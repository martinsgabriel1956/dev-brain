---
type: source
title: "State Management Local — Mobile (useState, ViewModel, StatefulWidget)"
aliases: ["mobile state local", "viewmodel android", "stateful widget flutter", "usestate mobile"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-state-management-local.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, state-local, viewmodel, stateful-widget, useState, compose-state]
skill: tech-mentor-mobile
status: stable
---

# State Management Local — Mobile

## TL;DR

Estado local: React Native usa `useState`/`useReducer` (hooks), Android Compose usa `ViewModel` com `StateFlow`/`UiState`, Flutter usa `StatefulWidget` ou `ValueNotifier`. Regra: estado local primeiro — elevar para global só quando necessário. `ViewModel` (Android) sobrevive a rotação de tela — `rememberSaveable` para estado que deve sobreviver ao processo kill.

## Claims Principais

| Claim | Confiança |
|---|---|
| ViewModel sobrevive a rotação de tela — Activity/Fragment recriados, ViewModel não | Alta |
| `rememberSaveable` (Compose) serializa estado para Bundle — sobrevive ao processo kill | Alta |
| `useState` em RN recria closure a cada render — `useRef` para valores que não causam render | Alta |
| `StatefulWidget` Flutter com `setState` suficiente para estado isolado por widget | Alta |

## Conceitos Abordados

- [[mobile-state-management-local]] · [[mobile-state-management-global]] · [[mobile-layouts-responsivos]]
