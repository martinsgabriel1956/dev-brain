---
type: source
title: "Go — Arquitetura e Patterns"
aliases: ["go clean architecture", "go repository pattern", "go dependency injection"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/go-arquitetura.md
source_url: ""
author: "lang-systems skill"
date_published: 2026-04-24
date_ingested: 2026-04-24
source_count: 0
tags: [go, arquitetura, clean-architecture, repository, dependency-injection, functional-options]
skill: lang-systems
status: stable
---

# Go — Arquitetura e Patterns

## TL;DR

Clean Architecture em Go usa `cmd/` para wiring, `internal/domain/` para entities, `internal/features/<domain>/` para handler/usecase/repository, e `internal/infrastructure/` para implementações. Dependency injection é manual via construtores — sem frameworks. Functional Options Pattern resolve configuração opcional sem structs de config explodindo em parâmetros.

## Claims Principais

| Claim | Confiança |
|---|---|
| Wiring explícito em `main.go` sem DI framework é idiomático em Go | Alta |
| Interface do Repository fica no domínio, implementação na infraestrutura | Alta |
| Functional Options Pattern (`WithTimeout`, `WithRetry`) é o padrão para configuração extensível | Alta |
| Erros específicos por domínio (`UserNotFoundError`) em vez de strings genéricas | Alta |
| Guard clauses no topo das funções eliminam aninhamento | Alta |

## Conceitos Abordados

- [[go-arquitetura]] · [[clean-architecture]] · [[hexagonal-architecture]] · [[go-ecossistema]] · [[go-producao]]
