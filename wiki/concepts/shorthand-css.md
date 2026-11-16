---
type: concept
title: "Shorthand CSS (propriedades que resumem outras)"
aliases: ["propriedade shorthand", "shorthand properties", "propriedade resumo", "TRBL", "top right bottom left"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 7
tags: [css, sintaxe, box-model, padding, margin, border, background]
skill: tech-mentor-frontend
status: stub
---

# Shorthand CSS (propriedades que resumem outras)

Uma propriedade que define várias outras de uma vez: `padding` resume `padding-top/-right/-bottom/-left`; `margin` idem; `border` resume `border-width`, `border-style` e `border-color`; `background` resume `background-color`, `-image`, `-repeat`, `-position`, `-attachment` ([[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]]).

## Ordem dos valores: sentido horário

Com quatro valores, a ordem é **top, right, bottom, left**: "sempre começa no top e aí gira no sentido horário", e a regra vale para "um monte" de propriedades (padding, margin, border-radius). Um valor só vale para os quatro lados. `border: 5px solid red` dá o mesmo efeito que as propriedades separadas ([[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]]).

`[external]` Com dois valores: vertical, horizontal; com três: top, horizontal, bottom (https://developer.mozilla.org/en-US/docs/Web/CSS/Shorthand_properties). No `border-radius` a ordem começa no canto superior esquerdo e também gira no sentido horário. Cuidado: um shorthand redefine as sub-propriedades omitidas para o valor inicial (`background: red` zera um `background-image` declarado antes).

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] chama de shorthand o `background` (url + no-repeat), a `margin` (um, dois, três ou quatro valores, estes "de uma maneira de relógio": top, right, bottom, left) e o `border-radius` (com dois valores, alterna a partir do canto superior esquerdo).

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], o shorthand de padding e margin vai em "sentido horário" ("meio-dia, 3, 6, 9"); um valor vale para os quatro lados, dois para vertical e horizontal, três para topo, laterais e base. As propriedades soltas (`padding-left`) servem para mudar um lado só.

## Shorthand × nesting de propriedades (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-nesting-aninhamento-sass]], `border-width` + `border-color` viram `border: 1px solid red`; no Sass, a alternativa é `border: { style: solid; color: purple; }`, que gera as longhands. Ele mesmo quase não usa a segunda forma.

## Key Sources

- [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]] — padding em sentido horário; background engloba background-color; border em três valores
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: margin, background e border-radius
- [[wiki/sources/frontpush-box-model-margin-padding-display-unidades]]: `margin: 12px 24px`; `padding` com 1, 2 e 4 valores "no círculo, no sentido horário" = as quatro propriedades separadas
- [[wiki/sources/frontpush-flex-direction-flex-wrap-flex-flow]]: `flex-flow` como atalho de `flex-direction` + `flex-wrap`; Násser prefere as duas longas
- [[wiki/sources/frontpush-flex-shrink-e-flex-shorthand]]: `flex` como atalho de grow, shrink e basis; padrão `0 1 auto`; o W3C recomenda usá-lo
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: sentido horário, meio-dia, 3, 6, 9
- [[wiki/sources/frontpush-nesting-aninhamento-sass]]: Sass aula 05: `border` shorthand × nesting de propriedades
