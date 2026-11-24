---
type: concept
title: "Operadores aritméticos em JavaScript"
aliases: ["operadores aritméticos", "operador de resto", "módulo %", "operadores JavaScript", "coerção com +"]
date_created: 2026-11-16
date_updated: 2026-11-24
source_count: 5
tags: [javascript, operadores, aritmetica, coercao, number]
skill: lang-dynamic
status: stub
---

# Operadores aritméticos em JavaScript

`+` (soma), `-` (subtração), `*` (multiplicação), `/` (divisão), `%` (resto) e `**` (potência, ES2016). Também `++` e `--` (incremento e decremento) e as atribuições compostas (`+=`, `-=`...). `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators

## Armadilhas

- **`+` com string concatena:** `'200' + 200` dá `'200200'`; os outros operadores convertem para número: `'200' - 200` dá `0`. É a mesma coerção implícita que faz `==` diferir de `===` ([[wiki/concepts/igualdade-javascript]]).
- **Divisão não é inteira:** `7 / 2` dá `3.5`; para o quociente inteiro, `Math.trunc(7 / 2)`.
- **Ponto flutuante:** todo `number` é IEEE 754, então `0.1 + 0.2` dá `0.30000000000000004`. Para dinheiro, guardar em centavos ou usar `bigint` ([[wiki/concepts/tipos-primitivos-javascript]]).
- **`%` é resto, não módulo matemático:** `-7 % 3` dá `-1`. O uso típico num `if` é testar par ou ímpar (`n % 2 === 0`).
- **Divisão por zero** dá `Infinity`, e `0 / 0` dá `NaN`; não lança erro.

Nas condicionais, quem decide são os operadores de comparação (`===`, `<`, `>`) e lógicos (`&&`, `||`, `!`); os aritméticos calculam o valor comparado ([[wiki/concepts/logica-de-programacao]]).

## No FrontPUSH

Em [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]], [[wiki/entities/nasser|Násser]] mostra `var soma = 200 + 200` e as cinco operações (mais, menos, multiplicação, divisão, resto), "que a gente vai trabalhar, por exemplo, em estruturas condicionais".

Em [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]], a aula 03 usa os comparadores (`>`, `>=`, `==`, `===`) e os lógicos (`&&`, `||`, `!`) que decidem as condições, como esta página já antecipava ([[wiki/concepts/estruturas-condicionais-javascript]]).

Em [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]], `i++` "é exatamente igual" a `i = i + 1`. Como instrução, sim; como expressão, `i++` devolve o valor antigo e `++i` o novo.

## No JavaScript Ninja, aula 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-aritmeticos]], são "quatro tipos de operadores aritméticos" (`+`, `-`, `*`, `/`), sem `%` nem `**`, mais os "abreviados": [[wiki/concepts/incremento-e-decremento|++ e --]] e a [[wiki/concepts/atribuicao-composta|atribuição composta]] (`+=`, `-=`, `*=`, `/=`). Espaço em volta do operador "não tem diferença nenhuma", mas deixa o código "mais legível". Coerção com string não aparece.

## No JavaScript Ninja, aula 03 (Fernando Daciuk)

[[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]] continua a série com os comparadores; a coerção que o `+` faz com string reaparece no `==` (`'1' == 1`) ([[wiki/concepts/igualdade-javascript]]).

## Key sources

- [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]]: FrontPUSH, JavaScript aula 02: as cinco operações aritméticas
- [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]]: FrontPUSH, JavaScript aula 03: comparadores e lógicos
- [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]]: FrontPUSH, JavaScript aula 06: i++ como i = i + 1
- [[wiki/sources/javascript-ninja-operadores-aritmeticos]]: JavaScript Ninja, aula 02: quatro operadores, ++/-- e +=; espaços para legibilidade
- [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]]: JavaScript Ninja, aula 03: continuação com igualdade e relacionais
