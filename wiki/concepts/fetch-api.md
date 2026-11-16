---
type: concept
title: "Fetch API"
aliases: ["fetch", "fetch()", "window.fetch"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
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

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: estados e municípios do IBGE com fetch + then
