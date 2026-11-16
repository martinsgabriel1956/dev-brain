---
type: concept
title: "Breakpoint"
aliases: ["breakpoints", "ponto de quebra", "media query breakpoint", "small medium large extra-large"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, responsividade, breakpoints, grid, resolucao, css]
skill: ux-ui-mentor
status: stub
---

# Breakpoint

Largura de tela em que o layout muda: número de colunas, max-width do conteúdo, empilhamento dos blocos. Cada faixa entre dois breakpoints tem seu próprio [[wiki/concepts/grid-de-colunas|grid]]. É o mecanismo do [[wiki/concepts/design-responsivo]].

## As faixas da aula

Em [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]] (slide):

| Faixa | Largura | Dispositivo |
|---|---|---|
| Small | <576 | smartphones |
| Medium | 720 | tablets |
| Large | 960 | notebooks |
| Extra-large | 1200 (na fala, "até 1440") | PCs, desktops |

Acima disso, 1600 para TV; o teto que ele adota para desktop é 1440.

## Resolução não é polegada

"Muita coisa se deve à resolução, não só a tamanho de tela": um monitor de 26" em Full HD tem menos pixels que um iMac de 27" com Retina 5K ([[wiki/entities/apple]]). O breakpoint olha para a largura em pixels, não para o tamanho físico.

`[external]` No CSS, o que conta são pixels CSS: uma tela Retina com `devicePixelRatio` 2 reporta metade da largura física às media queries (https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio). Por isso o iMac 5K se comporta como uma tela de cerca de 2560 px de largura.

## Bootstrap e a skill

- `[external]` Bootstrap 5: 576, 768, 992, 1200, 1400; containers de 540, 720, 960, 1140, 1320 (https://getbootstrap.com/docs/5.3/layout/breakpoints/). O 720 e o 960 da aula batem com containers, não com breakpoints.
- `[skill: ux-ui-mentor]` Sistema comum: 480, 768, 1024, 1280, 1536. "Breakpoints não são tamanhos de device, são pontos onde o layout quebra": adicione um "quando o conteúdo pede, não para cobrir todos os devices". Mobile-first (`min-width`) em vez de desktop-first (`max-width`).

## Relação com outros conceitos

- [[wiki/concepts/grid-de-colunas]]: 12 / 6 / 4 colunas conforme a faixa.
- [[wiki/concepts/design-responsivo]]: breakpoints são onde a resposta acontece.
- [[wiki/concepts/mobile-layouts-responsivos]]: o equivalente nativo (WindowSizeClass, size classes).

## Key Sources

- [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]] — faixas small/medium/large/extra-large; resolução x tamanho; teto de 1440, 1600 para TV
