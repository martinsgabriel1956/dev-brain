---
type: concept
title: "DDD — Domain-Driven Design"
aliases: ["domain-driven design", "ddd", "domínio"]
date_created: 2026-05-31
date_updated: 2026-07-09
source_count: 2
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

## Ubiquitous Language como Correção do Desalinhamento Dev-IA

[[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] aplica o pilar Ubiquitous Language fora do contexto tradicional de DDD (dev ↔ especialista de domínio) para o contexto de dev ↔ IA: verborragia e desalinhamento entre plano e implementação são sintoma de que dev e IA não compartilham vocabulário. A prática descrita: extrair a terminologia de domínio já presente na base de código para um arquivo markdown com tabelas de termos, mantido aberto durante todo o planejamento com a IA. Relato do autor: isso reduziu a verbosidade dos "thinking traces" da IA e aumentou o alinhamento entre o que foi planejado e o que foi implementado — o mesmo mecanismo de "conversas, código e conversas com especialistas derivam do mesmo modelo" descrito no pilar acima, só que a IA ocupa o papel do "especialista" a ser alinhado.

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
