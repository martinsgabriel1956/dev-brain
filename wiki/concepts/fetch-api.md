---
type: concept
title: "Fetch API"
aliases: ["fetch", "fetch()", "window.fetch"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 9
tags: [frontend, javascript, fetch-api, http, promise, json]
skill: tech-mentor-frontend
status: stub
---

# Fetch API

Função nativa do navegador (e do Node.js 18+) para fazer requisições HTTP. `fetch(url, opções)` devolve uma [[wiki/concepts/promise-javascript|promise]] que resolve num `Response`; o corpo é lido por outra promise (`res.json()`, `res.text()`). Ver [[wiki/concepts/requisicao-http]] e [[wiki/concepts/json]].

## Na NLW #1

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] busca os estados na API do [[wiki/entities/ibge]]: "eu prometo pra você que eu vou nesse site, mas eu vou voltar [...] posso voltar com dado, ou posso voltar sem nada". O padrão da aula é `fetch(url).then(res => res.json()).then(states => {...})`, dois `then` porque `res.json()` "também é uma promessa". O `catch` é citado e deixado para depois: a aula segue "o fluxo do caminho que dá certo".

## Precisões

- `fetch` só rejeita em falha de rede; um 404 ou 500 resolve normalmente, e é preciso checar `res.ok` `[external]` (https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).
- `[skill: tech-mentor-frontend]` `AbortSignal.timeout(ms)` cancela requisições lentas sem `setTimeout` manual; retry com backoff exponencial dá resiliência; `AbortController` cancela ao desmontar um componente.
- `async`/`await` escreve o mesmo encadeamento de forma linear: `const res = await fetch(url); const data = await res.json();`.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]], Diego diz que o navegador só faz GET. O `fetch` (e o axios, que o front-end costuma usar) faz POST, PUT e DELETE.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], Diego escolhe o Axios em vez do `fetch` pela `baseURL` compartilhada; o `fetch` com um wrapper faria o mesmo.

Em [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]], o `JSON.parse` é feito à mão sobre uma string colada. Com `fetch`, `response.json()` faz o mesmo parse sobre o corpo e devolve uma [[wiki/concepts/promise-javascript|Promise]]: é aí que entra o "JavaScript assíncrono" que a aula anuncia.

Em [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]], o Fetch é um dos exemplos de JavaScript assíncrono anunciados para as próximas aulas, junto com AJAX e Axios ([[wiki/concepts/javascript-assincrono]]).

Em [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]], a requisição é feita com `XMLHttpRequest`, `readyState` e `JSON.parse(responseText)`. O mesmo GET com fetch é `fetch(url).then(r => r.json())`, com Promise e sem estados ([[wiki/concepts/xmlhttprequest]]).

Em [[wiki/sources/frontpush-promises-resolve-reject-then-catch]], a Promise é criada à mão em volta do XHR. O `fetch` já devolve uma Promise, mas o seu `then` recebe um `Response` (o JSON vem de `response.json()`); no exemplo da aula, `response` já é o objeto.

Em [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]], o Axios é vendido como "mais enxuto" que o XHR à mão. O fetch nativo também cabe em uma linha; o que o Axios acrescenta é rejeitar em 4xx/5xx, o JSON automático, os interceptors e a `baseURL`.

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: estados e municípios do IBGE com fetch + then
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: "chamada AJAX [...] desde a época do jQuery"; o termo AJAX (2005) é anterior ao jQuery (2006)
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: o navegador faz outros métodos via fetch
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: Axios x fetch: baseURL
- [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]]: FrontPUSH, JavaScript aula 11: parse manual antes do response.json()
- [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]]: FrontPUSH, JavaScript aula 12: Fetch anunciado
- [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]]: FrontPUSH, JavaScript aula 14: XHR, o antecessor do fetch
- [[wiki/sources/frontpush-promises-resolve-reject-then-catch]]: FrontPUSH, JavaScript aula 15: Promise manual × fetch
- [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]]: FrontPUSH, JavaScript aula 16: Axios × fetch
