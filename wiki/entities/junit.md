---
type: entity
title: "JUnit"
aliases: ["junit"]
date_created: 2026-07-19
date_updated: 2026-08-21
source_count: 2
tags: [testes, tdd, junit, xunit, kent-beck, erich-gamma]
skill: tech-mentor-testing
status: stub
---

# JUnit

Framework de testes unitários para Java, criado por [[wiki/entities/kent-beck]] e [[wiki/entities/gang-of-four|Erich Gamma]] num voo de Zurique para a OOPSLA 1997, programado em par e feito test-first. É o membro fundador da família de frameworks conhecida como "[[wiki/concepts/tdd|Xunit]]" — nome que deriva diretamente dele.

## Origem e impacto

Antes do JUnit, Kent Beck já mantinha frameworks de teste caseiros em Smalltalk (ver [[wiki/entities/c3-project]]), mas eram [[wiki/concepts/seedwork|Seedwork]] — cada time reconstruía o próprio. JUnit foi o primeiro a ganhar tração ampla fora do Smalltalk, e Fowler credita sua simplicidade e adoção pela indústria como fator essencial no crescimento de Extreme Programming e Test-Driven Development. Introduziu o indicador de progresso vermelho/verde ("red bar/green bar"), que se tornou vocabulário padrão em ferramentas de teste.

## Proliferação de ports

Michael Feathers criou o CppUnit (provavelmente o primeiro port para outra linguagem); a partir daí praticamente toda linguagem ganhou um port de JUnit — a família XUnit. NUnit (C#) chegou a influenciar de volta o próprio Java: o uso de atributos no NUnit 2.0 (elogiado por Anders Hejlsberg) antecipou o padrão que o Java adotaria como annotations.

## Ver também

- [[wiki/concepts/tdd]]
- [[wiki/entities/gang-of-four]] — Erich Gamma, coautor do JUnit, também é um dos quatro autores do *Design Patterns*

## Key Sources

- [[wiki/sources/xunit-martin-fowler]]
- [[wiki/sources/seedwork-martin-fowler]] — fonte primária do termo Seedwork usado para descrever o antecessor caseiro do JUnit
