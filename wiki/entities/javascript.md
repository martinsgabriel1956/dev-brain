---
type: entity
title: "JavaScript"
aliases: ["JS", "Javascript"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 10
tags: [linguagem, javascript, ecmascript, frontend, backend, web]
skill: lang-dynamic
status: stub
---

# JavaScript

Linguagem de programação da web: a única que os navegadores executam de forma nativa (além do WebAssembly), e também usada fora deles, no servidor ([[wiki/entities/nodejs]]) e no mobile ([[wiki/entities/react-native]]). A especificação se chama [[wiki/concepts/ecmascript|ECMAScript]] (ECMA-262, mantida pelo comitê TC39 da Ecma International); "JavaScript" é o nome das implementações e marca registrada da Oracle. `[external]` https://tc39.es/ecma262/

- **Papel na página:** HTML dá o conteúdo ([[wiki/concepts/html-hipertexto]]), CSS dá o estilo ([[wiki/concepts/css]]), JavaScript dá o comportamento, manipulando o [[wiki/concepts/dom]] e reagindo a eventos.
- **Versões:** ES5 (2009); ES6/ES2015 (classes, módulos, `let`/`const`, arrow functions, promises); depois uma edição por ano (async/await no ES2017). Ver [[wiki/concepts/ecmascript]].
- **Tipos:** dinâmicos ([[wiki/concepts/tipos-primitivos-javascript]]); o [[wiki/entities/typescript]] acrescenta tipos estáticos e compila para JS.
- **Motores:** V8 (Chrome, Node, Deno), SpiderMonkey (Firefox), JavaScriptCore (Safari, Bun).

## No FrontPUSH

Em [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]], [[wiki/entities/nasser|Násser]] abre o módulo de JavaScript ES6+: JS é "linguagem de programação em si", ao contrário do HTML e do CSS, e "torna [...] uma página web dinâmica". Cresce porque a mesma linguagem serve no front-end, no back-end e no mobile. Antes do ES6 era "um pouco arcaico", o que explica o sucesso do [[wiki/concepts/jquery]].

Em [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]], [[wiki/entities/nasser|Násser]] dá a primeira aula de código do módulo: variáveis, `var`/`let`/`const`, case sensitive, tipos com `typeof`, concatenação, template string e operadores aritméticos.

Em [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]], a aula 03 cobre booleanos, truthy/falsy, comparadores, `==` × `===`, `if / else if / else`, `&&`/`||` e `switch case` ([[wiki/concepts/estruturas-condicionais-javascript]]).

Em [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]], a aula 04 cobre funções, parâmetro × argumento, `return` e as três formas de declarar, até a arrow com retorno implícito ([[wiki/concepts/arrow-functions]]).

Em [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]], a aula 05 trata objetos: literal com atributos e métodos, acesso por ponto, `this`, shorthand, mutação e a ideia de "tudo é objeto" com os métodos herdados de string e número ([[wiki/concepts/objetos-javascript]]).

Em [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]], a aula 06 cobre arrays (índices, aninhamento, `pop`, `push`, `length`) e as repetições `for` e `while` ([[wiki/concepts/estruturas-de-repeticao-javascript]]).

Em [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]], a aula 07 cobre callbacks, `forEach` e `map` ([[wiki/concepts/metodos-de-array-javascript]]).

Em [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]], a aula 08 abre o DOM: definição, eventos, `window`/`document` e `querySelector`, `innerText`, `classList`, `id` ([[wiki/concepts/dom]], [[wiki/concepts/window-e-bom]]).

Em [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]], a aula 09 cria elementos com `createElement`, `setAttribute`, `createTextNode` e `appendChild` ([[wiki/concepts/criacao-de-elementos-dom]]).

Em [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]], a aula 10 cobre eventos: `addEventListener`, callback por referência, `event.target` × `currentTarget`, `classList.toggle`, `keydown` e `resize` ([[wiki/concepts/propagacao-de-eventos-dom]]).

## Key sources

- [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]: FrontPUSH, módulo de JavaScript, aula 01: o que é JS e o que é ES6+
- [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]]: FrontPUSH, JavaScript aula 02: variáveis, tipos e operadores
- [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]]: FrontPUSH, JavaScript aula 03: condicionais
- [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]]: FrontPUSH, JavaScript aula 04: funções e arrow functions
- [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]: FrontPUSH, JavaScript aula 05: objetos
- [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]]: FrontPUSH, JavaScript aula 06: arrays e loops
- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: forEach e map
- [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]]: FrontPUSH, JavaScript aula 08: DOM parte 1
- [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]]: FrontPUSH, JavaScript aula 09: criar elementos
- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: eventos
