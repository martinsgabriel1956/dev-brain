---
type: concept
title: "Debug de Requisição HTTP"
aliases: ["debugar api", "devtools network", "debug http"]
date_created: 2026-09-30
date_updated: 2026-11-16
source_count: 4
tags: [debugging, http, devtools, api]
skill: tech-mentor-networking
status: stub
---

# Debug de Requisição HTTP

Em vez de "deu erro, tento de novo" ou copiar a mensagem para um LLM, **conferir as peças da conversa uma a uma** na aba *Network* do DevTools: URL, método, headers, payload, status code, response — comparando o que saiu com o que o servidor esperava.

Checklist (da fonte):
1. Qual método e qual recurso?
2. `Authorization` presente, com o nome certo e formato `Bearer <token>` (espaço!)? Token ainda válido? ([[wiki/concepts/http-headers]], [[wiki/concepts/jwt]])
3. Tem body / `Content-Type` correto?
4. Qual status voltou e o que o servidor quis dizer? ([[wiki/concepts/http-status-code]])
5. Foi barrada em [[wiki/concepts/middleware]] antes do controller?
6. Erro de [[wiki/concepts/cors]]? Então ajustar a origem permitida no servidor.

Ver método geral em [[wiki/concepts/debugging]] e [[wiki/concepts/requisicao-http]].

Em [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]], a aba Network com o filtro XHR (hoje "Fetch/XHR") mostra que a requisição sai depois da página e expõe Status Code, Request Method e Request URL. A resposta fica na aba Response; o status não está no JSON.

Em [[wiki/sources/frontpush-promises-resolve-reject-then-catch]], a aba Network mostra status 200, Preview, Response e Timing ("foram 340 milissegundos"). Para testar o erro, ele quebra a URL de propósito e confere a mensagem do `catch`.

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — exemplos 401 e CORS

## Key sources (adição 2026-10-09)
- [[wiki/sources/url-vs-uri-diferenca-urn-identificacao-localizacao]] — vocabulário: o que o DevTools chama de URL é URI + localização
- [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]]: FrontPUSH, JavaScript aula 14: aba Network com filtro XHR
- [[wiki/sources/frontpush-promises-resolve-reject-then-catch]]: FrontPUSH, JavaScript aula 15: Timing e caminho de erro de propósito
