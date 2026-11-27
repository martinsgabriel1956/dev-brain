---
type: concept
title: "null e undefined no JavaScript"
aliases: ["null", "undefined", "Cannot read property of null", "Cannot read properties of null", "TypeError null"]
date_created: 2026-11-16
date_updated: 2026-11-27
source_count: 16
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

## No JavaScript Ninja, aula 04 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-funcoes]], função sem `return` devolve `undefined` ("o valor é indefinido"), e uma variável que só existe dentro da função, lida de fora, dá "não está definido", que é `ReferenceError`, não `undefined`.

## No JavaScript Ninja, semana 3, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]], os dois são "os valores especiais": um significa "que um valor não foi passado ou não existe" para a propriedade, o argumento ou a variável; o `null` é passado de propósito, "dizendo a esse cara que não tem [...] valor nenhum", e precisa ser atribuído explicitamente. Para variável não declarada, a mesma tensão da aula 01: é `ReferenceError`, não `undefined`.

## No JavaScript Ninja, semana 4, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-truthy-e-falsy]], "o null é um valor falso". `undefined` também é falsy, mas não aparece em nenhum trecho legível da legenda. Os dois são os únicos que o `??` trata como ausência; o `||` troca qualquer falsy `[external]`.

## No JavaScript Ninja, semana 4, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]], a variável local lida de fora "não está definida". É `ReferenceError: x is not defined`, não o valor `undefined`, que só aparece em nome declarado sem valor.

## No JavaScript Ninja, semana 7, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-arrays-propriedade-length]], ler um índice que não existe (`array[5]` num array de 5, ou `array[-1]`) dá `undefined`, sem erro: "ele tentou imprimir o quinto [...] que o quinto não existe". `null` aparece como item do array. `[external]` `null.bola` lança `TypeError`; `?.` evita.

## No JavaScript Ninja, semana 8, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]], a função atribuída a variável sem `return` devolve `undefined` quando invocada, "porque eu não tenho nenhum retorno para essa expressão aqui".

## No JavaScript Ninja, semana 8, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]], a função sem `return` "é executável e não retorna nada" (devolve `undefined`). `[external]` Ler no objeto-função uma propriedade que só existe no objeto retornado também dá `undefined`: `retornaObjeto.lastName` (verificado).

## No JavaScript Ninja, semana 9, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-escopo-de-funcoes]], a aula espera `undefined` de `return sum()` com `sum` declarada depois, e a função roda. `[external]` Onde o `undefined` aparece de fato é nas variáveis: `var` depois do `return` existe com valor `undefined`, e `undefined + undefined` dá `NaN` (verificado). O erro de chamar `sum()` fora da função é `ReferenceError`, não `undefined`.

## No JavaScript Ninja, semana 9, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-hoisting]], a `var` lida antes da declaração vale `undefined` ("ele não disse que a variável não existia"), e uma nunca declarada dá "não foi definida". É a diferença `undefined` × `ReferenceError` desta página, mostrada no `console.log`. A função sem `return` imprime `undefined`, o "valor em branco" da aula.

## No JavaScript Ninja, semana 10, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-wrapper-objects]], o wrapper explica `name.length` em primitivos. `null` e `undefined` são os únicos primitivos sem wrapper, por isso `null.length` dá `TypeError: Cannot read properties of null` (verificado; [[wiki/concepts/wrapper-objects-javascript]]).

## Key sources

- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: o erro "style de null" com o script antes do elemento
- [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]]: FrontPUSH, JavaScript aula 02: variável sem valor é undefined; null ausente
- [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]]: FrontPUSH, JavaScript aula 03: undefined é falsy
- [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]]: JavaScript Ninja, aula 01: "a mesma coisa" na maior parte das vezes; undefined ≠ variável inexistente
- [[wiki/sources/javascript-ninja-funcoes]]: JavaScript Ninja, aula 04: função sem return dá undefined
- [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]]: JavaScript Ninja, semana 3, vídeo 01: valores especiais; null atribuído de propósito
- [[wiki/sources/javascript-ninja-truthy-e-falsy]]: JavaScript Ninja, semana 4, vídeo 01: null falsy; undefined ilegível
- [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]]: JavaScript Ninja, semana 4, vídeo 03: "não está definido" é ReferenceError
- [[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos]]: JavaScript Ninja, semana 5, vídeo 01: sem return e índice inexistente dão undefined
- [[wiki/sources/javascript-ninja-parametros-de-funcoes-como-arrays-e-objetos]]: JavaScript Ninja, semana 5, vídeo 02: parâmetro ausente é undefined; `undefined.curso` lança TypeError
- [[wiki/sources/javascript-ninja-arrays-propriedade-length]]: JavaScript Ninja, semana 7, vídeo 02: índice inexistente dá undefined; null como item
- [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]]: JavaScript Ninja, semana 8, vídeo 01: função sem return devolve undefined
- [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]]: JavaScript Ninja, semana 8, vídeo 02: sem return, undefined; propriedade lida na função em vez do retorno
- [[wiki/sources/javascript-ninja-escopo-de-funcoes]]: JavaScript Ninja, semana 9, vídeo 01: undefined esperado × função içada; var içada com undefined
- [[wiki/sources/javascript-ninja-hoisting]]: JavaScript Ninja, semana 9, vídeo 02: var içada vale undefined; nunca declarada dá ReferenceError
- [[wiki/sources/javascript-ninja-wrapper-objects]]: JavaScript Ninja, semana 10, vídeo 01: null e undefined não têm wrapper
