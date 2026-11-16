---
type: concept
title: "Box Model (CSS)"
aliases: ["CSS box model", "content-padding-border-margin"]
date_created: 2026-07-28
date_updated: 2026-11-16
source_count: 2
tags: [browser, css, box-model, layout]
skill: tech-mentor-frontend
status: draft
---
# Box Model (CSS)

Todo elemento renderizado é uma caixa composta por quatro camadas, de dentro para fora: **content**, **padding**, **border** e **margin**. Durante a etapa de [[wiki/concepts/reflow-layout|layout]], o browser calcula o tamanho final de cada caixa considerando essas camadas e o fluxo do documento — unidades relativas (`%`, `auto`) viram valores absolutos em pixels nesse momento.

## Margin auto e display

Em [[wiki/sources/principais-propriedades-css-color-background-font]], `margin: 0 auto` zera a margem vertical e divide a horizontal, centralizando uma section de 80%. O autor força `display: block` no link-botão porque o link é inline e ele quer "aplicar sempre as propriedades de box-model" ([[wiki/concepts/display-css]]). `[external]` Elementos inline ignoram width, height e margem vertical; `inline-block` também resolve. A dica de depurar com `border` tem custo: a borda soma ao tamanho da caixa (com o `box-sizing: content-box` padrão); `outline` não soma (https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing).

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
- [[wiki/sources/principais-propriedades-css-color-background-font]]: margin 0 auto; link forçado a bloco para usar o box model; border como printf
