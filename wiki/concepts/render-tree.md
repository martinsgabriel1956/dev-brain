---
type: concept
title: "Render Tree"
aliases: []
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [browser, render-tree, rendering-pipeline, dom, cssom]
skill: tech-mentor-frontend
status: draft
---
# Render Tree

Árvore resultante de combinar o [[wiki/concepts/dom]] (estrutura) com o [[wiki/concepts/cssom]] (estilos): o browser percorre o DOM e, para cada nó visível, consulta o CSSOM para achar os estilos computados.

Contém **apenas nós visíveis**:
- `display: none` → fora da render tree.
- `<head>` inteiro → fora.
- Tags `<script>` → fora.
- `visibility: hidden` → **entra** na render tree (o elemento é invisível, mas ainda ocupa espaço/geometria).

A render tree alimenta a etapa de [[wiki/concepts/reflow-layout|layout]], que calcula a geometria de cada caixa, seguida por [[wiki/concepts/paint-composite|paint e composite]]. Ver pipeline completo em [[wiki/concepts/critical-rendering-path]].

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
