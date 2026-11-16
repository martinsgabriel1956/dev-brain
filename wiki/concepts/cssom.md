---
type: concept
title: "CSSOM — CSS Object Model"
aliases: ["CSS Object Model"]
date_created: 2026-07-28
date_updated: 2026-11-16
source_count: 3
tags: [browser, cssom, css, rendering-pipeline, render-blocking]
skill: tech-mentor-frontend
status: draft
---
# CSSOM — CSS Object Model

Árvore que representa as regras de estilo CSS, construída em paralelo ao [[wiki/concepts/dom]] com um pipeline simétrico (bytes → caracteres → tokens → nós → árvore). O browser encontra as regras via tags `<link>` e `<style>`. O CSSOM mapeia cada regra CSS para os elementos que ela afeta, respeitando a cascata: cada nó herda estilos do pai a não ser que sobrescreva (ex. `font-size` definido no `body` propaga para os filhos).

**CSS é render-blocking**: o browser não pinta nada até o CSSOM estar completo. Sem essa espera, o browser renderizaria o HTML sem estilo e depois teria que redesenhar tudo (flash of unstyled content), o que seria uma experiência ruim.

O CSSOM é combinado com o DOM para formar a [[wiki/concepts/render-tree]] — ver pipeline completo em [[wiki/concepts/critical-rendering-path]].

## Seletores

Cada regra do CSSOM começa por um [[wiki/concepts/seletores-css|seletor]]; a aula [[wiki/sources/seletores-e-pseudo-elements-css]] mostra os tipos básicos e as [[wiki/concepts/pseudo-classe-css|pseudo-classes]]. `[external]` O navegador casa seletores da direita para a esquerda (do elemento para os ancestrais), por isso o seletor mais à direita é o que mais pesa no custo.

Em [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]], o painel Elements mostra a árvore e os estilos juntos, e a aula conclui que o DOM inclui "as propriedades CSS". É o CSSOM, combinado com o DOM na render tree.

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
- [[wiki/sources/seletores-e-pseudo-elements-css]] — tipos de seletor das regras CSS
- [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]]: FrontPUSH, JavaScript aula 08: estilos atribuídos ao DOM
