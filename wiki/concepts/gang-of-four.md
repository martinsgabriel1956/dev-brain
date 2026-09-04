---
type: entity
title: "Gang of Four"
aliases: ["GoF", "Gang of Four", "Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"]
date_created: 2026-05-05
date_updated: 2026-09-04
source_count: 2
tags: [design-patterns, gof, livro, arquitetura]
skill: tech-mentor-backend
status: stable
---

# Gang of Four (GoF)

Quatro desenvolvedores — Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides — que em **1994** publicaram *Design Patterns: Elements of Reusable Object-Oriented Software*, catalogando 23 padrões de design orientado a objetos.

## O Livro

**Design Patterns: Elements of Reusable Object-Oriented Software** (1994)

Documentou, catalogou e formalizou 23 padrões que resolvem problemas recorrentes de programação, independente de linguagem ou plataforma.

## Os 23 Padrões — Por Categoria

**[[creational-patterns]] (5):** Abstract Factory, Builder, Factory Method, Prototype, Singleton

**[[structural-patterns]] (7):** Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy

**[[behavioral-patterns]] (11):** Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor

## Relevância Atual

Todos os 23 padrões permanecem aplicáveis. Os mais frequentes em decisões arquiteturais modernas:

- [[strategy-pattern]] — elimina if/else, segue [[open-closed-principle]]
- [[observer-pattern]] — base de sistemas event-driven e DDD Domain Events
- [[factory-pattern]] / [[builder-pattern]] — criação desacoplada
- [[adapter-pattern]] — integração com libs/APIs externas
- [[facade-pattern]] — simplificação de subsistemas

## Key Sources

- [[sources/sete-padroes-de-design-de-software]]
- [[wiki/sources/decorator-xunitpatterns]] — xUnitPatterns.com (Meszaros) cita diretamente a definição original do GOF para o [[wiki/concepts/decorator-pattern|Decorator]], como parte da categoria "External Patterns" do site (padrões gerais emprestados de outros catálogos, não específicos de teste)
