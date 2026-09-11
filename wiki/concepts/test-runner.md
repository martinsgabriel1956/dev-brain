---
type: concept
title: "Test Runner"
aliases: ["executor de testes"]
date_created: 2026-09-11
date_updated: 2026-09-11
source_count: 1
tags: [testes, testcase-class, xunit, terminologia]
skill: tech-mentor-testing
status: stub
---

# Test Runner

Componente de [[wiki/concepts/tdd|xUnit]] que consome um [[wiki/concepts/test-suite-object|Test Suite Object]] — montado por uma [[wiki/sources/testcase-class-xunitpatterns|Testcase Class]] atuando como Test Suite Factory — e o executa, rodando cada [[wiki/concepts/testcase-object|Testcase Object]] nele contido. Segundo [[wiki/sources/testcase-class-xunitpatterns]], do ponto de vista de quem escreve testes, "toda a mágica" de descoberta, instanciação e execução acontece aqui e no Testcase Object; escrever [[wiki/concepts/test-method|Test Methods]] é a única responsabilidade do lado humano.

## Status: stub

Conhecido, até esta ingestão, apenas pela descrição de alto nível em [[wiki/sources/testcase-class-xunitpatterns]] — sem fonte primária dedicada ("Test Runner.html" no site, ainda não ingerida), a mecânica interna (como o runner descobre testes, reporta resultados, trata falhas de fixture) não está detalhada na wiki.

## Key Sources

- [[wiki/sources/testcase-class-xunitpatterns]] — única fonte até o momento; situa o Test Runner como consumidor final do Test Suite Object produzido pela Testcase Class
