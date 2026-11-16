---
type: concept
title: "Shorthand CSS (propriedades que resumem outras)"
aliases: ["propriedade shorthand", "shorthand properties", "propriedade resumo", "TRBL", "top right bottom left"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [css, sintaxe, box-model, padding, margin, border, background]
skill: tech-mentor-frontend
status: stub
---

# Shorthand CSS (propriedades que resumem outras)

Uma propriedade que define várias outras de uma vez: `padding` resume `padding-top/-right/-bottom/-left`; `margin` idem; `border` resume `border-width`, `border-style` e `border-color`; `background` resume `background-color`, `-image`, `-repeat`, `-position`, `-attachment` ([[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]]).

## Ordem dos valores: sentido horário

Com quatro valores, a ordem é **top, right, bottom, left**: "sempre começa no top e aí gira no sentido horário", e a regra vale para "um monte" de propriedades (padding, margin, border-radius). Um valor só vale para os quatro lados. `border: 5px solid red` dá o mesmo efeito que as propriedades separadas ([[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]]).

`[external]` Com dois valores: vertical, horizontal; com três: top, horizontal, bottom (https://developer.mozilla.org/en-US/docs/Web/CSS/Shorthand_properties). No `border-radius` a ordem começa no canto superior esquerdo e também gira no sentido horário. Cuidado: um shorthand redefine as sub-propriedades omitidas para o valor inicial (`background: red` zera um `background-image` declarado antes).

## Key Sources

- [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]] — padding em sentido horário; background engloba background-color; border em três valores
- [[wiki/sources/frontpush-box-model-margin-padding-display-unidades]]: `margin: 12px 24px`; `padding` com 1, 2 e 4 valores "no círculo, no sentido horário" = as quatro propriedades separadas
