---
type: concept
title: "Callback (JavaScript)"
aliases: ["callback", "função de callback", "callback hell", "error-first callback"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 14
tags: [javascript, nodejs, assincrono, funcoes, lang-dynamic]
skill: lang-dynamic
status: stub
---

# Callback (JavaScript)

Uma função passada como argumento para outra, que a chama depois, quando a operação termina. No Node, o padrão clássico é o *error-first*: `(err, resultado) => { if (err) ... }`.

O event loop executa o callback quando a operação de I/O termina, e o resto do programa não espera. Ver [[wiki/concepts/event-loop-performance-js]].

Callbacks aninhados viram o *callback hell*. [[wiki/concepts/promise-javascript|Promises]] e `async/await` resolvem a mesma necessidade com fluxo linear. Ver [[wiki/concepts/funcoes-javascript]].

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] explica com o pacote `sqlite3`: o callback é "chame de volta", e tem duas características:
- é "uma função passada como parâmetro";
- é chamada "depois de um certo tempo", porque "a sua aplicação não pode ficar travada 10 segundos esperando isso cadastrar no banco de dados".

**Analogia:** você pede uma cor ao vendedor e continua olhando roupas até ele voltar do depósito.

O que ele mostra no código:
- **Passagem por referência:** passa `afterInsertData` sem `()`, porque "se eu coloco assim [com parênteses], eu já estou imediatamente executando ela".
- **Erro:** trata o `err` com `return console.log(err)`.
- **Escopo:** o `res.render` vai para dentro do callback, porque `rows` só existe ali.
- **`this`:** dentro do callback, `this` é o `Statement`, com `lastID`. Por isso ele usa `function` e não arrow function, que não tem `this` próprio.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: `onClick={() => handleSelectItem(item.id)}`, porque passar `handleSelectItem(item.id)` "está executando a função, ele não está passando a função como referência".

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]], o `filename` do Multer recebe `callback(error, filename)`, o padrão error-first, com `null` quando não há erro.

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], o `then(execute)` recebe a função pelo nome, sem executá-la, e a chama quando o banco termina de abrir. Encadear `then` dentro de `then` vira "uma bagunça", e por isso a aula passa a [[wiki/concepts/async-await]]. A NLW #1 fazia o mesmo com callbacks do `sqlite3`.

## No JStack, aula 01

Em [[wiki/sources/jstack-como-funciona-o-nodejs]], callback é "ligue de volta": "depois que isso aqui terminar de executar, você me liga de volta e me passa esses dados". O slide usa o padrão error-first `function callback(err, data)`. O callback espera na *callback queue* até o [[wiki/concepts/event-loop-performance-js|event loop]] achar a call stack vazia.

## No JStack, aula 04

Em [[wiki/sources/jstack-criando-o-servidor-http]], dois callbacks: o do `createServer`, chamado a cada requisição com `(request, response)`, e o do `listen`, chamado uma vez quando o servidor está de pé.

Em [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]], as arrow functions são apresentadas como a sintaxe que os frameworks usam o tempo todo; o uso típico delas é justamente como callback ([[wiki/concepts/arrow-functions]]).

Em [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]], callback é "uma função genérica que você simplesmente pode colocar o que você quiser", passada como segundo argumento do `addEventListener` e como argumento do `forEach` e do `map`. O resumo da aula diz que o `forEach` "devolve uma função de callback"; ele recebe uma e devolve `undefined`.

## No JStack, aula 06

Em [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]], `handler: UserController.listUsers` guarda a função sem chamá-la ("eu não estou executando a função [...] só estou passando a referência"); o `index.js` a chama depois com `route.handler(request, response)`. Com métodos de classe, a referência solta perde o `this`.

Em [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]], a "boa prática" é declarar o callback à parte e passar só o nome: "deixar o nome da função como referência e aí quando clica, ele busca o nome da função". Isso também permite `removeEventListener` com a mesma referência.

Em [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]], a lista de ferramentas do assíncrono (AJAX, Axios, Promises, Fetch, async/await) deixa de fora o callback, que é o mecanismo mais antigo e que o curso já usou em `addEventListener` e `forEach` ([[wiki/concepts/javascript-assincrono]]).

Em [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]], `XHR.onreadystatechange = function () {...}` é um callback de evento: "verificar quando o estado mudar, e aí eu vou lá e disparo uma função" ([[wiki/concepts/xmlhttprequest]]).

Em [[wiki/sources/frontpush-promises-resolve-reject-then-catch]], `resolve` e `reject` "parecem uma variável, mas também [são] uma função": são callbacks que o `Promise` cria e passa ao executor. A aula os descreve como "uma função que declara outra função", mas eles só são chamados, não declarados pelo usuário.

Em [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]], "o event passa aqui automático, porque é uma função de callback": por isso dá para desestruturá-lo direto no parâmetro do handler.

## Key sources

- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: callbacks do sqlite3 (run/all), error-first, referência x execução, `this` x arrow
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: referência x execução no onClick do React
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: callback error-first do Multer
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: then com função nomeada, rumo ao await
- [[wiki/sources/jstack-como-funciona-o-nodejs]]: "ligue de volta"; callback queue e event loop
- [[wiki/sources/jstack-criando-o-servidor-http]]: callbacks do createServer e do listen
- [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]]: FrontPUSH, JavaScript aula 04: arrow functions como sintaxe de callback
- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: callback no addEventListener, forEach e map
- [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: handler guardado como referência
- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: callback nomeado por referência
- [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]]: FrontPUSH, JavaScript aula 12: o callback fora da lista do assíncrono
- [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]]: FrontPUSH, JavaScript aula 14: onreadystatechange como callback
- [[wiki/sources/frontpush-promises-resolve-reject-then-catch]]: FrontPUSH, JavaScript aula 15: resolve/reject como callbacks prontos
- [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]]: FrontPUSH, JavaScript aula 18: o event chega no callback
