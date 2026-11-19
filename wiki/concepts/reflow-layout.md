---
type: concept
title: "Layout (Reflow)"
aliases: ["reflow", "layout do browser"]
date_created: 2026-07-28
date_updated: 2026-11-19
source_count: 4
tags: [browser, layout, reflow, rendering-pipeline, box-model, performance]
skill: tech-mentor-frontend
status: draft
---
# Layout (Reflow)

Etapa do pipeline de renderização em que o browser calcula a geometria de cada elemento da [[wiki/concepts/render-tree]]: posição X/Y, largura e altura. Segue o [[wiki/concepts/box-model]] — cada elemento é uma caixa com content, padding, border e margin.

Unidades relativas viram absolutas nessa etapa: `width: 50%` vira um valor em pixels, margens `auto` são calculadas com base no espaço disponível. O cálculo é **recursivo**: o tamanho do pai depende dos filhos, e a posição dos filhos depende do pai. O browser resolve isso passando restrições de largura de cima para baixo e acumulando alturas de baixo para cima.

**Reflow disparado por JavaScript**: mudar uma propriedade geométrica (ex. `width`) força um novo reflow. Isso é o mais caro dos três níveis de custo do pipeline: reflow > repaint > composite (ver [[wiki/concepts/paint-composite]]).

**Layout thrashing**: ler uma propriedade de layout (ex. `offsetHeight`) e escrever estilos alternadamente dentro de um loop força reflow síncrono repetido. Ver [[wiki/concepts/layout-thrashing]].

## Animar top e left

O truque do menu mobile em [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]] (`position: relative` com −1000 px, zero no clique, `transition`) anima `top`/`left`, que refazem o layout a cada quadro. `transform: translateX()` dá o mesmo efeito sem reflow `[skill: tech-mentor-frontend]`. Ver [[wiki/concepts/paint-composite]] e [[wiki/concepts/css-position]].

Em [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]], o link é montado inteiro (atributo e texto) e anexado à página uma vez só, o que evita recálculos de layout repetidos. Para muitos nós, `DocumentFragment`.

## `width` × `scaleX` (FrontPUSH, otimização aula 07)

Em [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: `width` de 64 para 128 px e `scaleX(2)` dão "o mesmo efeito", mas "o mais custoso é o width", porque muda a geometria. O `transform` não entra no layout (a caixa mantém o espaço no fluxo), por isso também não é idêntico: estica o conteúdo e não empurra vizinhos.

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
- [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]: menu animado por `top`/`left` (reflow) x `transform`
- [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]]: FrontPUSH, JavaScript aula 09: montar fora da página e anexar uma vez
- [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: FrontPUSH, otimização aula 07: width refaz layout, scaleX não
