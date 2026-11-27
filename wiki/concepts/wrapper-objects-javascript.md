---
type: concept
title: "Wrapper Objects em JavaScript (autoboxing)"
aliases: ["wrapper objects", "wrapper object", "objeto envoltório", "objetos wrapper", "autoboxing javascript", "new String", "new Number", "new Boolean", "primitive wrapper"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 1
tags: [javascript, wrapper-objects, autoboxing, tipos-primitivos, construtores, conversao-de-tipos]
skill: lang-dynamic
status: stub
---

# Wrapper Objects em JavaScript

Primitivos não são objetos e não têm propriedades. Mesmo assim, `'Daciuk'.length` dá 6 e `(26).toFixed(1)` funciona. Ao acessar uma propriedade num primitivo, o motor o embrulha num objeto do construtor correspondente (`String`, `Number`, `Boolean`, `Symbol`, `BigInt`), lê a propriedade, que vem do protótipo (`String.prototype` etc.), e descarta o embrulho. É o *autoboxing*. `[external]` https://developer.mozilla.org/en-US/docs/Glossary/Primitive

```js
var name = 'Daciuk'
name.length            // 6: wrapper String temporário
name.foo = 1
name.foo               // undefined: gravou no wrapper descartado ('use strict' dá TypeError)

var s = new String('Daciuk')
typeof s               // 'object'
s.valueOf()            // 'Daciuk', o primitivo de volta
s === 'Daciuk'         // false
s == 'Daciuk'          // true
!!new Boolean(false)   // true: todo objeto é truthy

null.length            // TypeError: null e undefined não têm wrapper
```

## Com new × sem new

| Forma | Resultado | Uso |
|---|---|---|
| `new String(x)`, `new Number(x)`, `new Boolean(x)` | Objeto wrapper (`typeof` dá `'object'`) | Quase nunca. ESLint `no-new-wrappers` proíbe `[external]` |
| `String(x)`, `Number(x)`, `Boolean(x)` | Primitivo convertido | Conversão explícita de tipo |
| `Symbol()`, `BigInt(1)` | Primitivo; `new` dá `TypeError` | Os wrappers existem (`Object(1n)`), mas só por autoboxing |

`Number(x)` equivale ao `+x` unário ([[wiki/concepts/operadores-unarios-javascript]]) e `Boolean(x)` equivale a `!!x` ([[wiki/concepts/truthy-e-falsy]]). Na conversão implícita de um wrapper, como em `new Number(30) + 1`, o motor chama `valueOf` (depois `toString`) via `ToPrimitive` `[external]`.

## Armadilhas

- Comparar wrapper com `===` falha ([[wiki/concepts/igualdade-javascript]]).
- `if (new Boolean(false))` entra no bloco.
- Dois `new String('a')` são objetos distintos: `new String('a') === new String('a')` dá `false`.
- Ver [[wiki/concepts/pitfalls-de-linguagem]].

## No JavaScript Ninja, semana 10, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-wrapper-objects]], a aula inteira é sobre o tema. O critério de objeto é ter "propriedades e métodos"; o paradoxo é `name.length` num primitivo; a resposta é o "objeto wrapper [...] um envoltório", criado para o acesso e descartado. Os construtores sem `new` "servem mais como conversores do que construtores". A aula cita três wrappers (os da era ES5); `Symbol` e `BigInt` ficaram de fora.

## Relação com outros conceitos

- [[wiki/concepts/tipos-primitivos-javascript]]: quais valores são primitivos.
- [[wiki/concepts/objetos-javascript]]: protótipo, de onde os métodos vêm.
- [[wiki/concepts/string]]: o caso mais comum (`length`, `toUpperCase`).
- [[wiki/concepts/sistema-de-tipos]]: conversão implícita como tipagem fraca.

## Key sources

- [[wiki/sources/javascript-ninja-wrapper-objects]]: JavaScript Ninja, semana 10, vídeo 01: wrapper como envoltório; new × sem new; valueOf
