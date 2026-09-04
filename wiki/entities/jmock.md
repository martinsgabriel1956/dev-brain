---
type: entity
title: "JMock"
aliases: ["jmock"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_count: 2
tags: [testes, test-doubles, mock, java, ferramentas]
skill: tech-mentor-testing
status: stub
---

# JMock

Framework dinâmico de **[[wiki/concepts/test-doubles|Mock Object]]** para testes em Java. Catalogado no xUnitPatterns.com como ferramenta que implementa o padrão Mock Object, com destaque para sua **Configuration Interface** fluente — API de especificação de expectativas via method chaining — como diferencial de legibilidade. Ver [[wiki/sources/jmock]].

## Configuration Interface como Configurable Test Double gerado dinamicamente

O elogio de [[wiki/entities/gerard-meszaros]] ao JMock não é genérico ("é um framework de mock") — é específico à API fluente de configuração de expectativas. Isso o torna o exemplo concreto do lado **Configurable** da dualidade Hard-Coded vs. Configurable Test Double registrada em [[wiki/concepts/test-doubles]] — mas, dentro do próprio lado Configurable, o JMock representa especificamente a técnica **gerada dinamicamente** (via reflexão/proxy em runtime), em contraste com um **Hand-Built Test Double** (classe configurável escrita à mão pelo desenvolvedor — ver [[wiki/entities/sven-gorts]] e [[wiki/sources/utwhcm-xunitpatterns]]). [[wiki/sources/test-stub-xunitpatterns-meszaros]] já citava esse padrão de forma genérica ("muitas vezes gerado por reflexão/proxy dinâmico como no exemplo com JMock") antes de existir uma fonte primária dedicada ao JMock nesta wiki.

## Ligação histórica com a escola London/Mockist [external]

Não confirmado pela fonte primária ingerida (o verbete do xUnitPatterns.com é deliberadamente curto e não cita autoria), mas é fato externo bem estabelecido: o JMock foi criado por **Steve Freeman**, **Nat Pryce** e **Joe Walnes**, e Freeman/Pryce são também os autores de *Growing Object-Oriented Software, Guided by Tests* (2009) — o livro que formaliza a escola **London/Mockist** de TDD (ver [[wiki/concepts/tdd]] e [[wiki/concepts/unit-test-solitario-vs-sociavel]]). O JMock é, historicamente, uma das ferramentas de origem dessa escola — não apenas um exemplo posterior dela.

## Ver também

- [[wiki/concepts/test-doubles]] — taxonomia geral de Test Doubles; JMock implementa o tipo Mock via Configuration Interface
- [[wiki/concepts/tdd]] — escola London/Mockist associada historicamente ao JMock [external]
- [[wiki/entities/gerard-meszaros]] — autor do verbete que cataloga o JMock

## Key Sources

- [[wiki/sources/jmock]] — verbete de "Tools" do xUnitPatterns.com (Meszaros) que descreve o JMock e sua Configuration Interface fluente
- [[wiki/sources/utwhcm-xunitpatterns]] — verbete de "References" do mesmo site que revela a distinção Hand-Built vs. Dinamicamente Gerado, contextualizando o JMock como exemplo do segundo
