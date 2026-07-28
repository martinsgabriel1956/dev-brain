---
type: concept
title: "Layout (Reflow)"
aliases: ["reflow", "layout do browser"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [browser, layout, reflow, rendering-pipeline, box-model, performance]
skill: tech-mentor-frontend
status: draft
---
# Layout (Reflow)

Etapa do pipeline de renderização em que o browser calcula a geometria de cada elemento da [[wiki/concepts/render-tree]]: posição X/Y, largura e altura. Segue o [[wiki/concepts/box-model]] — cada elemento é uma caixa com content, padding, border e margin.

Unidades relativas viram absolutas nessa etapa: `width: 50%` vira um valor em pixels, margens `auto` são calculadas com base no espaço disponível. O cálculo é **recursivo**: o tamanho do pai depende dos filhos, e a posição dos filhos depende do pai. O browser resolve isso passando restrições de largura de cima para baixo e acumulando alturas de baixo para cima.

**Reflow disparado por JavaScript**: mudar uma propriedade geométrica (ex. `width`) força um novo reflow. Isso é o mais caro dos três níveis de custo do pipeline: reflow > repaint > composite (ver [[wiki/concepts/paint-composite]]).

**Layout thrashing**: ler uma propriedade de layout (ex. `offsetHeight`) e escrever estilos alternadamente dentro de um loop força reflow síncrono repetido. Ver [[wiki/concepts/layout-thrashing]].

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
