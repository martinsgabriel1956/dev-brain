---
type: entity
title: "JavaScript Ninja (curso)"
aliases: ["Curso JavaScript Ninja", "JS Ninja", "Javascript Ninja"]
date_created: 2026-11-24
date_updated: 2026-11-26
source_count: 26
tags: [curso, javascript, educacao, fundamentos]
skill: lang-dynamic
status: stub
---

# JavaScript Ninja (curso)

Curso de [[wiki/entities/javascript|JavaScript]] de [[wiki/entities/fernando-daciuk|Fernando Daciuk]], em português, dividido em aulas com várias partes. O que está na wiki é da era ES5: só `var`, sem `let`, `const` nem template literal ([[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]]).

A primeira aula tem ao menos duas partes; a segunda cobre variáveis e tipos de dados e anuncia operadores para a seguinte. Não confundir com o [[wiki/entities/lapa-ninja|Lapa Ninja]], galeria de landing pages.

## Aula 02

Em [[wiki/sources/javascript-ninja-operadores-aritmeticos]], expressões e operadores aritméticos; o vídeo seguinte é de igualdade e relacionais.

## Aula 03

Em [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]], igualdade (`==`, `===`) e relacionais; o vídeo seguinte é de funções.

## Aula 04

Em [[wiki/sources/javascript-ninja-funcoes]], funções. A primeira aula termina com um "desafio da semana", apresentado no vídeo seguinte; o curso parece ter cadência semanal (inferência, média).

## Semana 2

Em [[wiki/sources/javascript-ninja-operadores-logicos]], primeiro vídeo depois da correção do desafio da semana (esse vídeo de correção não está na wiki): operadores lógicos; o seguinte é de operadores unários. Dúvidas vão por email ou issue no GitHub. Como as páginas anteriores numeraram cada vídeo da primeira semana como "aula", esta leva é citada como "semana 2, vídeo NN" para não colidir.

Em [[wiki/sources/javascript-ninja-operadores-unarios]], o segundo vídeo: `+` e `-` unários, `+` como concatenação e `++`/`--` com efeito colateral; o seguinte é de estrutura léxica.

Em [[wiki/sources/javascript-ninja-estrutura-lexica]], o terceiro vídeo: estrutura léxica; o seguinte é o desafio da semana. O instrutor diz "nossa segunda aula do curso", o que confirma que esta leva é a aula 2 e que os quatro vídeos anteriores, numerados "aula 01–04" na wiki, são as partes da aula 1.

Em [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]], o quarto vídeo: `if`, `else` e `else if`. O desafio da semana 2, prometido no vídeo 03, passa para o seguinte.

## Semana 3

Em [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]], primeiro vídeo da "terceira aula": primitivos × objetos, objeto literal e função como objeto de primeira classe. A pasta de transcrições recomeçou em 01 e traz, depois dele, "Métodos de objeto" e a continuação. O desafio da semana 2, anunciado nos vídeos 03 e 04, não está entre as transcrições.

Em [[wiki/sources/javascript-ninja-metodos-de-objeto]], o segundo vídeo: métodos de objeto, reatribuir × acrescentar com ponto, `andar`, `aniversario` e `nomeCompleto`. O seguinte continua com objetos.

Em [[wiki/sources/javascript-ninja-metodos-de-objeto-continuacao]], o terceiro vídeo fecha a aula 3: revisão de métodos e o desafio da semana 3, no repositório `da2k/curso-javascript-ninja`. Cada aluno tem um fork, atualiza a master pelo `upstream`, faz cada desafio numa branch (`challenge-03`) e entrega por pull request ([[wiki/concepts/fork-e-upstream]]). Mostra que o curso é semanal, com email a cada semana, e que os desafios são "praticamente uma prova".

## Semana 4

Em [[wiki/sources/javascript-ninja-truthy-e-falsy]], primeiro vídeo da "quarta aula": truthy, falsy e `!!`. A pasta recomeçou em 01 e traz, depois dele, "Condicional Ternário" e "Escopo de variáveis e funções"; o vídeo anuncia o ternário como o próximo.

Em [[wiki/sources/javascript-ninja-condicional-ternario]], o segundo vídeo: o operador ternário ([[wiki/concepts/operador-ternario-javascript]]), com o desafio 3 como exemplo. O seguinte é de escopo de variáveis.

Em [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]], o terceiro vídeo: escopo global e local, variável sem `var` e garbage collection ([[wiki/concepts/poluicao-do-escopo-global]]). O seguinte é o desafio da semana 4, que não está entre as transcrições.

## Semana 6

Em [[wiki/sources/javascript-ninja-operador-virgula-e-switch]], primeiro vídeo depois da revisão do desafio (a legenda diz "cinquentinha", provavelmente o desafio 5): operador vírgula e `switch`. A pasta recomeçou em 01 e traz, depois dele, "Estrutura de repetição While", que o vídeo anuncia.

Em [[wiki/sources/javascript-ninja-estrutura-de-repeticao-while]], o segundo vídeo: o `while`, primeira estrutura de repetição. Fecha com "o desafio da semana de 6 está lançado", o que confirma a numeração da semana; o desafio não está entre as transcrições.

## Semana 7

Em [[wiki/sources/javascript-ninja-operador-modulo]], primeiro vídeo depois da "resolução do desafio da semana 6" (esse vídeo não está na wiki): o operador `%` e os pares de 0 a 20 com `while`, com um erro mantido ao vivo. A pasta recomeçou em 01; o vídeo anuncia arrays como o próximo.

Em [[wiki/sources/javascript-ninja-arrays-propriedade-length]], o segundo vídeo: arrays como objetos embutidos, a propriedade `length` e o percurso de trás para frente com `while`. O seguinte é de métodos de array.

Em [[wiki/sources/javascript-ninja-arrays-metodo-push-e-loop-for]], o terceiro vídeo: o método `push` (adiciona no fim e devolve o `length`) e o loop `for`.

## Semana 8

- [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]]: vídeo 01, depois da revisão do desafio da semana 7 (que não está na wiki). Abre "partes um pouco mais avançadas" de funções: sempre nomear, propriedade `name`, anônima × nomeada × "literal". Anuncia programação funcional.
- [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]]: vídeo 02, introdução à programação funcional: funções como cidadãos de primeira classe, objeto literal × função literal, função que retorna objeto. Anuncia retorno de funções.
- [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]]: vídeo 03, programação funcional parte 2: função que retorna função (`adder`), `add2(3)`, `adder(5)(8)`. Anuncia função como parâmetro.
- [[wiki/sources/javascript-ninja-programacao-funcional-parte-3]]: vídeo 04, programação funcional parte 3: objeto e função como parâmetro (`showFunction`). Diz que esta é a oitava aula de "umas 30". Anuncia o desafio da semana (não está na wiki).

## Semana 9

- [[wiki/sources/javascript-ninja-escopo-de-funcoes]]: vídeo 01, depois da "correção" do desafio 8 (que não está na wiki). A semana 9 é inferida pela sequência. Escopo de funções: função dentro de função, a interna invisível fora e lendo as variáveis da externa, e `function` depois do `return`. Anuncia hoisting.

## Key sources

- [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]]: aula 01, parte 2: variáveis e tipos de dados
- [[wiki/sources/javascript-ninja-operadores-aritmeticos]]: aula 02: operadores aritméticos
- [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]]: aula 03: igualdade e relacionais
- [[wiki/sources/javascript-ninja-funcoes]]: aula 04: funções; desafio da semana
- [[wiki/sources/javascript-ninja-operadores-logicos]]: semana 2, vídeo 01: operadores lógicos
- [[wiki/sources/javascript-ninja-operadores-unarios]]: semana 2, vídeo 02: operadores unários
- [[wiki/sources/javascript-ninja-estrutura-lexica]]: semana 2, vídeo 03: estrutura léxica; "segunda aula"
- [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]]: semana 2, vídeo 04: instruções condicionais
- [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]]: semana 3, vídeo 01: tipos de dados e objetos; "terceira aula"
- [[wiki/sources/javascript-ninja-metodos-de-objeto]]: semana 3, vídeo 02: métodos de objeto
- [[wiki/sources/javascript-ninja-metodos-de-objeto-continuacao]]: semana 3, vídeo 03: revisão de métodos; desafio 3; fluxo de fork
- [[wiki/sources/javascript-ninja-metodos-de-objeto-continuacao]]: semana 3, vídeo 03: métodos de objeto (continuação) e desafio 3
- [[wiki/sources/javascript-ninja-truthy-e-falsy]]: semana 4, vídeo 01: truthy e falsy; "quarta aula"
- [[wiki/sources/javascript-ninja-condicional-ternario]]: semana 4, vídeo 02: condicional ternário
- [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]]: semana 4, vídeo 03: escopo de variáveis e funções
- [[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos]]: semana 5, vídeo 01: retorno de funções com arrays e objetos; "quinta aula"
- [[wiki/sources/javascript-ninja-parametros-de-funcoes-como-arrays-e-objetos]]: semana 5, vídeo 02: parâmetros de funções como arrays e objetos
- [[wiki/sources/javascript-ninja-operador-virgula-e-switch]]: semana 6, vídeo 01: operador vírgula e estrutura condicional switch
- [[wiki/sources/javascript-ninja-estrutura-de-repeticao-while]]: semana 6, vídeo 02: estrutura de repetição while; desafio 6
- [[wiki/sources/javascript-ninja-operador-modulo]]: semana 7, vídeo 01: operador módulo; anuncia arrays
- [[wiki/sources/javascript-ninja-arrays-propriedade-length]]: semana 7, vídeo 02: arrays e a propriedade length; anuncia métodos
- [[wiki/sources/javascript-ninja-arrays-metodo-push-e-loop-for]]: semana 7, vídeo 03: método push e loop for
- [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]]: semana 8, vídeo 01: a importância de nomear funções; anuncia programação funcional
- [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]]: semana 8, vídeo 02: introdução à programação funcional; anuncia retorno de funções
- [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]]: semana 8, vídeo 03: funções que retornam funções; anuncia função como parâmetro
- [[wiki/sources/javascript-ninja-programacao-funcional-parte-3]]: semana 8, vídeo 04: objeto e função como parâmetro; curso com umas 30 aulas
- [[wiki/sources/javascript-ninja-escopo-de-funcoes]]: semana 9, vídeo 01: escopo de funções; anuncia hoisting
