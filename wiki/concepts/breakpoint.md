---
type: concept
title: "Breakpoint"
aliases: ["breakpoints", "ponto de quebra", "media query breakpoint"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, layout, responsividade, breakpoint, media-query, css, grid]
skill: ux-ui-mentor
status: stub
---

# Breakpoint

Largura de tela em que o layout passa a usar outro conjunto de estilos. Em [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]]: "é um valor de resolução onde eu falo para ele ler determinados estilos para poder aplicar a minha página". No CSS, vira uma media query, "uma cláusula para ele começar a ler determinada folha de estilo quando ele estiver abaixo de 960 pixels". Na landing page do [[wiki/entities/frontpush]], as colunas "quebraram justamente naquele breakpoint" ao passar para tablet ou celular.

## Quais valores

- **Aula:** 960 px como exemplo.
- `[external]` **Bootstrap 5:** 576, 768, 992, 1200 e 1400 px (https://getbootstrap.com/docs/5.3/layout/breakpoints/). Ver [[wiki/entities/twitter-bootstrap]].
- `[skill: ux-ui-mentor]` **Escala comum da skill:** 480, 768, 1024, 1280, 1536 px. Grid típico por faixa: 4 colunas no mobile, 8 no tablet, 12 no desktop ([[wiki/concepts/grid-de-colunas]]).

`[skill: ux-ui-mentor]` Regra: "adicione um breakpoint quando o conteúdo pede, não para cobrir todos os devices". Breakpoint é onde o layout quebra, não o tamanho de um aparelho. É a mesma razão da aula para preferir o responsivo ao adaptativo ([[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]]).

`[skill: ux-ui-mentor]` Mobile-first escreve o estilo base para a tela pequena e acrescenta com `@media (min-width: ...)`. O exemplo da aula ("abaixo de 960") é desktop-first, com `max-width`.

## Relação com outros conceitos

- [[wiki/concepts/design-responsivo]]: media queries e histórico.
- [[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]]: o adaptativo vive de breakpoints; o fluido vive entre eles.
- [[wiki/concepts/grid-de-colunas]]: colunas, gutter e margem mudam por breakpoint.

## Key Sources

- [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]]: definição, media query abaixo de 960 px, quebra na landing page do FrontPUSH
