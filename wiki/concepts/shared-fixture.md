---
type: concept
title: "Shared Fixture"
aliases: ["fixture compartilhado", "shared test fixture"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 2
tags: [testes, xunit, test-smell, fixture, terminologia]
skill: tech-mentor-testing
status: stub
---

# Shared Fixture

Padrão (e frequentemente anti-padrão) do catálogo xUnitPatterns.com em que o mesmo [[wiki/concepts/testcase-object|test fixture]] é reutilizado entre múltiplos testes, em vez de cada teste montar o próprio fixture isolado. Pode ser **deliberado** (ex.: fixture caro de montar, compartilhado intencionalmente por performance) ou **implícito/acidental** — o segundo caso é o que [[wiki/sources/there-is-always-an-exception-xunitpatterns]] documenta: ao reutilizar uma única instância da Testcase Class entre todos os [[wiki/concepts/test-method|Test Methods]] (comportamento do [[wiki/entities/nunit|NUnit]] 2.x e do [[wiki/entities/testng]]), qualquer objeto referenciado por uma [[wiki/concepts/instance-variable|instance variable]] passa a ser, sem intenção, compartilhado por todos os testes subsequentes.

## Consequência: Erratic Test

Um Shared Fixture implícito habilita dependência de ordem de execução entre testes — um teste pode alterar estado que outro teste (executado depois) lê ou depende, sem que isso seja visível no código de nenhum dos dois. Essa é uma das causas clássicas de [[wiki/concepts/erratic-test|Erratic Test]]: testes que passam ou falham de forma inconsistente, dependendo de fatores externos ao próprio teste (como a ordem em que os outros testes rodaram).

## Status: stub

Conceito novo, criado a partir de uma única fonte que o cita de passagem (referenciando uma página dedicada "Shared Fixture.html" no catálogo original, ainda não ingerida). A distinção formal entre Shared Fixture deliberado e implícito, bem como as variações do padrão no catálogo (ex.: Chained Tests, Prebuilt Fixture), permanece fora do escopo desta ingestão.

## Key Sources

- [[wiki/sources/there-is-always-an-exception-xunitpatterns]] — única fonte até o momento; documenta o caso implícito/acidental via reutilização de instância no NUnit 2.x
- [[wiki/sources/attribute-xunitpatterns]] — isola o termo "instance variable" (o vetor do vazamento) como um dos dois sentidos do glossário de "attribute"
