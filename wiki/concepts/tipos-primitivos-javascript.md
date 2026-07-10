---
type: concept
title: "Tipos Primitivos em JavaScript"
aliases: ["8 tipos de javascript", "typeof javascript", "primitive types javascript", "Object.prototype.toString"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 1
tags: [javascript, tipagem, type-checking, fundamentos]
skill: lang-dynamic
status: draft
---

# Tipos Primitivos em JavaScript

Apesar de JavaScript ser uma linguagem de **tipagem fraca** (fraca no sentido de conversão implícita de tipo entre operações — ver [[wiki/concepts/sistema-de-tipos]]), ela define **oito tipos** de valor: `null`, `undefined`, `boolean`, `number`, `bigint`, `string`, `symbol` e `object`.

## Duas formas de checar tipo

| | `typeof valor` | `Object.prototype.toString.call(valor)` |
|---|---|---|
| **Precisão** | Menos precisa — `typeof null` retorna `"object"` | Mais precisa — retorna `"[object Null]"`, `"[object Array]"` etc. |
| **Motivo** | Internamente, tudo em JS deriva de `Object` | Lê a assinatura interna `[[Class]]` do valor |
| **Uso histórico** | Checagem rápida do dia a dia | Usado por bibliotecas como Underscore para type-checking mais confiável |

`typeof` erra de forma notória em dois casos: `typeof null === "object"` (bug histórico da linguagem, mantido por compatibilidade) e `typeof NaN === "number"` (`NaN` significa "Not a Number", mas seu tipo *é* `number`).

## Os 8 tipos

| # | Tipo | `typeof` |
|---|---|---|
| 1 | `null` | `"object"` |
| 2 | `undefined` | `"undefined"` |
| 3 | `boolean` | `"boolean"` |
| 4 | `number` | `"number"` |
| 5 | `bigint` | `"bigint"` |
| 6 | `string` | `"string"` |
| 7 | `symbol` | `"symbol"` |
| 8 | `object` | `"object"` |

`Array`, `Date`, funções etc. não são tipos primitivos separados — são todos estruturas construídas sobre `object` (funções são exceção parcial: `typeof` de uma função retorna `"function"`).

## `undefined` vs. `null` em valores default

Uma distinção sutil e fonte comum de bugs: **parâmetros default de função só reagem a `undefined`**, não a `null` — porque `null` é considerado um valor "de verdade", enquanto `undefined` é a ausência de valor.

```js
function bar(a = [1, 2, 3]) { return a; }
bar();       // [1, 2, 3] — sem argumento, undefined aciona o default
bar(null);   // null — null É um valor, default não é acionado
```

Já expressões booleanas com `||` (`a = a || [1, 2, 3]`) reagem a **qualquer** valor falsy (`0`, `""`, `null`, `undefined`, `false`, `NaN`) — não só `undefined`. Confundir os dois mecanismos é uma armadilha comum: `bar(0)` com default de parâmetro preserva `0`, mas `a = a || fallback` substitui `0` pelo fallback.

## Conversão de tipo em concatenação e comparação

- `string + number` sempre vira concatenação de string, em qualquer ordem: `"1" + 2` e `1 + "2"` ambos retornam `"12"`.
- `==` faz conversão de tipo antes de comparar (`null == undefined` → `true`); `===` não converte nada. Ver detalhamento em [[wiki/concepts/pitfalls-de-linguagem]].

## Relação com outros conceitos

- [[wiki/concepts/sistema-de-tipos]] — tipagem fraca é sobre *conversão implícita entre tipos*, um eixo distinto (mas relacionado) de tipagem estática vs. dinâmica
- [[wiki/concepts/pitfalls-de-linguagem]] — `typeof null`, `==` vs `===` e coerção implícita já documentados ali como armadilhas gerais; esta página aprofunda o mecanismo tipo a tipo

## Key sources

- [[wiki/sources/8-tipos-de-javascript]]
