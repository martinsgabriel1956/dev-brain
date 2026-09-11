---
type: concept
title: "Test Suite Object"
aliases: ["objeto de suíte de teste"]
date_created: 2026-09-11
date_updated: 2026-09-11
source_count: 1
tags: [testes, testcase-class, xunit, terminologia]
skill: tech-mentor-testing
status: stub
---

# Test Suite Object

Coleção que agrupa todos os [[wiki/concepts/testcase-object|Testcase Objects]] produzidos por uma [[wiki/sources/testcase-class-xunitpatterns|Testcase Class]] atuando como Test Suite Factory — um Testcase Object por [[wiki/concepts/test-method|Test Method]]. É o objeto que o [[wiki/concepts/test-runner|Test Runner]] efetivamente consome e executa; nem a Testcase Class nem os Test Methods individuais são executados diretamente pelo runner.

## Status: stub

Conhecido, até esta ingestão, apenas pela descrição de alto nível em [[wiki/sources/testcase-class-xunitpatterns]]. O rodapé do site lista subtemas relacionados ainda não ingeridos ("Test Discovery", "Test Enumeration", "Test Selection") que provavelmente detalham como o Test Suite Object é montado e filtrado antes de chegar ao Test Runner.

## Key Sources

- [[wiki/sources/testcase-class-xunitpatterns]] — única fonte até o momento; situa o Test Suite Object como o produto intermediário entre a Testcase Class (fábrica) e o Test Runner (executor)
