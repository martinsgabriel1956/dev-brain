---
type: concept
title: "Expressão e instrução (JavaScript)"
aliases: ["expressão", "expression", "instrução", "statement", "expressão vs instrução", "expression vs statement"]
date_created: 2026-11-24
date_updated: 2026-11-25
source_count: 7
tags: [javascript, sintaxe, expressoes, fundamentos]
skill: lang-dynamic
status: stub
---

# Expressão e instrução (JavaScript)

**Expressão** é um trecho de código que é avaliado e produz um valor: `2 + 3`, `x`, `x = 0`, `f()`, `a > b`. **Instrução** (*statement*) é uma ação que o programa executa e não produz valor: `var x = 0`, `if`, `for`, `return`. Uma expressão pode virar instrução com ponto e vírgula (`x++;`), mas uma instrução não cabe onde se espera um valor: `const y = if (a) {}` é erro. `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators

Onde a diferença aparece:
- **REPL:** o Node ecoa o valor de uma expressão; depois de uma declaração (`var x = 0`), ecoa `undefined` ([[wiki/entities/nodejs]]).
- **Template literal:** `${}` aceita expressão, não instrução ([[wiki/concepts/template-literals]]).
- **Arrow function:** corpo sem chaves é uma expressão e já é o retorno ([[wiki/concepts/funcoes-javascript]]).
- **Operadores** constroem expressões a partir de outras ([[wiki/concepts/operadores-aritmeticos-javascript]], [[wiki/concepts/incremento-e-decremento]]).

## No JavaScript Ninja (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-aritmeticos]], expressão é "uma frase em JavaScript que pode ser avaliada para produzir um certo valor", e operadores são "uma das maneiras mais comuns de criar expressões". A definição está certa, mas o exemplo (`var x = 0`) é uma instrução; `x = 0` e `x` é que são expressões.

## No JavaScript Ninja, aula 04 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-funcoes]], instruções "são como se fossem sentenças completas de expressões" e terminam "sempre" com ponto e vírgula. Nem toda instrução é expressão (`if`, `var`, `return`), e o ponto e vírgula é em geral opcional pela ASI, com exceções ([[wiki/concepts/pitfalls-de-linguagem]]). A chamada `cinco()` dentro de `y + cinco()` é expressão: vale o retorno.

## No JavaScript Ninja, semana 2, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-unarios]], `-x` e `+x` são expressões que só produzem valor; `x++` produz valor e grava na variável. É a fronteira entre avaliar e ter efeito ([[wiki/concepts/efeito-colateral]]).

## No JavaScript Ninja, semana 2, vídeo 04 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]], o `if` é instrução: escolhe o que executar, não devolve valor. Para escolher um valor, o ternário (`y = x === 2 ? 2 : 10`) é a versão expressão ([[wiki/concepts/estruturas-condicionais-javascript]]).

## No JavaScript Ninja, semana 4, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-condicional-ternario]], o ternário vai "direto" numa atribuição (`sexo = ... ? 'a' : 'o'`). A aula o chama de "instrução", mas é expressão; é por isso que cabe ali, e o `if` não ([[wiki/concepts/operador-ternario-javascript]]).

## No JavaScript Ninja, semana 6, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operador-virgula-e-switch]], o operador vírgula "junta várias expressões em uma única expressão" ([[wiki/concepts/operador-virgula-javascript]]). O primeiro exemplo, `var a, b = 2, c`, não é uma expressão: é uma instrução `var` com uma lista de declarações, e a vírgula ali é separador. O segundo, `return x += 1, x`, é expressão de sequência de verdade.

## No JavaScript Ninja, semana 6, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-estrutura-de-repeticao-while]], o REPL mostra um valor no fim do `while`, "o último retorno". Não é retorno: é o valor de conclusão da instrução, o da última expressão executada no corpo (`counter++` devolvendo 9).

## Key sources

- [[wiki/sources/javascript-ninja-operadores-aritmeticos]]: expressão como "frase" avaliada; var x = 0 como exemplo (impreciso)
- [[wiki/sources/javascript-ninja-funcoes]]: JavaScript Ninja, aula 04: instrução como "sentença"; ponto e vírgula; chamada como expressão
- [[wiki/sources/javascript-ninja-operadores-unarios]]: JavaScript Ninja, semana 2, vídeo 02: -x avalia sem alterar x
- [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]]: JavaScript Ninja, semana 2, vídeo 04: if como instrução
- [[wiki/sources/javascript-ninja-condicional-ternario]]: JavaScript Ninja, semana 4, vídeo 02: ternário é expressão (a aula diz instrução)
- [[wiki/sources/javascript-ninja-operador-virgula-e-switch]]: JavaScript Ninja, semana 6, vídeo 01: operador vírgula junta expressões; a vírgula do var é instrução, não expressão
- [[wiki/sources/javascript-ninja-estrutura-de-repeticao-while]]: JavaScript Ninja, semana 6, vídeo 02: valor de conclusão do while no REPL
