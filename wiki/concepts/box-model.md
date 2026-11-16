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

## Deslocar a caixa sem mexer no fluxo

Em [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]], `position: relative` com `top` desloca a caixa inteira, mas a posição original continua reservada ("imagine" o contorno tracejado). Já `absolute` tira a caixa do fluxo, e o irmão sobe para ocupar o espaço. A margem empurra os vizinhos; `top` e `left` não empurram. Ver [[wiki/concepts/css-position]].

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
- [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]: relative mantém o espaço da caixa; absolute o libera
