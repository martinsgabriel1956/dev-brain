---
type: concept
title: "for...in e o operador in (JavaScript)"
aliases: ["for...in", "for in", "for-in", "operador in", "in", "percorrer propriedades", "enumerar chaves", "guard-for-in", "Object.hasOwn"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 1
tags: [javascript, loops, objetos, propriedades, prototipo, operador-in]
skill: lang-dynamic
status: stub
---

# for...in e o operador in

O `for...in` percorre as **chaves** de um objeto; o operador `in` testa se uma chave existe nele. Os dois olham a cadeia de [[wiki/concepts/objetos-javascript|protótipos]], não só o objeto. `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in

```js
var car = { brand: 'VW', model: 'Gol', year: 2013 }

for (var prop in car) {
  console.log(prop, car[prop])   // brand VW / model Gol / year 2013
}

'brand' in car       // true
2 in car             // false
'toString' in car    // true: herdada de Object.prototype
Object.hasOwn(car, 'toString')   // false: só as próprias
```

A chave vem como string, por isso o valor se lê com colchetes, `car[prop]`, e não com ponto ([[wiki/concepts/notacao-de-ponto-e-colchetes]]).

## Armadilhas

- **Herdadas entram no laço.** O `for...in` lista toda chave enumerável da cadeia. Para só as próprias: `if (Object.hasOwn(obj, k))` dentro do laço (regra `guard-for-in` do ESLint) ou `Object.keys(obj)` / `Object.entries(obj)` `[external]`.
- **Não usar em array.** Os índices vêm como strings (`'0'`, `'1'`), e o que alguém pendurar em `Array.prototype` aparece no laço. Para valores, `for` com índice, `forEach` ou `for...of` ([[wiki/concepts/estruturas-de-repeticao-javascript]], [[wiki/concepts/array]], [[wiki/concepts/pitfalls-de-linguagem]]).
- **Ordem.** Desde o ES2020: chaves que são índices inteiros em ordem crescente, depois as strings na ordem de inserção. `{ b, 2, a, 1 }` dá `1, 2, b, a`.
- **`in` × valor.** Em array, `2 in ['a', 'b', 'c']` é `true` porque testa o índice 2, não o valor 2.
- **`in` × `undefined`.** `obj.x === undefined` não distingue "não existe" de "existe com `undefined`"; `'x' in obj` distingue ([[wiki/concepts/null-e-undefined]]).

## No JavaScript Ninja, semana 11, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-lacos-loops]], o `for...in` "serve pra você percorrer propriedades de um objeto": imprime as chaves de um carro (marca, modelo, ano) e, "no formato de array", os valores VW, Gol e 2013. O `in` sozinho testa "se uma propriedade também existe em um objeto" (`2 in car` é falso). O alerta da aula é desempenho: "ele é mais lento do que o for normal". Não fala das herdadas, que são o risco maior.

## Key sources

- [[wiki/sources/javascript-ninja-lacos-loops]]: JavaScript Ninja, semana 11, vídeo 01: for...in em objeto, car[prop], operador in, "mais lento que o for"
