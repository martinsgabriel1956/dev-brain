---
type: concept
title: "Unidades de viewport (vh, vw, dvh, svh, lvh)"
aliases: ["viewport units", "viewport unit", "vh", "vw", "100vh", "dvh", "svh", "lvh", "unidades relativas à tela"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [css, frontend, unidades, viewport, responsivo, mobile]
skill: tech-mentor-frontend
status: stub
---

# Unidades de viewport

Unidades CSS proporcionais à área visível do navegador: `1vh` = 1% da altura, `1vw` = 1% da largura. Na aula de position do [[wiki/entities/frontpush|FrontPUSH]] o `body` recebe `height: 100vh` para ocupar "sempre fullscreen na tela inteira". Para o autor, essas medidas surgiram porque "hoje em dia nós temos vários dispositivos e a gente quer construir interfaces responsivas" ([[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]). Ver [[wiki/concepts/design-responsivo]].

## O problema do 100vh no celular `[external]`

No mobile, a barra de endereço aparece e some com o scroll. `vh` usa a viewport grande (barra recolhida), então `100vh` corta o fim da tela quando a barra está visível. A família nova separa os casos (https://developer.mozilla.org/en-US/docs/Web/CSS/length#relative_length_units_based_on_viewport):

- `svh` (*small*): barra visível, a menor altura possível;
- `lvh` (*large*): barra recolhida, igual ao `vh` antigo;
- `dvh` (*dynamic*): acompanha a barra em tempo real. É o certo para telas cheias, mas muda de valor durante o scroll.

`vw` tem outro detalhe: inclui a barra de rolagem vertical, então `width: 100vw` cria scroll horizontal no desktop. Para largura cheia, `width: 100%` costuma bastar (a margem padrão de 8 px do `body` também pede `margin: 0`).

## Relação com outros conceitos

- Unidades relativas viram pixels na etapa de layout ([[wiki/concepts/reflow-layout]]).
- Container queries trazem unidades relativas ao contêiner (`cqi`, `cqw`), não à viewport `[skill: tech-mentor-frontend]`.

## Key Sources

- [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]: `body` com `100vh` para a demonstração ocupar a tela
