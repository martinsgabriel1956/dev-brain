---
type: concept
title: "Test-Specific Subclass"
aliases: ["subclasse específica para teste"]
date_created: 2026-09-11
date_updated: 2026-09-11
source_count: 1
tags: [testes, test-doubles, testabilidade]
skill: tech-mentor-testing
status: stub
---

# Test-Specific Subclass

Um dos três mecanismos catalogados por [[wiki/entities/gerard-meszaros]] para tornar uma dependência de um SUT [[wiki/sources/substitutable-dependency-xunitpatterns|substituível]], ao lado de [[wiki/concepts/dependency-injection|Dependency Injection]] e [[wiki/concepts/dependency-lookup|Dependency Lookup]]. Em vez de injetar ou buscar a dependência externamente, uma subclasse usada apenas em teste sobrescreve o ponto do SUT onde a dependência real seria criada ou obtida, substituindo-a por um [[wiki/concepts/test-doubles|Test Double]] sem exigir um mecanismo de injeção/lookup externo.

## Status: stub

Conhecido, até esta ingestão, só pela menção nomeada em [[wiki/sources/substitutable-dependency-xunitpatterns]] — nenhuma fonte já ingerida detalha a mecânica (qual método é sobrescrito, se exige um construtor de teste dedicado) ou dá exemplo de código. Nem [[wiki/sources/test-double-xunitpatterns-meszaros]] nem [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]] — as duas fontes mais próximas do tema já ingeridas — nomeiam esse terceiro mecanismo, apesar de citarem "substitutable dependency" de passagem.

## Key Sources

- [[wiki/sources/substitutable-dependency-xunitpatterns]] — única fonte que nomeia o mecanismo até o momento, como um dos três listados no verbete de glossário "substitutable dependency"
