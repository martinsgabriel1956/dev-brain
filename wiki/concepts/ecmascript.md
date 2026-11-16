---
type: concept
title: "ECMAScript (ES6, ES2015 e as edições anuais)"
aliases: ["ES", "ES6", "ES2015", "ES6+", "ECMA-262", "TC39"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 4
tags: [ecmascript, javascript, es6, es2015, tc39, especificacao]
skill: lang-dynamic
status: stub
---

# ECMAScript

Especificação da linguagem que os navegadores e o Node implementam como [[wiki/entities/javascript]]. O documento é o ECMA-262, publicado pela Ecma International e escrito pelo comitê técnico TC39. `[external]` https://tc39.es/ecma262/, https://ecma-international.org/technical-committees/tc39/

## Edições

| Nome | Ano | Destaques |
|---|---|---|
| ES3 | 1999 | base dos navegadores dos anos 2000 |
| ES4 | — | abandonada em 2008 |
| ES5 | 2009 | `"use strict"`, `JSON`, `Array.prototype.forEach`/`map`/`filter` |
| ES6 = ES2015 | 2015 | `let`/`const`, arrow functions, classes, módulos (`import`/`export`), promises, template strings, desestruturação |
| ES7 = ES2016 | 2016 | `**`, `Array.prototype.includes` |
| ES8 = ES2017 | 2017 | async/await, `Object.entries`/`values` |

`[external]` Desde 2015 o nome oficial é o ano; "ES7", "ES8" são apelidos. A regra "último dígito do ano mais um" só vale até ES10 = ES2019. "ES6+" é o JavaScript moderno: tudo do ES2015 em diante.

## Como uma novidade entra

Cada proposta passa pelos estágios 0 a 4 do TC39. No estágio 4 entra na edição do ano seguinte. Navegadores e o [[wiki/entities/typescript]] costumam implementar a partir do estágio 3. `[skill: lang-dynamic]` Exemplo recente: a API Temporal chegou ao Stage 4 em março de 2026 e vem ligada por padrão no Node 26.

## Especificação × ferramentas × APIs da web

- **Ferramentas não são edições.** Babel e Webpack não "vieram" com o ES6. O Babel traduz sintaxe nova para navegadores antigos, e o Webpack empacota módulos ([[wiki/concepts/transpilador]], [[wiki/concepts/pipeline-de-assets]]).
- **DOM e `fetch` não são ECMAScript.** São APIs da plataforma web (WHATWG/W3C) ([[wiki/concepts/dom]]). O que tornou o [[wiki/concepts/jquery]] dispensável foi a soma das duas coisas.

## No FrontPUSH

Em [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]], [[wiki/entities/nasser|Násser]] diz que "esse ES vem de ECMAScript", a "organização" que "gerencia o JavaScript", e que as versões seguem "o ano, só que mais um" (ES6 = 2015, ES7 = 2016, ES8 = 2017). Webpack, Babel, arrow functions e async/await aparecem juntos como "conceitos [que] vieram mais nessas versões"; só os dois últimos são da especificação.

Em [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]], o ES6 aparece duas vezes como divisor: "antes do ES6 só existia o var" e a template string é "uma sintaxe do próprio ES6 para frente". As duas estão certas (ES2015).

Em [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]], a arrow function, anunciada como novidade do ES6+ na aula 01, é mostrada na prática (ES2015).

Em [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]], o *method shorthand* (`area() {}`) é apresentado como notação que "já vem com o JavaScript 6": correto, é do ES2015. Os métodos de `String` e `Number` também são da especificação, não do navegador.

## Key sources

- [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]: FrontPUSH, módulo de JavaScript, aula 01: ES vem de ECMAScript; versões por ano
- [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]]: FrontPUSH, JavaScript aula 02: let/const e template string como ES6
- [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]]: FrontPUSH, JavaScript aula 04: arrow functions
- [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]: FrontPUSH, JavaScript aula 05: method shorthand do ES2015
