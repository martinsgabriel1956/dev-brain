---
type: concept
title: "async/await (JavaScript)"
aliases: ["async await", "await", "async function", "Promise.all", "função assíncrona"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 7
tags: [javascript, assincronia, promise, async-await, promise-all, nodejs, lang-dynamic]
skill: tech-mentor-data
status: stub
---

# async/await (JavaScript)

`async` e `await` são uma forma de escrever código com [[wiki/concepts/promise-javascript|promises]] como se fosse sequencial. Uma função `async` sempre devolve uma promise. Dentro dela, `await p` pausa só aquela função até `p` resolver, devolve o valor ou lança o erro, que um `try/catch` captura. O resto do programa continua rodando enquanto isso: o `await` não trava o processo, só a função. Ver [[wiki/concepts/callback-javascript]] para o estilo anterior e [[wiki/concepts/error-handling-estruturado]].

`[skill: lang-dynamic]` Três pontos que costumam confundir:

- **A promise começa quando é criada.** Chamar `db.run(...)` já dispara a operação; o `await` só espera o resultado. Guardar a promise num array não a "deixa para depois".
- **`Promise.all([...])`** espera várias promises ao mesmo tempo e rejeita na primeira que falhar, sem cancelar as outras. Ela não executa nada "um por um". Para ordem garantida, use `for (const x of lista) { await f(x) }`. Quando todas precisam terminar mesmo com falhas, use `Promise.allSettled` `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all).
- **`await` fora de função `async`** só funciona no topo de um módulo ES. Em CommonJS (`require`), como no Node das NLWs, ele precisa de uma função `async` em volta `[external]` (https://nodejs.org/api/esm.html#top-level-await).

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], [[wiki/entities/mayk-brito|Mayk]] chega ao `await` pelo incômodo do `then` dentro de `then`: "a palavra do momento chama-se espera". O `createProffy` é `async` e faz `await db.run(...)` três vezes, usando o `lastID` de cada inserção na próxima. "Não consigo [usar o await] se essa função não tiver na frente dela uma palavra chamada async." Os horários viram um array de `db.run` sem `await` ("eu quero guardar ele no array para executar depois"), esperado com `await Promise.all(...)`, que "vai um por um". As duas explicações estão erradas: os `db.run` disparam no `map`, e quem enfileira as escritas é o SQLite. Também faltou uma transação, e uma falha nos horários deixa professor e aula gravados.

## Na NLW #2, dia 2 (Diego Fernandes)

Handlers `async` e `await` em cada operação do Knex, "a famosa promise". Sem `try/catch`, a rejeição não chega ao middleware de erro do Express 4. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## Na NLW #2, dia 3 (Diego Fernandes)

`async function searchTeachers` com `await api.get('classes', { params })`; sem `try/catch`, o 400 por filtro ausente vira rejeição não tratada. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

Em [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]], async/await entra no roteiro do módulo de JavaScript do FrontPUSH como novidade do ES6+ e base da comunicação do front-end com o back-end. `[external]` Chegou no ES2017 (ES8), dois anos depois das promises ([[wiki/concepts/ecmascript]]).

## No JStack, aula 03

[[wiki/sources/jstack-o-que-sao-modulos]] ensina módulos CommonJS, onde não há top-level `await`. Ver [[wiki/concepts/modulos-nodejs]].

Em [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]], `async`/`await` fecha a lista de ferramentas do JavaScript assíncrono do FrontPUSH. O exemplo da aula (requisição → JSON → objeto → cadastro) é uma cadeia dependente, o caso de `await` em sequência ([[wiki/concepts/javascript-assincrono]]).

Em [[wiki/sources/frontpush-promises-resolve-reject-then-catch]], a Promise é consumida com `then`/`catch`. Com `async/await` seria `const user = await minhaPromise()` dentro de `try/catch`.

## Key sources

- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: await no createProffy, async obrigatório, Promise.all explicado como sequencial
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: await no Knex e Express 4
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: busca de professores sem catch
- [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]: FrontPUSH, JavaScript aula 01: async/await no roteiro, ES2017
- [[wiki/sources/jstack-o-que-sao-modulos]]: módulos CJS, sem top-level await
- [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]]: FrontPUSH, JavaScript aula 12: async/await anunciado; exemplo de cadeia dependente
- [[wiki/sources/frontpush-promises-resolve-reject-then-catch]]: FrontPUSH, JavaScript aula 15: then/catch, equivalente com await
