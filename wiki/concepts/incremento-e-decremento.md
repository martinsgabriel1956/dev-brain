---
type: concept
title: "Incremento e decremento (++ e --)"
aliases: ["++", "--", "incremento", "decremento", "pós-incremento", "pré-incremento", "pós-decremento", "pré-decremento", "i++", "++i", "postfix increment", "prefix increment"]
date_created: 2026-11-24
date_updated: 2026-11-25
source_count: 5
tags: [javascript, operadores, incremento, decremento, expressoes]
skill: lang-dynamic
status: stub
---

# Incremento e decremento (`++` e `--`)

`x++` e `++x` somam 1 a `x`; `x--` e `--x` subtraem 1. A posição decide o **valor da expressão**, não o efeito:

| | Efeito em `x` (começando em 5) | Valor devolvido |
|---|---|---|
| `x++` (pós) | 6 | 5, o antigo |
| `++x` (pré) | 6 | 6, o novo |
| `x--` (pós) | 4 | 5 |
| `--x` (pré) | 4 | 4 |

`[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment

- **Sozinhos numa linha, pré e pós fazem o mesmo.** A diferença só aparece quando o valor é usado: `y = x++`, `arr[i++]`, `console.log(++x)`, ou o eco do REPL.
- **Só valem para referências:** variável ou propriedade (`obj.n++`, `arr[0]++`). `5++` é `SyntaxError`; numa `const`, `TypeError`.
- **Convertem para número**, ao contrário de `+=`: com `let s = '5'`, `s++` deixa 6, mas `s += 1` dá `'51'` ([[wiki/concepts/atribuicao-composta]]).
- **Uso típico:** o passo do `for` (`i++`), onde pré e pós dão no mesmo ([[wiki/concepts/estruturas-de-repeticao-javascript]]).
- **Estilo:** Douglas Crockford desaconselhava `++`/`--`, e a regra `no-plusplus` do ESLint os proíbe (fora do `for`, se configurada), preferindo `x += 1` por clareza (média-alta) ([[wiki/concepts/pitfalls-de-linguagem]]).

## No JavaScript Ninja (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-aritmeticos]], os dois são "operadores aritméticos abreviados". No REPL: `soma++` ecoa o valor antigo e deixa 22; `++soma` "já vai, adicionou mais um, e depois ele vai interpretar o valor", e mostra 23; `soma--` mostra 22 e deixa 21; `--soma` mostra 20. A demonstração está certa; o nome "abreviado" mistura `++` com `+=`.

Em [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]], `i++` "é exatamente igual" a `i = i + 1`: vale como instrução, não como expressão ([[wiki/concepts/operadores-aritmeticos-javascript]]).

## No JavaScript Ninja, semana 2, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-unarios]], `++` e `--` entram como operadores unários que, ao contrário de `+x` e `-x`, "causam o efeito colateral. Ele atribui o novo valor a essa variável": com `x = 3`, `x++` deixa 4 e `++x` deixa 5 ([[wiki/concepts/operadores-unarios-javascript]]).

## No JavaScript Ninja, semana 3, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-metodos-de-objeto]], `pessoa.idade++` dentro do método `aniversario`: o `++` "vai incrementar o valor e vai automaticamente atribuir", e funciona sobre propriedade como sobre variável. A legenda o chama de "operador binário"; é unário.

## No JavaScript Ninja, semana 6, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operador-virgula-e-switch]], `return x += 1, x` é "a mesma coisa que usar o operador de pré-incremento": soma, depois devolve o último valor da sequência, como `return ++x` ([[wiki/concepts/operador-virgula-javascript]]).

## No JavaScript Ninja, semana 6, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-estrutura-de-repeticao-while]], `console.log(counter--)` imprime e "daí atribui menos um"; com o `--` na condição, `while (counter--)` testa o valor antigo, então o corpo imprime de 9 a 0 e o contador termina em -1.

## Key sources

- [[wiki/sources/javascript-ninja-operadores-aritmeticos]]: pós e pré-incremento e decremento pelo eco do REPL
- [[wiki/sources/javascript-ninja-operadores-unarios]]: JavaScript Ninja, semana 2, vídeo 02: ++/-- como unários com efeito colateral
- [[wiki/sources/javascript-ninja-metodos-de-objeto]]: JavaScript Ninja, semana 3, vídeo 02: ++ em propriedade de objeto
- [[wiki/sources/javascript-ninja-operador-virgula-e-switch]]: JavaScript Ninja, semana 6, vídeo 01: return x += 1, x equivale a return ++x
- [[wiki/sources/javascript-ninja-estrutura-de-repeticao-while]]: JavaScript Ninja, semana 6, vídeo 02: counter-- no corpo e na condição do while
