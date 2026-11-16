---
type: source
title: "JStack, aula 05: criando a primeira rota da API"
aliases: ["JStack aula 05", "primeira rota", "GET /users com Node puro"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [nodejs, http, roteamento, request-method, request-url, get, json, json-stringify, content-type, mocks, dados-em-memoria, status-code, 404, 405, favicon, express, igualdade-estrita, xss, jstack, iniciante, lang-dynamic]
skill: tech-mentor-backend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/jstack-criando-a-primeira-rota-da-api.md"
source_url: ""
author: "Mateus Silva"
date_published: ""
date_ingested: 2026-11-16
---

# JStack, aula 05: criando a primeira rota da API

## TL;DR

Quinta aula (cerca de 5 min) do [[wiki/entities/jstack]], com [[wiki/entities/mateus-silva]]. Cria o primeiro endpoint, `GET /users`, no servidor `http` da [[wiki/sources/jstack-criando-o-servidor-http|aula 04]]. A aula vai em cinco passos:

1. **Ler a request.** `console.log(request.method, request.url)`: pela barra do navegador vem sempre `GET`, e `/` é "o endpoint padrão". O `GET /favicon.ico` é o navegador procurando o ícone da aba e pode ser ignorado.
2. **Rota.** `if (request.url === '/users' && request.method === 'GET')`: pelo REST, GET numa coleção sem ID é uma listagem. Ver [[wiki/concepts/roteamento-http]].
3. **Resposta JSON.** `writeHead(200, { 'Content-Type': 'application/json' })` e `end(JSON.stringify(users))`, porque "dentro do end a gente sempre precisa mandar uma string".
4. **Dados mockados.** `src/mocks/users.js` exporta um array de `{ id, name }` (2 é Rose, 3 é José). "Mocks é um nome que a gente dá para [...] dados fake", na memória e sem banco. Ver [[wiki/concepts/dados-em-memoria-vs-persistencia]].
5. **404.** Sem `else`, rota desconhecida fica "carregando eternamente". O `else` responde `404` em `text/html` com "Cannot GET /asd", "aquele formatinho que o Express usa". Ele cita que existe código para método não permitido (405), mas usa sempre 404 "para facilitar a nossa vida". O `if/else if` vai para um arquivo de rotas na próxima aula.

As correções estão em "Tensões e precisões". `request.url` inclui a query string, então `/users?page=2` cai no 404. Ecoar `request.url` num HTML sem escapar é uma porta para XSS. E `end` aceita Buffer, não só string.

## Key Claims

### Lendo a request

- **Método e URL.** O método "está dentro da variável request [...] no atributo method"; o endpoint "também está dentro de request, mas agora no atributo URL".
- **Navegador.** "Quando a gente acessa o URL direto aqui do navegador, toda vez a requisição vai ser do tipo get e o endpoint barra é o endpoint padrão do HTTP quando a gente não informa nada." Ver [[wiki/concepts/metodos-http]].
- **Favicon.** O `GET /favicon.ico` é "uma requisição que o próprio navegador faz para tentar encontrar esse íconezinho que ele coloca aqui na aba"; fica para o módulo de React.

### GET /users

- **Por que listagem.** "O método HTTP é o get, ou seja, a gente está tentando obter informações e [...] a minha URL é barra users e eu não estou passando nenhuma ID", então "o cliente está esperando uma listagem de usuários". Ver [[wiki/concepts/api-rest]] e [[wiki/concepts/recurso-rest]].
- **Condição.** `request.url === '/users' && request.method === 'GET'`, com "igual igual igual" ([[wiki/concepts/igualdade-javascript]]).
- **Status e tipo.** Continua 200, "porque não tem regra de negócio", mas o Content-Type passa a `application/json`, "como eu já falei lá na aula de REST" ([[wiki/sources/jstack-http-e-apis-rest]]).

### Mocks

- **Sem banco.** "A gente não vai trabalhar com banco de dados, a gente vai trabalhar com informações na memória."
- **`src/mocks/users.js`.** "Mocks é um nome que a gente dá para quando a gente vai trabalhar com dados fake, que realmente não vão ser armazenados." `module.exports = [{ id: 1, name: ... }, { id: 2, name: 'Rose' }, { id: 3, name: 'José' }]`, importado com `const users = require('./mocks/users')`. Ver [[wiki/concepts/modulos-nodejs]].

### JSON.stringify

- **String no `end`.** "Dentro do end a gente sempre precisa mandar uma string", e `JSON.stringify` converte "array e objetos para strings no formato json". Ver [[wiki/concepts/json]].
- **Visualização.** No Chrome aparece formatado por "essa extensão aqui no meu Google Chrome", um visualizador de JSON achado "no primeiro, segundo link" de uma busca.

### 404 e o formato do Express

- **Sem resposta, sem fim.** Numa URL que não existe, "ele vai ficar carregando eternamente", porque "a gente não tá dizendo para o nosso servidor o que ele precisa fazer quando a url não for users, ou quando ela for users, mais o método não for get".
- **404.** O bloco de resposta vai para o `else` com `404`, "porque a gente não encontrou a rota". Ver [[wiki/concepts/http-status-code]].
- **405 citado e descartado.** "A gente tem [...] um status code específico para métodos não permitidos, ou seja, a rota users existe, mas se o usuário estivesse fazendo por exemplo, um post", "mas aqui não é muito relevante".
- **Formato do Express.** `text/html` com `` `Cannot ${request.method} ${request.url}` ``: "Cannot GET /", "Cannot GET /asd". Ver [[wiki/entities/express]].
- **Próximo passo.** Com mais endpoints, "ia ter que ficar fazendo um monte de else if aqui dentro", então as rotas vão para um arquivo separado.

## Tensões e precisões

- **`request.url` inclui a query string.** É o *request target* cru: `/users?page=2` não é igual a `'/users'` e cai no 404, e `/users/` (barra no fim) também. O certo é comparar só o caminho: `new URL(request.url, 'http://localhost').pathname`, com `searchParams` para os query params `[external]` https://nodejs.org/api/http.html#messageurl. Ver [[wiki/concepts/query-string]] e [[wiki/concepts/url]].
- **Ecoar a URL em HTML sem escapar.** `` `Cannot ${request.method} ${request.url}` `` em `text/html` reflete na página o que o cliente mandou. O navegador codifica `<`, `>` e aspas no path pela barra de endereço, mas um link ou cliente qualquer pode mandar o caminho cru. O Express escapa esse texto; aqui, `text/plain` ou escapar resolve. Ver [[wiki/concepts/xss]].
- **405 tem regra.** `POST /users` com a rota existente deveria ser 405 Method Not Allowed, com o header `Allow: GET` dizendo os métodos aceitos; 404 diz "não existe", o que engana o cliente `[external]` https://www.rfc-editor.org/rfc/rfc9110#name-405-method-not-allowed. A simplificação é declarada, mas o motivo vale registro.
- **`end` não exige string.** Aceita string, `Buffer` ou `Uint8Array`. O que não aceita é objeto ou array, daí o `JSON.stringify`.
- **"Carregando eternamente" tem prazo.** Sem `end`, a conexão fica aberta até o timeout: o Node 18+ tem `server.requestTimeout` de 300 s por padrão, e o navegador desiste antes ou depois conforme o caso `[external]` https://nodejs.org/api/http.html#serverrequesttimeout.
- **"Mock" é outro termo em testes.** Em testes, *mock* é um dublê que verifica interações ([[wiki/concepts/test-doubles]]). Dados fake em memória são mais *fixture*, *seed* ou *in-memory data*. O nome da pasta é convenção comum, mas a ambiguidade confunde depois.
- **Visualizador de JSON já vem no Chrome.** Desde a versão 117 o Chrome tem um "pretty-print" nativo para respostas JSON; extensão é opcional.
- **`/` não é "o endpoint padrão do HTTP".** É o navegador que manda `/` quando a URL não tem caminho: no HTTP/1.1 o request target não pode ser vazio, e a forma mínima é `/`.
- **Charset do JSON.** `application/json` não precisa de `charset`: o JSON é UTF-8 por definição (RFC 8259), então "José" chega certo, ao contrário do `text/html` sem charset da aula 04.

## Entities

- [[wiki/entities/jstack]]: o curso
- [[wiki/entities/mateus-silva]]: instrutor
- [[wiki/entities/nodejs]]: `request.method`, `request.url`, `response.end`
- [[wiki/entities/express]]: formato "Cannot GET /"

## Concepts

- [[wiki/concepts/roteamento-http]]: `if` por método + caminho, o embrião do roteador
- [[wiki/concepts/metodos-http]]: GET pela barra do navegador
- [[wiki/concepts/api-rest]]: GET na coleção = listagem
- [[wiki/concepts/recurso-rest]]
- [[wiki/concepts/http-status-code]]: 200, 404, 405
- [[wiki/concepts/json]]: `JSON.stringify` e `application/json`
- [[wiki/concepts/dados-em-memoria-vs-persistencia]]: `mocks/users.js`
- [[wiki/concepts/test-doubles]]: "mock" no sentido de testes
- [[wiki/concepts/query-string]]: `request.url` com query
- [[wiki/concepts/url]]
- [[wiki/concepts/igualdade-javascript]]: `===`
- [[wiki/concepts/xss]]: URL refletida em HTML
- [[wiki/concepts/modulos-nodejs]]: `require('./mocks/users')`

## Open Questions

- O arquivo de rotas da próxima aula vai separar caminho e query com `new URL`, ou continuar comparando `request.url` inteiro?
- Quando aparecer `GET /users/:id`, como o curso vai extrair o ID sem framework?

## Raw quotes

> "Dentro do end a gente sempre precisa mandar uma string."

> "Mocks é um nome que a gente dá para quando a gente vai trabalhar com dados fake."

> "Ia ter que ficar fazendo um monte de else if aqui dentro."
