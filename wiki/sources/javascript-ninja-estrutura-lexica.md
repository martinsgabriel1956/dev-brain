---
type: source
title: "Estrutura léxica (JavaScript Ninja, semana 2, vídeo 03)"
aliases: ["JavaScript Ninja estrutura léxica", "JS Ninja case sensitive, comentários, literais, identificadores", "03 - Estrutura Léxica"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [javascript, estrutura-lexica, case-sensitive, comentarios, literais, identificadores, palavras-reservadas, unicode, naming]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-estrutura-lexica.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-24
---

# Estrutura léxica (JavaScript Ninja, semana 2, vídeo 03)

## TL;DR

Terceiro vídeo da "nossa segunda aula do curso" [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 13 min), depois de [[wiki/sources/javascript-ninja-operadores-unarios|operadores unários]]. [[wiki/entities/fernando-daciuk|Fernando Daciuk]] se apresenta ("Fernando da Silva" na legenda) e usa slides e o terminal.

- **Estrutura léxica** é "um conjunto de regras que vai definir [...] o modo que a gente vai usar para se escrever nessa linguagem": como nomear variáveis e funções, que caracteres usar, como comentar, "como separar uma instrução de outra" ([[wiki/concepts/estrutura-lexica-javascript]]).
- **Case sensitive:** `animal` e `Animal` são variáveis diferentes; `ANIMAL` "não está definido".
- **Comentários:** de linha (`//`), que o JavaScript "simplesmente ignora", e de bloco (`/* */`), para várias linhas ou uma só ([[wiki/concepts/comentarios-o-que-nao-o-como]]).
- **Literais:** "valores que aparecem diretamente no programa": `12`, `1.2`, strings com aspas simples ou duplas, booleanos, objeto (`{}`) e array (`[]`) literais.
- **Identificadores:** começam com letra, `_` ou `$`; depois aceitam dígitos de 0 a 9 e caracteres Unicode (`var π = 3.14` funciona), "mas você não deve utilizar", pelo bem "dos próximos desenvolvedores" ([[wiki/concepts/identificadores-javascript]]).
- **Palavras reservadas** (lista na [[wiki/entities/mdn-web-docs|MDN]]) não podem nomear variáveis nem funções; algumas, como `enum`, estão "reservadas pro futuro".
- Próximo vídeo: o desafio da semana.

## Key Claims

### O que é

- "Estrutura léxica de uma linguagem qualquer de programação é um conjunto de regras que vai definir quais são o modo que a gente vai usar para se escrever nessa linguagem."
- É "o nível mais baixo da linguagem": como "nomear variáveis, de como pode nomear funções, e tipo de caracteres que a gente pode utilizar. A forma como a gente cria comentários [...] Como separar uma instrução de outra."

### Case sensitive

- "Ele diferencia letras maiúsculas de letras minúsculas."
- `var animal = 'cachorro'` e `var Animal = 'macaco'`: "as duas variáveis são diferentes". `animal` devolve cachorro, `Animal` devolve macaco.
- Declarar `animal` e chamar `ANIMAL`: "ele vai dizer que o ANIMAL, todo em maiúsculo, não está definido".
- "Qualquer coisa que você escrever [...] cuide muito com a forma como você vai escrever."

### Comentários

- Dois formatos. O de linha "usa duas barras", como no desafio da semana passada: "o JavaScript simplesmente ignora [...] porque aquilo significa um comentário".
- Para quê: "dizer o que está sendo feito naquele momento, ou para você marcar alguns trechos de código". `// var animal = 'cachorro'` não define nada: "ele simplesmente ignora e não interpreta".
- O de bloco: "você pode escrever mais de uma linha"; "posso também utilizar em uma única linha, que funciona do mesmo jeito".

### Literais

- "Literais são valores que aparecem diretamente no programa. Digamos que são valores que não mudam. São valores que fazem parte do código JavaScript."
- Exemplos: o número `12` ("se eu colocar aqui no meu terminal [...] ele vai me retornar 12"), strings, booleanos, `1.2` ("um número decimal"), aspas simples ou duplas, objeto literal "formado pela chave" com "chave, 2 pontos, valor", e array literal.
- "Não existe nada que crie ele. Ele já existe dentro da linguagem JavaScript. Por isso ele é um literal."

### Identificadores

- "Identificadores nada mais são do que nomes": para "nomear uma variável, para nome[ar] uma função".
- "Eles podem iniciar com underscore ou $ [...] qualquer letra minúscula ou qualquer letra maiúscula"; "são os únicos caracteres diferentes que ele pode iniciar".
- "Eles podem conter, além de todos os caracteres que eu já falei, dígitos de 0 a 9."
- "Podem conter também qualquer caractere Unicode": `var π = 3.14` devolve 3,14. "Mas ele funcionou, sim, mas você não deve utilizar [...] pelo bem dos próximos desenvolvedores que forem pegando no teu código."
- O argumento: alguém "da Arábia Saudita" nomeando variáveis "com aqueles caracteres arábicos": "como que a gente aqui no Brasil vai ditar um código dele?" Com letras, dígitos, `_` e `$`, "você [vai] ter o código mundialmente fácil [de] digitar".

### Palavras reservadas

- Lista "no site da MDN", com o link na descrição do vídeo.
- "São palavras que o JavaScript separa [...] identificadores de palavras-chave da própria linguagem [...] que você não pode usar para nomear variáveis e nem para nomear funções."
- Exemplos (legenda muito ruim): `const`, `continue`, `debugger`, `default`, `delete`, `do`, `function`, `import`; "reservadas pro futuro": `enum`, `await`, `implements`, `protected`.

### Encerramento

- "Basicamente são essas regras que você precisa saber"; outras aparecem "com o andar do curso".

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para a gramática léxica de JavaScript; as precisões vêm da MDN (Lexical grammar) e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação). https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar

1. **"Valores que não mudam" mistura literal com constante.** Literal é a forma de escrever um valor no código. O valor de um literal primitivo é fixo, mas a variável que o recebe pode mudar, e `{}`/`[]` criam a cada avaliação um objeto novo e mutável: `var a = [1]; a.push(2)` vale. Imutabilidade é outro assunto ([[wiki/concepts/var-let-const]], [[wiki/concepts/objetos-javascript]]).
2. **Faltam literais.** `[external]` `null` é literal (`undefined` não: é uma propriedade global). Há ainda regex (`/ab+c/`), template (`` `oi ${x}` ``, [[wiki/concepts/template-literals]]), BigInt (`10n`), hexadecimal (`0xff`), binário (`0b1010`) e separador numérico (`1_000_000`, ES2021).
3. **"Qualquer caractere Unicode" é exagero.** `[external]` O primeiro caractere precisa ter a propriedade Unicode *ID_Start* (letras de qualquer alfabeto, `$`, `_`) e os seguintes *ID_Continue* (dígitos, alguns acentos combinantes). `π`, `ação` e `日本` valem; emoji não (`var 😀` é `SyntaxError`), nem começar com dígito ([[wiki/concepts/identificadores-javascript]], [[wiki/concepts/unicode]]).
4. **A recomendação de ASCII é estilo, não regra.** Nomes com acento funcionam e são legíveis para quem fala a língua; o argumento da aula é de colaboração internacional. Convenções como camelCase não aparecem ([[wiki/concepts/naming]]).
5. **Palavras reservadas mudaram desde a gravação.** `[external]` Hoje são reservadas sempre: `break`, `case`, `catch`, `class`, `const`, `continue`, `debugger`, `default`, `delete`, `do`, `else`, `export`, `extends`, `false`, `finally`, `for`, `function`, `if`, `import`, `in`, `instanceof`, `new`, `null`, `return`, `super`, `switch`, `this`, `throw`, `true`, `try`, `typeof`, `var`, `void`, `while`, `with`, e `enum` (a única ainda sem uso). `implements`, `interface`, `let`, `package`, `private`, `protected`, `public`, `static` e `yield` só em modo estrito; `await` só em módulos e funções `async`. `class`, `const`, `export`, `extends`, `import` e `super` eram "futuras" no ES5 e viraram palavras-chave no ES2015. `undefined`, `NaN` e `Infinity` não são reservadas. Como nomes de propriedade, reservadas valem: `obj.class` e `{ default: 1 }`.
6. **"Como separar uma instrução de outra" ficou só no anúncio.** O ponto e vírgula e a inserção automática (ASI) foram ditos na aula de funções; as armadilhas estão em [[wiki/concepts/pitfalls-de-linguagem]].
7. **`ANIMAL` não definido é `ReferenceError`.** Case sensitive vale também para palavras-chave (`Var` não é `var`) e para APIs (`document.getElementById`, não `getElementByID`).
8. **Comentário de bloco não aninha.** `/* a /* b */ c */` termina no primeiro `*/` e deixa `c */` como código. A convenção `/** */` é JSDoc ([[wiki/concepts/comentarios-o-que-nao-o-como]]).
9. **Onde isso aparece no compilador.** É o trabalho do *lexer*, a primeira fase da [[wiki/concepts/compilador|compilação]]: transformar o texto em tokens (identificadores, palavras-chave, literais, operadores) e descartar espaços e comentários.
10. **Legenda.** Trocas principais: "Lá"→Olá, "JavaScript inicia"→Ninja, "Fernando da Silva"→Fernando Daciuk, "léxico"→léxica, "aquele sensitivo"/"esse incentivo"/"Key Sensitive"→case sensitive, "vai mal"→var animal (média), "extingue"/"tinha"→string, "blog"→bloco, "uma rede"/"errei"→um array (média-alta), "quando eu escolhe"/"onde escolho"/"desktop"→underscore, "US$"→$, "o ícone"→Unicode (média-alta), "13 ou 14"→3,14, "pico"→pi (média), "ditos"/"distros"→dígitos (média), "MDL"→MDN, "elevadas"→reservadas, "conste"/"contínuo"/"de Bang"/"de fogo"/"foi no chão"/"importe"→const/continue/debugger/default/function/import, "em número ao Haiti implemente"→enum, await, implements (média-alta). Lista dos trechos literais no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor (se apresenta).
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.
- [[wiki/entities/mdn-web-docs]]: lista de palavras reservadas indicada.

## Concepts

- [[wiki/concepts/estrutura-lexica-javascript]] (criado neste ingest)
- [[wiki/concepts/identificadores-javascript]] (criado neste ingest)
- [[wiki/concepts/comentarios-o-que-nao-o-como]]
- [[wiki/concepts/naming]]
- [[wiki/concepts/unicode]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/template-literals]]
- [[wiki/concepts/var-let-const]]
- [[wiki/concepts/pitfalls-de-linguagem]]
- [[wiki/concepts/compilador]]

## Open Questions

- A lista de palavras reservadas está quase toda perdida na legenda ("gay, 15, LS, 7", "que se tem falha, ele fora", "isso"); pela ordem alfabética da MDN, devem ser `break`, `case`, `catch`/`class`, `else`, `export`/`extends`, `false`/`finally`, `for`, `if`. Inferência (média).
- "Você usa o basta" para abrir o comentário de bloco: provavelmente "barra asterisco"; ficou literal.
- "Fui chamado Marduk detonador de medo", "Tu entrou mesmo no menu 12": a legenda perdeu esses exemplos de literais.
- "Vou colocar um fim 3 ponto 14": provavelmente o próprio `π`; ficou literal.
- "Nossa segunda aula" confirma que os vídeos "01 – 03" desta leva são a aula 2 do curso; ver a nota de numeração em [[wiki/entities/javascript-ninja]].

## Raw quotes

- "um conjunto de regras que vai definir [...] o modo que a gente vai usar para se escrever nessa linguagem"
- "Mas ele funcionou, sim, mas você não deve utilizar."
- "você [vai] ter o código mundialmente fácil [de] digitar"
