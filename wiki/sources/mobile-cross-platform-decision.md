---
type: source
title: "Decisão Cross-Platform — Flutter vs React Native vs KMP vs Nativo"
aliases: ["cross platform mobile", "flutter vs react native", "mobile decision framework"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-cross-platform-decision.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, cross-platform, flutter, react-native, kmp, nativo, decisao]
skill: tech-mentor-mobile
status: stable
---

# Decisão Cross-Platform

## TL;DR

Flutter para UI pixel-perfect cross-platform com Dart. React Native quando o time é JS/TS e o app não precisa de UI 100% nativa. KMP (Kotlin Multiplatform) para compartilhar lógica de negócio mantendo UI nativa em cada plataforma. Nativo puro para apps com requirements de hardware intenso (câmera, AR, saúde, jogos). A decisão é irreversível no curto prazo — avaliar team expertise primeiro.

## Claims Principais

| Claim | Confiança |
|---|---|
| Flutter renderiza com Skia/Impeller próprio — UI idêntica em iOS/Android independente de versão OS | Alta |
| React Native nova arquitetura (JSI) elimina bridge — performance próxima ao nativo | Alta |
| KMP compartilha domain/data layer; UI permanece nativa em Compose e SwiftUI | Alta |
| Nativo obrigatório para: Bluetooth intensivo, ARKit/ARCore, HealthKit/Health Connect | Alta |
| Team expertise > performance teórica na decisão de plataforma | Alta |

## Conceitos Abordados

- [[mobile-cross-platform-decision]] · [[mobile-kmp]] · [[mobile-design-system]] · [[mobile-metricas-criticas]]
