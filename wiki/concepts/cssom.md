---
type: concept
title: "CSSOM — CSS Object Model"
aliases: ["CSS Object Model"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [browser, cssom, css, rendering-pipeline, render-blocking]
skill: tech-mentor-frontend
status: draft
---
# CSSOM — CSS Object Model

Árvore que representa as regras de estilo CSS, construída em paralelo ao [[wiki/concepts/dom]] com um pipeline simétrico (bytes → caracteres → tokens → nós → árvore). O browser encontra as regras via tags `<link>` e `<style>`. O CSSOM mapeia cada regra CSS para os elementos que ela afeta, respeitando a cascata: cada nó herda estilos do pai a não ser que sobrescreva (ex. `font-size` definido no `body` propaga para os filhos).

**CSS é render-blocking**: o browser não pinta nada até o CSSOM estar completo. Sem essa espera, o browser renderizaria o HTML sem estilo e depois teria que redesenhar tudo (flash of unstyled content), o que seria uma experiência ruim.

O CSSOM é combinado com o DOM para formar a [[wiki/concepts/render-tree]] — ver pipeline completo em [[wiki/concepts/critical-rendering-path]].

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
