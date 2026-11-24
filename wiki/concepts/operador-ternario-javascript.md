---
type: concept
title: "Operador ternário (condicional) em JavaScript"
aliases: ["ternário", "operador condicional", "condicional ternário", "conditional operator", "?:", "ternary"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 1
tags: [javascript, operador-ternario, condicionais, expressoes]
skill: lang-dynamic
status: stub
---

# Operador ternário (condicional) em JavaScript

`condição ? valorSeTruthy : valorSeFalsy`. É o único operador do JavaScript com três operandos, daí o nome; o oficial é *operador condicional*. `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator

## Expressão, não instrução

O ternário produz um valor, então cabe onde o `if` não cabe: atribuição, argumento, `return`, template literal, JSX ([[wiki/concepts/expressao-javascript]]).

```js
var artigo = pessoa.sexo === 'feminino' ? 'a' : 'o';
```

Substitui só o `if`/`else` que escolhe um valor. Para efeitos colaterais, vários comandos por ramo ou `if` sem `else`, o `if` continua melhor ([[wiki/concepts/estruturas-condicionais-javascript]]).

## Condição por truthy/falsy

A condição passa por *ToBoolean*, como no `if`: `'sim' ? 'porta' : 'janela'` dá `'porta'` ([[wiki/concepts/truthy-e-falsy]]).

## Armadilhas

- `cond ? true : false` é redundante quando `cond` já é booleano; para converter, `Boolean(x)` ou `!!x` (regra `no-unneeded-ternary` do ESLint). `[external]`
- Precedência baixa e associatividade à direita: `a ? b : c ? d : e` é `a ? b : (c ? d : e)`. Ternários aninhados ficam difíceis de ler; acima de dois níveis, `if`/`else if` ou um objeto de mapeamento. `[external]`
- No JSX, `cond ? <A /> : null` é a forma segura contra o `0` renderizado de `cond && <A />` ([[wiki/concepts/renderizacao-condicional]], [[wiki/concepts/operadores-logicos-javascript]]).

## No JavaScript Ninja, semana 4, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-condicional-ternario]], o ternário "substitui o if": uma linha no lugar de cinco, com atribuição direta (`sexo = ... ? 'a' : 'o'`, do desafio 3) e condição por truthy/falsy (`'sim' ? 'porta' : 'janela'`). Só "para verificações pequenas": condições grandes ficam "ruim de ler". A aula chama o ternário de "instrução", mas é expressão; e usa `1 === 2 ? true : false`, que é redundante.

## Key sources

- [[wiki/sources/javascript-ninja-condicional-ternario]]: JavaScript Ninja, semana 4, vídeo 02: sintaxe, atribuição direta e uso só em verificações pequenas
