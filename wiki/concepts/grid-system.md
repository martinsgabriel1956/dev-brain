---
type: concept
title: "Grid system por classes (estilo Bootstrap)"
aliases: ["grid system", "sistema de grids", "grid de classes", ".col-N", ".grid-N", "Bootstrap grid"]
date_created: 2026-11-16
date_updated: 2026-11-24
source_count: 5
tags: [css, sass, grid-system, grid-de-colunas, layout, responsividade, bootstrap]
skill: tech-mentor-frontend
status: stub
---

# Grid system por classes (estilo Bootstrap)

Biblioteca de CSS que transforma o [[wiki/concepts/grid-de-colunas]] do design em classes: um **container** com `max-width` centralizado e itens com largura em **porcentagem** de N/12 colunas (`.grid-5`, `.col-md-7`), que empilham abaixo de um [[wiki/concepts/breakpoint]]. Foi popularizado pelo 960.gs e pelo [[wiki/entities/twitter-bootstrap|Bootstrap]], com float até o Bootstrap 3 e flexbox a partir do 4.

## No FrontPUSH

- [[wiki/sources/frontpush-for-while-each-sass]]: `@for` gerando `.grid-1`…`.grid-12`.
- [[wiki/sources/frontpush-funcoes-sass]]: `grid($col, $total: 12)` devolvendo a %.
- [[wiki/sources/frontpush-grid-system-sass-parte-1]]: o porquê (precisão contra o `flex-grow` "no olho"), o container de largura máxima com fluidez abaixo dela (motivo: monitores 21:9) e o mixin `responsive` com `xl`/`l`/`m`/`s`/`xs`. Sem Flexbox nem Grid Layout; continua na parte 2.

## Peças

| Peça | O que faz |
|---|---|
| container | `max-width` (1416 px no grid 96 + 24), `margin: 0 auto`, padding lateral |
| coluna | `width: N/12` em % (com o gutter descontado) |
| gutter | espaço entre colunas: padding interno, margin ou `gap` |
| breakpoint | abaixo dele, `width: 100%` e as colunas empilham |

## Hoje

`[skill: tech-mentor-frontend]` O [[wiki/concepts/css-grid]] faz tudo isso no próprio CSS: `grid-template-columns: repeat(12, 1fr)` + `gap: 24px` + `grid-column: span 5`, sem conta de porcentagem nem de gutter. Container queries (`@container`) permitem quebrar pelo espaço do componente. O grid de classes continua em sistemas legados e em projetos com Bootstrap. Para aprender, montar um é bom exercício de `%`, `box-sizing` e media query ([[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]]).

## Grid de dashboard com sidebar

Na [[wiki/sources/frontpush-dashboards-overview-do-projeto-dashclass|aula 02 do módulo de dashboards]]: em dashboards o grid é "um pouco mais recuado, não é centralizado como a gente costuma fazer em landing pages", com "um pequeno recuo" e "uns tamanhos ali que variam", "mas a gente continua no padrão de 12 grids". Detalhes prometidos para aulas seguintes.

## Grid de dashboard (aula 03)

Na [[wiki/sources/frontpush-dashboards-grids-e-patterns|aula 03 do módulo de dashboards]], os valores do grid com sidebar: grid 1 = coluna 70, gutter 30, offset 240 (container 1.170); grid 2 = 80/30/120 (1.290); grid 3 = 66/30/280 (1.122). Detalhe em [[wiki/concepts/grid-de-dashboard]].

## Key sources

- [[wiki/sources/frontpush-grid-system-sass-parte-1]]: motivação, container e mixin de breakpoints
- [[wiki/sources/frontpush-for-while-each-sass]]: classes `.grid-N` geradas por `@for`
- [[wiki/sources/frontpush-funcoes-sass]]: função `grid()` em %
- [[wiki/sources/frontpush-dashboards-overview-do-projeto-dashclass]]: FrontPUSH, dashboards aula 02: 12 colunas recuadas pela sidebar
- [[wiki/sources/frontpush-dashboards-grids-e-patterns]]: FrontPUSH, dashboards aula 03: valores dos três grids
