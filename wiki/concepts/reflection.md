---
type: concept
title: "Reflection"
aliases: ["reflexão", "introspecção"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 2
tags: [oo, testes, xunit, terminologia, mecanismo-de-linguagem]
skill: tech-mentor-testing
status: stub
---

# Reflection

A capacidade de um programa examinar sua própria estrutura enquanto está em execução ([[wiki/sources/reflection-xunitpatterns]]). É frequentemente usada em ferramentas e frameworks para reduzir o trabalho necessário para adicionar novas funcionalidades — o próprio verbete não detalha mecanismo por linguagem, mantendo a definição no nível conceitual.

## Uso concreto no xUnit: despacho do Testcase Object

O uso mais citado na wiki é o mecanismo interno de [[wiki/concepts/testcase-object|Testcase Object]]: o construtor da Testcase Class recebe o nome do [[wiki/concepts/test-method|Test Method]] a executar e o guarda numa instance variable ([[wiki/concepts/pluggable-behavior|Pluggable (Method) Selector]]); quando o Test Runner chama `run`, o objeto usa reflection para localizar e invocar o método cujo nome está guardado ali. Ver [[wiki/sources/testcase-object-xunitpatterns]] e [[wiki/sources/pluggable-behavior-xunitpatterns]].

## Segundo uso concreto: Test Discovery

[[wiki/sources/test-discovery-xunitpatterns]] cita reflection como o mecanismo genérico por trás de **[[wiki/concepts/test-discovery|Test Discovery]]** em tempo de execução — o Test Automation Framework inspeciona a estrutura de uma classe para descobrir automaticamente quais métodos são [[wiki/concepts/test-method|Test Methods]]. A própria fonte, porém, documenta uma exceção não formalizada explicitamente por ela: a macro `CPPUNIT_TEST_SUITE_REGISTRATION` do [[wiki/entities/cppunit|CppUnit]] resolve a mesma descoberta em **tempo de compilação**, sem reflection em runtime — a fonte chama isso de "compile time knowledge", tratando-o como via secundária ao mecanismo principal.

## Status: stub

Criado a partir de [[wiki/sources/reflection-xunitpatterns]], verbete de glossário curto (definição de uma frase). Já era citado, sem fonte primária própria, em três páginas da wiki antes desta ingestão — esta é a primeira vez que o termo ganha página dedicada.

## Key Sources

- [[wiki/sources/reflection-xunitpatterns]] — fonte primária isolada: definição genérica do termo
- [[wiki/sources/testcase-object-xunitpatterns]] — aplicação concreta: despacho do Test Method via reflection
- [[wiki/sources/pluggable-behavior-xunitpatterns]] — classifica esse uso como Pluggable (Method) Selector, que depende de reflection para resolver o nome em runtime
- [[wiki/sources/test-discovery-xunitpatterns]] — segundo uso concreto: Test Discovery via reflection em runtime, com a exceção do compile-time knowledge (macro do CppUnit)
