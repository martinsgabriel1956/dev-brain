---
type: concept
title: "Box Model (CSS)"
aliases: ["CSS box model", "content-padding-border-margin"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [browser, css, box-model, layout]
skill: tech-mentor-frontend
status: draft
---
# Box Model (CSS)

Todo elemento renderizado é uma caixa composta por quatro camadas, de dentro para fora: **content**, **padding**, **border** e **margin**. Durante a etapa de [[wiki/concepts/reflow-layout|layout]], o browser calcula o tamanho final de cada caixa considerando essas camadas e o fluxo do documento — unidades relativas (`%`, `auto`) viram valores absolutos em pixels nesse momento.

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
