---
type: concept
title: "Escopo em JavaScript (global, de função e de bloco)"
aliases: ["escopo", "scope", "escopo de função", "escopo de bloco", "escopo global", "escopo léxico", "lexical scope", "function scope", "block scope"]
date_created: 2026-11-24
date_updated: 2026-11-26
source_count: 7
tags: [javascript, escopo, funcoes, var, let, const, closure]
skill: lang-dynamic
status: stub
---

# Escopo em JavaScript (global, de função e de bloco)

Escopo é a região do código onde um nome existe. `[external]` https://developer.mozilla.org/en-US/docs/Glossary/Scope

| Escopo | Quem cria | O que vive nele |
|---|---|---|
| Global | o script (ou o módulo, que tem escopo próprio) | o que é declarado fora de tudo |
| De função | cada `function` | `var`, parâmetros e o que for declarado dentro |
| De bloco | cada `{ }` (`if`, `for`, bloco solto) | `let`, `const` e `class` |

- **Léxico:** de dentro se enxerga o de fora, nunca o contrário. O escopo é decidido por onde a função foi **escrita**, não por onde é chamada. Uma função que continua usando variáveis do escopo onde nasceu, mesmo depois que ele terminou, é uma *closure* ([[wiki/concepts/stale-closure]]).
- **Sombreamento:** um nome declarado dentro esconde o de mesmo nome de fora.
- **Sem declaração:** atribuir a um nome nunca declarado cria uma global no modo não estrito e lança `ReferenceError` no estrito (`'use strict'`, padrão em módulos ES e classes).
- **Ler de fora** um nome que só existe dentro lança `ReferenceError: x is not defined` ([[wiki/concepts/null-e-undefined]]: não é `undefined`).
- `var` × `let`/`const`: o primeiro ignora o bloco e respeita a função; os outros respeitam os dois ([[wiki/concepts/var-let-const]]).

Escopo é um dos motivos para funções: o que é de dentro não vaza nem colide com o resto do programa ([[wiki/concepts/funcoes-javascript]]).

## No JavaScript Ninja (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-funcoes]], `var fernando` dentro de `function qualquer()` não existe fora ("não está definido"), nem depois de invocar a função; já o `x` de fora é lido e alterado de dentro. "As funções criam um escopo: toda variável declarada dentro da função, ela só existe dentro daquela função." Para tirar o valor de lá, `return`. Escopo de bloco não aparece, porque a aula só usa `var`.

## No JavaScript Ninja, semana 4, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]], a aula volta ao tema com dois escopos, global ("fora de função") e local ("dentro de uma função"), e acrescenta: atribuir sem `var` dentro da função cria uma global, mas só depois da invocação; parâmetros também são locais; e o global "é algo ruim", "um erro de design da linguagem" ([[wiki/concepts/poluicao-do-escopo-global]]). Escopo de bloco e de módulo ainda não aparecem (era ES5).

## No JavaScript Ninja, semana 6, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operador-virgula-e-switch]], a lista `var a, b = 2, c` dentro de uma função deixa as três variáveis locais: fora dela, `a` "não foi definido". Retoma a aula de escopo e a global implícita ([[wiki/concepts/poluicao-do-escopo-global]]).

## No JavaScript Ninja, semana 8, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]], o `adder` mostra o escopo léxico funcionando depois do fim da função de fora: a função interna retornada ainda soma o `x` que `adder` recebeu ("o 2 que eu já tinha passado na primeira vez"). `[external]` Cada chamada de `adder` cria um escopo novo, então `add2` e `add10` não se misturam (verificado). A aula não usa o nome [[wiki/concepts/closure-javascript|closure]].

## No JavaScript Ninja, semana 9, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-escopo-de-funcoes]], a função passa a ser dona de outra função: `sum`, declarada dentro de `myFunction`, não existe fora ("o escopo dela é aquela função onde ela está dentro"; fora, `ReferenceError`), mas lê `number1` e `number2` da função de fora, que valem "para toda essa função". A posição da declaração no corpo não muda o resultado, porque a `function` sobe para o topo do escopo ([[wiki/concepts/hoisting-javascript]]).

## Key sources

- [[wiki/sources/javascript-ninja-funcoes]]: var dentro da função não existe fora; o de fora é acessível de dentro
- [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]]: JavaScript Ninja, semana 4, vídeo 03: global × local, global implícita, parâmetros locais
- [[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos]]: JavaScript Ninja, semana 5, vídeo 01: criar o escopo na função e expor o retorno, sem objeto global
- [[wiki/sources/javascript-ninja-parametros-de-funcoes-como-arrays-e-objetos]]: JavaScript Ninja, semana 5, vídeo 02: parâmetro com nome diferente da variável de fora
- [[wiki/sources/javascript-ninja-operador-virgula-e-switch]]: JavaScript Ninja, semana 6, vídeo 01: variáveis da lista com vírgula ficam locais
- [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]]: JavaScript Ninja, semana 8, vídeo 03: escopo léxico preservado na função retornada (closure)
- [[wiki/sources/javascript-ninja-escopo-de-funcoes]]: JavaScript Ninja, semana 9, vídeo 01: função aninhada só existe dentro da externa e lê o escopo dela
