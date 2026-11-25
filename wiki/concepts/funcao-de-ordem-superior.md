---
type: concept
title: "Função de ordem superior"
aliases: ["higher-order function", "HOF", "função de alta ordem", "função que recebe função", "função que retorna função"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 2
tags: [javascript, funcoes, programacao-funcional, callback, higher-order-function]
skill: lang-dynamic
status: stub
---

# Função de ordem superior

Função de ordem superior é uma função que **recebe** outra função como argumento ou **devolve** uma função, ou as duas coisas `[external]` (https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function). Só existe em linguagens com [[wiki/concepts/funcoes-de-primeira-classe|funções de primeira classe]]. A função recebida é o [[wiki/concepts/callback-javascript|callback]]; a função devolvida costuma ser uma [[wiki/concepts/closure-javascript|closure]].

```js
function showFunction(fn) { return fn(); }        // recebe função
function adder(x) { return function (y) { return x + y; }; }  // devolve função
[1, 2, 3].map(adder(10));                         // as duas juntas: [11, 12, 13]
```

Em JavaScript estão por toda parte: os [[wiki/concepts/metodos-de-array-javascript|métodos de array]] `map`, `filter`, `reduce` e `forEach`, além de `addEventListener`, `setTimeout`, `then` e decorators/middlewares. São o principal instrumento de composição na [[wiki/concepts/programacao-funcional]], e [[wiki/concepts/currying]] é um caso particular, uma função que devolve função a cada argumento.

## No JavaScript Ninja, semana 8 (Fernando Daciuk)

Os dois lados aparecem em vídeos seguidos, sem o nome do conceito:

- **Devolve função:** em [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]], `adder(2)` devolve `add2`, e `adder(5)(8)` dá 13.
- **Recebe função:** em [[wiki/sources/javascript-ninja-programacao-funcional-parte-3]], `showFunction(fn)` recebe a função "como um parâmetro normal" e retorna `fn()`. A função é passada pelo nome, "sem invocar", ou anônima direto no parâmetro.

## Key sources

- [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]]: JavaScript Ninja, semana 8, vídeo 03: função que devolve função (adder)
- [[wiki/sources/javascript-ninja-programacao-funcional-parte-3]]: JavaScript Ninja, semana 8, vídeo 04: função que recebe função (showFunction)
