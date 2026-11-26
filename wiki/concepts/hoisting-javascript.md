---
type: concept
title: "Hoisting (JavaScript)"
aliases: ["hoisting", "içamento", "elevação", "içar declarações", "temporal dead zone", "zona morta temporal", "TDZ"]
date_created: 2026-11-26
date_updated: 2026-11-26
source_count: 1
tags: [javascript, escopo, funcoes, var, let, const, hoisting]
skill: lang-dynamic
status: stub
---

# Hoisting (JavaScript)

Antes de executar um escopo (script, módulo, função ou bloco), o motor registra todas as declarações dele. O efeito é como se elas subissem para o topo do escopo `[external]` (https://developer.mozilla.org/en-US/docs/Glossary/Hoisting). O código não se move: é a fase de criação do escopo que acontece antes da primeira linha rodar.

| Declaração | O que sobe | Usar antes da linha |
|---|---|---|
| `function f() {}` | nome e corpo | funciona |
| `var x = 1` | só o nome, com `undefined` | dá `undefined` |
| `var f = function () {}` | só o nome `f`, com `undefined` | `TypeError: f is not a function` |
| `let` / `const` / `class` | o nome, sem valor (zona morta temporal) | `ReferenceError: Cannot access 'x' before initialization` |

Por isso uma `function` escrita depois do `return` ainda pode ser chamada pelo `return`. O `return` interrompe a execução, mas as declarações já foram registradas. O mesmo não vale para uma função em `var`/`const` ([[wiki/concepts/var-let-const]], [[wiki/concepts/arrow-functions]]).

Hoisting é por escopo: a `function` declarada dentro de outra sobe só até o topo da função de fora, e continua invisível fora dela ([[wiki/concepts/escopo-javascript]]). Guias de estilo costumam proibir o uso antes da declaração (`no-use-before-define` do ESLint) mesmo quando funciona `[external]`.

## No JavaScript Ninja, semana 9, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-escopo-de-funcoes]], `return sum()` vem antes de `function sum() {}` e funciona, contra a expectativa de `undefined` da própria aula ("tudo que acontece depois do return o JavaScript simplesmente ignora"). "Que magia é essa?" A aula dá o nome, hoisting, e deixa a explicação para o vídeo seguinte. Verificado no Node 22: com as variáveis também depois do `return`, o resultado vira `NaN`, porque só o nome delas sobe.

## Key sources

- [[wiki/sources/javascript-ninja-escopo-de-funcoes]]: JavaScript Ninja, semana 9, vídeo 01: função declarada depois do return funciona; nome anunciado
