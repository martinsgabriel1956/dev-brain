---
type: concept
title: "Estrutura léxica do JavaScript"
aliases: ["gramática léxica", "lexical grammar", "estrutura léxica", "case sensitive", "literais JavaScript", "literal", "comentários em JavaScript"]
date_created: 2026-11-24
date_updated: 2026-11-27
source_count: 2
tags: [javascript, estrutura-lexica, case-sensitive, comentarios, literais, tokens, lang-dynamic]
skill: lang-dynamic
status: stub
---

# Estrutura léxica do JavaScript

As regras do nível mais baixo da linguagem: como o texto do código vira tokens. Define espaços e quebras de linha, comentários, identificadores, palavras reservadas, literais, pontuação e a inserção automática de ponto e vírgula. É o que o *lexer* aplica na primeira fase da [[wiki/concepts/compilador|compilação]]. `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar

## Case sensitive

Maiúsculas e minúsculas contam: `animal`, `Animal` e `ANIMAL` são três nomes. Usar um que não foi declarado dá `ReferenceError`. Vale para palavras-chave (`Var` não é `var`) e APIs (`getElementById`).

## Espaços e comentários

Espaços, tabs e quebras de linha só separam tokens (`a+++b` é `a++ + b`). Quebra de linha também conta para a ASI ([[wiki/concepts/pitfalls-de-linguagem]]).

- `// até o fim da linha`
- `/* bloco, uma ou várias linhas */`, que não aninha
- `/** ... */`, convenção JSDoc
- `#!/usr/bin/env node` na primeira linha (hashbang, ES2023)

Quando comentar: [[wiki/concepts/comentarios-o-que-nao-o-como]].

## Literais

A forma de escrever um valor direto no código, sem calcular nem chamar nada:

| Tipo | Exemplos |
|---|---|
| Número | `12`, `1.2`, `.5`, `1e3`, `0xff`, `0b1010`, `0o17`, `1_000_000` |
| BigInt | `10n` |
| String | `'a'`, `"a"`, `` `a ${x}` `` ([[wiki/concepts/template-literals]]) |
| Booleano e nulo | `true`, `false`, `null` |
| Objeto e array | `{ nome: 'x' }`, `[1, 2]` ([[wiki/concepts/objetos-javascript]]) |
| Regex | `/ab+c/i` |

`undefined` não é literal: é uma propriedade global ([[wiki/concepts/null-e-undefined]]). Literal não quer dizer imutável: `{}` e `[]` criam um objeto novo e alterável a cada avaliação, e a variável que recebe o literal pode ser reatribuída ([[wiki/concepts/var-let-const]]).

## Identificadores e palavras reservadas

Regras de nomes e a lista do que não pode ser nome: [[wiki/concepts/identificadores-javascript]].

## No JavaScript Ninja, semana 2, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-estrutura-lexica]], estrutura léxica é "um conjunto de regras que vai definir [...] o modo que a gente vai usar para se escrever nessa linguagem". A aula cobre case sensitive (`animal` × `Animal`), os dois comentários, literais como "valores que aparecem diretamente no programa" (e, impreciso, "que não mudam"), identificadores e palavras reservadas. "Como separar uma instrução de outra" é anunciado, mas não tratado.

Relacionado: [[wiki/concepts/tipos-primitivos-javascript]], [[wiki/concepts/expressao-javascript]].

## No JavaScript Ninja, semana 11, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-lacos-loops]], o ponto e vírgula depois do `while (...)` de um `do...while` é apresentado como obrigatório. Desde o ES2015 a inserção automática o cobre, mesmo na mesma linha (verificado); fica como estilo.

## Key sources

- [[wiki/sources/javascript-ninja-estrutura-lexica]]: JavaScript Ninja, semana 2, vídeo 03: case sensitive, comentários, literais, identificadores, reservadas
- [[wiki/sources/javascript-ninja-lacos-loops]]: JavaScript Ninja, semana 11, vídeo 01: ; depois do do...while e a inserção automática
