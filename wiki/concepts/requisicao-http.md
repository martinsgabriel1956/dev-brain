---
type: concept
title: "Requisição HTTP"
aliases: ["http request", "anatomia da requisição", "http request response"]
date_created: 2026-09-30
date_updated: 2026-11-16
source_count: 10
tags: [http, api, protocolo, cliente-servidor]
skill: tech-mentor-networking
status: stub
---

# Requisição HTTP

Mensagem que o cliente envia ao servidor; o servidor responde com outra mensagem ([[wiki/concepts/http-status-code|status]] + headers + body). É uma **conversa**, e bibliotecas (fetch, Axios) e ferramentas (Postman, navegador) são só interfaces para produzi-la.

## Anatomia

| Parte | Papel |
|---|---|
| [[wiki/concepts/metodos-http\|Método]] | Intenção (GET, POST, PUT, DELETE) |
| URL | Qual [[wiki/concepts/recurso-rest\|recurso]] (ex.: `/usuarios/42`) |
| [[wiki/concepts/http-headers\|Headers]] | Metadados sobre a comunicação |
| Body (opcional) | O conteúdo em si (ex.: nome, e-mail, senha num POST) |

Resposta: status, headers (ex.: `Content-Type`) e body. **HTTP ≠ JSON**: JSON é o formato do conteúdo; HTTP é o protocolo.

## Caminho no servidor

rota → [[wiki/concepts/middleware]] → controller → service → banco → resposta. Normalmente protegida por [[wiki/concepts/http-vs-https|HTTPS]].

## Depuração

[[wiki/concepts/debug-de-requisicao-http]]: a aba Network do DevTools mostra URL, método, headers, payload, status e response.

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] apresenta `req` e `res` nas rotas do [[wiki/entities/express]]: "Req é uma requisição. Requisição é um pedido. Res é uma resposta." A resposta vem com `res.send`, `res.sendFile` e `res.render`. "Lembra que tudo é dado, gente."

## No JStack, aula 02

Em [[wiki/sources/jstack-http-e-apis-rest]], a request tem cinco blocos: URL/endpoint (recurso), query params, método (ação), headers (informações adicionais) e body (corpo); a response tem headers, Content-Type, status code e body. A aula chama o status code de "outro header" e diz que só POST e PUT levam body; ver as correções na página da fonte.

Em [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]], a aula promete "API e requisição HTTP" para buscar o JSON "via HTTP" em vez de copiar e colar. No exemplo do e-commerce, o ID vai na URL e o JSON volta no corpo da resposta; no cadastro, vai no corpo do `POST` com `Content-Type: application/json`.

Em [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]], a requisição "via URL por meio do protocolo HTTP" é o exemplo central de tarefa assíncrona: o código segue enquanto a resposta (um JSON) não chega ([[wiki/concepts/javascript-assincrono]]).

Em [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]], "requisição nada mais é do que as informações de padronização que você precisa para poder realizar a comunicação". A requisição é a mensagem (método, URL, cabeçalhos, corpo); o padrão é o protocolo. Exemplo: o GET a `api.github.com/users/<usuário>` ([[wiki/concepts/api]]).

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — anatomia completa do clique até a resposta
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: req/res no Express
- [[wiki/sources/jstack-http-e-apis-rest]]: cinco blocos da request e quatro da response

## Key sources (adição 2026-10-06)

- [[wiki/sources/estado-global-stateless-side-effects-reprodutibilidade-galego]] — HTTP stateless: cada requisição carrega a identificação do usuário; ver [[wiki/concepts/request-context]] e [[wiki/concepts/estado-global-em-servidor]].

## Key sources (adição 2026-10-09)
- [[wiki/sources/url-vs-uri-diferenca-urn-identificacao-localizacao]] — a URL da requisição é uma URI que localiza o recurso; query param seleciona o recurso (ver [[wiki/concepts/url]])

## Na NLW #2, dia 2 (Diego Fernandes)

"Toda mensagem [...] ela tem cabeçalho e corpo": cabeçalho como metadados, corpo como conteúdo. A aula põe no cabeçalho o "tipo da mensagem" (criar, listar), que na verdade é o método da linha de requisição. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## Key sources (adição 2026-11-10)

- [[wiki/sources/polling-sse-websocket-comunicacao-em-tempo-real]] — HTTP como pergunta e resposta: sem gatilho do cliente o servidor não fala, origem do problema de tempo real
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: cabeçalho e corpo; o método fora do header
- [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]]: FrontPUSH, JavaScript aula 11: JSON buscado via HTTP (anunciado)
- [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]]: FrontPUSH, JavaScript aula 12: requisição como exemplo de assíncrono
- [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]]: FrontPUSH, JavaScript aula 13: requisição como "informações de padronização"
