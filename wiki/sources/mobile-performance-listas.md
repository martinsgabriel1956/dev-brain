---
type: source
title: "Otimização de Listas Mobile — FlashList, LazyColumn, ListView.builder"
aliases: ["mobile listas", "flatlist performance", "flashlist", "lazycol android", "mobile recyclerview"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-performance-listas.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, listas, flashlist, flatlist, lazycol, recyclerview, virtualizacao, performance]
skill: tech-mentor-mobile
status: stable
---

# Performance de Listas Mobile

## TL;DR

Virtualização é obrigatória em listas longas — renderizar apenas itens visíveis + buffer. React Native: `FlashList` (Shopify) sobre `FlatList` — recicla células como RecyclerView nativo. Android: `LazyColumn` (Compose) ou `RecyclerView`. Flutter: `ListView.builder` com `itemExtent` para scroll position fixo. Antipattern: `ScrollView` com `map()` — renderiza tudo de uma vez, OOM em listas longas.

## Claims Principais

| Claim | Confiança |
|---|---|
| FlashList 10x mais rápido que FlatList — recicla JSI cell views vs recriar | Alta |
| `itemExtent` no Flutter `ListView.builder` elimina cálculo de altura por item | Alta |
| LazyColumn Compose reutiliza composition por default — não precisa de key manual | Alta |
| `ScrollView` + `map()` renderiza todos os itens — anti-pattern para listas > 50 items | Alta |

## Conceitos Abordados

- [[mobile-performance-listas]] · [[mobile-metricas-criticas]] · [[mobile-animacoes-performaticas]] · [[mobile-profiling]]
