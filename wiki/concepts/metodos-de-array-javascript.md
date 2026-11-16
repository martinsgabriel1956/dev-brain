---
type: concept
title: "Métodos de array em JavaScript (forEach, map, filter, reduce...)"
aliases: ["forEach", "map", "filter", "reduce", "find", "some", "every", "métodos de array", "array methods", "pop", "push"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [javascript, array, foreach, map, filter, reduce, callback, imutabilidade]
skill: lang-dynamic
status: stub
---

# Métodos de array em JavaScript

Métodos de `Array.prototype` que recebem um callback `(item, índice, array)` e percorrem o array sem índice manual ([[wiki/concepts/callback-javascript]]). `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

## Os principais

| Método | Devolve | Uso |
|---|---|---|
| `forEach(fn)` | `undefined` | efeito para cada item (log, DOM) |
| `map(fn)` | array novo, mesmo tamanho | transformar cada item (o retorno de `fn`) |
| `filter(fn)` | array novo, só os que passam | filtrar por condição (truthy) |
| `find(fn)` / `findIndex(fn)` | o primeiro item (ou índice) | buscar um |
| `some(fn)` / `every(fn)` | booleano | algum / todos passam |
| `reduce(fn, inicial)` | um valor | somar, agrupar, montar objeto |

`forEach`, `map`, `filter` e `reduce` não alteram o array original. Já `push`, `pop`, `shift`, `unshift`, `splice`, `sort` e `reverse` mudam o array no lugar; `toSorted`, `toReversed` e `toSpliced` (ES2023) são as versões que devolvem cópia ([[wiki/concepts/imutabilidade]]).

## Armadilhas

- `map` com chaves e sem `return` devolve um array de `undefined` ([[wiki/concepts/arrow-functions]]).
- `forEach` não para com `break` e não espera `await`; para isso, `for...of` ([[wiki/concepts/estruturas-de-repeticao-javascript]]).
- `const x = arr.forEach(...)` é sempre `undefined`.
- Encadear é comum: `pedidos.filter(p => p.pago).map(p => p.total)`.

## No React

Listas viram JSX com `map`, cada elemento com `key` estável; `forEach` não serve porque não devolve nada ([[wiki/entities/react]]). Atualizar estado com cópia (`[...lista, novo]`, `lista.filter(...)`) em vez de `push`.

Relacionado: [[wiki/concepts/array]], [[wiki/concepts/funcoes-javascript]].

## No FrontPUSH

Em [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]], [[wiki/entities/nasser|Násser]] mostra o `forEach` (item, índice, array, "o que importa é a ordem") e o `map`, que "devolve um array modificado, enquanto o forEach não devolve nada", juntando `marcas` e `carros` pela posição. Na [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript|aula 06]], `pop`, `push` e `length`.

## No JStack, aula 06

Em [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]], `routes.find(routeObject => ...)` devolve o primeiro objeto de rota que casa método e caminho, ou `undefined`; o `if (route)` decide entre chamar o handler e responder 404.

## Key sources

- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: forEach, map e a diferença entre os dois
- [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: find na tabela de rotas
