---
type: concept
title: "DDD — Domain-Driven Design"
aliases: ["domain-driven design", "ddd", "domínio"]
date_created: 2026-05-31
date_updated: 2026-05-31
source_count: 1
tags: [ddd, arquitetura, bounded-context, aggregate, domain-events, hexagonal]
skill: tech-mentor-backend
status: draft
---

# DDD — Domain-Driven Design

## TL;DR

Abordagem arquitetural que coloca o **domínio do negócio** no centro do design. O código deve espelhar o modelo mental dos especialistas do negócio. Conceitos centrais: Bounded Context, Aggregate, Domain Events, Ubiquitous Language.

## Pilares

- **Ubiquitous Language** — devs e negócio usam o mesmo vocabulário
- **Bounded Context** — fronteiras explícitas onde um modelo é válido
- **Aggregate** — unidade de consistência; processa commands, emite eventos
- **Domain Events** — fatos significativos que aconteceram no domínio
- **Repository** — abstração de persistência (domínio não conhece banco)

## Arquitetura Hexagonal + DDD

O domínio fica no centro, protegido de detalhes de infraestrutura:

```
[HTTP/gRPC Adapters]
        ↓
[Application Services]
        ↓
[Domain: Aggregates, Domain Events, Value Objects]  ← puro, sem I/O
        ↓
[Repository Interfaces] ← abstrações, não implementações
        ↓
[DB Adapters, Message Adapters]
```

[[efeitos-colaterais]] ficam nas bordas — o domínio é puro e testável.

## Conexão com Event Sourcing

DDD e [[event-sourcing]] são complementares: Domain Events (DDD) são exatamente os eventos persistidos em Event Sourcing. O Aggregate emite eventos que descrevem o que aconteceu; o Event Store os persiste.

## Uso no Nubank

O [[nubank]] usa DDD como base para organizar o domínio financeiro — contas, transações, limites de crédito. A combinação DDD + [[programacao-funcional]] + [[event-sourcing]] permite que o codebase envelheça como vinho.

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
