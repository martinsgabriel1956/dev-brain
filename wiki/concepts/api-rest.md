---
type: concept
title: "API REST (RESTful)"
aliases: ["REST", "RESTful", "API RESTful", "REST API"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 7
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

## No JStack, aula 02

Em [[wiki/sources/jstack-http-e-apis-rest]], [[wiki/entities/mateus-silva|Mateus Silva]] define REST como "um padrão para construção de APIs que utiliza o protocolo HTTP" cuja "grande sacada" é retornar "uma representação do estado": JSON no lugar do HTML montado, para web e React Native. Recursos no plural (`GET /products`, `GET /products/10`, `POST`, `PUT`, `DELETE`).

**Correção:** REST é estilo arquitetural de [[wiki/entities/roy-fielding|Roy Fielding]], não amarrado a HTTP nem a JSON. O HTML também é representação, e o hipertexto (HATEOAS) é central na tese. O mesmo recurso pode servir HTML ou JSON por [[wiki/concepts/content-negotiation]]. Plural é convenção `[skill: tech-mentor-backend]`.

## Na NLW #2, dia 2 (Diego Fernandes)

"Full MVC" (HTML pronto do servidor) contra API REST (só dados em JSON), porque "o único dispositivo na Terra capaz de entender HTML é o navegador" e o mesmo back-end serve web e mobile. A comparação é de quem renderiza; REST em si é o estilo de Fielding, não o formato JSON. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## Primeira rota no JStack (aula 05)

Em [[wiki/sources/jstack-criando-a-primeira-rota-da-api]], a regra vira código: GET em `/users`, sem ID, é listagem, e a resposta é JSON (`application/json`). Ver [[wiki/concepts/roteamento-http]].

Em [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]], a troca entre front e back é "por meio de uma API e [...] de arquivos de linguagem unificada", o JSON. A aula ainda não define API; isso fica para a seguinte, com requisição HTTP.

Em [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]], a API é o meio da requisição front → back, acessada "via URL" e devolvendo JSON, com os métodos ligados ao CRUD (POST cria, PUT atualiza). A aula diz que a API "reflete o banco de dados"; `[skill: tech-mentor-backend]` o recurso REST não precisa espelhar tabela. Ver [[wiki/concepts/api]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: MVC com template engine x API REST com JSON; um back-end para web e mobile
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: rotas semânticas: método + recurso
- [[wiki/sources/jstack-http-e-apis-rest]]: HTML × JSON como "representação do estado"; plural; REST como "padrão HTTP" (corrigido)
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: Full MVC × API REST
- [[wiki/sources/jstack-criando-a-primeira-rota-da-api]]: GET /users como listagem em JSON
- [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]]: FrontPUSH, JavaScript aula 11: API + JSON entre front e back
- [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]]: FrontPUSH, JavaScript aula 13: API via URL, métodos e CRUD
