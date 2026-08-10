---
type: concept
title: "Liskov Substitution Principle (LSP)"
aliases: ["LSP", "liskov", "substituição de liskov"]
date_created: 2026-05-01
date_updated: 2026-08-06
source_count: 3
tags: [solid, oop, architecture]
skill: tech-mentor-backend
status: stub
---

## Definição

Objetos de uma subclasse (ou implementação de interface) devem poder substituir objetos da classe base sem quebrar o comportamento esperado.

## Relação com Proxy

O [[proxy-pattern]] depende do LSP: tanto o proxy quanto a classe real implementam a mesma interface. O código cliente (Controller) pode receber qualquer um dos dois sem saber a diferença — e o comportamento esperado é preservado.

## Exemplo — Ave, Pica-pau e Pinguim

Via [[wiki/sources/principios-solid-ilustrados]]: uma classe `Ave` implementa `bicar()` e `voar()`. A subclasse `PicaPau` herda ambos sem problema. Já `Pinguim` quebra o princípio — `voar()` lançaria exceção. Sinal prático: se toda subclasse nova exige lançar exceção ou "lutar" contra o que herdou, a abstração da classe base está no nível errado, e insistir nela tem efeito destrutivo na evolução do sistema. O princípio empurra a pensar no que a base deveria realmente fornecer em comum para todas as subclasses — o que por sua vez ajuda a respeitar [[wiki/concepts/open-closed-principle|OCP]] ao programar contra interfaces.

## Definição Formal (Fonte Primária) e Exemplo Coffee/Cappuccino/Water

Via [[wiki/sources/solid-principles-in-pictures-ugonna-thelma]]: "se S é subtipo de T, objetos do tipo T podem ser substituídos por objetos do tipo S." A autora dá um exemplo textual mais preciso que a ilustração de café descrita de segunda mão em [[wiki/sources/principios-solid-ilustrados]]: se a classe pai retorna `Coffee`, uma subclasse pode retornar `Cappuccino` (subtipo compatível), mas não `Water` (tipo não relacionado) — o critério de substituição é sobre compatibilidade de tipo de retorno, não apenas "a subclasse consegue fazer algo parecido".

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[wiki/sources/principios-solid-ilustrados]]
- [[wiki/sources/solid-principles-in-pictures-ugonna-thelma]]
