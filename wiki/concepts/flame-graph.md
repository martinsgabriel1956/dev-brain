---
type: concept
title: "Flame Graph"
aliases: []
date_created: 2026-09-22
date_updated: 2026-11-11
source_count: 3
tags: [flame-graph]
skill: tech-mentor-infra
status: stub
---

# Flame Graph

Stub criado durante sweep de lint (links quebrados) a partir de referências em 2 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/flame-graph-profiling]]: [[wiki/concepts/flame-graph]]
- Em [[wiki/sources/performance-methods]]: [[wiki/concepts/flame-graph]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## Leitura prática em Node.js

Em [[wiki/sources/cpu-profiling-nodejs-inspector-autocannon-erick-wendel]], o profile de uma rota lenta é recortado na janela do teste de carga e lido pelo topo: as funções mais caras aparecem primeiro, e descer pela árvore leva da rota ao `cloneDeep` do [[wiki/entities/lodash]]. Ver [[wiki/concepts/cpu-profiling]].

## Key sources

- [[wiki/sources/flame-graph-profiling]]
- [[wiki/sources/performance-methods]]
- [[wiki/sources/cpu-profiling-nodejs-inspector-autocannon-erick-wendel]]: `.cpuprofile` gravado com `node:inspector/promises` e lido de cima para baixo até o `cloneDeep`; ver [[wiki/concepts/cpu-profiling]]
