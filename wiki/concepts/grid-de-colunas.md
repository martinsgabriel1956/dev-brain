---
type: concept
title: "Grid de Colunas"
aliases: ["column grid", "layout grid", "grid de 12 colunas", "12-column grid", "gutter", "calha"]
date_created: 2026-11-13
date_updated: 2026-11-15
source_count: 2
tags: [ui, ui-design, layout, grid, grid-de-colunas, alinhamento, consistencia, figma]
skill: ux-ui-mentor
status: stub
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

## Grid como esqueleto

Em [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]]: grids "criam a estrutura básica, o esqueleto para o seu design", colunas onde os elementos são colocados e alinhados. Servem ao designer (alinhamento, "consistência de distância") e ao dev (resoluções, [[wiki/concepts/breakpoint|breakpoints]]). Na landing page do [[wiki/entities/frontpush]], 12 colunas imaginárias se dividem em 7–8 + 4–5 no site e 4 + 8 no design. No wireframe, o conteúdo pega as seis colunas centrais e sobram três de cada lado. A coluna vira unidade de distância: "quanto que tem de distância de um elemento para o outro? Ah, é uma coluna."

O padrão citado para colunas por dispositivo é o Bootstrap Grid System ([[wiki/entities/twitter-bootstrap]]). `[external]` 12 colunas e seis faixas de breakpoint no Bootstrap 5 (https://getbootstrap.com/docs/5.3/layout/grid/).

## Relação com outros conceitos

- [[wiki/concepts/consistencia-visual]] — o grid é o mesmo em todas as telas, o que dá ritmo e alinhamento.
- [[wiki/concepts/grid-de-8-pontos]] — o grid de 8 decide os vãos; o de colunas decide onde as coisas começam e terminam.
- [[wiki/concepts/grid-de-icones]] — o mesmo princípio de "réguas", em escala de ícone.
- [[wiki/concepts/design-responsivo]] — o número de colunas cai em telas menores.

## Key Sources

- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — 12 colunas de 72, gutter de 32, centralizado; 12 pelos bons múltiplos
- [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]] — grid como esqueleto; 12 colunas no FrontPUSH (7–8 + 4–5; 4 + 8); seis colunas centrais no wireframe; "é uma coluna" de distância
