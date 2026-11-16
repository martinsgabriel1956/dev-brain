---
type: concept
title: "Escala tipográfica"
aliases: ["escala de texto", "escala de fontes", "escala de tamanho de fonte", "type scale", "tamanho de fonte", "font-size", "modular scale", "escala modular", "escala do Figma"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 2
tags: [ui, ui-design, tipografia, escala-tipografica, font-size, hierarquia-visual, consistencia, design-tokens, style-guide]
skill: ux-ui-mentor
status: stub
---

# Escala tipográfica

Conjunto fechado de tamanhos de fonte que um projeto usa para títulos, subtítulos e corpo, em vez de escolher cada tamanho na hora. É a primeira das variáveis tipográficas: na aula de abertura de [[wiki/concepts/tipografia]], "literalmente escala é o tamanho, é o tamanho do texto", a resposta a "que tamanho eu coloco no título, [...] no subtítulo, [...] no corpo de texto" ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]).

No CSS é o `font-size`; o WhatFont mostra como "size" ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]). É o equivalente textual da [[wiki/concepts/escala-de-espacamento]]: poucos valores, escolhidos de antemão.

## O problema: inconsistência

O erro que [[wiki/entities/nasser|Násser]] diz ver em "muitas interfaces": elementos "da mesma hierarquia" com tamanhos diferentes, e destaques em cores diferentes que não batem com o tamanho. A escala existe para que o mesmo nível tenha sempre o mesmo tamanho ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]). Ver [[wiki/concepts/consistencia-visual]] e [[wiki/concepts/hierarquia-visual]].

A escala é "muito comum [...] em style guides" e responde à dúvida de quem começa, "quais são os tamanhos dos títulos, dos subtítulos" ([[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]).

## Como montar (segundo a aula de escala)

Em [[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]:

- **Partir da [[wiki/concepts/legibilidade-e-leiturabilidade|legibilidade]]:** corpo de texto entre 14 e 21 px como regra geral.
- **Tamanho versus espaço:** muito conteúdo puxa tudo para baixo (NYT: corpo de 14 px); pouco conteúdo permite exagerar (Framer: 106/32 px; Apple: 80/28 px).
- **Desktop e mobile:** uma escala para cada, como no style guide do [[wiki/entities/nubank]] em produção. Ver [[wiki/concepts/design-responsivo]].
- **Até 6 degraus, na prática 4:** espelhando h1–h6 do HTML. Ele usa h1 enorme no hero, h2 de 48, um título de 36, outro de 18 e corpo de 16.
- **Diferenças significativas:** os passos crescem com o tamanho (96 → 144 → 288 na escala do [[wiki/entities/figma]]), porque 144 e 160 lado a lado mal se distinguem. Ver [[wiki/concepts/contraste]].
- **A lista dele:** 14, 16, 18, 24, 36, 48, 52, 64, 72, 84, 96, misturando a escala do Figma com a [[wiki/concepts/grid-de-8-pontos|regra dos 8pt]].

## Escala modular

`[skill: ux-ui-mentor]` A versão sistemática é escolher uma razão e multiplicar em série: 1.125 (Major Second, compacta), 1.25 (Major Third, a mais comum em UI), 1.333 (Perfect Fourth, editorial), 1.5 (Perfect Fifth, display). Ferramentas: typescale.com e utopia.fyi. Para tipografia fluida, `clamp()` (por exemplo `clamp(2rem, 5vw, 4rem)`) e utopia.fyi eliminam breakpoints por tamanho.

A escala da aula não tem razão fixa: é escolhida à mão, como a escala híbrida de espaçamento.

## Aula x skill: o piso do corpo

`[skill: ux-ui-mentor]` Escala mínima de produto: 12 / 14 / 16 (corpo, nunca abaixo) / 18 / 20 / 24 / 30 / 36 / 48 px.

As duas divergem no piso: a aula aceita corpo a partir de 14 px (e cita o corpo de 14 px do NYT), enquanto a skill não desce o corpo abaixo de 16 px ([[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]).

## Olhar de dev

`[skill: ux-ui-mentor]` A escala vira token (`fontSize.sm = 0.875rem`, `fontSize.base = 1rem`...) e o nível do heading (h1–h6) fica separado do estilo visual. `[external]` O MDN desaconselha usar headings para redimensionar texto: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements.

## Key Sources

- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]: escala = tamanho; inconsistência como erro comum; WhatFont
- [[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]: 14–21 px, tamanho vs. espaço, até 6 variações, escala do Figma + 8pt
