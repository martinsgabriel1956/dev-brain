---
type: concept
title: "Roteamento HTTP (servidor)"
aliases: ["roteamento", "router", "rotas da API", "server-side routing", "route matching"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [http, api, roteamento, backend, nodejs, express, tech-mentor-backend]
skill: tech-mentor-backend
status: stub
---

# Roteamento HTTP (servidor)

Decidir qual código atende uma requisição a partir do **método** e do **caminho** (`GET /users` → listar; `GET /users/:id` → buscar um). Não confundir com o roteamento no navegador de uma SPA ([[wiki/concepts/client-side-routing]]).

## Da condicional ao roteador

1. **`if` por método + caminho.** Funciona para uma ou duas rotas e vira cadeia de `else if` depois.
2. **Tabela de rotas.** Um array ou mapa `{ method, path, handler }` percorrido a cada requisição.
3. **Parâmetros de caminho.** `/users/:id` exige casar padrões (regex, `URLPattern` ou árvore de prefixos) e entregar `params.id` ao handler.
4. **Roteador de framework.** [[wiki/entities/express]], Fastify e Hono fazem os passos acima mais middlewares, e alguns usam árvores (radix) para casar rotas sem percorrer a lista.

## Regras que um roteador acerta

- **Comparar o *pathname*, não a URL crua.** No Node, `request.url` traz a query string (`/users?page=2`); use `new URL(request.url, 'http://localhost')` e compare `pathname` ([[wiki/concepts/query-string]]).
- **Decidir sobre a barra final** (`/users` × `/users/`): normalizar ou redirecionar.
- **404 × 405.** Caminho inexistente = 404. Caminho existente com método errado = 405 Method Not Allowed com `Allow: GET, POST` `[external]` https://www.rfc-editor.org/rfc/rfc9110#name-405-method-not-allowed. Ver [[wiki/concepts/http-status-code]].
- **Sempre responder.** Toda requisição precisa terminar em resposta (inclusive a de fallback), senão a conexão fica pendurada até o timeout.

## No JStack (aula 05)

Em [[wiki/sources/jstack-criando-a-primeira-rota-da-api]], [[wiki/entities/mateus-silva]] faz o passo 1: `if (request.url === '/users' && request.method === 'GET')` responde a lista em JSON, e o `else` responde 404 "Cannot GET /asd", no formato do Express. Ele cita o 405 e opta pelo 404, e anuncia que a cadeia de `else if` vai para um arquivo de rotas na aula seguinte. A comparação com `request.url` inteiro quebra com query string.

## Aula 06: tabela de rotas

Em [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]], o passo 2: `src/routes.js` exporta `[{ endpoint, method, handler }]`, e o `index.js` faz `routes.find(r => r.endpoint === request.url && r.method === request.method)` e chama `route.handler(request, response)`, com 404 se não achar. Rota nova é mais um objeto no array. Ainda faltam parâmetros de caminho (`/users/:id`), pathname sem query e 405.

## Key sources

- [[wiki/sources/jstack-criando-a-primeira-rota-da-api]]: if por método + URL, 404 de fallback, 405 citado
- [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: tabela de rotas com find e handler
