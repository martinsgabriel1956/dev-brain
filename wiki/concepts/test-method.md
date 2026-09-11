---
type: concept
title: "Test Method"
aliases: ["método de teste"]
date_created: 2026-09-11
date_updated: 2026-09-11
source_count: 1
tags: [testes, testcase-class, xunit, terminologia]
skill: tech-mentor-testing
status: stub
---

# Test Method

Unidade elementar de lógica de teste em [[wiki/concepts/tdd|xUnit]]: um método que implementa um único [[wiki/sources/test-case-xunitpatterns|test case]]. Precisa estar associado a uma classe em linguagens orientadas a objetos — é exatamente esse o papel da [[wiki/sources/testcase-class-xunitpatterns|Testcase Class]], que agrupa um conjunto de Test Methods relacionados. Em tempo de execução, cada Test Method vira um [[wiki/concepts/testcase-object|Testcase Object]] separado, instanciando a Testcase Class uma vez por método — o que permite manipular Test Methods individualmente (selecioná-los, pular, reordenar) em vez de tratá-los como um bloco monolítico.

## Status: stub

Citado por nome em quase todas as fontes já ingeridas do cluster xUnitPatterns.com ([[wiki/sources/test-case-xunitpatterns]], [[wiki/sources/test-fixture-xunitpatterns]], [[wiki/sources/annotation-xunitpatterns]]), mas até [[wiki/sources/testcase-class-xunitpatterns]] nenhuma fonte tratava o termo como assunto central — apenas de passagem. Sem página primária dedicada ("Test Method.html" no site), a mecânica de como um Test Method vira Testcase Object fica limitada ao que [[wiki/sources/testcase-class-xunitpatterns]] descreve a partir da perspectiva da Testcase Class.

## Key Sources

- [[wiki/sources/testcase-class-xunitpatterns]] — descreve, pela primeira vez de forma central, como Test Methods são agrupados numa Testcase Class e transformados em Testcase Objects em tempo de execução
- [[wiki/sources/test-case-xunitpatterns]] — cita Test Method como o que a Testcase Class agrupa
- [[wiki/sources/annotation-xunitpatterns]] — cita Test Method como uma das duas coisas que JUnit 4.0 marca via annotation (a outra é a própria Testcase Class)
