---
type: source
title: "Functions e arrow functions em JavaScript (FrontPUSH)"
aliases: ["FrontPUSH functions e arrow functions", "módulo de JavaScript ES6, aula 04", "Functions & Arrow functions"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, funcoes, arrow-function, parametro, argumento, return, metodo, string, react, vue, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-functions-e-arrow-functions-javascript.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Functions e arrow functions em JavaScript (FrontPUSH)

## TL;DR

Aula 04 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (a legenda o chama de "Nácia", como nas aulas de UI). Arrow functions importam porque frameworks como [[wiki/entities/react]] e [[wiki/entities/vue]] estão "sempre [...] batendo na tecla" nelas.

- **Função:** "blocos de códigos que são reaproveitados", como uma `areaRetangulo` num programa de polígonos. Ver [[wiki/concepts/funcoes-javascript]].
- **Parâmetros:** pode ter ou não. `areaRetangulo(a, b)` tem dois e `helloWorld()` nenhum. "Quando eu escrevo aqui é parâmetro, quando eu passo diretamente é argumento."
- **Métodos e propriedades:** `console` é um objeto; `log` é método, `memory` é propriedade ([[wiki/concepts/programacao-orientada-a-objetos]]).
- **Retorno:** `helloWorld` "não me retorna nada, ela simplesmente executa"; `areaRetangulo` faz `return a * b`, e só aparece no console com `console.log(areaRetangulo(4, 2))`. "Regrinha" de boa prática: o tipo que entra é o tipo que sai.
- **Três formas:** declaração `function areaRetangulo(a, b) {}`; expressão `const areaRetangulo = function (a, b) {}`, "exatamente igual"; e arrow `(a, b) => {}`, "exatamente a mesma coisa". Ver [[wiki/concepts/arrow-functions]].
- **Encurtando:** com o retorno "em somente uma linha", sai o `return` e saem as chaves: `(a, b) => a * b`. Com um parâmetro só, saem os parênteses: `name => name.toUpperCase()`.
- **String como objeto:** `toUpperCase` existe porque a string "já se torna um objeto" e "herda várias propriedades e vários métodos" ([[wiki/concepts/string]]).

## Key Claims

### Função e parâmetros

- "São blocos de códigos que são reaproveitados." Num programa que calcula a área de vários polígonos, decompostos em quadrados e retângulos, a `areaRetangulo` evita "ficar escrevendo esse mesmo trecho de código toda vez".
- "Pode deter ou não de parâmetros": a área do retângulo precisa de "o lado A e o lado B"; `helloWorld` não precisa de nenhum e só "printe no console.log a questão do HelloWorld".
- "Quando eu escrevo aqui é parâmetro, quando eu passo diretamente é argumento."
- "Console é um objeto em que quando eu aperto o ponto, eu tenho como acessar tanto os métodos, que são as funções, tanto as propriedades, como por exemplo, memory é uma propriedade, log é um método."

### Retorno

- Funções "executam determinadas funcionalidades, podendo ou não retornar algo". O `helloWorld` "não me retorna nada, ela simplesmente executa alguma coisa".
- "Tem uma regrinha também, que é sempre bom, aquilo que você insere, o tipo de dado que você insere na função, é o mesmo tipo de dado que retorna na função [...] são boas práticas."
- `areaRetangulo(4, 2)` devolve 8, "porém ele não está retornando no console, ele só vai retornar o número", até envolver a chamada num `console.log`.

### Declaração, expressão e arrow

- `const areaRetangulo = function (a, b) {...}`: "eu declarar a função área retângulo dessa forma aqui é exatamente igual a eu declarar dessa forma aqui". Com 6 e 2 dá 12.
- "Eu apagar esse function e colocar uma setinha, por isso que se chama arrow function, arrow vem de seta [...] é exatamente a mesma coisa." Com 8 e 2 dá 16.
- "Quando está em somente uma linha, eu posso apagar o return [...] e simplesmente apagar as chaves [...] com bem menos verbosidade em uma única linha." Com 10 e 2 dá 20.
- "Talvez não seja muito intuitivo eu encurtar muito, mas é importante que a gente entenda essas sintaxes que são muito comuns quando a gente partir para algum tipo de framework."

### Um parâmetro

- `const upperName = function (name) { return name.toUpperCase() }`: "como isso aqui é um string, ele já se torna um objeto, só de ser um objeto, o string já herda várias propriedades e vários métodos que são inerentes a ele".
- Vira `name => name.toUpperCase()`: "quando eu tenho mais de um argumento eu preciso [dos parênteses], quando eu tenho somente um, não é necessário."

## Entities

- [[wiki/entities/nasser]]: instrutor (diz o nome, transcrito "Nácia" e "Nasser").
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6.
- [[wiki/entities/javascript]]: assunto da aula.
- [[wiki/entities/react]] e [[wiki/entities/vue]]: frameworks em que a sintaxe arrow é comum.

## Concepts

- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/arrow-functions]] (criado neste ingest)
- [[wiki/concepts/var-let-const]]
- [[wiki/concepts/string]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/programacao-orientada-a-objetos]]
- [[wiki/concepts/callback-javascript]]
- [[wiki/concepts/framework-web]]
- [[wiki/concepts/ecmascript]]

## Precisões e tensões com a wiki

`⚠️` Sem arquivo de referência na skill lang-dynamic para funções e arrow functions; as precisões vêm do MDN (`[external]`).

- **A aula promete "as diferenças" e mostra só a sintaxe.** `[external]` Arrow function não é "exatamente a mesma coisa": não tem `this` próprio (usa o de fora), não tem `arguments`, não pode ser chamada com `new` e não tem `prototype` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions). É essa diferença que pesa nos frameworks. Em handlers e callbacks, o `this` léxico evita o `.bind(this)` dos componentes de classe do React. No Vue, `methods` e `computed` escritos como arrow perdem o `this` do componente. Ver [[wiki/concepts/arrow-functions]].
- **Declaração e expressão também não são "exatamente iguais".** `[external]` A declaração `function f() {}` é içada (*hoisting*) inteira e pode ser chamada antes da linha em que aparece. `const f = function () {}` só existe depois da atribuição; chamar antes dá `ReferenceError`. O "Ctrl C, Ctrl V e comentar" da demo esconde isso ([[wiki/concepts/var-let-const]]).
- **Retorno implícito é por expressão, não por linha.** O que permite tirar `return` e chaves é o corpo ser uma única expressão. Para devolver um objeto, são precisos parênteses: `() => ({ a: 1 })`; sem eles, `{}` vira bloco e a função devolve `undefined`.
- **Parênteses:** são opcionais só com exatamente um parâmetro simples. Com zero, padrão (`(x = 1) =>`), desestruturação (`({ id }) =>`) ou rest (`(...args) =>`), são obrigatórios. Formatadores como o Prettier põem os parênteses sempre (`arrowParens: "always"` por padrão).
- **"O tipo que entra é o tipo que sai" não é regra.** `isPar(n)` recebe número e devolve booleano; `name.length` recebe string e devolve número. A boa prática real é a função devolver sempre o mesmo tipo (não um número às vezes e `undefined` às vezes), o que o [[wiki/entities/typescript]] deixa explícito.
- **String não "se torna um objeto".** `[external]` Ela continua primitiva; para `.toUpperCase()`, o motor a embrulha num objeto `String` temporário (*autoboxing*) e o método vem de `String.prototype`. Mesma imprecisão do "tudo é objeto" da [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript|aula 02]]; ver [[wiki/concepts/tipos-primitivos-javascript]].
- **`console.memory`** é propriedade não padronizada, só do Chrome. `console.log` está em todo ambiente.
- **Parâmetro × argumento** dito certo, ao contrário da NLW #1, que usou os dois como sinônimos ([[wiki/concepts/funcoes-javascript]]). Na parte do `upperName`, porém, a aula volta a dizer "argumento" para o parâmetro.
- **Sem `return`, a função devolve `undefined`**, não "nada": `console.log(helloWorld())` imprime "HelloWorld" e depois `undefined`.

## Open Questions

- Há 4,6 s sem legenda (00:07:23–00:07:27) antes de "Uma outra coisa muito importante, pessoal, que eu me lembrei aqui".
- O nome exato da função na tela: `helloWorld` ou `HelloWorld`? A legenda alterna.

## Raw quotes

- "são blocos de códigos que são reaproveitados"
- "quando eu escrevo aqui é parâmetro, quando eu passo diretamente é argumento"
- "arrow vem de seta"
