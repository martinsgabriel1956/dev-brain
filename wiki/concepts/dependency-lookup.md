---
type: concept
title: "Dependency Lookup"
aliases: ["service locator", "busca de dependência"]
date_created: 2026-09-11
date_updated: 2026-09-11
source_count: 2
tags: [testes, test-doubles, dependency-injection, acoplamento, testabilidade]
skill: tech-mentor-testing
status: stub
---

# Dependency Lookup

Um dos mecanismos catalogados por [[wiki/entities/gerard-meszaros]] para tornar uma dependência de um SUT [[wiki/sources/substitutable-dependency-xunitpatterns|substituível]] ([[wiki/sources/substitutable-dependency-xunitpatterns|substitutable dependency]]): em vez de receber a dependência de fora (como em [[wiki/concepts/dependency-injection|Dependency Injection]]), o componente a **busca** através de um registro ou service locator configurável. [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]] situa Dependency Lookup como a opção preferida para **customer tests**, em contraste com Dependency Injection, preferida para **unit tests** — sem detalhar a causa raiz dessa preferência por nível de teste.

## Status: stub

Ainda não há fonte primária dedicada ao mecanismo em si (como funciona o registro/service locator, exemplos de código). Ambas as fontes que citam o termo até agora o fazem só por contraste com Dependency Injection, nunca como objeto central. Candidata a expansão se uma fonte dedicada ao termo for ingerida.

## Key Sources

- [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]] — Dependency Lookup como um dos dois mecanismos de instalação de Test Double conhecidos até então, preferido para customer tests
- [[wiki/sources/substitutable-dependency-xunitpatterns]] — verbete de glossário que nomeia Dependency Lookup como um dos três mecanismos formais para tornar uma dependência substituível, ao lado de [[wiki/concepts/dependency-injection|Dependency Injection]] e [[wiki/concepts/test-specific-subclass|Test-Specific Subclass]]
