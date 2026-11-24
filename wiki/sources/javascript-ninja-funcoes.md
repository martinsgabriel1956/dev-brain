---
type: source
title: "Funções (JavaScript Ninja, aula 04)"
aliases: ["JavaScript Ninja aula 04", "JS Ninja funções", "04 - Funções"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [javascript, funcoes, function, invocacao, return, undefined, escopo, escopo-de-funcao, parametros, argumentos, nan, instrucoes, ponto-e-virgula, reuso, nodejs, repl]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-funcoes.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-24
---

# Funções (JavaScript Ninja, aula 04)

## TL;DR

Quarto vídeo da primeira aula do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 13 min), depois de [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais|igualdade e relacionais]], com [[wiki/entities/fernando-daciuk|Fernando Daciuk]] ("Fernando da Silva" na legenda de novo) no REPL do [[wiki/entities/nodejs|Node]]. Fecha o "apanhado geral" antes do desafio da semana.

- **Função** é "um bloco de código JavaScript nomeado e que pode ser invocado usando o operador abre e fecha parênteses". Mínimo: `function`, nome, `()` e `{}` ([[wiki/concepts/funcoes-javascript]]).
- **Invocar × referenciar:** `soma()` executa e devolve o valor; `soma` sem parênteses "simplesmente vai me retornar a função", sem executar. Sem conteúdo nem `return`, o valor "é indefinido" ([[wiki/concepts/null-e-undefined]]).
- **Ponto e vírgula** "no final de cada instrução eu devo colocar sempre". Instruções "são como se fossem sentenças completas de expressões" ([[wiki/concepts/expressao-javascript]]).
- **Reuso:** `function soma() { x = x + 1; }` incrementa o `x` de fora a cada chamada (1 → 2 → 3 → 4). "Funções são blocos de código que eu posso reutilizar" ([[wiki/concepts/dry]]).
- **Escopo:** variável declarada dentro da função "só existe dentro daquela função"; as de fora são acessíveis de dentro ([[wiki/concepts/escopo-javascript]]).
- **`return`** devolve um valor; `y + cinco()` dá 9 porque "a função invocada vale 5".
- **Parâmetros:** `function soma(x, y) { return x + y; }`. `soma()` sem argumentos dá `NaN`, "not a number"; `soma(1, 2)` dá 3 ([[wiki/concepts/tipos-primitivos-javascript]]).

## Key Claims

### Declarar e invocar

- "Que é uma função? Basicamente, um bloco de código JavaScript nomeado e que pode ser invocado usando o operador abre e fecha parênteses."
- "Eu preciso da palavra-chave function [...] vou dar um nome para minha função, vou abrir e fechar parênteses e vou abrir chaves [...] dentro das chaves é onde vai todo o conteúdo da minha função."
- "Para invocar essa função [...] eu vou usar o nome da função e usar o operador abre e fecha parênteses, que vai me retornar o valor dela. Como eu não tenho nada, o valor é indefinido."
- "Se eu não usar o operador, o que acontece? Ele simplesmente vai me retornar a função. Ele simplesmente não vai executá-lo."
- "Aprendeu agora mais um operador [...] abre e fecha parênteses, que ele serve para invocar funções."

### Instruções e ponto e vírgula

- "Eu coloquei um ponto e vírgula no final [...] da instrução"; "instruções, na verdade, [são] uma sentença de código"; "no final de cada instrução, eu devo colocar sempre um ponto e vírgula em JavaScript [...] ali finaliza uma instrução". Mais sobre isso "em breve".
- "Expressões [...] são as frases em JavaScript [...] e as instruções são como se fossem sentenças completas de expressões."

### Reuso

- `var x = 1; function soma() { x = x + 1; }`. Chamar `soma()` devolve `undefined` ("não tem nem retornando nenhum valor"), mas `x` passa a 2, depois a 3: "o x se incrementado mais uma vez".
- "Funções são blocos de código que eu posso reutilizar [...] você não vai precisar ficar digitando milhões de códigos aleatórios."
- `soma` sem parênteses mostra a função e deixa `x` em 3, "porque você não invocou a função"; com `soma()`, `x` vai a 4.

### Escopo

- `function qualquer() { var fernando = 'Fernando'; }`. Fora, `fernando` "não está definido [...] porque eu defini a variável Fernando dentro da função, mas estou tentando acessar ela de fora".
- "As funções criam um escopo: toda variável declarada dentro da função, ela só existe dentro daquela função [...] o escopo da variável, ela depende da função que ela está inserida."
- O inverso funciona: "eu consigo acessar valores, variáveis, de fora de uma função dentro de uma função" (o `x` incrementado).
- Invocar `qualquer()` não muda nada: devolve `undefined`, e "essa variável Fernando só vai valer aqui dentro".

### Retorno

- `function qualquer2() { var fernando = 'Fernando'; return fernando; }`: "funções, elas podem [...] retornar valores". Fora, `fernando` continua não definido, mas `qualquer2()` devolve `'Fernando'`: "usando a palavra-chave return, ele vai retornar o valor dessa variável".
- `var y = 4; function cinco() { return 5; }`. `cinco()` dá 5 e `y + cinco()` dá 9, "porque y vale 4, a função invocada vale 5".

### Parâmetros e NaN

- "Funções também podem receber argumentos ou parâmetros": `function soma(x, y) { return x + y; }`. "Esses argumentos são valores que eu vou poder passar para essa função quando invocar ela."
- `soma()` "não é número, porque eu mandei somar dois valores que eu não passei": `NaN`, "not a number [...] um valor também para quando [...] uma expressão que deveria ser feito com números [...] não retorna um número".
- `soma(1, 2)` dá 3.
- Antes, ele sai do REPL e entra de novo para apagar a `soma` anterior.

### Encerramento

- "Foi só um apanhado geral"; variáveis, arrays, instruções, expressões, funções e objetos voltam "detalhadamente". O desafio da semana fica para o próximo vídeo.

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para os fundamentos de JavaScript; as precisões vêm do MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação).

1. **Função não precisa de nome.** Funções anônimas (`function () {}`), expressões de função em variáveis e arrow functions (ES2015) são comuns, e a wiki já as registra em [[wiki/concepts/funcoes-javascript]]. Em JavaScript a função é um valor (um objeto chamável): por isso `soma` sem parênteses mostra `[Function: soma]` e pode ser passada como [[wiki/concepts/callback-javascript|callback]].
2. **Parâmetro × argumento.** Na declaração `soma(x, y)`, `x` e `y` são parâmetros; `1` e `2` na chamada são argumentos. A aula chama os da declaração de "dois argumentos", a mesma troca que a wiki registra na NLW.
3. **Ponto e vírgula não é obrigatório "sempre".** `[external]` A inserção automática (ASI) completa a maioria das instruções, e estilos como o StandardJS os omitem. O que importa são os casos em que a ASI falha: linha que começa com `(`, `[` ou crase cola na anterior, e `return` seguido de quebra de linha devolve `undefined`. Declaração de função (`function f() {}`) também não leva ponto e vírgula (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion) ([[wiki/concepts/pitfalls-de-linguagem]]).
4. **Instrução não é "sentença completa de expressões".** Algumas instruções são expressões com ponto e vírgula (`x = 1;`), mas `if`, `for`, `return` e `var` não são expressões nem produzem valor ([[wiki/concepts/expressao-javascript]]).
5. **O `soma` da demo é efeito colateral.** Mudar o `x` de fora funciona, mas é o padrão que dificulta raciocinar e testar. A versão com parâmetro e `return` (`x = soma(x, 1)`) é a mesma ideia sem estado escondido, e é para onde a própria aula caminha.
6. **Escopo de função vale para `var`.** `[external]` `let` e `const` (ES2015) têm escopo de bloco, mais estreito. Sem declaração nenhuma (`fernando = 'x'` dentro da função), o modo não estrito cria uma global sem aviso; no modo estrito é `ReferenceError`. Acessar variáveis de fora é o escopo léxico, base das closures ([[wiki/concepts/escopo-javascript]], [[wiki/concepts/var-let-const]]).
7. **`NaN` é do tipo number.** `typeof NaN` é `"number"`, e `soma()` dá `NaN` porque `undefined + undefined` não é número. "Não é um número exato" é impreciso: é o resultado de uma operação numérica inválida. Para testar, `Number.isNaN` ([[wiki/concepts/tipos-primitivos-javascript]]). Parâmetro default (ES2015: `function soma(x = 0, y = 0)`) evitaria o `NaN`.
8. **Não precisava sair do REPL.** Declarar `function soma` de novo substitui a anterior.
9. **Legenda.** Trocas: "Fernando da Silva"→Fernando Daciuk, "soluções" (3×)/"se moções"→funções, "infantil" (2×)→function, "Funchal"→function (o eco `[Function: soma]`), "some" (3×)→soma, "fui dando"→Fernando, "estilingue"/"estilo"→string, "muito chame" e "o"→return (média), "retorno default"→retornou undefined (média-alta), "aí nem"→NaN, "nota zero"/"nota em número"→not a number (média-alta), "paramos"→parâmetros, "reis"/"Rei"→arrays/array. Lista dos trechos literais no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor (se apresenta).
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.
- [[wiki/entities/nodejs]]: REPL das demonstrações.

## Concepts

- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/escopo-javascript]] (criado neste ingest)
- [[wiki/concepts/expressao-javascript]]
- [[wiki/concepts/var-let-const]]
- [[wiki/concepts/null-e-undefined]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/dry]]
- [[wiki/concepts/pitfalls-de-linguagem]]
- [[wiki/concepts/callback-javascript]]

## Open Questions

- "E que é uma função social?": provavelmente "o que é uma função? É basicamente".
- "Que ela odeie mais dez", "atribuindo a ela um maduro", "Irina Shayk", "no Titanic é o valor que funcionava", "eu entrei no intervalo, 4, 7": a legenda perdeu essas frases; o código de cada demo se reconstrói pelo resultado.
- O desafio da semana está no próximo vídeo.

## Raw quotes

- "um bloco de código JavaScript nomeado e que pode ser invocado usando o operador abre e fecha parênteses"
- "toda variável declarada dentro da função, ela só existe dentro daquela função"
- "você não vai precisar ficar digitando milhões de códigos aleatórios"
