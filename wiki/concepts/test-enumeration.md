---
type: concept
title: "Test Enumeration"
aliases: ["enumeração de testes", "test method enumeration", "test suite enumeration"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 1
tags: [testes, testcase-class, test-runner, xunit, terminologia]
skill: tech-mentor-testing
status: stub
---

# Test Enumeration

Técnica manual de registrar explicitamente, no código, quais [[wiki/concepts/test-method|Test Methods]] pertencem a um [[wiki/concepts/test-suite-object|Test Suite Object]] (**Test Method Enumeration**) e/ou quais Test Suite Objects compõem uma **Suite of Suites** (**Test Suite Enumeration**) — o oposto manual de **[[wiki/concepts/test-discovery|Test Discovery]]**. Segundo [[wiki/sources/test-discovery-xunitpatterns]], deve ser usada apenas em dois cenários: o framework não suporta Test Discovery, ou o time precisa montar uma **Named Test Suite** com um subconjunto de testes escolhidos a dedo de várias suítes (ex.: uma suíte de *Smoke Test*) e o framework não suporta **Test Selection**.

## Exemplo motivador (o que Test Discovery elimina)

O exemplo canônico citado é uma função `suite()` de [[wiki/entities/cppunit|CppUnit]] (versão antiga) que constrói manualmente um `CppUnit::TestSuite`, adicionando cada `Test Method` um por um via `addTest(new CppUnit::TestCaller<...>(...))`. É exatamente esse código repetitivo que Test Discovery — via reflection ou compile-time knowledge — torna desnecessário.

## Combinação comum: Suite Enumeration manual + Method Discovery automático

A fonte nota que é comum combinar Test *Suite* Enumeration (decidir manualmente quais suítes compõem a Suite of Suites) com Test *Method* Discovery (descoberta automática dos métodos dentro de cada suíte); o inverso — enumerar métodos manualmente dentro de uma suíte descoberta automaticamente — é raro.

## Status: stub

Citada extensivamente por contraste em [[wiki/sources/test-discovery-xunitpatterns]], [[wiki/concepts/test-suite-object]] e [[wiki/concepts/testcase-object]], mas ainda sem verbete de glossário primário dedicado (`Test Enumeration.html`) ingerido — a página também definiria formalmente **Test Suite Factory**, termo cujo link no site original aponta para essa mesma página ainda não lida.

## Key Sources

- [[wiki/sources/test-discovery-xunitpatterns]] — cita Test Enumeration extensivamente por contraste com Test Discovery; único gatilho de quando usá-la; exemplo motivador em CppUnit
- [[wiki/concepts/test-suite-object]] — nomeia Test Enumeration como um dos dois mecanismos de criação, antes desta ingestão
- [[wiki/concepts/testcase-object]] — mesma citação de passagem, do lado do Testcase Object
