---
type: concept
title: "Testcase Object"
aliases: ["objeto de caso de teste"]
date_created: 2026-09-11
date_updated: 2026-09-11
source_count: 1
tags: [testes, testcase-class, xunit, terminologia]
skill: tech-mentor-testing
status: stub
---

# Testcase Object

Instância de uma [[wiki/sources/testcase-class-xunitpatterns|Testcase Class]], criada em tempo de execução — uma para cada [[wiki/concepts/test-method|Test Method]]. É o mecanismo concreto por trás da reclassificação já registrada em [[wiki/sources/test-case-xunitpatterns]] de que a Testcase Class "é na verdade" uma **Test Suite Factory**: ao instanciar-se uma vez por Test Method, a fábrica produz um Testcase Object por método, e todos eles são agrupados num [[wiki/concepts/test-suite-object|Test Suite Object]] que o [[wiki/concepts/test-runner|Test Runner]] executa.

## Status: stub

Conhecido, até esta ingestão, apenas pela descrição de alto nível em [[wiki/sources/testcase-class-xunitpatterns]] ("How It Works"). A própria fonte remete a uma página dedicada ("Testcase Object", ainda não ingerida) para a "verdadeira mágica" — detalhes de como a instanciação e a associação a um único Test Method funcionam internamente permanecem fora do escopo desta fonte.

## Key Sources

- [[wiki/sources/testcase-class-xunitpatterns]] — única fonte até o momento; descreve o Testcase Object como o produto da Testcase Class atuando como Test Suite Factory, um por Test Method
