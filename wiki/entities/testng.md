---
type: entity
title: "TestNG"
aliases: ["testng"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 1
tags: [testes, xunit, java, test-fixture]
skill: tech-mentor-testing
status: stub
---

# TestNG

Framework de testes para Java, inspirado em anotações no estilo JUnit/NUnit, mas com modelo de execução diferente do JUnit em pelo menos um ponto documentado na wiki.

## A exceção da instanciação por Test Method

Segundo [[wiki/sources/there-is-always-an-exception-xunitpatterns]], o TestNG é um dos dois únicos membros conhecidos da família [[wiki/concepts/tdd|xUnit]] (o outro é o [[wiki/entities/nunit]] 2.x) que **não** cria um [[wiki/concepts/testcase-object|Testcase Object]] separado por [[wiki/concepts/test-method|Test Method]] — rompendo a regra de design considerada fundamental para alcançar "Independent Test" na família xUnit. A fonte não detalha a mecânica interna do TestNG (diferente do que faz para o NUnit, via citação de James Newkirk); apenas nomeia o framework como a outra exceção conhecida pelo autor.

## Status: stub

Conhecido até esta ingestão apenas por essa menção única. Sem página dedicada cobrindo sintaxe, grupos de teste, ou o restante do modelo de execução do framework.

## Key Sources

- [[wiki/sources/there-is-always-an-exception-xunitpatterns]] — única fonte até o momento
