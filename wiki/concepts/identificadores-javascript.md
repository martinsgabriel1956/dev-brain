---
type: concept
title: "Identificadores e palavras reservadas em JavaScript"
aliases: ["identificador", "identifier", "nome de variável", "palavras reservadas", "reserved words", "palavras-chave JavaScript", "keywords"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 1
tags: [javascript, identificadores, palavras-reservadas, naming, unicode, estrutura-lexica, lang-dynamic]
skill: lang-dynamic
status: stub
---

# Identificadores e palavras reservadas em JavaScript

Identificador é o nome de uma variável, função, classe, parâmetro ou rótulo. Faz parte da [[wiki/concepts/estrutura-lexica-javascript]]. `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers

## Regras

- **Primeiro caractere:** letra (de qualquer alfabeto, propriedade Unicode *ID_Start*), `$` ou `_`. Nunca dígito.
- **Seguintes:** os mesmos, mais dígitos e marcas combinantes (*ID_Continue*).
- `π`, `ação`, `$el`, `_privado`, `item2` valem; `2item`, `meu-nome`, `😀` não (`SyntaxError`).
- Escapes Unicode valem (`a` é `a`), mas ninguém usa.
- Diferenciam maiúsculas e minúsculas ([[wiki/concepts/estrutura-lexica-javascript]]).

Poder usar Unicode não quer dizer que se deva: em time internacional, ASCII é o comum. Convenções (camelCase para variáveis e funções, PascalCase para classes, `UPPER_SNAKE` para constantes) são estilo, não regra ([[wiki/concepts/naming]], [[wiki/concepts/unicode]]).

## Palavras reservadas

Não podem ser identificadores. `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#reserved_words

- **Sempre:** `break`, `case`, `catch`, `class`, `const`, `continue`, `debugger`, `default`, `delete`, `do`, `else`, `export`, `extends`, `false`, `finally`, `for`, `function`, `if`, `import`, `in`, `instanceof`, `new`, `null`, `return`, `super`, `switch`, `this`, `throw`, `true`, `try`, `typeof`, `var`, `void`, `while`, `with`.
- **Futura:** `enum`.
- **Só em modo estrito:** `implements`, `interface`, `let`, `package`, `private`, `protected`, `public`, `static`, `yield`.
- **Só em módulos e funções `async`:** `await`.
- **Não são reservadas**, apesar de parecerem: `undefined`, `NaN`, `Infinity` (globais não graváveis), `of`, `get`, `set`, `async`, `from` (palavras contextuais).

Como **nome de propriedade**, reservadas valem desde o ES5: `obj.class`, `{ default: 1 }`, `import.meta` ([[wiki/concepts/notacao-de-ponto-e-colchetes]]).

## No JavaScript Ninja, semana 2, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-estrutura-lexica]], identificadores "nada mais são do que nomes"; começam com letra, `_` ou `$` e depois aceitam dígitos. `var π = 3.14` funciona, "mas você não deve utilizar", pelo bem dos "próximos desenvolvedores". As palavras reservadas ficam num link para a MDN; a lista da aula (da era ES5, com `enum`, `implements`, `protected` como "futuras") mudou desde então. "Qualquer caractere Unicode" é exagero: emoji não vale.

## Key sources

- [[wiki/sources/javascript-ninja-estrutura-lexica]]: JavaScript Ninja, semana 2, vídeo 03: regras de identificador, Unicode e palavras reservadas
