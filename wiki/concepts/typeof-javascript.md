---
type: concept
title: "Operador typeof em JavaScript"
aliases: ["typeof", "operador typeof", "typeof null", "typeof operator", "checagem de tipo em tempo de execução", "type guard typeof"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 1
tags: [javascript, typeof, operador-unario, tipos-primitivos, validacao-de-argumentos]
skill: lang-dynamic
status: stub
---

# Operador typeof em JavaScript

Operador unário que devolve, como string, o tipo do operando. É confiável para primitivos e falho para objetos: tudo que não é função dá `'object'`, inclusive array e `null`. `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof

| Operando | `typeof` |
|---|---|
| `undefined`, variável não declarada | `'undefined'` |
| `true` / `false` | `'boolean'` |
| `1`, `NaN`, `Infinity` | `'number'` |
| `'JS Ninja'` | `'string'` |
| `Symbol()` | `'symbol'` |
| `1n` | `'bigint'` |
| `function () {}`, `class {}` | `'function'` |
| `{}`, `[]`, `new String('a')`, **`null`** | `'object'` |

Todos verificados no Node 22.23.

## Armadilhas

- **`typeof null === 'object'`** é bug da primeira implementação (tag de tipo 0, o mesmo dos objetos). Uma proposta de corrigir no ES6 foi rejeitada por compatibilidade `[external]`. Para `null`, usar `x === null` ([[wiki/concepts/null-e-undefined]]).
- **`typeof NaN === 'number'`**: a guarda `typeof x === 'number'` deixa `NaN` passar. `Number.isFinite(x)` não deixa `[external]`.
- **Array e objeto** caem juntos em `'object'`: `Array.isArray(x)` ([[wiki/concepts/array]]); objeto não nulo, `x !== null && typeof x === 'object'`; tipo exato, `Object.prototype.toString.call(x)` ([[wiki/concepts/tipos-primitivos-javascript]]).
- **Zona morta temporal:** `typeof y` antes de `let y` dá `ReferenceError`, embora `typeof naoDeclarada` dê `'undefined'` ([[wiki/concepts/hoisting-javascript]]).

## Uso como guarda

```js
function subtract(num1, num2) {
  if (typeof num1 === 'number' && typeof num2 === 'number') {
    return num1 - num2
  }
  return 'Entre com dois números'
}
subtract(10, 2)    // 8
subtract('10', 2)  // 'Entre com dois números'
subtract(NaN, 1)   // NaN: passou na guarda
```

Em TypeScript, o mesmo `typeof` dentro de `if` é *type guard* e estreita o tipo no bloco `[external]`. Ver [[wiki/concepts/validacao-de-entrada]].

## No JavaScript Ninja, semana 10, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-typeof]], a regra é "você pode confiar no typeof se você for utilizar ele para valores primitivos, de preferência número, string e Boolean". O bug do `null` é apresentado como "já documentado", com a previsão, que não se cumpriu, de que o ES6 o corrigiria. A guarda acima é a demo da aula (o texto exato da mensagem está ilegível na legenda).

## Relação com outros conceitos

- [[wiki/concepts/operadores-unarios-javascript]]: família do operador.
- [[wiki/concepts/wrapper-objects-javascript]]: `typeof new String('a')` dá `'object'`.
- [[wiki/concepts/sistema-de-tipos]]: checagem em tempo de execução de uma linguagem dinâmica.

## Key sources

- [[wiki/sources/javascript-ninja-typeof]]: JavaScript Ninja, semana 10, vídeo 02: tabela do typeof; typeof null; guarda em subtract
