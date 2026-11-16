---
type: concept
title: "Template literals (template strings) em JavaScript"
aliases: ["template string", "template strings", "crase", "interpolação de string", "concatenação de strings"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [javascript, string, es6, template-literals, concatenacao, interpolacao]
skill: lang-dynamic
status: stub
---

# Template literals

String delimitada por crase (`` ` ``), do ES2015 ([[wiki/concepts/ecmascript]]). Aceita interpolação com `${expressão}` e quebra de linha sem `\n`. Substitui a concatenação com `+`. `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals

```js
const nome = 'Násser'
const sobrenome = 'Yousef'
nome + sobrenome              // 'NásserYousef' (sem espaço)
nome + ' ' + sobrenome        // 'Násser Yousef'
`${nome} tem o sobrenome ${sobrenome}`
```

- **O que cabe no `${}`:** qualquer expressão (`${a + b}`, `${f()}`, `${ok ? 'sim' : 'não'}`). Comandos como `if` e `for` não cabem.
- **Conversão:** o resultado da expressão vira string; um objeto vira `[object Object]`.
- **Tagged templates:** `` tag`texto ${x}` `` passa as partes para uma função (ex.: `String.raw`, bibliotecas de SQL e CSS-in-JS).
- **Herança:** a interpolação veio do CoffeeScript, entre outros ([[wiki/concepts/transpilador]]). Ver também [[wiki/concepts/string]].

## No FrontPUSH

Em [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]], [[wiki/entities/nasser|Násser]] concatena `nome + sobrenome` ("juntou uma na outra", sem espaço), corrige com `' '` e mostra a alternativa do ES6: crase e "dólar entre chaves", onde dá para pôr "o que eu quiser de JavaScript" (na verdade, qualquer expressão).

Em [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]], a saída do loop ainda concatena com `+` (`'fruta ' + frutas[i]`), duas aulas depois de apresentar a template string.

Em [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]], `'marca: ' + item` e `item + ' ' + carros[index]` seguem com `+`; com template, `` `${item} ${carros[index]}` ``.

## Key sources

- [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]]: FrontPUSH, JavaScript aula 02: concatenação com + e template string
- [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]]: FrontPUSH, JavaScript aula 06: concatenação com + no loop
- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: concatenação com + no map
