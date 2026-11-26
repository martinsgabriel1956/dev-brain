---
type: source
title: "Hoisting (JavaScript Ninja, semana 9, vídeo 02)"
aliases: ["JavaScript Ninja hoisting", "JS Ninja içamento", "02 - hoisting"]
date_created: 2026-11-26
date_updated: 2026-11-26
source_count: 0
tags: [javascript, hoisting, escopo, funcoes, var, function-declaration, function-expression, undefined]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-hoisting.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-26
---

# Hoisting (JavaScript Ninja, semana 9, vídeo 02)

## TL;DR

Segundo vídeo da semana 9 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 14,5 min), de [[wiki/entities/fernando-daciuk|Fernando Daciuk]]. Explica a "magia" que fechou [[wiki/sources/javascript-ninja-escopo-de-funcoes|escopo de funções]]: a `function sum` escrita depois do `return` que ainda funciona ([[wiki/concepts/hoisting-javascript]]).

- **O nome:** hoisting, que tradutores vertem como "içamento ou elevação: algo que você está movendo para cima".
- **Função literal sobe inteira:** o JavaScript "pega todas as funções, funções literais, e joga pra cima", para o início da função, e elas valem "para todo o escopo da função". Por isso `return sum()` antes da declaração funciona.
- **Função atribuída a variável, não:** com `var sum = function ...` depois do `return`, o erro é "is not a function". A variável sobe "como um undefined" e só recebe a função na linha da atribuição, que nunca roda ([[wiki/concepts/var-let-const]]).
- **Variáveis:** `console.log` antes e depois de `var ... = 10` mostra `undefined` e depois 10; uma variável nunca declarada dá "não foi definida" (`ReferenceError`). "Variáveis, elas existem dentro do escopo onde elas estão, mas elas só estão disponíveis a partir do momento onde elas foram declaradas" ([[wiki/concepts/null-e-undefined]]).
- **Escopos:** `myFunction`, fora de qualquer função, está no escopo global; `sum`, dentro dela, no local ([[wiki/concepts/escopo-javascript]]).
- **A dica:** não escrever função depois do `return` ("não faz sentido nenhum"); declarar as variáveis "sempre no início da função", depois as funções literais, e o `return` "sempre na última linha da função", salvo um `return` dentro de `if`.

## Key Claims

### O que é hoisting

- "Essa funcionalidade do JavaScript [...] traduzem isso como içamento ou elevação, algo que você está movendo para cima."
- Com variáveis: "o JavaScript pega essa variável, move para cima como um undefined, e depois, naquele ponto da variável, que ele atribui valor."

### Função literal × função atribuída a variável

- "Quando eu tenho uma função literal em JavaScript, ainda que eu retorne [...] ela cria ela depois de uma instrução britânico [provavelmente return] [...] ele pega essa função e moda aqui pra cima."
- "Sempre que tiver uma função literal, ela vai valer para todo o escopo da função."
- Com `sum` atribuída a uma variável depois do `return`: "Ele disse [...] is not a function. Ou seja, agora ele disse que a função sum não existe."
- "Quando eu tenho uma função declarada aqui para uma variável, ele pega essa variável, ele coloca aqui como um undefined, e depois [...] ele cria a variável e atribui a função."
- "Funções literais [...] estão disponíveis dentro de todo o escopo onde elas foram criadas. [...] Mas variáveis, elas só estão disponíveis a partir do ponto [...] onde é feita a atribuição para elas."

### Hoisting de variáveis

- Uma variável com valor dez, lida por `console.log` com os rótulos "antes de declarar" e "depois de declarar". "Você pode passar parâmetros para o console. Então você pode separar por vírgula."
- Um erro ao vivo: "eu esqueci de colocar vírgula para separar [...] foi besteira minha".
- Antes da declaração, o valor é `undefined`: "ele não disse que a variável não existia". Para uma variável nunca criada, "ele disse que [...] não foi definida. Ou seja, não foi nem criada."
- "O JavaScript [...] declara ela, não coloca atribuição nenhuma, e aqui, onde ela está sendo atribuída, [...] ele faz a atribuição."

### Recapitulação

- A função literal: "ele joga a função pra cima e simplesmente executa".
- "O escopo dela vai ser sempre a função onde ela está dentro. E essa função, myFunction, [...] ela está disponível no escopo global. [...] Eu tenho myFunction no escopo global, e eu tenho a função sum no escopo local."
- Uma variável com 50: na primeira leitura `undefined`, depois 50. O terceiro valor vem da função sem `return`, que "simplesmente inventou um valor em branco pra mim".

### A dica

- "Isso pode causar efeitos colaterais na hora de você desenvolver um programa."
- "Obviamente você não vai fazer isso aqui, que é uma função depois do return. Não faz sentido nenhum." Mas "se você vê um código dessa forma, você sabe que assim ele vai funcionar."
- "Sempre que você for declarar uma variável, [declare] no início da função [...] porque é basicamente isso que o JavaScript vai fazer se você não fizer."
- Dá para declarar no topo sem valor e atribuir depois, "não tem problema nenhum", mas são "quatro linhas" onde "você poderia economizar isso com duas".
- Depois das variáveis, "suas funções literais", e "no final [...] retorne sempre na última linha da função, a não ser que" seja "um return dentro do if".
- "A dica [...] pra evitar problemas com hoisting no JavaScript é declarar sempre funções, variáveis no início da função."

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para hoisting. As precisões vêm da MDN e da especificação, marcadas `[external]`, sem fetch. As demos foram reproduzidas no Node 22.23.

1. **"Função literal" é a declaração de função.** `[external]` O nome técnico é *function declaration* (`function sum() {}` como instrução). A atribuída a variável é *function expression* (`var sum = function () {}`). O curso já chamava a declaração de "literal" em [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]]. Isso confunde, porque a expressão também é um literal de função.
2. **Nada se move.** `[external]` "Joga pra cima" é a metáfora usual; o glossário da MDN diz que o interpretador "parece mover" as declarações para o topo. Mas o código não é reescrito: o motor cria os nomes do escopo antes de executar o corpo. É isso que explica o "ignora o que vem depois do return": a execução para no `return`, e o registro dos nomes já aconteceu.
3. **O erro da expressão é `TypeError`.** Verificado: `var sum = function sum() {...}` depois do `return` dá `TypeError: sum is not a function`. O nome existe e vale `undefined`, então a chamada falha. A variável nunca declarada dá `ReferenceError: dois is not defined`. A aula mostra os dois sem nomear a diferença.
4. **`let`, `const` e `class` também são içados.** `[external]` Mas ficam na zona morta temporal: ler antes da linha dá `ReferenceError: Cannot access 'x' before initialization`, não `undefined`. Uma *arrow function* em `const` se comporta assim. A aula é da era ES5 e só usa `var` ([[wiki/concepts/var-let-const]], [[wiki/concepts/arrow-functions]]).
5. **"Declare no topo" é conselho da era `var`.** `[external]` Crockford e o JSLint pediam um `var` no topo de cada função, justamente por causa do hoisting. Com `let`/`const`, a recomendação atual (por exemplo, no guia da Airbnb) é declarar perto do primeiro uso, e a TDZ pega o uso antecipado. O curso, na semana 6, já preferia um `var` por variável ([[wiki/sources/javascript-ninja-operador-virgula-e-switch]]).
6. **"Return sempre na última linha" contra o *early return*.** `[external]` A própria aula abre exceção para o `return` dentro de `if`. Esse retorno antecipado (*guard clause*) é a prática recomendada para reduzir aninhamento ([[wiki/concepts/estruturas-condicionais-javascript]]). A regra vale para o `return` final, não para todos.
7. **"Global" depende de onde o arquivo roda.** `[external]` Num script do navegador ou no REPL, `function myFunction` no topo vira propriedade do objeto global. Num arquivo executado pelo Node (CommonJS), o topo é o escopo do módulo: `typeof globalThis.myFunction` dá `'undefined'` (verificado). Para a aula a diferença não importa, porque `myFunction` é acessível em todo o arquivo ([[wiki/concepts/poluicao-do-escopo-global]]).
8. **"Valor em branco" é `undefined`.** A função sem `return` devolve `undefined` (verificado); o `console.log` imprime `undefined`, não vazio ([[wiki/concepts/funcoes-javascript]]).
9. **A vírgula esquecida.** `console.log("antes" x)` dá `SyntaxError: missing ) after argument list` (verificado), e o arquivo nem começa a rodar. É o erro ao vivo da aula.
10. **Legenda.** Trocas principais: "da Silva"→Daciuk, "Rochinha"/"restinho"/"rostinho"→hoisting, "pensamento"→içamento, "default"→undefined (3×), "Fonte Santa"→função sum, "mais infantil"/"uma infantil"→myFunction, "parabéns"→parâmetros, "da internet"→do return, "uma internet dentro do iPhone"→um return dentro do if. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/hoisting-javascript]]
- [[wiki/concepts/var-let-const]]
- [[wiki/concepts/escopo-javascript]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/null-e-undefined]]
- [[wiki/concepts/arrow-functions]]
- [[wiki/concepts/poluicao-do-escopo-global]]
- [[wiki/concepts/estruturas-condicionais-javascript]]

## Open Questions

- **"Significa royalty na tradução literal".** Talvez "hoisting, que significa içamento", com o termo trocado (média-baixa). Ficou literal; "Augusto citou alguns tradutores" também.
- **"Depois de uma instrução britânico"** e **"depois do ano"**: pela demo, "depois do return" (média). Literais no raw.
- **"Fazer o gol e jogar para cima"** e **"pega o jogador para cima"**: talvez "fazer o hoisting" e "joga ela para cima"; literais.
- **Os nomes da demo de variáveis.** "Uma variável chamada de novo", "o ano", "a variável ano", "dois"/"2 não foi definida" e "50 quilos no valor de um ano" não dão para reconstruir. A variável nunca declarada parece ser `dois` ou `two`.
- **"Onde DJs"**: talvez `node index.js`; literal.
- **"Ele declarou como diferente"** e **"como definidas"**: talvez "como undefined"; literais.
- **"Sobre Tim"** no fecho: talvez "sobre hoisting"; literal.
- O vídeo seguinte não é anunciado.

## Raw quotes

- "traduzem isso como içamento ou elevação, algo que você está movendo para cima"
- "variáveis, elas existem dentro do escopo onde elas estão, mas elas só estão disponíveis a partir do momento onde elas foram declaradas"
- "obviamente você não vai fazer isso aqui, que é uma função depois do return"
