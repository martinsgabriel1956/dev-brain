---
type: concept
title: "Tree Shaking"
aliases: ["remoção de código morto", "dead code elimination frontend"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [frontend, bundler, tree-shaking, build, performance]
skill: tech-mentor-frontend
status: stable
---

# Tree Shaking

Etapa do processo de bundling em que o bundler (Webpack, Rollup, esbuild, Vite) analisa quais funções e módulos são de fato usados no código e remove do bundle final tudo que nunca é importado em nenhum lugar.

## Por que importa

Sem tree shaking, um bundle pode ultrapassar facilmente alguns megabytes, obrigando o usuário a baixar código morto antes de ver qualquer coisa na tela. O ganho de tree shaking depende de **como** você importa: importar uma biblioteca inteira (`import _ from 'lodash'`) traz o pacote completo; importar só a função usada (`import debounce from 'lodash/debounce'`, ou um pacote ESM-first) permite ao bundler eliminar o resto.

Tree shaking funciona de forma confiável com módulos ES (`import`/`export` estáticos) — módulos CommonJS (`require`) dificultam a análise estática porque imports podem ser condicionais/dinâmicos.

## Complementar a: code splitting

Tree shaking remove código **morto** (nunca usado); [[wiki/concepts/code-splitting]] divide código **vivo** em pedaços carregados sob demanda. Os dois atacam o mesmo problema (bundle grande demais) por ângulos diferentes e normalmente são usados juntos.

## Ver também

- [[wiki/concepts/code-splitting]]

## Key Sources

- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
