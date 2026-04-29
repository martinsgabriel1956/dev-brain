---
type: source
title: "Monitoramento Mobile — Crashlytics, Sentry, Performance Monitoring"
aliases: ["mobile monitoramento", "mobile crashlytics", "mobile sentry", "mobile observabilidade"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-monitoramento.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, monitoramento, crashlytics, sentry, performance-monitoring, alertas]
skill: tech-mentor-mobile
status: stable
---

# Monitoramento Mobile

## TL;DR

Firebase Crashlytics para crash reporting + symbolication automática. Sentry para erros com breadcrumbs e session replay. Firebase Performance Monitoring para métricas automáticas de startup e network. Alertar em crash-free rate < 99.5% e ANR rate > 0.1% — thresholds que o Google Play usa para badging. Logs estruturados com userId/sessionId para correlacionar incidentes.

## Claims Principais

| Claim | Confiança |
|---|---|
| Crashlytics symbolication automática — stack trace legível sem upload manual de dSYM/mapping | Alta |
| Sentry session replay captura taps e telas antes do crash — reduz MTTR | Alta |
| Firebase Performance registra cold/warm start automaticamente sem instrumentação manual | Alta |
| Alert em crash-free < 99.5% — Google Play pode bloquear rollout com crash rate elevado | Alta |

## Conceitos Abordados

- [[mobile-monitoramento]] · [[mobile-metricas-criticas]] · [[mobile-cicd]] · [[observabilidade]]
