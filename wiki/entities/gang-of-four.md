---
type: entity
title: "Gang of Four (GoF)"
aliases: ["GoF", "gang of four", "Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"]
date_created: 2026-05-01
date_updated: 2026-09-22
source_count: 8
tags: [design-patterns, books, oop, junit, testes, gof, livro, arquitetura]
skill: tech-mentor-backend
status: stable
---

## Quem são

Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides — os quatro autores do livro *Design Patterns: Elements of Reusable Object-Oriented Software* (1994), considerado o catálogo oficial dos 23 padrões de projeto clássicos.

## Erich Gamma também é coautor do JUnit

Além do *Design Patterns*, Erich Gamma programou em par com [[wiki/entities/kent-beck]] a primeira versão do [[wiki/entities/junit]], num voo de Zurique para a OOPSLA 1997 — feita test-first. JUnit se tornou o membro fundador da família de frameworks de teste "Xunit". Ver [[wiki/sources/xunit-martin-fowler]].

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

- [[wiki/sources/design-pattern-proxy]]
- [[wiki/sources/xunit-martin-fowler]] — Erich Gamma, coautor do JUnit
- [[wiki/sources/design-pattern-observer-codigo-fonte-tv]] — vídeo cita a definição formal do GoF para o Observer ("dependência um-para-muitos... notificados e atualizados automaticamente")
- [[wiki/sources/testcase-object-xunitpatterns]] — Meszaros cita o **Command** [GOF] explicitamente como o padrão por trás do Testcase Object: cada teste da família xUnit é um objeto Command com método `run` padrão
- [[wiki/sources/command-xunitpatterns]] — verbete de External Patterns dedicado à definição canônica do próprio **Command**, citada diretamente ("encapsulate a request as an object...")
- [[wiki/sources/adapter-xunitpatterns]] — verbete de External Patterns dedicado à definição canônica do **Adapter**, citada diretamente ("convert the interface of a class into another interface clients expect...")
- [[wiki/sources/sete-padroes-de-design-de-software]] — livro de 1994, 23 padrões, base de toda a discussão
- [[wiki/sources/decorator-xunitpatterns]] — xUnitPatterns.com (Meszaros) cita diretamente a definição original do GOF para o [[wiki/concepts/decorator-pattern|Decorator]], como parte da categoria "External Patterns" do site (padrões gerais emprestados de outros catálogos, não específicos de teste)
