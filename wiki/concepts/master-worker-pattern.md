---
type: concept
title: "Master-Worker Pattern"
aliases: ["Master-Worker", "padrão mestre-trabalhador"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_count: 1
tags: [design-patterns, sistemas-distribuidos, coordenacao, paralelismo]
skill: tech-mentor-backend
status: stub
---

# Master-Worker Pattern

Padrão de distribuição de trabalho: um **Master** divide o trabalho em unidades e as publica num repositório compartilhado (fila, espaço coordenado); múltiplos **Workers**, genéricos e desacoplados entre si, leem unidades de trabalho, processam e escrevem os resultados de volta.

No contexto de [[wiki/concepts/javaspaces|JavaSpaces]], é o padrão de software mais comum: o "espaço" funciona como o repositório compartilhado, e ambientes típicos têm vários espaços, múltiplos masters e muitos workers genéricos. O mesmo princípio aparece em filas de trabalho modernas (task queues, background jobs) — o [[wiki/concepts/tuple-space|tuple space]] é uma das formas mais antigas de implementá-lo.

## Key sources

- [[wiki/sources/tuple-space-wikipedia]] — descrição do padrão no contexto de JavaSpaces
