---
type: concept
title: "Grid de Colunas"
aliases: ["column grid", "layout grid", "grid de 12 colunas", "12-column grid", "gutter", "calha"]
date_created: 2026-11-13
date_updated: 2026-11-15
source_count: 2
tags: [ui, ui-design, layout, grid, grid-de-colunas, alinhamento, consistencia, figma]
skill: ux-ui-mentor
status: draft
---

# Grid de Colunas

Divisões verticais da página ("colunas, réguas") em que o conteúdo se alinha. É a primeira coisa a acertar antes de mexer em espaçamento ([[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]).

## Por que 12 colunas

No desktop, "por padrão sempre 12 colunas": 12 divide por 2, 3, 4 e 6, então o mesmo grid acomoda layouts de duas, três, quatro ou seis partes iguais.

## A configuração da aula

12 colunas de 72, gutter de 32 ("o espaço entre cada coluna"), centralizado no frame do [[wiki/entities/figma]]. Largura total do conteúdo: 12 × 72 + 11 × 32 = 1216 (conta do agente). O headline encosta na primeira coluna; os blocos distribuídos na horizontal terminam alinhados ao grid.

## Anatomia

`[skill: ux-ui-mentor]` Margem | coluna | gutter | coluna | ... | margem. Grids típicos por breakpoint na skill:

| Breakpoint | Colunas | Gutter | Margem |
|---|---|---|---|
| Mobile (< 768 px) | 4 | 16 | 16 |
| Tablet (768–1024 px) | 8 | 24 | 24 |
| Desktop (1024–1440 px) | 12 | 24 | 32 |
| Wide (> 1440 px) | 12 | 32 | auto (max-width centralizado) |

O gutter de 32 da aula corresponde à linha "wide" da skill. Os valores de coluna, gutter e margem saem da [[wiki/concepts/escala-de-espacamento]] (72 = 9 × 8; 32 e 16 também são múltiplos de 8), o que junta o grid de colunas ao [[wiki/concepts/grid-de-8-pontos]].

`[skill: ux-ui-mentor]` No código, o equivalente direto é `display: grid; grid-template-columns: repeat(12, 1fr); gap: 32px;` dentro de um container com max-width e `margin-inline: auto`.

## Relação com outros conceitos

- [[wiki/concepts/consistencia-visual]] — o grid é o mesmo em todas as telas, o que dá ritmo e alinhamento.
- [[wiki/concepts/grid-de-8-pontos]] — o grid de 8 decide os vãos; o de colunas decide onde as coisas começam e terminam.
- [[wiki/concepts/grid-de-icones]] — o mesmo princípio de "réguas", em escala de ícone.
- [[wiki/concepts/design-responsivo]] — o número de colunas cai em telas menores.

## Max-width: coluna + gutter

Em [[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]], o grid sai do Figma no tipo **Center** (coluna fixa, grid centralizado), e não Stretch. Stretch "sempre vai preencher a tela inteira", mas pede "uma série de breakpoints maior". Coluna e gutter definem o max-width do conteúdo (12 × coluna + 11 × gutter, conta do agente):

| Coluna | Gutter | Max-width |
|---|---|---|
| 72 | 32 | 1216 |
| 72 | 36 | **1260** (o que ele mais usa) |
| 96 | 24 | 1416 (rumo a 1440) |
| 96 | 32 | 1504 |
| 96 | 36 | 1548 (TV, rumo a 1600) |

O grid é "um guia", não uma régua de precisão: figuras de 88 ou ilustrações que saem da coluna são normais se o alinhamento continua no grid. Blocos do mesmo número de colunas viram a mesma classe no código ("tudo é div, tudo é bloco"). Onde 12 não divide (três elementos com sobras), agrupar e usar distribuir horizontal spacing. Ver também [[wiki/concepts/equilibrio-visual]]: o grid deixa contar o peso de cada lado.

`[external]` O Bootstrap 5, que ele cita como origem, usa colunas fluidas e gutter de 24 px; containers até 1320 (https://getbootstrap.com/docs/5.3/layout/containers/).

## Key Sources

- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — 12 colunas de 72, gutter de 32, centralizado; 12 pelos bons múltiplos
- [[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]] — 72 + 36 = 1260 (o principal), 1216, 1416, 1504, 1548; Center x Stretch; pensar em blocos; grid como guia; equilíbrio do menu
