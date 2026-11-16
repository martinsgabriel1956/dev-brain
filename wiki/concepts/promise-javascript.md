---
type: concept
title: "Promise (JavaScript)"
aliases: ["promise", "promessa", "then", "catch", "Promise"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
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

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: promessa pendente, then encadeado, catch citado
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: then no useEffect, await no submit sem catch
