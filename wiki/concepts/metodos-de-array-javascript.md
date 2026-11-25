---
type: concept
title: "Métodos de array em JavaScript (forEach, map, filter, reduce...)"
aliases: ["forEach", "map", "filter", "reduce", "find", "some", "every", "métodos de array", "array methods", "pop", "push"]
date_created: 2026-11-16
date_updated: 2026-11-25
source_count: 5
tags: [javascript, array, foreach, map, filter, reduce, callback, imutabilidade]
skill: lang-dynamic
status: stub
---

# Métodos de array em JavaScript

Métodos de `Array.prototype` que recebem um callback `(item, índice, array)` e percorrem o array sem índice manual ([[wiki/concepts/callback-javascript]]). `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

> No FrontPUSH, a lista "Filter, map, Index" do slide de pré-requisitos do React ([[wiki/sources/frontpush-o-que-preciso-saber-de-javascript-antes-do-react]]) cita "Index", que não é método: os candidatos são `indexOf` e `findIndex`.

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

## No JavaScript Ninja, semana 7, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-arrays-propriedade-length]], o fecho anuncia "o método do array" para o vídeo seguinte; até aqui o curso só usou a propriedade `length`.

## No JavaScript Ninja, semana 7, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-arrays-metodo-push-e-loop-for]], o primeiro método do curso é o `push`: "push significa empurrar", adiciona no fim e "já retorna o length do array" (de 6 para 7). Entra qualquer valor: objeto, `null`, outro array, função. A aula não diz que ele muda o array no lugar nem que aceita vários argumentos; um array empurrado vira um item só (para espalhar, `push(...outro)` ou `concat`).

## Key sources

- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: forEach, map e a diferença entre os dois
- [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: find na tabela de rotas
- [[wiki/sources/frontpush-o-que-preciso-saber-de-javascript-antes-do-react]]: FrontPUSH, React aula 02: filter, map, "index" e forEach para exibir JSON; "index" não existe (indexOf/findIndex ou 2º parâmetro do map)
- [[wiki/sources/javascript-ninja-arrays-propriedade-length]]: JavaScript Ninja, semana 7, vídeo 02: anuncia os métodos de array
- [[wiki/sources/javascript-ninja-arrays-metodo-push-e-loop-for]]: JavaScript Ninja, semana 7, vídeo 03: push adiciona no fim e devolve o length
