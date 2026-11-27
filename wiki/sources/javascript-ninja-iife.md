---
type: source
title: "IIFE (JavaScript Ninja, semana 9, vídeo 03)"
aliases: ["JavaScript Ninja IIFE", "JS Ninja função autoexecutável", "03 - IIFE - Immediately-Invoked Function Expression"]
date_created: 2026-11-26
date_updated: 2026-11-27
source_count: 0
tags: [javascript, iife, funcoes, function-expression, escopo, escopo-global, named-function-expression]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-iife.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-26
---

# IIFE (JavaScript Ninja, semana 9, vídeo 03)

## TL;DR

Terceiro vídeo da semana 9 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 13 min), de [[wiki/entities/fernando-daciuk|Fernando Daciuk]], depois de [[wiki/sources/javascript-ninja-hoisting|hoisting]]. Apresenta a [[wiki/concepts/iife|IIFE]], *Immediately-Invoked Function Expression*: "uma expressão [de] função invocada imediatamente, ou uma função auto executável".

- **Para invocar, é preciso um nome:** `sum` (declaração) se chama pelo nome; `var sum2 = function () {...}` (anônima) se chama pelo nome da variável, porque funções são "objetos de primeira classe" ([[wiki/concepts/funcoes-de-primeira-classe]]).
- **O nome de uma função atribuída a variável só existe dentro dela:** `sum3` recebe uma função com nome próprio. Chamada pelo nome interno de fora, dá erro; de dentro, funciona ("só que ela existe dentro desse escopo") ([[wiki/concepts/escopo-javascript]]).
- **Anônima solta não tem como invocar**, a não ser atribuída a variável ou a "uma propriedade do objeto" (`objeto.prop()`) ([[wiki/concepts/objetos-javascript]]).
- **Declaração não se invoca direto:** `function ... () {...}()` dá "um erro sintático", o parêntese "não era esperado". Envolvendo a função em parênteses, ela vira "uma expressão de função", e aí `(function () {...})()` executa na hora ([[wiki/concepts/expressao-javascript]]).
- **Os parênteses da chamada podem ficar dentro ou fora:** `(function () {}())` e `(function () {})()` "funcionam do mesmo jeito".
- **A vantagem:** "você fecha um escopo local. Você não precisa ter um escopo global". Com 30 arquivos, uma global mudada em um muda em todos ([[wiki/concepts/poluicao-do-escopo-global]]).
- **Regra do curso daqui em diante:** todos os desafios virão dentro de uma IIFE, "escopo local para tudo".

## Key Claims

### Nome

- "Na verdade, o que significa IIFE? Significa *Immediately-Invoked Function Expression*, o que significa, na verdade, uma expressão [de] função invocada imediatamente, ou uma função auto executável."

### Como invocar uma função

- "Para você executar uma função, você precisa de um nome para chamar ela."
- `sum`, "função literal": "executou ela chamando ela pelo nome e usando os parênteses".
- `sum2` é anônima, mas "foi atribuída a uma variável [...] consigo executar essa função [...] através do nome da variável", "como funções são objetos de primeira classe".

### Nome próprio da função em variável

- `sum3` recebe uma função com nome próprio (ilegível na legenda): `sum` dá 3, `sum2` dá 5 e `sum3` dá 13 (5 + 8). Chamar o nome interno de fora: "ele não existe [...] porque, na verdade, ele é uma função que foi atribuída somente a sum3."
- Com um `console.log` dentro da função, chamando o nome interno sem executar: o log aparece, "ou seja, ele existe [...] Só que ela existe dentro desse escopo [...] porque é aqui que ela foi criada".

### Anônima sem nome

- "Não existe uma forma de eu executar uma função anônima se ela não tiver o nome, ou [...] não for atribuído a uma variável, ou [...] uma propriedade do objeto."
- Objeto com uma propriedade que recebe uma função anônima: "ainda que anônima, sem nome [...] eu consigo executar". O retorno é 3.

### Transformar em expressão

- Invocar a declaração direto: "vai dar um erro sintático [...] dizendo que não era esperado o parênteses ali, porque é uma função literal."
- "Ela precisa ser, ou se tornar, uma expressão. [...] É uma das formas de utilizar parênteses para envolver a função."
- "Quando ela está dentro [dos parênteses] [...] agora é uma expressão, e melhor, uma expressão de função, que seria basicamente a mesma coisa que eu atribuir [a] uma variável."
- "Ele pegou essa expressão e, automaticamente, a partir do momento em que ele termina de fazer a leitura da função, ele executa ela."
- Como o retorno não tem onde ficar, a IIFE vai dentro de um `console.log`: o resultado é 3.

### A vantagem

- "Você fecha um escopo local. Você não precisa ter um escopo global."
- "Os parênteses [...] posso colocar tanto aqui dentro como fora dos primeiros parênteses, que ele vai funcionar do mesmo jeito."
- "Imagine que você tem lá 30 arquivos JavaScript [...] Se em outros arquivos JavaScript você mudar o valor dessa variável, o valor dessa variável vai ser [...] alterado [em] todos os arquivos." "Quanto menor for o teu escopo, melhor para você."
- Promete projetos pequenos, em equipe, com "vários testes com essa questão de objetos globais".

### Desafios em IIFE

- "A partir de agora, todos os nossos [...] desafios, eles vão estar dentro de uma IIFE." "A gente vai manter a prática de usar sempre escopo local para tudo."

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para IIFE. As precisões vêm da MDN e da especificação, marcadas `[external]`, sem fetch. As demos foram reproduzidas no Node 22.23.

1. **O erro depende de a função ter nome.** Verificado: `function () { return 1 + 2 }()` dá `SyntaxError: Function statements require a function name`; `function sum() { return 1 + 2 }()` dá `SyntaxError: Unexpected token ')'`, o "não era esperado o parênteses" da aula. Em início de instrução, `function` é sempre lido como declaração, e a declaração não aceita `()` depois.
2. **É uma *named function expression*.** `[external]` O nome próprio de `var sum3 = function nome() {}` só existe dentro do corpo da função. Serve para recursão e para o stack trace. Verificado: de fora, `ReferenceError: addition is not defined` (com o nome reconstruído). É o motivo pelo qual a regra de [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]] (`var funcShow = function funcShow`) não cria um segundo nome global.
3. **A anônima ganha nome.** `[external]` Desde o ES2015, `obj.prop = function () {}` e `var f = function () {}` inferem `name` (`obj.prop.name` é `'prop'`, verificado). Continuam sem nome a IIFE e o callback.
4. **Parênteses não são a única forma.** `[external]` Qualquer operador que force contexto de expressão serve: `!function () {}()`, `void function () {}()`, `+function () {}()`. Também `(() => {})()` com arrow function. O Crockford preferia a chamada dentro dos parênteses, `(function () {}())`. Os dois estilos são equivalentes, como diz a aula.
5. **A armadilha do ponto e vírgula.** `[external]` Uma IIFE logo depois de uma linha sem `;` vira chamada da linha anterior: `var a = 1` seguido de `(function () {...})()` dá `TypeError: 1 is not a function` (verificado). Daí o `;(function () {})()` de projetos sem ponto e vírgula. A regra do curso de "ponto e vírgula sempre" ([[wiki/sources/javascript-ninja-funcoes]]) evita o problema.
6. **A IIFE é a solução da era ES5.** `[external]` Ela era a forma de criar escopo sem função nomeada: módulos de bibliotecas (o *module pattern*, que devolve um objeto com o que é público) e o `(function ($) {...})(jQuery)`. Hoje, módulos ES têm escopo próprio por arquivo, e `let`/`const` dentro de `{ }` criam escopo de bloco. A IIFE continua útil para `await` no topo em scripts que não são módulo (`(async () => {...})()`) e no código que bundlers geram. Ver [[wiki/concepts/closure-javascript]] e [[wiki/concepts/encapsulamento]].
7. **30 arquivos no mesmo global.** `[external]` Vale para `<script>` clássicos no navegador, que dividem um único objeto global (`window`). Arquivos do Node (CommonJS) e módulos ES não compartilham o topo; cada um tem o seu escopo ([[wiki/concepts/poluicao-do-escopo-global]]).
8. **"Expressão é como criar um valor"**: certo. `[external]` Expressão é o que produz valor e pode ficar onde se espera um valor ([[wiki/concepts/expressao-javascript]]). A declaração de função é instrução, por isso não aceita `()` em seguida.
9. **Legenda.** Trocas principais: "na índia"→Ninja, "decidiu"→Daciuk, "Rui"/"Ruiz"→hoisting, "aço e afins"→as IIFEs, "eficiente"→IIFE, "mídia que levou o que ele chama de paixão"→*Immediately-Invoked Function Expression*, "são dois"/"SAMU 2"/"ação 2"→sum2, "são três"/"ação de 3"→sum3, "tático"→sintático, "parentes"/"paredes"→parênteses, "ideia"/"lei"/"beleza"→IIFE. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/iife]]
- [[wiki/concepts/expressao-javascript]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/funcoes-de-primeira-classe]]
- [[wiki/concepts/escopo-javascript]]
- [[wiki/concepts/poluicao-do-escopo-global]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/hoisting-javascript]]
- [[wiki/concepts/closure-javascript]]
- [[wiki/concepts/encapsulamento]]

## Open Questions

- **O nome interno de `sum3`.** "Roda de samba", "a diversão", "essa audição", "chamar a atenção", "a versão", "da sala entrei" se referem ao mesmo nome. Talvez `addition`/`adicao` (baixa). Ficaram literais.
- **"Uma propriedade chamada própria"** e **"objeto próprio"**: talvez `prop` e `objeto.prop` (média). Literais.
- **"Fantochada", "uma fase no chão", "uma foto"**: provavelmente "função" ou *function*; literais, como em vídeos anteriores.
- **"Mandam um que"**: talvez "mandar um cat", para mostrar o arquivo; literal.
- **"Pode abrir mais falar"**: talvez "abrir uma issue"; literal.
- **"Lembra kit de conversão de escopo global, uma vez que ele puxa algo ruim"**: provavelmente "lembra que a gente conversou de escopo global, que ele é algo ruim" ([[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]]).
- **"Comentário do mundo do exercício"**: talvez "o enunciado do exercício"; literal.
- O vídeo não anuncia o próximo assunto. Na wiki, o seguinte é [[wiki/sources/javascript-ninja-wrapper-objects]] (semana 10, vídeo 01).

## Raw quotes

- "para você executar uma função, você precisa de um nome para chamar ela"
- "ela precisa ser, ou se tornar, uma expressão"
- "quanto menor for o teu escopo, melhor para você"
