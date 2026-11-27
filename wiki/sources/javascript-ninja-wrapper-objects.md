---
type: source
title: "Wrapper Objects (JavaScript Ninja, semana 10, vídeo 01)"
aliases: ["JavaScript Ninja Wrapper Objects", "JS Ninja objetos envoltório", "01 - Wrapper Objects"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 0
tags: [javascript, wrapper-objects, autoboxing, tipos-primitivos, construtores, conversao-de-tipos, coercao, truthy-falsy]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-wrapper-objects.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-27
---

# Wrapper Objects (JavaScript Ninja, semana 10, vídeo 01)

## TL;DR

Primeiro vídeo depois da revisão do desafio da semana 9 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 11 min), de [[wiki/entities/fernando-daciuk|Fernando Daciuk]]. Numeração "semana 10" inferida: a aula abre com a revisão "do Desafio da Semana 9" e o arquivo é o `01`. Apresenta os [[wiki/concepts/wrapper-objects-javascript|wrapper objects]] e o uso dos mesmos construtores, sem `new`, como conversores.

- **O que é objeto:** "se esse cara, ele tem propriedades e métodos, então ele é um objeto". Primitivos não têm; arrays, objetos e funções são objetos ([[wiki/concepts/tipos-primitivos-javascript]], [[wiki/concepts/objetos-javascript]]).
- **O paradoxo:** `name = 'Daciuk'` é primitivo, mas `name.length` dá 6. "Então, o porquê que eles têm propriedades?"
- **Construtores:** "objetos, ou funções, no caso, que criam novos objetos", usados com a palavra-chave `new`. Para os primitivos, três: `String`, `Number`, `Boolean`. `new String('Daciuk')` é "um objeto do tipo String", com `valueOf()` que devolve "o valor literal".
- **O wrapper:** ao buscar uma propriedade num primitivo, o JavaScript "cria um novo objeto pra mim, que é o objeto wrapper", "um envoltório", usa a propriedade e "gera esse tipo de descarte"; `name` continua primitivo.
- **No dia a dia, literal:** criar `new String`/`new Number` "não é o que você vai utilizar muito".
- **Sem `new`, conversores:** `String(10)` dá string; `String(52) + 2` concatena; com `Number`, soma ([[wiki/concepts/operadores-aritmeticos-javascript]]). `Boolean(0)` é falso, `Boolean({})` é verdadeiro, "o mesmo que [...] os dois sinais de exclamação" ([[wiki/concepts/truthy-e-falsy]]).
- **Fecho:** "JavaScript é uma linguagem de tipagem dinâmica", converte "se ele achar que é necessário", por isso é preciso entender a conversão ([[wiki/concepts/sistema-de-tipos]]).

## Key Claims

### Primitivos × objetos

- "A gente sabe que valores primitivos, eles não são objetos." Lista: número, um trecho ilegível ("x isto", provavelmente string), booleano, "valor indefinido". "Todos os outros tipos de valores em JavaScript são objetos: arrays, objetos, funções."
- Critério: "Se esse cara, ele tem propriedades e métodos, então ele é um objeto, certo? Se ele não tem propriedades e métodos, então ele não é um objeto."
- O valor primitivo "é um valor exatamente da forma como ele [...] é apresentado".

### O paradoxo do length

- `name` recebe `'Daciuk'`; `name.length` "me retorna seis, que é o valor da quantidade de caracteres que tem na string".
- "Só que eu acabei de falar que valores primitivos não são objetos. Então, o porquê que eles têm propriedades?"
- Compara com o `length` do array, que "conta a quantidade de itens do array" ([[wiki/sources/javascript-ninja-arrays-propriedade-length]]).

### Construtores e new

- "São objetos, ou funções, no caso, que criam novos objetos." O curso promete voltar a construtores "mais para frente".
- "Você utiliza a palavra-chave [...] new, que vai criar algo novo." São "basicamente três construtores ali para esses valores primitivos".
- O exemplo cria string, número (30) e Boolean "com um valor falso" via `new` (a linha está ilegível na legenda).
- `new String(...)` é "um objeto do tipo String"; `name.length` continua funcionando. O valor fica guardado e "é o valueOf, name ponto valueOf. Essa função [...] vai me retornar [...] o valor exato, ou o valor literal".

### O wrapper object

- "Na verdade, não é [...] essa stringzinha literal que ela tem a propriedade length." Ao buscar um método ou propriedade, o JavaScript "entende o tipo do objeto [...] cria um novo objeto pra mim, que é o objeto wrapper [...] um envoltório".
- "A tradução de wrapper significa um envoltório." Ele "vai envolver a minha string literal [em] um objeto do tipo String, para que eu possa utilizar a propriedade".
- Depois do uso, o objeto é descartado da memória e `name` continua sendo string.

### Literal no dia a dia

- "Não é o que você vai utilizar muito no dia a dia. É interessante você saber [...] como o JavaScript faz essa conversão de valores."
- `new Number(30)`: "você vê que ele é um objeto"; com `valueOf` "ele traz o valor literal do que é o número 30".

### Construtores sem new

- "Quando a gente usa sem new, esses caras, eles servem mais como conversores do que construtores." São "funções globais, porque elas estão disponíveis em qualquer lugar do teu código".
- `String(10)` devolve o 10 como string, "porque eu usei [...] a função String".
- `String(52) + 2`: "faz a concatenação", porque o `+` com uma string "converte os dois valores" para string. Com `Number`, soma.
- `Boolean(0)`: "o meu valor é falso". `Boolean({})`: verdadeiro, "porque o objeto vazio representa true". "É o mesmo que [...] os dois sinais de exclamação [...] o equivalente booleano daquele valor."

### Tipagem dinâmica

- "Você não precisa dizer [...] que tipo é aquele valor." "Ele automaticamente vai mudar o tipo, se for necessário." "Por isso é bastante importante você entender como ele faz essa [...] conversão de valores, para que você não se perca."
- O tema cai no desafio da semana.

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para wrapper objects. As precisões vêm da MDN e da especificação, marcadas `[external]`, sem fetch. As demos foram reproduzidas no Node 22.23.

1. **O nome técnico é autoboxing.** `[external]` A especificação faz `ToObject` no primitivo ao acessar propriedade; o método vem de `String.prototype`, `Number.prototype`, `Boolean.prototype` (https://developer.mozilla.org/en-US/docs/Glossary/Primitive). A wiki já usava o termo em [[wiki/concepts/string]] e [[wiki/concepts/objetos-javascript]] (FrontPUSH). O "descarte" é modelo mental: os motores otimizam e em geral nem alocam o objeto.
2. **A prova do descarte.** Verificado: `name.foo = 1; name.foo` dá `undefined`, porque a propriedade foi gravada no wrapper descartado. Em *strict mode*, a atribuição dá `TypeError: Cannot create property 'foo' on string 'abc'`.
3. **São cinco wrappers, não três.** `[external]` Os três da aula são os da era ES5. `Symbol` (ES2015) e `BigInt` (ES2020) também têm wrapper, mas não aceitam `new` (verificado: `Symbol is not a constructor`, `BigInt is not a constructor`); `Object(1n)` dá objeto. `null` e `undefined` não têm wrapper: `null.length` dá `TypeError` ([[wiki/concepts/null-e-undefined]]). A lista de primitivos da aula também omite `null`, `symbol` e `bigint` ([[wiki/concepts/tipos-primitivos-javascript]]).
4. **Por que evitar `new String` vai além do hábito.** Verificado: `typeof new String('Daciuk')` dá `'object'`; `new String('Daciuk') === 'Daciuk'` dá `false` e `==` dá `true` ([[wiki/concepts/igualdade-javascript]]). E `new Boolean(false)` é truthy, porque todo objeto é truthy ([[wiki/concepts/truthy-e-falsy]]). `[external]` ESLint tem a regra `no-new-wrappers` para isso ([[wiki/concepts/pitfalls-de-linguagem]]).
5. **Conversões verificadas.** `String(52) + 2` dá `'522'`; `Number('52') + 2` dá 54; `Boolean(0)` dá `false`; `Boolean({})` e `!!{}` dão `true`. Casos de borda que a aula não mostra: `Number('')` dá 0, `Number('abc')` dá `NaN`, `Number(null)` dá 0, `Number(undefined)` dá `NaN`, `String(null)` dá `'null'`. O `+` unário faz o mesmo que `Number()` ([[wiki/concepts/operadores-unarios-javascript]]).
6. **Conversão implícita é tipagem fraca, não dinâmica.** A aula atribui a conversão automática à "tipagem dinâmica". Na taxonomia da wiki ([[wiki/concepts/sistema-de-tipos]]), dinâmica é o tipo ser checado em tempo de execução; a conversão implícita entre tipos é o eixo da tipagem *fraca*. O próprio curso, na aula 03, chamou o JavaScript de "tipagem fraca, dinâmica" ([[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]]). Python é dinâmico e não converte `'52' + 2`.
7. **`valueOf` é o que a conversão implícita usa.** `[external]` Em `new Number(30) + 1` (dá 31, verificado), o motor chama `ToPrimitive`, que tenta `valueOf` e depois `toString`. É a ponte entre as duas metades da aula.
8. **Legenda.** Trocas principais: "na índia"→Ninja, "feriado nacional"→Fernando Daciuk, "da Silk"→Daciuk, "lei"→length, "elimina torna"/"eliminatória"→ele me retorna, "estilingue"/"swing"/"extingue"→String, "consultor(es)"/"consultoria"→construtor(es), "Nil"/"uniu"→new, "bullying"/"bolha"→Boolean, "velho e óbvio Mané em Porto Velho"→valueOf, name ponto valueOf, "um golpe"/"opta"→wrapper, "com cadeado"→concatenado, "permitidos"→primitivos. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/wrapper-objects-javascript]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/string]]
- [[wiki/concepts/truthy-e-falsy]]
- [[wiki/concepts/sistema-de-tipos]]
- [[wiki/concepts/operadores-aritmeticos-javascript]]
- [[wiki/concepts/operadores-unarios-javascript]]
- [[wiki/concepts/operadores-logicos-javascript]]
- [[wiki/concepts/igualdade-javascript]]
- [[wiki/concepts/pitfalls-de-linguagem]]
- [[wiki/concepts/null-e-undefined]]

## Open Questions

- **A linha dos três `new`:** "minha variável nem Manuel da Silva, que para uma variável chamada Meu nome está passando 30, para variável mídia". Provavelmente `name = new String('Daciuk')`, `number = new Number(30)` e uma terceira com `new Boolean(false)` (média). Literal no raw.
- **"x isto"** na lista de primitivos: provavelmente string (média). **"Os valores booleanos é falso"**: talvez "true e false". **"Valor indefinido"**: undefined, talvez também null.
- **"Vai nem me viu isso"**, **"o meu filho isso"**, **"mas sim usando nisto"**, **"Nildo 30"**: provavelmente `var name = new String`, `new String`, "string usando new String" e `new Number(30)` (média). Literais.
- **"Esse time dócil"** e **"um valor nasceu"**: talvez o valor `'Daciuk'` (baixa). **"Nessa idade"**: talvez "nessa variável".
- **"Os preços dos objetos construtores"**: talvez "os wrappers, os objetos construtores" (baixa).
- **"Faz a curva T o valor de name"**: provavelmente "converte o valor de name" (média).
- **"%52"** e **"para esse fim"**: provavelmente `'52'` entre aspas e "para string" (média).
- **"Pra matar"**, depois de usar `Number`: talvez o resultado 54 (baixa).
- **"Luis Peru"**, **"F para o array"**, **"os jovens"**, **"o vai tu"**: ilegíveis; literais.
- O vídeo não anuncia o próximo. Na wiki, o seguinte é [[wiki/sources/javascript-ninja-typeof]] (semana 10, vídeo 02).

## Raw quotes

- "se esse cara, ele tem propriedades e métodos, então ele é um objeto"
- "a tradução de wrapper significa um envoltório"
- "eles servem mais como conversores do que construtores"
