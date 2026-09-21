---
type: entity
title: "Fit (Framework for Integrated Test)"
aliases: ["Fit", "Framework for Integrated Test"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 1
tags: [testes, fit, data-driven-test, adapter, customer-test]
skill: tech-mentor-testing
status: stub
---

# Fit (Framework for Integrated Test)

Framework de testes de aceitação/[[wiki/sources/customer-test-xunitpatterns|customer test]] em que casos de teste são expressos como tabelas de dados (ex.: HTML), em vez de código. No vocabulário do catálogo xUnitPatterns.com, o termo "fixture" tem um sentido próprio dentro do Fit, distinto dos outros dois sentidos já documentados na wiki ([[wiki/sources/testcase-class-xunitpatterns|Testcase Class]] em VbUnit/NUnit, e [[wiki/sources/test-fixture-xunitpatterns|test context]] em xUnit genérico): é o **[[wiki/concepts/adapter-pattern|Adapter]]** [GOF] que interpreta a tabela do Fit e invoca métodos no [[wiki/sources/sut-xunitpatterns|SUT]], implementando um **[[wiki/concepts/data-driven-test|Data-Driven Test]]**.

Ainda sem fonte primária isolada dedicada ao próprio Fit (o catálogo cita o framework apenas de passagem, dentro de verbetes sobre outros termos) — página `FIT.html` do site ainda não ingerida.

## Ver também

- [[wiki/concepts/adapter-pattern]]
- [[wiki/concepts/data-driven-test]]

## Key Sources

- [[wiki/sources/test-fixture-fit-xunitpatterns]] — verbete de glossário dedicado ao sentido de "fixture" dentro do Fit: Adapter que interpreta a tabela e invoca o SUT, implementando um Data-Driven Test
- [[wiki/sources/testcase-class-xunitpatterns]] — cita o Fit de passagem, na seção "Further Reading", ao distinguir os três sentidos de "fixture"
