---
type: concept
title: "XMLHttpRequest (XHR)"
aliases: ["XHR", "XMLHttpRequest", "readyState", "onreadystatechange", "responseText"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [javascript, web-api, xhr, ajax, http, assincrono, readystate, lang-dynamic]
skill: lang-dynamic
status: stub
---

# XMLHttpRequest (XHR)

A Web API original do navegador para fazer requisições HTTP por script, base do [[wiki/concepts/ajax|AJAX]]. Apesar do nome, trafega qualquer formato (hoje quase sempre [[wiki/concepts/json]]). Foi substituída na prática pela [[wiki/concepts/fetch-api|Fetch API]], mas continua por baixo de bibliotecas como o [[wiki/entities/axios|Axios]] no navegador.

`[external]` (MDN, especificação XHR do WHATWG), sem referência na skill lang-dynamic.

## Uso básico

```javascript
const xhr = new XMLHttpRequest()
xhr.open("GET", "https://api.github.com/users/octocat") // 3º parâmetro async = true por padrão
xhr.onload = function () {
  if (xhr.status >= 200 && xhr.status < 300) {
    console.log(JSON.parse(xhr.responseText))
  }
}
xhr.onerror = function () {
  console.log("falha de rede")
}
xhr.send() // o argumento é o corpo (null/vazio num GET)
```

## readyState

| Valor | Constante | Significado |
|---|---|---|
| 0 | `UNSENT` | criado, `open` ainda não chamado |
| 1 | `OPENED` | `open` chamado |
| 2 | `HEADERS_RECEIVED` | cabeçalhos e status recebidos |
| 3 | `LOADING` | corpo chegando |
| 4 | `DONE` | terminou, **com sucesso ou não** |

`onreadystatechange` dispara a cada mudança. `readyState === 4` não basta: é preciso conferir `status` ([[wiki/concepts/http-status-code]]); falha de rede dá `status` 0. `onload`, `onerror` e `responseType = "json"` simplificam.

## Pontos de atenção

- XHR síncrono (`async = false`) bloqueia a página e está obsoleto na thread principal ([[wiki/concepts/javascript-assincrono]]).
- O handler é um [[wiki/concepts/callback-javascript|callback]] de evento: roda quando o [[wiki/concepts/event-loop-performance-js|event loop]] entrega a resposta.
- Requisições para outra origem seguem as regras de [[wiki/concepts/cors]].
- No DevTools, a aba Network filtra por "Fetch/XHR" ([[wiki/concepts/debug-de-requisicao-http]]).

## No FrontPUSH, JavaScript aula 14

Em [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]], [[wiki/entities/nasser|Násser]] instancia `new XMLHttpRequest()` (a primeira "classe" do curso), faz `open('GET', <API do GitHub>)` e `send(null)`, e no `onreadystatechange` testa `readyState` 4 ("quando der certo") antes de `JSON.parse(XHR.responseText)`. Falta conferir o `status`.

Em [[wiki/sources/frontpush-promises-resolve-reject-then-catch]], o mesmo XHR vai para dentro de uma Promise e ganha o teste que faltava: dentro do `readyState == 4`, `if (XHR.status == 200)` resolve, senão rejeita. "O estado de pronto não significa que deu certo." Embrulhar uma API de callback numa Promise é *promisificar*.

Em [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]], o Axios é "um encapsulamento do XML HTTP request": no navegador ele usa XHR por baixo (`response.request` é o XHR), e no Node o módulo `http`.

## Key sources

- [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]]: FrontPUSH, JavaScript aula 14: XHR com open, send, readyState e responseText
- [[wiki/sources/frontpush-promises-resolve-reject-then-catch]]: FrontPUSH, JavaScript aula 15: XHR promisificado, com status 200
- [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]]: FrontPUSH, JavaScript aula 16: Axios como embrulho do XHR
