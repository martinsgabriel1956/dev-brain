---
type: concept
title: "Test Runner"
aliases: ["executor de testes"]
date_created: 2026-09-11
date_updated: 2026-09-21
source_count: 3
tags: [testes, testcase-class, xunit, terminologia]
skill: tech-mentor-testing
status: stub
---

# Test Runner

Componente de [[wiki/concepts/tdd|xUnit]] que consome um [[wiki/concepts/test-suite-object|Test Suite Object]] — montado por uma [[wiki/sources/testcase-class-xunitpatterns|Testcase Class]] atuando como Test Suite Factory — e o executa, rodando cada [[wiki/concepts/testcase-object|Testcase Object]] nele contido. Segundo [[wiki/sources/testcase-class-xunitpatterns]], do ponto de vista de quem escreve testes, "toda a mágica" de descoberta, instanciação e execução acontece aqui e no Testcase Object; escrever [[wiki/concepts/test-method|Test Methods]] é a única responsabilidade do lado humano.

## Como o Test Runner "sabe" quais testes rodar

[[wiki/sources/test-discovery-xunitpatterns]], fonte primária dedicada, fecha a lacuna deixada em aberto acima: o mecanismo se chama **[[wiki/concepts/test-discovery|Test Discovery]]** — o Test Automation Framework usa [[wiki/concepts/reflection|reflection]] em runtime (ou conhecimento em tempo de compilação) para descobrir automaticamente Test Methods e Test Suite Objects, sem que o Test Runner precise de um registro manual. A alternativa manual, **[[wiki/concepts/test-enumeration|Test Enumeration]]**, só é recomendada quando o framework não suporta Discovery ou quando se precisa de uma Named Test Suite com subconjunto de testes escolhido a dedo.

## Graphical Test Runner e Test Tree Explorer

[[wiki/sources/testcase-object-xunitpatterns]] traz o primeiro exemplo visual da wiki de um **Graphical Test Runner**: o do [[wiki/entities/junit]] embutido no Eclipse, que permite ao usuário "descer" (drill down) na árvore de testes — o **Test Tree Explorer** — para inspecionar os Testcase Objects individuais dentro de um Test Suite Object. A fonte confirma que essa capacidade de inspeção/manipulação em tempo real é justamente o motivo pelo qual o Test Runner precisa tratar testes como objetos (Testcase Object como Command [GOF]), e não como procedimentos: um Test Runner gráfico precisa poder navegar e selecionar testes individuais na árvore, o que exige que cada teste seja um objeto manipulável.

## Status: stub

Conhecido, até esta ingestão, apenas pela descrição de alto nível em [[wiki/sources/testcase-class-xunitpatterns]] e pelo exemplo do Graphical Test Runner do Eclipse acima — sem fonte primária dedicada ("Test Runner.html" no site, ainda não ingerida), a mecânica interna (como o runner descobre testes, reporta resultados, trata falhas de fixture) não está detalhada na wiki.

## Key Sources

- [[wiki/sources/testcase-class-xunitpatterns]] — situa o Test Runner como consumidor final do Test Suite Object produzido pela Testcase Class
- [[wiki/sources/testcase-object-xunitpatterns]] — exemplo concreto do Graphical Test Runner do JUnit no Eclipse; Test Tree Explorer
- [[wiki/sources/test-discovery-xunitpatterns]] — **fonte primária dedicada** ao mecanismo pelo qual o Test Runner descobre os testes a executar (Test Discovery vs. Test Enumeration)
