---
type: concept
title: "Atribuição composta (+=, -=, *=, /=)"
aliases: ["+=", "-=", "*=", "/=", "%=", "**=", "operadores de atribuição", "compound assignment", "atribuição abreviada", "&&=", "||=", "??="]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 1
tags: [javascript, operadores, atribuicao, expressoes]
skill: lang-dynamic
status: stub
---

# Atribuição composta (`+=`, `-=`, `*=`, `/=`)

`x op= y` é atalho para `x = x op y`: `soma += 20` é `soma = soma + 20`. Existem para todos os aritméticos (`+=`, `-=`, `*=`, `/=`, `%=`, `**=`), para os bit a bit (`<<=`, `&=`...) e, desde o ES2021, para os lógicos: `a ||= b`, `a &&= b`, `a ??= b`, que só atribuem se a condição pedir. `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#assignment_operators

- É uma **expressão**: vale o novo valor (`(x += 2)` devolve o resultado) ([[wiki/concepts/expressao-javascript]]).
- `+=` segue a regra do `+`: com string, concatena. `let s = '5'; s += 1` dá `'51'`, enquanto `s++` daria 6 ([[wiki/concepts/incremento-e-decremento]]).
- `x += 1` é a forma que o ESLint (`no-plusplus`) e vários guias preferem a `x++`.
- Não funciona com `const`: reatribuir lança `TypeError` ([[wiki/concepts/var-let-const]]).

## No JavaScript Ninja (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-aritmeticos]], "mais igual, menos igual, vezes igual, dividido igual" são "outro formato de utilizar os operadores aritméticos abreviados": `soma += 20` leva 21 a 41, `soma -= 20` volta a 21. "Isso aqui é basicamente igual a soma igual soma mais 20." Faltam `%=`, `**=` e os lógicos.

## Key sources

- [[wiki/sources/javascript-ninja-operadores-aritmeticos]]: +=, -=, *=, /= com a variável soma
