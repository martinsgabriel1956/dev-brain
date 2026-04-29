---
type: source
title: "Go — Fundamentos da Linguagem"
aliases: ["go basics", "go tipos primitivos", "go slices maps structs"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/go-fundamentos.md
source_url: ""
author: "lang-systems skill"
date_published: 2026-04-24
date_ingested: 2026-04-24
source_count: 0
tags: [go, fundamentos, tipos, slices, maps, structs, zero-values, iota]
skill: lang-systems
status: stable
---

# Go — Fundamentos da Linguagem

## TL;DR

Go é uma linguagem compilada, estaticamente tipada, com garbage collection e foco em sistemas distribuídos. Zero values garantem que toda variável tem um estado inicial definido. Slices são a estrutura central — arrays são raramente usados diretamente. Structs + interfaces substituem herança com composição explícita.

## Claims Principais

| Claim | Confiança |
|---|---|
| Zero values eliminam uninitialized bugs — toda variável tem um estado válido por padrão | Alta |
| Slices são views de arrays — capacidade e comprimento são conceitos distintos | Alta |
| `iota` é o mecanismo idiomático para enumerações e bitmasks | Alta |
| Pointer receivers modificam o original; value receivers operam em cópia | Alta |
| Go não tem classes — structs + métodos + interfaces substituem herança | Alta |
| `for range` é a forma idiomática; C-style apenas quando índice é necessário | Média |

## Conceitos Abordados

- [[go-fundamentos]] · [[go-oop-composicao]] · [[go-concorrencia]] · [[go-stdlib]]
