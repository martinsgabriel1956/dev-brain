---
type: source
title: "Go — OOP: Composição, Interfaces e Receivers"
aliases: ["go embedding", "go interfaces implícitas", "go receivers", "go duck typing"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/go-oop-composicao.md
source_url: ""
author: "lang-systems skill"
date_published: 2026-04-24
date_ingested: 2026-04-24
source_count: 0
tags: [go, oop, composicao, embedding, interfaces, receivers, duck-typing]
skill: lang-systems
status: stable
---

# Go — OOP: Composição, Interfaces e Receivers

## TL;DR

Go não tem herança — usa **composição via embedding**. Embedding promove métodos e campos mas não cria relação "é um". Interfaces são implícitas (duck typing) — qualquer tipo que implementa os métodos satisfaz a interface, sem `implements`. Pointer receivers modificam o original e devem ser usados consistentemente quando um método precisa mutar o struct.

## Claims Principais

| Claim | Confiança |
|---|---|
| Embedding não é herança — `Dog` com `Animal` embedded não pode substituir `Animal` | Alta |
| Interfaces implícitas permitem satisfazer contratos de libs externas sem modificá-las | Alta |
| Pointer receiver em qualquer método → todos os métodos devem ser pointer receiver | Alta |
| `fmt.Stringer` (interface `String() string`) é o padrão de serialização de tipos custom | Alta |
| Type switch é mais idiomático que múltiplos type assertions sequenciais | Alta |

## Conceitos Abordados

- [[go-oop-composicao]] · [[go-fundamentos]] · [[go-arquitetura]] · [[clean-architecture]]
