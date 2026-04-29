---
type: source
title: "Métricas Críticas de Performance Mobile"
aliases: ["mobile metricas", "mobile performance metrics", "cold start mobile", "TTI mobile"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-metricas-criticas.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, metricas, performance, cold-start, TTI, FPS, ANR, crash-rate]
skill: tech-mentor-mobile
status: stable
---

# Métricas Críticas de Performance Mobile

## TL;DR

Métricas obrigatórias: Cold Start < 2s, Warm Start < 1s, FPS ≥ 60 (90/120 em dispositivos premium), ANR rate < 0.1% (Google Play threshold), Crash-free rate > 99.5%. Time to Interactive (TTI) mede quando o usuário pode interagir, não apenas quando a tela aparece. Medir sempre em dispositivos de baixo custo (Motorola G series) — não em flagship.

## Claims Principais

| Claim | Confiança |
|---|---|
| Cold Start > 2s = abandono de usuário; Google Play rebaixa apps com ANR > 0.47% | Alta |
| FPS < 60 é perceptível imediatamente — Perfetto e Android Studio Profiler medem por frame | Alta |
| TTI é a métrica real de UX — spinner visível não significa app interativo | Alta |
| Testar em dispositivo médio-baixo (Moto G) — flagship esconde problemas de real-world users | Alta |
| Crash-free rate < 99.5% = problema crítico — Firebase Crashlytics por padrão | Alta |

## Conceitos Abordados

- [[mobile-metricas-criticas]] · [[mobile-profiling]] · [[mobile-monitoramento]] · [[mobile-baseline-profiles]]
