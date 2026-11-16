---
type: concept
title: "Breakpoint"
aliases: ["breakpoints", "ponto de quebra", "media query breakpoint", "sm md lg xl xxl"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, layout, grid, breakpoint, design-responsivo, media-query, css]
skill: ux-ui-mentor
status: stub
---

# Breakpoint

A largura de tela em que o layout muda: o número de colunas, as margens ou a disposição dos blocos. Em [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]], o autor manda olhar os breakpoints do [[wiki/entities/material-design]] e do iOS, e diz que usou os do [[wiki/entities/twitter-bootstrap|Bootstrap]] ("o large, o extra large") nas aulas, "por ser muito utilizado na web".

## Os números de sempre

"Oito colunas, 12 colunas, quatro colunas, então você percebe que sempre são esses números que a gente está sempre circundando." `[skill: ux-ui-mentor]` A tabela da skill: 4 colunas abaixo de 768 px, 8 entre 768 e 1024, 12 acima de 1024. Ver [[wiki/concepts/grid-de-colunas]].

## Bootstrap

`[external]` Bootstrap 5: `sm` 576, `md` 768, `lg` 992, `xl` 1200, `xxl` 1400 (o `xxl` é novo em relação ao 4.x): https://getbootstrap.com/docs/5.0/layout/breakpoints/

## Decisão de conteúdo

`[skill: ux-ui-mentor]` "Breakpoints não são tamanhos de device — são pontos onde o layout quebra." Adicione um quando o conteúdo pedir, não para cobrir todos os aparelhos. No CSS, cada breakpoint vira uma media query (`@media (min-width: 768px)`).

## Relação com outros conceitos

- [[wiki/concepts/design-responsivo]]: o layout fluido muda de forma nos breakpoints.
- [[wiki/concepts/design-adaptativo]]: um layout distinto para cada breakpoint.
- [[wiki/concepts/grid-de-colunas]]: o número de colunas por breakpoint.

## Key Sources

- [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]]: breakpoints do Material Design, iOS e Bootstrap; 4, 8 e 12 colunas
