---
type: concept
title: "null e undefined no JavaScript"
aliases: ["null", "undefined", "Cannot read property of null", "Cannot read properties of null", "TypeError null"]
date_created: 2026-11-16
date_updated: 2026-11-24
source_count: 4
tags: [javascript, tipos, null, undefined, erros, dom, frontend]
skill: tech-mentor-frontend
status: stub
---

# null e undefined no JavaScript

Dois valores que representam "nada". `undefined` é o que o JavaScript dá a uma variável declarada sem valor, a um parâmetro não passado ou a uma propriedade que não existe. `null` é "vazio" colocado de propósito, por quem escreveu o código ou por uma API: `document.querySelector()` devolve `null` quando nenhum elemento casa com o seletor `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null). Ver [[wiki/concepts/tipos-primitivos-javascript]].

Nenhum dos dois tem propriedades. Ler `algo.style` quando `algo` é `null` lança `TypeError: Cannot read properties of null (reading 'style')` (nas versões antigas do Chrome, "Cannot read property 'style' of null").

`[skill: tech-mentor-frontend]` Para evitar o erro, verifique antes de usar (`if (el)`) ou use o encadeamento opcional (`el?.style`), e garanta que o script rode depois de o elemento existir (ver [[wiki/concepts/carregamento-de-scripts]]). `el ?? padrão` troca `null`/`undefined` por um valor padrão.

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], [[wiki/entities/mayk-brito|Mayk]] provoca o erro de propósito. Com o `<script>` no começo do body, `document.querySelector('#container').style...` roda antes de o container existir, e o console diz que não pôde "ler a propriedade style de null". `null` é "vazio", como a casa da música "que não tinha teto, não tinha nada"; "não tem propriedade nenhuma em null". A regra que fica: "sempre que você vir esse erro [...] significa que você não pegou o objeto do jeito que deveria ter pego". Ele cita de passagem a variante "of undefined", sem separar os dois casos.

Em [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]], `let nada` sem valor é "indefinida, ou seja, undefined". O `null` não aparece entre os tipos da aula.

Em [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]], `undefined` entra na lista de valores que o `if` "vai entender como falso". O item anterior não tem legenda e é provavelmente o `null`.

## No JavaScript Ninja, aula 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]], `null` é "nenhum valor" e `undefined`, "a ausência de valor", e "na maior parte das vezes a gente vai tratar eles como sendo a mesma coisa". A aula diz que `undefined` "representa quando a variável não existe", mas o erro de digitação ao vivo (`numero[3]`) mostra o contrário: variável inexistente lança `ReferenceError` ("não está definido"); `undefined` é o valor de uma variável declarada sem atribuição. `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined

## Key sources

- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: o erro "style de null" com o script antes do elemento
- [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]]: FrontPUSH, JavaScript aula 02: variável sem valor é undefined; null ausente
- [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]]: FrontPUSH, JavaScript aula 03: undefined é falsy
- [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]]: JavaScript Ninja, aula 01: "a mesma coisa" na maior parte das vezes; undefined ≠ variável inexistente
