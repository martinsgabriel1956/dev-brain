---
type: concept
title: "Funções de primeira classe"
aliases: ["first-class functions", "first-class function", "funções como valores", "função como objeto", "objetos de primeira classe"]
date_created: 2026-11-24
date_updated: 2026-11-25
source_count: 3
tags: [javascript, funcoes, programacao-funcional, fundamentos]
skill: lang-dynamic
status: stub
---

# Funções de primeira classe

Uma linguagem tem funções de primeira classe quando a função é um valor como outro qualquer: pode ser atribuída a uma variável, passada como argumento, devolvida por outra função e guardada em estruturas de dados `[external]` (https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function). Em JavaScript isso vale porque função é objeto (chamável), com propriedades como `name` e `length` ([[wiki/concepts/objetos-javascript]], [[wiki/concepts/funcoes-javascript]]).

```js
var dobro = function (x) { return x * 2 }  // atribuída (anônima na sintaxe)
[1, 2, 3].map(dobro)                       // passada como argumento: callback
function somaDe(n) { return function (x) { return x + n } }  // devolvida
var ops = { dobro: dobro }                 // guardada num objeto: método
```

É a base de callbacks, funções de ordem superior (`map`, `filter`, `reduce`), closures e métodos ([[wiki/concepts/programacao-funcional]]). Desde o ES2015, a função anônima atribuída a uma variável ganha o nome dela por inferência (`dobro.name === 'dobro'`).

## No JavaScript Ninja, semana 3, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]], "o function, na verdade, ele é um tipo de objeto", e funções "são objetos de primeira classe [...] porque eles podem ser atribuídos a variáveis". A demonstração guarda uma função anônima numa variável e a invoca pelo nome da variável. Só a atribuição aparece; passar e retornar funções ficam para depois.

## No JavaScript Ninja, semana 3, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-metodos-de-objeto]], o quarto uso da lista, guardar a função numa estrutura de dados, aparece: função atribuída a uma propriedade de objeto é método.

## Key sources

- [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]]: JavaScript Ninja, semana 3, vídeo 01: função é objeto; atribuída a variável, anônima
- [[wiki/sources/javascript-ninja-metodos-de-objeto]]: JavaScript Ninja, semana 3, vídeo 02: função guardada em propriedade = método
- [[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos]]: JavaScript Ninja, semana 5, vídeo 01: função como valor de propriedade de objeto retornado
