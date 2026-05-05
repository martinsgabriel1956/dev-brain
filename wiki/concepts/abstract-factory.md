---
type: concept
title: "Abstract Factory Pattern"
aliases: ["abstract factory", "fábrica abstrata"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [design-patterns, creational, abstract-factory, gof]
skill: tech-mentor-backend
status: stub
---

# Abstract Factory Pattern

Padrão [[creational-patterns|criacional]] que fornece uma interface para criar **famílias de objetos relacionados** sem especificar suas classes concretas.

## Distinção do Factory Method

- **[[factory-pattern|Factory Method]]** — cria um tipo de objeto, subclasses decidem qual
- **Abstract Factory** — cria *famílias* de objetos relacionados (ex: botão + checkbox + scrollbar para Windows OU para Mac)

## Relação com Facade

Abstract Factory pode servir como alternativa ao [[facade-pattern]] quando a preocupação principal é esconder do cliente *como* os objetos do subsistema são criados — não apenas simplificar o acesso a eles.

## Quando usar

- Quando o sistema precisa ser independente de como seus produtos são criados
- Quando você quer garantir que produtos de uma família sejam usados juntos
- Exemplos: UI cross-platform, drivers de banco de dados, temas visuais

## Key Sources

- [[sources/design-pattern-facade]] — mencionado nas relações com outros padrões
