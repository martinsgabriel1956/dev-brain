---
type: concept
title: "Currying e aplicação parcial"
aliases: ["currying", "curry", "função curried", "aplicação parcial", "partial application"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 2
tags: [javascript, funcoes, programacao-funcional, currying, aplicacao-parcial, closure]
skill: lang-dynamic
status: stub
---

# Currying e aplicação parcial

**Currying** transforma uma função de vários argumentos numa sequência de funções de um argumento cada: `soma(a, b)` vira `soma(a)(b)` `[external]` (https://developer.mozilla.org/en-US/docs/Glossary/Currying). O nome vem do lógico Haskell Curry (de memória, não verificado). **Aplicação parcial** é fixar parte dos argumentos e receber de volta uma função que espera o resto. Com a versão curried, aplicar parcialmente é só chamar a primeira função.

```js
const adder = x => y => x + y;   // curried
const add2 = adder(2);           // aplicação parcial: x fixado em 2
add2(3);                         // 5
adder(5)(8);                     // 13, duas invocações seguidas
[1, 2, 3].map(adder(10));        // a função pré-configurada vira callback
```

Precisa de [[wiki/concepts/funcoes-de-primeira-classe|funções de primeira classe]] (para retornar a função) e de [[wiki/concepts/closure-javascript|closures]] (para a função interna lembrar o primeiro argumento). É prática comum de [[wiki/concepts/programacao-funcional]]. Em Haskell toda função é curried. Em JavaScript é opcional, e `fn.bind(null, 2)` faz aplicação parcial sem reescrever a função `[external]`.

## No JavaScript Ninja, semana 8, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]], `adder(2)` devolve a função `add2`, `add2(3)` dá 5 e `adder(5)(8)` dá 13. A aula pergunta "qual a vantagem disso?" sem dar o nome currying e sem responder com um caso de uso; diz só que, sem funções de primeira classe, "você precisa passar os dois parâmetros [...] direto".

## No JavaScript Ninja, semana 8, vídeo 04 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-programacao-funcional-parte-3]], a função vira parâmetro, e com isso a pergunta do vídeo anterior ("qual a vantagem disso?") ganha resposta: `[1, 2, 3].map(adder(10))` dá `[11, 12, 13]` (verificado no Node 22). A aula não junta os dois vídeos.

## Key sources

- [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]]: JavaScript Ninja, semana 8, vídeo 03: adder(2)(3) e adder(5)(8), sem o nome do padrão
- [[wiki/sources/javascript-ninja-programacao-funcional-parte-3]]: JavaScript Ninja, semana 8, vídeo 04: a função curried vira callback
