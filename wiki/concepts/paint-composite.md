---
type: concept
title: "Paint e Composite"
aliases: ["paint", "compositing", "compositor"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [browser, paint, composite, gpu, rendering-pipeline, performance]
skill: tech-mentor-frontend
status: draft
---
# Paint e Composite

Duas etapas finais do pipeline de renderização, depois do [[wiki/concepts/reflow-layout|layout]]:

**Paint**: o browser percorre cada nó da [[wiki/concepts/render-tree]] (já com geometria calculada) e gera instruções de pintura — por exemplo "desenhe um retângulo azul na posição 10,20 com largura 250 e altura 50px". O browser não pinta tudo numa superfície só: divide a página em **camadas** (layers). Elementos com `transform`, `opacity` ou `will-change` geralmente ganham camada própria, porque mover uma camada é muito mais barato que repintar tudo.

**Composite**: a GPU pega todas as camadas pintadas, aplica as transformações e combina elas na ordem certa. Animações que só usam `transform`/`opacity` são performáticas porque mexem apenas no compositing — sem recalcular layout nem repintar.

**Hierarquia de custo**: mudar `width` → reflow (mais caro); mudar `color` → só repaint; mudar `transform`/`opacity` → só composite (mais barato). Confirmado em `references/frontend-performance-deep.md` da skill `tech-mentor-frontend`: `transform`/`opacity` marcados como "GPU: sem reflow", enquanto `left`/`top`/`width` "provocam reflow".

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
