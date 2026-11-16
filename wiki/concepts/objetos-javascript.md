---
type: concept
title: "Objetos em JavaScript (literal, this e protótipo)"
aliases: ["objeto", "object literal", "objeto literal", "this", "protótipo", "prototype chain", "cadeia de protótipos", "method shorthand", "autoboxing"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 4
tags: [javascript, objetos, this, prototipo, metodos, es6]
skill: lang-dynamic
status: stub
---

# Objetos em JavaScript

Coleção de propriedades chave → valor. Uma propriedade cujo valor é função se chama **método**. É o único tipo não primitivo; arrays, funções, datas e o próprio `console` são objetos ([[wiki/concepts/tipos-primitivos-javascript]]). `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects

```js
const retangulo = {
  a: 4,
  b: 8,
  area() { return this.a * this.b },        // method shorthand (ES2015)
  perimetro: function () { return 2 * this.a + 2 * this.b },
}
retangulo.area()      // 32
retangulo['a']        // 4, colchetes aceitam chave variável
retangulo.border = 1  // cria propriedade nova, mesmo com const
```

## this

Dentro de um método chamado como `obj.metodo()`, `this` é `obj`. O valor depende da chamada, não do lugar onde a função foi escrita: `const f = retangulo.area; f()` perde o `this`. Arrow functions não têm `this` próprio; como método, pegam o de fora ([[wiki/concepts/arrow-functions]]).

## Protótipo

Todo objeto aponta para outro, o seu protótipo, de onde herda propriedades. `{}` herda de `Object.prototype` (`toString`, `hasOwnProperty`); arrays, de `Array.prototype` (`map`, `filter`). Primitivos não são objetos, mas `'abc'.length` e `(26).toFixed(1)` funcionam porque o motor embrulha o valor num objeto temporário (`String`, `Number`) que usa `String.prototype` ou `Number.prototype` (*autoboxing*). `class` (ES2015) é sintaxe sobre essa cadeia ([[wiki/concepts/programacao-orientada-a-objetos]]).

## Vários objetos do mesmo formato

Um literal descreve um objeto só. Para criar vários: função fábrica (`const criaRetangulo = (a, b) => ({ a, b, area() { return this.a * this.b } })`) ou `class Retangulo { constructor(a, b) {...} }`.

## Utilidades

- `Object.keys`, `Object.values`, `Object.entries` para percorrer.
- Spread (`{ ...obj, a: 2 }`) para copiar com mudança; `Object.freeze` para impedir mutação ([[wiki/concepts/imutabilidade]]).
- Desestruturação: `const { a, b } = retangulo` ([[wiki/concepts/desestruturacao-javascript]]).
- `JSON.stringify` e `JSON.parse` convertem de e para texto ([[wiki/concepts/json]]).

Relacionado: [[wiki/concepts/objeto-vs-estrutura-de-dados]], [[wiki/concepts/abstracao]].

## No FrontPUSH

Em [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]], [[wiki/entities/nasser|Násser]] parte da abstração (a caneta tem características e funções), monta `quadrado` e `retangulo` com atributos e métodos, troca o parâmetro por `this.lado`, mostra o *method shorthand* "do JavaScript 6" e muda e acrescenta propriedades depois de criado. O "filho de outro objeto" é a cadeia de protótipos; o "toda variável já é um objeto" ignora que primitivos só são embrulhados no acesso.

Em [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]], o array é "um objeto do tipo array" que "herdou muitas funções e propriedades de forma nativa" (`indexOf`, `join`, `map`, `pop`, `push`): aqui o "tudo é objeto" está certo, via `Array.prototype`.

Em [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]], o "filho de outro objeto" vira literal: um `h1` é `HTMLHeadingElement` → `HTMLElement` → `Element` → `Node` → `EventTarget`, e daí vêm `innerText`, `classList` e `addEventListener`.

Em [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]], o `event` é o objeto que o navegador entrega ao listener: "sempre coloca no console para você ver quais são as propriedades", porque cada tipo de evento traz propriedades diferentes. `this` aparece como "o próprio evento" e depois, certo, como "o próprio elemento".

## Key sources

- [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]: FrontPUSH, JavaScript aula 05: literal, ponto, this, method shorthand, mutação, "filho de outro objeto"
- [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]]: FrontPUSH, JavaScript aula 06: array como objeto que herda de Array.prototype
- [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]]: FrontPUSH, JavaScript aula 08: elementos do DOM e a cadeia de protótipos
- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: event como objeto a explorar
