---
type: source
title: "Chamadas HTTP + Loading States + Error Handling — Mobile"
aliases: ["mobile networking", "mobile http", "mobile loading states", "mobile error handling"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-chamadas-http.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, networking, http, loading-states, error-handling, tanstack-query, retrofit, interceptor]
skill: tech-mentor-mobile
status: stable
---

# Chamadas HTTP — Mobile

## TL;DR

TanStack Query (RN/Expo) ou Riverpod FutureProvider (Flutter) para server state — cache automático, retry configurável, sem boilerplate de loading/error. Retrofit + OkHttp interceptors para Android nativo — interceptors para auth, logging, retry. Todo loading state deve ter skeleton/shimmer, não apenas spinner. Tratar offline graciosamente: mostrar dados em cache + badge "offline".

## Claims Principais

| Claim | Confiança |
|---|---|
| TanStack Query elimina loading/error boilerplate — stale-while-revalidate automático | Alta |
| OkHttp interceptors para auth header, logging e retry — sem duplicar por request | Alta |
| Skeleton/shimmer > spinner — reduz percepção de latência (content shifting previsível) | Alta |
| Timeout obrigatório em toda chamada — sem timeout, goroutine/thread vaza em rede lenta | Alta |

## Conceitos Abordados

- [[mobile-chamadas-http]] · [[mobile-offline-first-basico]] · [[mobile-state-management-global]] · [[cache]]
