---
type: concept
title: "Callback (JavaScript)"
aliases: ["callback", "função de callback", "callback hell", "error-first callback"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 4
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

## Key sources

- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: callbacks do sqlite3 (run/all), error-first, referência x execução, `this` x arrow
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: referência x execução no onClick do React
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: callback error-first do Multer
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: then com função nomeada, rumo ao await
