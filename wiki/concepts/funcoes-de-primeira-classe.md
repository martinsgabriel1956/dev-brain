---
type: concept
title: "Funções de primeira classe"
aliases: ["first-class functions", "first-class function", "funções como valores", "função como objeto", "objetos de primeira classe"]
date_created: 2026-11-24
date_updated: 2026-11-25
source_count: 5
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

## No JavaScript Ninja, semana 7, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-arrays-metodo-push-e-loop-for]], uma função `soma(x, y)` vai para dentro de um array com `push` e é chamada pelo índice: sem argumentos dá `NaN`, com 1 e 2 dá 3. O instrutor chama isso de "programação funcional no JavaScript" e adia o assunto de passar função como argumento.

## No JavaScript Ninja, semana 8, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]], a consequência de função ser objeto: ela tem propriedades e métodos "embutidos", e `name` guarda o nome da própria função, independente da variável que a recebe (`var funcShow = function funcShow() {}`). `[external]` Ser valor é o que torna a anônima possível; a inferência do ES2015 dá nome a ela quando há uma variável ou propriedade de onde tirar.

## Key sources

- [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]]: JavaScript Ninja, semana 3, vídeo 01: função é objeto; atribuída a variável, anônima
- [[wiki/sources/javascript-ninja-metodos-de-objeto]]: JavaScript Ninja, semana 3, vídeo 02: função guardada em propriedade = método
- [[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos]]: JavaScript Ninja, semana 5, vídeo 01: função como valor de propriedade de objeto retornado
- [[wiki/sources/javascript-ninja-arrays-metodo-push-e-loop-for]]: JavaScript Ninja, semana 7, vídeo 03: função guardada em array e invocada pelo índice
- [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]]: JavaScript Ninja, semana 8, vídeo 01: função como objeto com a propriedade name
