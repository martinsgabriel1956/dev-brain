---
type: concept
title: "Extract Interface"
aliases: ["extrair interface"]
date_created: 2026-09-11
date_updated: 2026-09-11
source_count: 2
tags: [refactoring, testes, test-doubles, dependency-injection, interface]
skill: tech-mentor-testing
status: stub
---

# Extract Interface

Refatoração catalogada por [[wiki/entities/martin-fowler|Fowler]] (*Refactoring: Improving the Design of Existing Software*): quando vários clientes usam apenas um subconjunto da interface de uma classe, ou duas classes compartilham parte de sua interface, extrai-se esse subconjunto para uma interface própria. É uma refatoração estrutural de **tipos**, não de comportamento — nada muda no que o sistema faz, só o vocabulário de tipos que os clientes enxergam.

## Papel em testes: pré-requisito para Test Doubles em linguagens estaticamente tipadas

Fonte primária: [[wiki/sources/extract-interface-xunitpatterns]]. Em linguagens com tipagem estática, uma variável tipada pela **classe concreta** de uma dependência real não aceita um [[wiki/concepts/test-doubles|Test Double]] no lugar — mesmo que o double implemente toda a API relevante, ele não *é* aquela classe aos olhos do compilador. Extrair uma interface que cobre a API usada pelo SUT, e retipar a variável para essa interface, faz com que tanto a implementação real quanto o double satisfaçam o mesmo tipo declarado — viabilizando a substituição sem alterar o SUT além da declaração de tipo. É o mecanismo concreto por trás da propriedade **substitutable dependency** (ver [[wiki/sources/substitutable-dependency-xunitpatterns]]) quando o mecanismo de instalação é [[wiki/concepts/dependency-injection|Dependency Injection]]. Citada de passagem, antes desta fonte dedicada, em [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]] e em [[wiki/concepts/test-doubles]].

## Status: stub

Fonte disponível é minimalista (problema + solução em uma frase cada, sem mecânica passo a passo) — a própria página original se declara desatualizada em relação ao capítulo publicado do livro de Fowler. Candidata a expansão se uma fonte mais detalhada (o capítulo do livro, ou um exemplo de código) for ingerida.

## Key Sources

- [[wiki/sources/extract-interface-xunitpatterns]] — verbete de "Code Refactorings" do xUnitPatterns.com, conteúdo atribuído a Fowler: definição formal do problema e da solução
- [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]] — cita a refatoração de passagem, como pré-requisito em linguagens estaticamente tipadas
