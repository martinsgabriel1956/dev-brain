---
type: concept
title: "Grid de dashboard (12 colunas com offset para a sidebar)"
aliases: ["grid com offset", "grid de dashboard", "grid deslocado", "grid recuado"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 1
tags: [grid, grid-de-colunas, dashboard, sidebar, offset, gutter, container, figma]
skill: ux-ui-mentor
status: stub
---

# Grid de dashboard (12 colunas com offset para a sidebar)

O mesmo [[wiki/concepts/grid-de-colunas|grid de 12 colunas]] das landing pages, alinhado à esquerda e empurrado para a direita por um **offset** do tamanho da [[wiki/concepts/sidebar]]. Em vez de um container centralizado, o conteúdo ocupa o espaço que sobra ao lado da navegação.

## Os três grids do DashClass

Em [[wiki/sources/frontpush-dashboards-grids-e-patterns]], [[wiki/entities/nasser|Násser]] mostra três variações, todas num frame de 1440 × 900 (16:10), tipo Left no [[wiki/entities/figma|Figma]], com gutter de 30 px:

| Grid | Coluna | Offset | Container (12 col. + 11 gutters) | Sobra à direita |
|---|---|---|---|---|
| 1 (o que ele usa) | 70 px | 240 px | 1.170 px | 30 px |
| 2 | 80 px | 120 px | 1.290 px | 30 px |
| 3 | 66 px | 280 px | 1.122 px | 38 px |

Os containers e as sobras são cálculo a partir dos valores do slide; os containers batem com os números ditos na aula.

- Por que manter as 12 colunas: "para [...] a gente não mudar o modelo de forma muito abrupta"; o modelo "é muito versátil". Variar um pouco offset e gutter "não tem problema nenhum".
- Por que container curto: em empresa, "computadores [...] mais capadinhos", HD ou Full HD "no máximo"; desenhar no tamanho real aproxima o design do que vai ser implementado.
- No Figma é fixo; fluido e [[wiki/concepts/breakpoint|breakpoints]] ficam para depois.

## Ressalvas

- 1440 ainda é mais largo que notebooks de 1366 × 768 e 1536 × 864, comuns em empresa (`[external]`, StatCounter, média); o layout de 1.410 px precisa ficar fluido no código.
- `[skill: ux-ui-mentor]` A referência `grid-layout.md` recomenda container fluido para dashboards. Em CSS, o mais comum é uma coluna fixa para a sidebar e uma coluna `1fr` com o grid de 12 dentro (inferência, alta). Ver [[wiki/concepts/css-grid]].
- O offset de 120 px provavelmente corresponde à sidebar recolhida, só com ícones (inferência, média).

Ver também [[wiki/concepts/grid-system]].

## Key Sources

- [[wiki/sources/frontpush-dashboards-grids-e-patterns]]: os três grids, frame 1440 × 900, container curto
