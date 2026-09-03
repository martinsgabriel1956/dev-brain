---
type: entity
title: "JUnit"
aliases: ["junit"]
date_created: 2026-07-19
date_updated: 2026-08-31
source_count: 5
tags: [testes, tdd, junit, xunit, kent-beck, erich-gamma, test-fixture]
skill: tech-mentor-testing
status: stub
---

# JUnit

Framework de testes unitários para Java, criado por [[wiki/entities/kent-beck]] e [[wiki/entities/gang-of-four|Erich Gamma]] num voo de Zurique para a OOPSLA 1997, programado em par e feito test-first. É o membro fundador da família de frameworks conhecida como "[[wiki/concepts/tdd|Xunit]]" — nome que deriva diretamente dele. O verbete de glossário [[wiki/sources/xunit-xunitpatterns]] define formalmente "xUnit" como qualquer framework baseado no padrão do **JUnit ou SUnit** — cita [[wiki/entities/sunit|SUnit]], o framework caseiro de Beck em Smalltalk, como o segundo ancestral de referência, ao lado do próprio JUnit.

## Origem e impacto

Antes do JUnit, Kent Beck já mantinha frameworks de teste caseiros em Smalltalk (ver [[wiki/entities/c3-project]]), mas eram [[wiki/concepts/seedwork|Seedwork]] — cada time reconstruía o próprio. JUnit foi o primeiro a ganhar tração ampla fora do Smalltalk, e Fowler credita sua simplicidade e adoção pela indústria como fator essencial no crescimento de Extreme Programming e Test-Driven Development. Introduziu o indicador de progresso vermelho/verde ("red bar/green bar"), que se tornou vocabulário padrão em ferramentas de teste.

## Test context separado da Testcase Class

O verbete de glossário dedicado ao termo [[wiki/sources/test-fixture-xunitpatterns|test fixture]] cita JUnit nominalmente como exemplo de variante de xUnit que mantém o **test context** (o [[wiki/concepts/indirect-input-output|test fixture]]) conceitualmente separado da **Testcase Class** que o cria — "JUnit and its direct ports fall into this camp". Isso reforça a reclassificação já registrada em [[wiki/sources/test-case-xunitpatterns]]: a Testcase Class "é na verdade" uma **Test Suite Factory**, e o test fixture é o produto dessa fábrica a cada execução de teste, não um atributo fixo embutido na própria classe. A fonte não nomeia quais variantes de xUnit ficam fora desse grupo (fundindo os dois conceitos num único objeto persistente).

## Proliferação de ports

Michael Feathers criou o CppUnit (provavelmente o primeiro port para outra linguagem); a partir daí praticamente toda linguagem ganhou um port de JUnit — a família XUnit. NUnit (C#) chegou a influenciar de volta o próprio Java: o uso de atributos no NUnit 2.0 (elogiado por Anders Hejlsberg) antecipou o padrão que o Java adotaria como annotations.

## Ver também

- [[wiki/concepts/tdd]]
- [[wiki/entities/gang-of-four]] — Erich Gamma, coautor do JUnit, também é um dos quatro autores do *Design Patterns*

## Key Sources

- [[wiki/sources/xunit-martin-fowler]]
- [[wiki/sources/xunit-xunitpatterns]] — verbete de glossário que define formalmente "xUnit" e nomeia SUnit como o segundo framework de referência da família
- [[wiki/sources/seedwork-martin-fowler]] — fonte primária do termo Seedwork usado para descrever o antecessor caseiro do JUnit
- [[wiki/sources/c3-martin-fowler]] — linha do tempo do C3 (1993-1999), projeto onde o antecessor do JUnit foi usado
- [[wiki/sources/test-fixture-xunitpatterns]] — verbete de glossário dedicado ao termo test fixture/test context: cita JUnit e seus ports diretos como exemplo de variante de xUnit que mantém o test context separado da Testcase Class que o cria
