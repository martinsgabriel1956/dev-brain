---
type: concept
title: "Escala tipográfica"
aliases: ["escala de texto", "type scale", "tamanho de fonte", "font-size", "modular scale"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, tipografia, escala-tipografica, font-size, hierarquia-visual, consistencia, design-tokens]
skill: ux-ui-mentor
status: stub
---

# Escala tipográfica

A primeira das variáveis tipográficas. Na aula de abertura de [[wiki/concepts/tipografia]], "literalmente escala é o tamanho, é o tamanho do texto": a resposta a "que tamanho eu coloco no título, [...] no subtítulo, [...] no corpo de texto" ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]).

## O problema: inconsistência

O erro que [[wiki/entities/nasser|Násser]] diz ver em "muitas interfaces": elementos "da mesma hierarquia" com tamanhos diferentes, e destaques em cores diferentes que não batem com o tamanho. A escala existe para que o mesmo nível tenha sempre o mesmo tamanho. Ver [[wiki/concepts/consistencia-visual]] e [[wiki/concepts/hierarquia-visual]].

No CSS é o `font-size`; o WhatFont mostra como "size".

## Escala modular

`[skill: ux-ui-mentor]` Escolhe-se uma razão e aplica-se em série: 1.125 (Major Second, compacto), 1.250 (Major Third, a mais comum em UI), 1.333 (Perfect Fourth, editorial), 1.5 (Perfect Fifth, display). Escala mínima de produto: 12 / 14 / 16 (corpo, nunca abaixo) / 18 / 20 / 24 / 30 / 36 / 48 px, como tokens (`fontSize.base = 1rem`). Tamanho fluido com `clamp(2rem, 5vw, 4rem)`. Ferramentas: typescale.com e utopia.fyi.

Mesma lógica da [[wiki/concepts/escala-de-espacamento]]: poucos valores, escolhidos de antemão.

## Key Sources

- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]: escala = tamanho; inconsistência como erro comum; WhatFont
