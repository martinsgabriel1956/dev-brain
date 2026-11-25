---
type: source
title: "A importância de nomear funções (JavaScript Ninja, semana 8, vídeo 01)"
aliases: ["JavaScript Ninja nomear funções", "JS Ninja function name", "01 - A importância de nomear funções", "função nomeada JavaScript Ninja"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 0
tags: [javascript, funcoes, funcao-anonima, funcao-nomeada, function-name, debugging, stack-trace, function-expression, function-declaration, naming, es2015]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-a-importancia-de-nomear-funcoes.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-25
---

# A importância de nomear funções (JavaScript Ninja, semana 8, vídeo 01)

## TL;DR

Primeiro vídeo depois da revisão do desafio da semana 7 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 9 min), por isso citado como semana 8 (inferência, alta). Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] ("Fernando da Silva" na legenda). Abre "algumas partes um pouco mais avançadas do uso de funções" ([[wiki/concepts/funcoes-javascript]]).

- **A regra nova:** "a partir de agora a gente vai procurar sempre dar nome às nossas funções", inclusive quando a função é atribuída a uma variável, "de preferência o mesmo nome" da variável ([[wiki/concepts/naming]]).
- **Por quê:** facilita o debug, porque "o debug, normalmente, ou do Node, ou do navegador, ele vai utilizar o nome da função" ([[wiki/concepts/debugging]]).
- **Função é objeto:** tem propriedades e métodos "embutidos"; um deles é `name`, que "retorna o nome da função" ([[wiki/concepts/objetos-javascript]], [[wiki/concepts/funcoes-de-primeira-classe]]).
- **Invocar × referenciar:** `func()` devolve o retorno ("Ray"); `func.name` sem invocar lê a propriedade, que "vem em branco" porque a função é anônima.
- **Sem nome não cria:** `function () {}` solto no console dá erro; atribuída a uma variável, cria normalmente ([[wiki/concepts/expressao-javascript]]).
- **Com nome:** `var funcShow = function funcShow() {}`, e `funcShow.name` traz "o nome da função mesmo", não o da variável.
- **Função literal** (`function nome() {}`): invocada pelo próprio nome; `name` também traz o nome. Diferença entre os tipos de função fica "para depois".
- **Anônimas continuam valendo** "em alguns casos específicos", quando for dito explicitamente.
- **Próximo vídeo:** "programação funcional em JavaScript" ([[wiki/concepts/programacao-funcional]]).

## Key Claims

### A regra

- "Até agora a gente tem colocado, quando a gente atribui uma função a uma variável, [...] uma função anônima."
- "A partir de agora a gente vai procurar sempre dar nome às nossas funções."
- "Vou atribuir uma função chamada de [...], que também pode ser o mesmo nome da variável. De preferência o mesmo nome [...] para ficar mais facilmente encontrada."
- "A partir de hoje, todos os exercícios que a gente fizer, quando estiver criando função e a gente for atribuir [a] uma variável, a gente vai sempre nomear a função."

### Por que nomear: debug

- "Quando a gente precisa encontrar erros, ou procurar por erros no nosso código, fica muito mais fácil encontrar um problema se uma função estiver nomeada."
- "Porque o debug, normalmente, ou do Node, ou do navegador, ele vai utilizar o nome da função pra poder debugar."
- A objeção: "se você atribui uma função a uma variável, eu não consigo invocar ela usando o nome da variável? Sim, a gente consegue." O problema é outro: função é objeto, e o objeto guarda o próprio nome.

### Função é objeto; a propriedade name

- "Funções, elas, na verdade, são um tipo de objeto [...] elas podem ter propriedades e elas podem ter métodos também."
- "O próprio objeto de função [...] tem algumas propriedades e alguns métodos embutidos. [...] Um deles é o método name, que [...] retorna o nome da função." (Chama de método; é propriedade.)
- `var func = function () { return 'Ray' }`: `func()` mostra "o Ray, que é o retorno dessa função"; `func.name`, sem invocar, "como não nomeei a função, o name ele vem em branco".
- "Invocação é você utilizar os parênteses logo após a função, é uma das formas de invocar a função."

### Sem nome, não dá para criar solta

- "Eu crio uma função assim, eu não consigo invocar ela, já que ele espera que eu passo [...] um nome para essa função."
- "A partir do momento em que eu [...] atribuo a ela para uma variável, [...] eu consigo criar a função normalmente." Invocada, devolve `undefined`, "porque eu não tenho nenhum retorno" ([[wiki/concepts/null-e-undefined]]).

### Nomeando

- `var funcShow = function funcShow() {}`: "ele vai trazer para mim o nome da função. Ou seja, não é uma variável que ele vai trazer, é o nome da função mesmo."
- "Ainda que eu atribuo uma variável àquela função, a variável não quer dizer que [é] o nome da função [...] uma variável só está recebendo."

### Função literal e anônimas

- Função literal "como eu não atribuí a variável, vou invocar ela com o nome da função"; sem invocar, "somente como um objeto", o `name` devolve o nome dela.
- "A gente vai ver depois [...] qualquer diferença de função literal, e por que existe a função literal, e qual outro tipo de função que existe também."
- "Funções anônimas é um recurso bastante interessante do JavaScript [...] e a gente vai utilizar bastante esse formato também."
- "Na maioria dos casos agora a gente vai sempre nomear a função, a não ser que isso explicitamente seja dito, que aquela função não precisa de um nome."

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para `Function.prototype.name` nem para nomes de função em stack trace (busca em `nodejs-diagnostics.md` e `nodejs-core.md` sem resultado). As precisões vêm da MDN e da especificação, marcadas `[external]`; os comportamentos foram reproduzidos no Node 22.23. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name

1. **O `name` em branco não se reproduz mais.** `[external]` Desde o ES2015, a função anônima atribuída a uma variável ganha o nome dela por inferência: `var func = function () { return 'Ray' }; func.name` dá `'func'` (verificado no Node 22). A aula é de antes disso, num Node que ainda devolvia `''` (inferência, alta). Continua vazio quando não há nome para inferir: `(function () {}).name` e `[function () {}][0].name` dão `''` (verificado). A página [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]] já registrava a inferência ([[wiki/concepts/ecmascript]]).
2. **Onde nomear ainda paga.** `[external]` Em callback, o stack trace mostra o nome só se a função tiver um: com `[1].map(function () { throw ... })` a linha sai `at [eval]:9:33`; com `function cb()`, `at cb (...)` (verificado). O argumento do debug, então, vale hoje sobretudo para callbacks, IIFEs e handlers, e menos para `var x = function () {}` ([[wiki/concepts/callback-javascript]], [[wiki/concepts/debugging]]).
3. **`name` é propriedade, não método.** `[external]` Não se invoca (`func.name`, sem parênteses) e é somente leitura: o descritor é `writable: false, configurable: true` (verificado).
4. **O erro não é de invocar.** `[external]` `function () {}` no início de uma linha é lido como declaração, e declaração exige nome: `SyntaxError: Function statements require a function name` (verificado). Não tem a ver com não conseguir invocar. Entre parênteses, `(function () {})`, vira expressão e é válida ([[wiki/concepts/expressao-javascript]]).
5. **O nome da expressão é interno.** `[external]` Em `var a = function outro() {}`, `a.name` dá `'outro'`, mas `outro` não existe fora da função (`typeof outro` dá `'undefined'`, verificado). Dentro, serve para recursão segura: `var g = function fat(n) { return n <= 1 ? 1 : n * fat(n - 1) }` dá 120 para 5, mesmo se `g` for reatribuída. Usar o mesmo nome da variável, como a aula pede, evita a confusão.
6. **"Função literal".** A aula chama `function nome() {}` de função literal. Na MDN isso é *function declaration*; "function literal" costuma nomear a forma com `function` em geral, inclusive a expressão (uso de Douglas Crockford em *JavaScript: The Good Parts*, de memória, não verificado). A diferença prática que a aula adia é o hoisting: a declaração existe antes da linha em que aparece; a expressão em `var`, não `[external]`.
7. **Arrow functions.** `[external]` São sempre anônimas na sintaxe e dependem da inferência para ter `name` ([[wiki/concepts/arrow-functions]]). A regra "sempre nomear" da aula não se aplica a elas; a aula é anterior ao uso corrente de arrow.
8. **Legenda.** Trocas principais: "na índia"→Ninja; "da Silva"→Daciuk; "nem me"/"nem"/"no time"/"Ney"→name (8×); "funk"/"varanda Infante"→func; "funk Show"/"vai fazer show"→funcShow; "Bangu é"/"debate de ideias"/"divulgar"→debug/debugar; "Nordeste"→Node; "boletim"→built-in; "instrutor"→interpretador; "diferente"→undefined; "no meio"/"o nome e"/"no nome e"→nomeia/nomeei; "lateral"→literal; "queria"/"querer"→crio/criar; "sim vou catar"→sem invocar; "ficção"/"fonte"→função. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.
- [[wiki/entities/nodejs]]: o console da demonstração; citado como debugger.

## Concepts

- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/funcoes-de-primeira-classe]]
- [[wiki/concepts/naming]]
- [[wiki/concepts/debugging]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/expressao-javascript]]
- [[wiki/concepts/callback-javascript]]
- [[wiki/concepts/ecmascript]]
- [[wiki/concepts/arrow-functions]]
- [[wiki/concepts/null-e-undefined]]
- [[wiki/concepts/programacao-funcional]]

Vídeo anterior do curso na wiki: [[wiki/sources/javascript-ninja-arrays-metodo-push-e-loop-for]] (semana 7, vídeo 03). A revisão do desafio da semana 7, citada na abertura, não está na wiki.

Vídeo seguinte na wiki: [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]] (semana 8, vídeo 02), o de programação funcional que este anuncia.

## Open Questions

- **"Uma função chamada de fala"**: o nome dado no primeiro exemplo (talvez `func`); baixa. Literal.
- **"Eu chamava de espontânea"**: provavelmente `func.name` digitado no console (média); literal.
- **"O nome de frente com uma função" / "eu chamo de ponto name"**: provavelmente "o nome de func pra função" e `func.name` (média); literal.
- **"Mais fundo são dois" / "estão falando que são dois" / "pegar para cuidar de mim"**: o nome da função literal (algo como `myFunction2`) e "pegar a propriedade name"; baixa. Literal.
- **"Ray"**: o valor retornado pelo exemplo (talvez `'hey'`); a legenda escreve "Ray" duas vezes. Literal.
- **"Agora já JavaScript" / "a linguagem"**: abertura e transição ilegíveis (baixa).

## Raw quotes

- "A partir de agora a gente vai procurar sempre dar nome às nossas funções."
- "O debug [...] ele vai utilizar o nome da função pra poder debugar."
- "Não é uma variável que ele vai trazer, é o nome da função mesmo."
