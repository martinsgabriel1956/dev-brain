---
type: concept
title: "Transpilador (Sass, Less, CoffeeScript, Babel)"
aliases: ['transpiler', 'pré-processador']
date_created: 2026-10-14
date_updated: 2026-11-16
source_count: 6
tags: [transpilador, build, javascript, css, historia]
skill: tech-mentor-frontend
status: draft
---

# Transpilador (Sass, Less, CoffeeScript, Babel)

Traduz uma linguagem em outra (não gera código de máquina). Sass/Less → [[wiki/concepts/css]]; CoffeeScript (Jeremy Ashkenas, 2009) → JavaScript, deixando legados como interpolação de string, escopo e arrow functions, incorporados ao ES6 (2015) e tornando-o obsoleto; Babel mantém essa função. Etapa do [[wiki/concepts/pipeline-de-assets]]. Contraste: [[wiki/concepts/pipeline-de-compilacao]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]], o TypeScript "é convertido para JavaScript". `[skill: lang-dynamic]` No Node 24+, o type stripping apaga os tipos sem gerar código novo, e o `tsc` fica só para checar tipos ou gerar o build.

Em [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]], Babel e Webpack são citados entre os "conceitos [que] vieram mais nessas versões" do ES6+. São ferramentas, não edições do [[wiki/concepts/ecmascript]]: o Babel traduz o JS novo para navegador antigo e o Webpack empacota módulos.

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]

## Na NLW #2, dia 1 (Diego Fernandes)

O `react-scripts` esconde Babel ("o JavaScript mais moderno para um JavaScript um pouquinho mais antigo") e Webpack. O Babel também transforma o JSX e apaga os tipos do TypeScript, sem checá-los. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Na NLW #2, dia 2 (Diego Fernandes)

`tsc --init` com `target: ES2017`, "as funcionalidades que o Node entende"; o ts-node-dev com `--transpile-only` só converte, sem checar tipos. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## Key sources (adição 2026-10-14)

- [[wiki/sources/por-que-c-e-alto-nivel-abstracao-portabilidade-hardware]] — alternativa citada para melhorar o ecossistema de C: linguagens que transpilam para C ([[wiki/concepts/dependencia-de-caminho-em-tecnologia]])
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: TypeScript convertido para JS; type stripping no Node
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: Babel no react-scripts
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: target ES2017 e transpile-only
- [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]: FrontPUSH, JavaScript aula 01: Babel e Webpack como se fossem do ES6
