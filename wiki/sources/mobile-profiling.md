---
type: source
title: "Profiling Mobile — Perfetto, Instruments, Android Studio Profiler"
aliases: ["mobile profiling", "android profiler", "xcode instruments", "perfetto mobile"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-profiling.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, profiling, perfetto, instruments, android-profiler, cpu, memory, jank]
skill: tech-mentor-mobile
status: stable
---

# Profiling Mobile

## TL;DR

Android: Perfetto para system tracing, Android Studio Profiler (CPU/Memory/Network). iOS: Xcode Instruments (Time Profiler, Allocations, Leaks). React Native: Flipper + Hermes Profiler. Medir antes de otimizar — nunca otimizar por intuição. Focar em frames que ultrapassam 16ms (janks). Memory leaks em listas são causa comum de degradação progressiva.

## Claims Principais

| Claim | Confiança |
|---|---|
| Perfetto é mais preciso que Android Studio Profiler para system-level tracing | Alta |
| Instruments `Time Profiler` mostra CPU por frame — identificar métodos na UI thread | Alta |
| Hermes Profiler (RN) usa sampling profile — não instrumentação, overhead mínimo | Alta |
| Memory leak em `RecyclerView`/`FlatList`: listener não removido no `onDetach` | Alta |
| Profiling em dispositivo real — emulador não reflete thermal throttling e cache de hardware | Alta |

## Conceitos Abordados

- [[mobile-profiling]] · [[mobile-metricas-criticas]] · [[mobile-animacoes-performaticas]] · [[mobile-performance-listas]]
