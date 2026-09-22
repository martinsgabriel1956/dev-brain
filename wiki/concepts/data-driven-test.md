---
type: concept
title: "Data-Driven Test"
aliases: ["teste dirigido por dados", "data driven test"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 2
tags: [testes, fit, data-driven-test, adapter, interpreter]
skill: tech-mentor-testing
status: stub
---

# Data-Driven Test

Teste cujo comportamento — os casos exercitados e os resultados esperados — é definido por uma fonte de dados externa (uma tabela, uma planilha, um arquivo), em vez de codificado à mão em cada asserção. O exemplo canônico citado pelo catálogo xUnitPatterns.com é o **[[wiki/entities/fit|Fit]]**: a tabela do Fit descreve os casos, e um **[[wiki/concepts/adapter-pattern|Adapter]]** [GOF] (chamado de "fixture" no vocabulário do Fit) interpreta essa tabela e invoca métodos no [[wiki/sources/sut-xunitpatterns|SUT]] — um [[wiki/concepts/adapter-pattern|Adapter]] atuando também como **Interpreter** [GOF] no sentido de "tabela/dados dirigindo o teste".

Vantagem prática: adicionar um novo caso de teste vira uma linha de dados, não uma nova função de teste — útil quando quem define os casos (ex.: um analista de negócio) não escreve código.

## Ver também

- [[wiki/entities/fit]]
- [[wiki/concepts/adapter-pattern]]
- [[wiki/sources/sut-xunitpatterns]]

## Key Sources

- [[wiki/sources/test-fixture-fit-xunitpatterns]] — verbete de glossário que define o fixture do Fit como o Adapter que implementa um Data-Driven Test
- [[wiki/sources/testcase-class-xunitpatterns]] — cita o termo de passagem, junto de Fit e Interpreter [GOF], na seção "Further Reading"
