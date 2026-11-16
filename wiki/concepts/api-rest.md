---
type: concept
title: "API REST (RESTful)"
aliases: ["REST", "RESTful", "API RESTful", "REST API"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [api, rest, http, json, backend, arquitetura]
skill: lang-dynamic
status: stub
---

# API REST (RESTful)

Estilo de arquitetura para APIs sobre HTTP, descrito por Roy Fielding em 2000. Seus pilares são recursos identificados por URL, interface uniforme ([[wiki/concepts/metodos-http|métodos HTTP]] e [[wiki/concepts/http-status-code|status]]), comunicação sem estado entre requisições e respostas que podem ser guardadas em cache `[external]` (https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm). Uma API que segue esses princípios é chamada de RESTful. Ver [[wiki/concepts/recurso-rest]].

## Dados em vez de HTML

Na aula de [[wiki/entities/diego-fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]), o contraste é com o "MVC" em que a View é um [[wiki/concepts/template-engine]]. Nesse modelo, a rota `/users` devolve o HTML pronto da listagem. Na API REST, a mesma rota devolve só os dados, em [[wiki/concepts/json]], e cada cliente monta a própria tela: React na web, React Native no celular, ou até "uma API pública".

O ganho que a aula destaca é ter um back-end para vários clientes, porque "o React Native ele não lê HTML". Ver [[wiki/concepts/arquitetura-cliente-servidor]] e [[wiki/concepts/renderizacao-ssr-vs-csr]].

## Precisões

- **REST não é o oposto de MVC.** A API pode continuar com models e controllers; a "view" passa a ser a serialização em JSON.
- **JSON é convenção, não regra.** REST não fixa formato, e JSON é só o mais comum.
- **Muita API "REST" é só HTTP + JSON.** Raramente se segue o modelo à risca, com links entre recursos (HATEOAS).

Relacionado: [[wiki/concepts/contrato-de-api]], [[wiki/concepts/api-versioning]], [[wiki/concepts/requisicao-http]].

No dia 2 ([[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]), Diego dá a regra prática: as rotas são "muito semânticas". O método diz a ação e o caminho diz o recurso: `GET /users` lista, `POST /users` cria, `GET /users/5` busca um.

## Na NLW #2, dia 2 (Diego Fernandes)

"Full MVC" (HTML pronto do servidor) contra API REST (só dados em JSON), porque "o único dispositivo na Terra capaz de entender HTML é o navegador" e o mesmo back-end serve web e mobile. A comparação é de quem renderiza; REST em si é o estilo de Fielding, não o formato JSON. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: MVC com template engine x API REST com JSON; um back-end para web e mobile
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: rotas semânticas: método + recurso
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: Full MVC × API REST
