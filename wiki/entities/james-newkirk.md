---
type: entity
title: "James Newkirk"
aliases: ["Newkirk"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 1
tags: [testes, nunit, xunit, dotnet]
skill: tech-mentor-testing
status: stub
---

# James Newkirk

Um dos autores do [[wiki/entities/nunit|NUnit]] 2.0. Citado em [[wiki/sources/there-is-always-an-exception-xunitpatterns]] admitindo publicamente que a decisão de reutilizar uma única instância da Testcase Class entre todos os [[wiki/concepts/test-method|Test Methods]] (em vez de instanciar uma nova a cada método, como o [[wiki/entities/junit|JUnit]] faz) foi um erro de design — ele não havia entendido, à época, o raciocínio por trás do "JUnit New Instance Behavior", e reconhece que a reutilização cria um [[wiki/concepts/shared-fixture|Shared Fixture]] implícito, fonte de dependência de ordem de execução entre testes.

## Status: stub

Conhecido, até esta ingestão, apenas por essa citação única em xUnitPatterns.com. Sem página dedicada na wiki para biografia ou outros trabalhos.

## Key Sources

- [[wiki/sources/there-is-always-an-exception-xunitpatterns]] — única fonte até o momento; citação direta admitindo o erro de design do NUnit 2.0
