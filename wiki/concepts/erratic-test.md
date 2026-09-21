---
type: concept
title: "Erratic Test"
aliases: ["teste errático", "flaky test (xunitpatterns)"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 2
tags: [testes, xunit, test-smell, terminologia]
skill: tech-mentor-testing
status: stub
---

# Erratic Test

Test smell do catálogo xUnitPatterns.com: uma família de testes que passam ou falham de forma inconsistente, sem relação direta com mudanças no código sob teste — geralmente causados por fatores externos ao teste em si, como estado compartilhado entre testes, dependência de ordem de execução, ou dependência de recursos externos não controlados (rede, relógio, filesystem).

## Relação com Production Bugs

[[wiki/sources/production-bugs-xunitpatterns]] cita **Chained Tests** — uma forma deliberada de *Interacting Tests* (uma das variações de Erratic Test) — como o que dificulta isolar e rodar um único teste ao tentar contornar um [[wiki/concepts/production-bugs|Lost Test]]. Também cita *Unrepeatable Test* (outra variação) como causa raiz de **Infrequently Run Tests**, resolvida ao trocar para uma estratégia de Fresh Fixture.

## Causa documentada: Shared Fixture implícito

[[wiki/sources/there-is-always-an-exception-xunitpatterns]] cita Erratic Test como consequência direta de um [[wiki/concepts/shared-fixture|Shared Fixture]] implícito: quando o [[wiki/entities/nunit|NUnit]] 2.x reutiliza a mesma instância de Testcase Class entre [[wiki/concepts/test-method|Test Methods]], variáveis de instância acabam compartilhadas entre testes sem intenção — um teste pode deixar estado que afeta o resultado de outro, dependendo da ordem de execução.

## Status: stub

Conceito novo, criado a partir de uma única fonte que o cita de passagem (referenciando uma página dedicada "Erratic Test.html" no catálogo original, ainda não ingerida). A taxonomia completa de variações de Erratic Test do livro de Meszaros (ex.: Interacting Tests, Test Run Wars, Unrepeatable Test, Lonely Test) permanece fora do escopo desta ingestão.

## Key Sources

- [[wiki/sources/there-is-always-an-exception-xunitpatterns]] — documenta uma causa específica (Shared Fixture implícito por reuso de instância) via NUnit 2.x
- [[wiki/sources/production-bugs-xunitpatterns]] — cita Chained Tests/Interacting Tests e Unrepeatable Test como variações que se cruzam com Production Bugs
