---
type: concept
title: "Notação de ponto e de colchetes (JavaScript)"
aliases: ["dot notation", "bracket notation", "notação de ponto", "notação de colchetes", "property accessors", "acesso a propriedade"]
date_created: 2026-11-24
date_updated: 2026-11-27
source_count: 5
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

## No JavaScript Ninja, semana 3, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]], só o ponto: `objeto.propriedade`, `pessoa.nome`, `carro.cor`, `carro.motor`. Os colchetes não voltam.

## No JavaScript Ninja, semana 3, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-metodos-de-objeto]], o ponto também escreve: `pessoa.cor = 'caucasiano'` cria a propriedade sem perder as outras, e `pessoa.andar = function () {...}` cria um método. "Novas atribuições, sempre [...] o nome do objeto, ponto, o nome da propriedade, é igual, o valor." `[external]` Se a propriedade já existe, o ponto sobrescreve.

## No JavaScript Ninja, semana 7, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-arrays-propriedade-length]], as duas notações juntas: `array[qtd]` pega o item e `.bola` a propriedade do objeto que está nele (`array[3].bola` dá `'azul'`).

## No JavaScript Ninja, semana 11, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-lacos-loops]], os colchetes voltam dentro do [[wiki/concepts/for-in-javascript|for...in]]: a chave vem numa variável string, então o valor sai com `car[prop]`, "no formato de array". Com ponto, `car.prop` procuraria uma propriedade chamada `prop`.

## Key sources

- [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]]: `pessoa.altura` × `pessoa['altura']`; arrays como objetos
- [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]]: JavaScript Ninja, semana 3, vídeo 01: leitura com ponto em pessoa e carro
- [[wiki/sources/javascript-ninja-metodos-de-objeto]]: JavaScript Ninja, semana 3, vídeo 02: ponto para criar propriedade e método
- [[wiki/sources/javascript-ninja-arrays-propriedade-length]]: JavaScript Ninja, semana 7, vídeo 02: array[qtd].bola
- [[wiki/sources/javascript-ninja-lacos-loops]]: JavaScript Ninja, semana 11, vídeo 01: car[prop] dentro do for...in
