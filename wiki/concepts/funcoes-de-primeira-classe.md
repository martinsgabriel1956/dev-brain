---
type: concept
title: "Funções de primeira classe"
aliases: ["first-class functions", "first-class function", "funções como valores", "função como objeto", "objetos de primeira classe"]
date_created: 2026-11-24
date_updated: 2026-11-26
source_count: 9
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

## No JavaScript Ninja, semana 8, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]], o termo vira "cidadãos de primeira classe": funções "têm o mesmo tratamento dos objetos no JavaScript", e "tudo aquilo que você consegue fazer com objetos [...] você também consegue fazer com funções". A aula percorre três usos: criar como literal, atribuir a variável e (para objetos) retornar de uma função; retornar funções fica para o vídeo seguinte. `[external]` `f instanceof Object` dá `true` e `f.prop = 1` funciona (verificado no Node 22).

## No JavaScript Ninja, semana 8, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]], o terceiro uso da lista, a função devolvida por outra: `function adder(x) { return function (y) { return x + y; }; }`, com `adder(2)(3)` = 5 e `adder(5)(8)` = 13. A aula diz que "só linguagens que te dão o poder de utilizar funções de primeira classe" fazem isso. `[external]` Precisa também de [[wiki/concepts/closure-javascript|closure]] para a função interna lembrar o `x`; o padrão é [[wiki/concepts/currying|currying]].

## No JavaScript Ninja, semana 8, vídeo 04 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-programacao-funcional-parte-3]], o último dos usos da lista: passar função como argumento, "como um parâmetro normal [que] poderia ser qualquer tipo de valor". Com isso o curso cobre os quatro (atribuir, guardar em estrutura, retornar e passar). Quem recebe função é [[wiki/concepts/funcao-de-ordem-superior|função de ordem superior]].

## No JavaScript Ninja, semana 9, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-iife]], a anônima atribuída a `sum2` se invoca pelo nome da variável, porque funções são "objetos de primeira classe"; o mesmo vale para a anônima como valor de propriedade de objeto ([[wiki/concepts/iife]]).

## Key sources

- [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]]: JavaScript Ninja, semana 3, vídeo 01: função é objeto; atribuída a variável, anônima
- [[wiki/sources/javascript-ninja-metodos-de-objeto]]: JavaScript Ninja, semana 3, vídeo 02: função guardada em propriedade = método
- [[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos]]: JavaScript Ninja, semana 5, vídeo 01: função como valor de propriedade de objeto retornado
- [[wiki/sources/javascript-ninja-arrays-metodo-push-e-loop-for]]: JavaScript Ninja, semana 7, vídeo 03: função guardada em array e invocada pelo índice
- [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]]: JavaScript Ninja, semana 8, vídeo 01: função como objeto com a propriedade name
- [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]]: JavaScript Ninja, semana 8, vídeo 02: cidadãos de primeira classe; paralelo objeto × função
- [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]]: JavaScript Ninja, semana 8, vídeo 03: função que retorna função (adder)
- [[wiki/sources/javascript-ninja-programacao-funcional-parte-3]]: JavaScript Ninja, semana 8, vídeo 04: função passada como argumento
- [[wiki/sources/javascript-ninja-iife]]: JavaScript Ninja, semana 9, vídeo 03: anônima invocada pela variável ou pela propriedade
