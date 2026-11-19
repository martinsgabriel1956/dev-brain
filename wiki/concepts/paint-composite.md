---
type: concept
title: "Paint e Composite"
aliases: ["paint", "compositing", "compositor"]
date_created: 2026-07-28
date_updated: 2026-11-19
source_count: 3
tags: [browser, paint, composite, gpu, rendering-pipeline, performance]
skill: tech-mentor-frontend
status: draft
---
# Paint e Composite

Duas etapas finais do pipeline de renderização, depois do [[wiki/concepts/reflow-layout|layout]]:

**Paint**: o browser percorre cada nó da [[wiki/concepts/render-tree]] (já com geometria calculada) e gera instruções de pintura — por exemplo "desenhe um retângulo azul na posição 10,20 com largura 250 e altura 50px". O browser não pinta tudo numa superfície só: divide a página em **camadas** (layers). Elementos com `transform`, `opacity` ou `will-change` geralmente ganham camada própria, porque mover uma camada é muito mais barato que repintar tudo.

**Composite**: a GPU pega todas as camadas pintadas, aplica as transformações e combina elas na ordem certa. Animações que só usam `transform`/`opacity` são performáticas porque mexem apenas no compositing — sem recalcular layout nem repintar.

**Hierarquia de custo**: mudar `width` → reflow (mais caro); mudar `color` → só repaint; mudar `transform`/`opacity` → só composite (mais barato). Confirmado em `references/frontend-performance-deep.md` da skill `tech-mentor-frontend`: `transform`/`opacity` marcados como "GPU: sem reflow", enquanto `left`/`top`/`width` "provocam reflow".

## Menu que entra e sai

A aula de position ([[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]) esconde o menu mobile com `relative` e −1000 px e o traz de volta com `transition`. A versão só de composite: `transform: translateX(-100%)` → `translateX(0)`, com `opacity` se quiser fade.

## Três caminhos, não quatro etapas sempre (FrontPUSH, otimização aula 07)

Em [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]], o pipeline é estilo → layout → pintura → composição e o navegador passaria pelas quatro "toda vez que ele renderiza". O ponto do artigo é o contrário: `transform`/`opacity` com camada própria pulam layout e pintura. A aula também diz que `transform` "não é tão performático quanto o opacity"; os dois são composição pura. Queda de frame com muitos `translate` vem de camadas demais, falta de camada (repinta) ou animação dirigida por JS. `will-change` promove a camada antes, mas cada camada gasta memória de GPU. Sombra animada repinta: anime a `opacity` de um `::after` com a sombra.

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
- [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]: transição de menu por `top` e a alternativa com `transform`
- [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: FrontPUSH, otimização aula 07: transform × opacity, will-change, sombra
