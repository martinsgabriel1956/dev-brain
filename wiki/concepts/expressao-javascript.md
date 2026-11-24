---
type: concept
title: "Expressão e instrução (JavaScript)"
aliases: ["expressão", "expression", "instrução", "statement", "expressão vs instrução", "expression vs statement"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 1
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

## Key sources

- [[wiki/sources/javascript-ninja-operadores-aritmeticos]]: expressão como "frase" avaliada; var x = 0 como exemplo (impreciso)
