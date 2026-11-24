---
type: concept
title: "Operadores unários em JavaScript"
aliases: ["operador unário", "unary operators", "mais unário", "menos unário", "unary plus", "unary minus", "+x", "-x", "typeof", "void", "delete"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 2
tags: [javascript, operadores, operadores-unarios, coercao, efeito-colateral, lang-dynamic]
skill: lang-dynamic
status: stub
---

# Operadores unários em JavaScript

Operador unário tem um operando só (`-x`), ao contrário do binário (`a - b`). `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#unary_operators

| Operador | Faz | Efeito colateral |
|---|---|---|
| `+x` | converte para número (`Number(x)`) | não |
| `-x` | converte para número e inverte o sinal | não |
| `!x` | converte para booleano e inverte ([[wiki/concepts/operadores-logicos-javascript]]) | não |
| `~x` | NOT bit a bit sobre inteiro de 32 bits (`~5` é `-6`) ([[wiki/concepts/bitwise-operations]]) | não |
| `typeof x` | devolve o tipo como string (`typeof NaN` é `'number'`) | não |
| `void x` | avalia e devolve `undefined` | não |
| `delete obj.p` | remove a propriedade | sim |
| `++x`, `x++`, `--x`, `x--` | soma ou subtrai 1 e grava ([[wiki/concepts/incremento-e-decremento]]) | sim |
| `await p` | espera a promise | (suspende a função) |

## Mais unário

`+x` aplica *ToNumber*: `+'3'` é `3`, `+''` e `+' '` são `0`, `+true` é `1`, `+null` é `0`, `+undefined` e `+'abc'` são `NaN`, `+[]` é `0`, `+'0x10'` é `16`. Com BigInt, `TypeError`. É a forma curta de `Number(x)`; diferente de `parseInt`, que lê o prefixo numérico (`parseInt('12px', 10)` é `12`, `+'12px'` é `NaN`) ([[wiki/concepts/tipos-primitivos-javascript]]).

Uso comum: converter antes de somar, já que o `+` binário concatena se um lado for string: `+'3' + 3` é `6`, `'3' + 3` é `'33'` ([[wiki/concepts/operadores-aritmeticos-javascript]]).

## Menos unário

Mesma conversão, sinal invertido: `-'3'` é `-3`, `-'abc'` é `NaN`. `-0` existe e é `=== 0`, mas `Object.is(-0, 0)` é false.

## Armadilhas

- `a + +b` soma `b` convertido; `a+++b` é `(a++) + b`; `- -x` precisa do espaço (`--x` é decremento) ([[wiki/concepts/pitfalls-de-linguagem]]).
- `typeof null` é `'object'`, erro histórico ([[wiki/concepts/null-e-undefined]]).

## No JavaScript Ninja, semana 2, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-unarios]], o `+` unário "vai tentar converter o valor que está vendo depois dele em número", ou dá `NaN`; o `-` unário faz o mesmo "e ele inverte o sinal". `-x` "não causa efeito colateral", enquanto `++`/`--` "causam o efeito colateral". Ficam de fora `typeof`, `void`, `delete` e `~`; o `!` foi o vídeo anterior.

## Key sources

- [[wiki/sources/javascript-ninja-operadores-unarios]]: JavaScript Ninja, semana 2, vídeo 02: + e - unários, concatenação, ++/-- com efeito colateral
- [[wiki/sources/javascript-ninja-metodos-de-objeto]]: JavaScript Ninja, semana 3, vídeo 02: ++ em propriedade, de novo chamado de "binário"
