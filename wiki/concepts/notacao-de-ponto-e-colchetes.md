---
type: concept
title: "Notação de ponto e de colchetes (JavaScript)"
aliases: ["dot notation", "bracket notation", "notação de ponto", "notação de colchetes", "property accessors", "acesso a propriedade"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 1
tags: [javascript, objetos, propriedades, array, sintaxe]
skill: lang-dynamic
status: stub
---

# Notação de ponto e de colchetes (JavaScript)

As duas formas de ler e escrever uma propriedade de objeto em JavaScript:

| | Ponto | Colchetes |
|---|---|---|
| Sintaxe | `pessoa.altura` | `pessoa['altura']` |
| Chave | identificador válido, escrito no código | qualquer expressão, convertida para string (ou symbol) |
| Chave dinâmica | não | sim: `pessoa[campo]` |
| Chave com hífen, espaço ou começando por número | não | sim: `obj['data-id']`, `arr[0]` |

`[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors

Arrays são objetos, e os índices são chaves: `numeros[3]` e `numeros['3']` leem a mesma propriedade. `numeros.3` é erro de sintaxe, por isso arrays usam colchetes ([[wiki/concepts/array]], [[wiki/concepts/objetos-javascript]]).

**Qual usar:** ponto sempre que a chave é fixa e é identificador; colchetes quando a chave vem de uma variável ou não é identificador. A escolha é de legibilidade: com chave literal, os motores modernos geram o mesmo acesso nas duas formas, e a regra `dot-notation` do ESLint pede o ponto (inferência, média-alta).

## No JavaScript Ninja (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]], [[wiki/entities/fernando-daciuk|Daciuk]] usa `pessoa['altura']` para provar que "no JavaScript não existem arrays [...] eles nada mais são do que objetos". Ele recomenda o ponto porque "a notação de objeto é mais rápida". A recomendação é boa, o motivo não.

## Key sources

- [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]]: `pessoa.altura` × `pessoa['altura']`; arrays como objetos
