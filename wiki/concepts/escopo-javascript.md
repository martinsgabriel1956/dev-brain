---
type: concept
title: "Escopo em JavaScript (global, de função e de bloco)"
aliases: ["escopo", "scope", "escopo de função", "escopo de bloco", "escopo global", "escopo léxico", "lexical scope", "function scope", "block scope"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 2
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

## Key sources

- [[wiki/sources/javascript-ninja-funcoes]]: var dentro da função não existe fora; o de fora é acessível de dentro
- [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]]: JavaScript Ninja, semana 4, vídeo 03: global × local, global implícita, parâmetros locais
