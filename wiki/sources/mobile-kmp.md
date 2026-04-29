---
type: source
title: "Kotlin Multiplatform (KMP) — Compartilhar Lógica de Negócio"
aliases: ["kmp", "kotlin multiplatform", "kmm", "shared logic ios android"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-kmp.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, kmp, kotlin-multiplatform, ios, android, shared-logic, coroutines]
skill: tech-mentor-mobile
status: stable
---

# Kotlin Multiplatform (KMP)

## TL;DR

KMP compartilha lógica de negócio (domain, data, use cases) entre iOS e Android mantendo UI nativa em cada plataforma (Compose + SwiftUI). Diferente do Flutter: UI não é compartilhada. `commonMain` para código compartilhado, `expect/actual` para implementações específicas por plataforma. Ktor para networking multiplataforma; SQLDelight para banco local.

## Claims Principais

| Claim | Confiança |
|---|---|
| KMP compartilha domain/data — UI permanece nativa (Compose no Android, SwiftUI no iOS) | Alta |
| `expect/actual` permite APIs com mesmo contrato e implementação por plataforma | Alta |
| Ktor é o cliente HTTP recomendado para commonMain — suporta iOS e Android | Alta |
| SQLDelight gera code type-safe a partir de SQL real — equivalente ao sqlc para mobile | Alta |
| KMP estável desde 2023 — adotado por Netflix, VMware, Philips | Alta |

## Conceitos Abordados

- [[mobile-kmp]] · [[mobile-cross-platform-decision]] · [[mobile-armazenamento-local]] · [[mobile-chamadas-http]]
