---
type: concept
title: "Tree Shaking"
aliases: ["remoção de código morto", "dead code elimination frontend"]
date_created: 2026-08-03
date_updated: 2026-11-16
source_count: 3
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

## CJS × ESM (JStack, aula 03)

[[wiki/sources/jstack-o-que-sao-modulos]] ensina só CommonJS (`require`/`module.exports`), o formato que atrapalha a análise estática descrita acima. Ver [[wiki/concepts/modulos-nodejs]] para a comparação com ESM.

Em [[wiki/sources/frontpush-modules-js-import-export-default]], as funções de retângulo vão num objeto exportado como `default`. Agrupar assim impede o bundler de descartar a função que não for usada; exports nomeados com `import * as retangulo` dão o mesmo agrupamento sem esse custo.

## Key Sources

- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
- [[wiki/sources/jstack-o-que-sao-modulos]]: curso ensina CJS, o formato que dificulta tree shaking
- [[wiki/sources/frontpush-modules-js-import-export-default]]: FrontPUSH, JavaScript aula 17: objeto default × tree-shaking
