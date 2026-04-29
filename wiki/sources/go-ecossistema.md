---
type: source
title: "Go — Ecossistema e Tooling"
aliases: ["go frameworks", "go chi", "go sqlc", "go sqlx", "go gorm", "go modules"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/go-ecossistema.md
source_url: ""
author: "lang-systems skill"
date_published: 2026-04-24
date_ingested: 2026-04-24
source_count: 0
tags: [go, ecossistema, chi, gin, echo, sqlc, sqlx, gorm, modules, linting]
skill: lang-systems
status: stable
---

# Go — Ecossistema e Tooling

## TL;DR

Para HTTP: `net/http` puro (Go 1.22+ com path params nativos) ou Chi para roteamento composable sem mágica. Para SQL: sqlc (type-safe, code generation a partir de queries SQL reais) é recomendado; GORM para projetos que precisam de migrations automáticas. golangci-lint com staticcheck e errcheck em CI.

## Claims Principais

| Claim | Confiança |
|---|---|
| Go 1.22+ suporta path parameters nativos em `net/http` — Chi ainda agrega middleware composable | Alta |
| sqlc gera código Go type-safe a partir de SQL real — zero N+1 acidental, zero interface{} | Alta |
| GORM é conveniente mas gera queries imprevisíveis em relacionamentos complexos | Alta |
| golangci-lint com staticcheck detecta erros não-checados e código morto | Alta |
| Gin/Echo têm overhead de reflection; Chi é apenas wrapper sobre net/http padrão | Média |

## Conceitos Abordados

- [[go-ecossistema]] · [[go-stdlib]] · [[go-arquitetura]] · [[go-producao]]
