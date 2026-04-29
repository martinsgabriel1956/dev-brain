---
type: source
title: "Baseline Profiles — Android (Redução de Cold Start)"
aliases: ["baseline profiles android", "ART compilation", "android cold start"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-baseline-profiles.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, android, baseline-profiles, cold-start, ART, performance, startup]
skill: tech-mentor-mobile
status: stable
---

# Baseline Profiles — Android

## TL;DR

Baseline Profiles instruem o ART (Android Runtime) a pré-compilar caminhos críticos de código antes da primeira execução — reduzindo cold start em 30-40%. Gerados com `BaselineProfileRule` (Macrobenchmark), incluídos no APK/AAB. A Play Store distribui o perfil compilado para novos usuários antes do primeiro launch. Integrar em CI para detectar regressões.

## Claims Principais

| Claim | Confiança |
|---|---|
| Baseline Profiles reduzem cold start 30-40% — pré-compilação ART de caminhos críticos | Alta |
| Play Store distribui perfil compilado para dispositivos antes do primeiro download | Alta |
| Gerados com `BaselineProfileRule` do Macrobenchmark — automatizável em CI | Alta |
| Sem Baseline Profile, ART usa JIT na primeira execução — frames lentos perceptíveis | Alta |

## Conceitos Abordados

- [[mobile-baseline-profiles]] · [[mobile-metricas-criticas]] · [[mobile-profiling]] · [[mobile-cicd]]
