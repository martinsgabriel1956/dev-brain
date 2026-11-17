---
type: concept
title: "Promise (JavaScript)"
aliases: ["promise", "promessa", "then", "catch", "Promise"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 8
tags: [javascript, promise, assincronia, fetch-api, lang-dynamic]
skill: tech-mentor-frontend
status: stub
---

# Promise (JavaScript)

Objeto que representa um valor que ainda vai chegar. Começa pendente (*pending*) e termina resolvida (*fulfilled*) ou rejeitada (*rejected*). `then` registra o que fazer com o valor, `catch` o que fazer com o erro, e cada `then` devolve uma nova promise, o que permite encadear. Ver [[wiki/concepts/fetch-api]].

## Na NLW #1

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] explica como "uma promessa do tipo, cara, ó, eu prometo pra você": o console mostra primeiro "Promise {<pending>}" e depois a resposta. Retornar `res.json()` de dentro do primeiro `then` faz o segundo `then` receber os dados: "já que você retornou uma promessa, eu também sou uma promessa".

## Precisões

- Um erro não tratado numa promise vira *unhandled rejection*; uma cadeia sem `catch` falha em silêncio para o usuário `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).
- `async`/`await` é açúcar sintático sobre promises; `try/catch` substitui o `.catch`.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], `.then` dentro do `useEffect` (que não aceita `async`) e `await api.post` no `handleSubmit`, sem `catch`.

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], `Database.open(...)` devolve uma promessa: "eu vou tentar. Se eu conseguir, então eu vou fazer o restante". O `.then(execute)` vira `await`, e os horários são esperados com `Promise.all`, que a aula descreve como "um por um". Ver [[wiki/concepts/async-await]].

## Na NLW #2, dia 3 (Diego Fernandes)

`api.get(...).then(...)` no `useEffect`, `api.post(...).then(alert).catch(alert)` no cadastro e `await api.get` na busca, sem `catch`. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

Em [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]], o JSON abre a parte de "JavaScript assíncrono" do FrontPUSH, mas `parse` e `stringify` são síncronos; a Promise só aparece quando o JSON vier por `fetch`.

Em [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]], as Promises ("o que são promessas") aparecem na lista de ferramentas do assíncrono, depois do AJAX e do Axios. Na prática Axios e Fetch já devolvem Promises, e `async/await` é sintaxe sobre elas ([[wiki/concepts/javascript-assincrono]]).

## No FrontPUSH, JavaScript aula 15

Em [[wiki/sources/frontpush-promises-resolve-reject-then-catch]], [[wiki/entities/nasser|Násser]] embrulha o XHR da aula 14 em `return new Promise(function (resolve, reject) {...})`: `resolve(JSON.parse(XHR.responseText))` com status 200, `reject` no resto. `console.log(result)` mostra `Promise {<pending>}`, e o `then`/`catch` é "uma cascata de possibilidades": o `resolve` levanta "uma bandeirinha verde" que "aciona o then". Precisões: o executor roda na hora (só a rede fica no fundo); o log nunca mostraria o valor, só `<fulfilled>`; a cascata de verdade é o encadeamento de `then`s; rejeitar com `Error`.

Em [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]], a Promise feita à mão some: "vou literalmente apagar a promise", porque `axios.get` já devolve uma. O `.then` vai direto na chamada.

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: promessa pendente, then encadeado, catch citado
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: then no useEffect, await no submit sem catch
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: promessa do banco, then e Promise.all
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: then/catch × await no front
- [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]]: FrontPUSH, JavaScript aula 11: JSON como porta de entrada do assíncrono
- [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]]: FrontPUSH, JavaScript aula 12: Promises anunciadas
- [[wiki/sources/frontpush-promises-resolve-reject-then-catch]]: FrontPUSH, JavaScript aula 15: new Promise com XHR, pending, then/catch
- [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]]: FrontPUSH, JavaScript aula 16: Promise pronta do Axios
