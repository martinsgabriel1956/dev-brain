---
type: source
title: "Go — Avançado"
aliases: ["go generics", "go reflection", "go cgo", "go wasm", "go memory model"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/go-avancado.md
source_url: ""
author: "lang-systems skill"
date_published: 2026-04-24
date_ingested: 2026-04-24
source_count: 0
tags: [go, avancado, generics, reflection, cgo, wasm, memory-model, gc]
skill: lang-systems
status: stable
---

# Go — Avançado

## TL;DR

Go 1.18+ trouxe generics — eliminam duplicação mas aumentam complexidade de mensagens de erro. Reflection é como `encoding/json` e ORMs funcionam internamente; na aplicação, prefira generics ou code generation (sqlc, protoc). cgo permite interop com C mas quebra portabilidade e desativa o race detector. GC em Go 1.21+ tem latência de pausa < 1ms.

## Claims Principais

| Claim | Confiança |
|---|---|
| Generics em Go usam type constraints via interfaces — não templates C++ | Alta |
| `sync/atomic` elimina lock overhead mas é difícil de raciocinar corretamente | Alta |
| Reflection sem verificação em compile-time — lento e frágil para uso geral | Alta |
| cgo quebra portabilidade, inviabiliza race detector, adiciona overhead de contexto | Alta |
| GC pausas < 1ms em Go 1.21+ com GOGC e GOMEMLIMIT tuning | Alta |
| WASM via Go gera bundle grande — performance inferior ao JS nativo para UI | Média |

## Conceitos Abordados

- [[go-avancado]] · [[go-fundamentos]] · [[go-concorrencia]] · [[go-producao]]
