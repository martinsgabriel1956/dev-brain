---
type: concept
title: "Operadores lógicos em JavaScript (&&, ||, !, ??)"
aliases: ["&&", "||", "!", "??", "AND OR NOT em JavaScript", "curto-circuito", "short-circuit evaluation", "operador E", "operador OU", "operador not", "nullish coalescing"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 5
tags: [javascript, operadores, operadores-logicos, boolean, curto-circuito, precedencia, lang-dynamic]
skill: lang-dynamic
status: stub
---

# Operadores lógicos em JavaScript (&&, ||, !, ??)

A versão JavaScript de AND, OR e NOT da [[wiki/concepts/logica-booleana]]. Com booleanos, a tabela é a clássica: `&&` só é true se os dois lados forem true; `||`, se pelo menos um for; `!` inverte. Com outros valores, entram duas regras que a tabela não mostra. `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#binary_logical_operators

## Devolvem um operando, não um booleano

- `a && b`: se `a` for falsy, devolve `a`; senão, devolve `b`. `'a' && 0` é `0`; `null && x` é `null`.
- `a || b`: se `a` for truthy, devolve `a`; senão, devolve `b`. `'' || 'padrão'` é `'padrão'`.
- `!a` sempre devolve booleano; `!!a` é a conversão explícita (igual a `Boolean(a)`).

Truthy e falsy em [[wiki/concepts/truthy-e-falsy]].

## Curto-circuito

O lado direito só é avaliado quando necessário: `&&` para no primeiro falsy, `||` no primeiro truthy. Daí os idiomas `obj && obj.prop`, `valor || padrao`, `cond && fazAlgo()` e o `cond && <Componente />` do React ([[wiki/concepts/renderizacao-condicional]]). Efeitos colaterais no lado direito podem não acontecer.

## `??` (ES2020)

`a ?? b` devolve `b` só se `a` for `null` ou `undefined`, ao contrário do `||`, que troca qualquer falsy (`0 || 10` é `10`; `0 ?? 10` é `0`). Misturar `??` com `&&` ou `||` sem parênteses é `SyntaxError` ([[wiki/concepts/null-e-undefined]]). Atribuições lógicas `&&=`, `||=`, `??=` (ES2021) em [[wiki/concepts/atribuicao-composta]].

## Precedência

`!` > relacionais (`<`, `>=`) > igualdade (`===`, `!==`) > `&&` > `||` > `??`. Consequências:

- `x === 3 && y === 7` dispensa parênteses.
- `a || b && c` é `a || (b && c)`.
- `!x === 3` é `(!x) === 3`, não `!(x === 3)`. Para negar uma comparação, `x !== 3` ([[wiki/concepts/pitfalls-de-linguagem]], [[wiki/concepts/igualdade-javascript]]).

De Morgan para simplificar condições: `!(a && b)` é `!a || !b`; `!(a || b)` é `!a && !b`.

## No JavaScript Ninja, semana 2, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-logicos]], os três operadores com `x = 3` e `y = 7`: `x === 3 && y === 7` é true, "ele só retorna true quando os dois valores são verdadeiros"; `x === 3 || y === 3` é true porque basta um lado; o not "vai inverter um valor", mas negar a comparação "não é utilizado". A aula diz que eles "sempre [retornam true] ou falso", o que só vale com operandos booleanos, e não fala de curto-circuito.

Relacionado: [[wiki/concepts/estruturas-condicionais-javascript]], [[wiki/concepts/tipos-primitivos-javascript]].

## `!` como operador unário

[[wiki/sources/javascript-ninja-operadores-unarios]], a aula seguinte, não cita o `!`, mas ele é o terceiro unário ao lado de `+x` e `-x`: os três convertem o operando (para booleano ou número) e não alteram a variável ([[wiki/concepts/operadores-unarios-javascript]]).

## No JavaScript Ninja, semana 2, vídeo 04 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]], `&&` e `||` entram no `if` porque "retornam também valores booleanos": `if (x === y && x === 3)` e `if (x === 5 || ...)`. Com comparações de cada lado, é verdade; com valores quaisquer, o `if` recebe um operando e o converte ([[wiki/concepts/estruturas-condicionais-javascript]]).

## No JavaScript Ninja, semana 4, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-truthy-e-falsy]], o `!` aparece aplicado a valores quaisquer, não só a comparações, e o `!!` como conversão explícita. É a peça que faltava para entender por que `&&` e `||` decidem por truthy/falsy ([[wiki/concepts/truthy-e-falsy]]).

## No JavaScript Ninja, semana 4, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-condicional-ternario]], o ternário é a alternativa explícita ao `cond && valor` e ao `valor || padrao` quando os dois ramos importam; não troca `0` ou `''` por engano ([[wiki/concepts/operador-ternario-javascript]]).

## Key sources

- [[wiki/sources/javascript-ninja-operadores-logicos]]: JavaScript Ninja, semana 2, vídeo 01: &&, || e ! com comparações estritas
- [[wiki/sources/javascript-ninja-operadores-unarios]]: JavaScript Ninja, semana 2, vídeo 02: ! entre os unários
- [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]]: JavaScript Ninja, semana 2, vídeo 04: && e || dentro do if
- [[wiki/sources/javascript-ninja-truthy-e-falsy]]: JavaScript Ninja, semana 4, vídeo 01: `!` e `!!` com valores quaisquer
- [[wiki/sources/javascript-ninja-condicional-ternario]]: JavaScript Ninja, semana 4, vídeo 02: ternário × && e ||
