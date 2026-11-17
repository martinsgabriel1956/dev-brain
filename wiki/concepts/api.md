---
type: concept
title: "API (Application Programming Interface)"
aliases: ["API", "Application Programming Interface", "interface de programação", "API web", "API pública"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [api, interface, contrato, api-web, http, backend, frontend]
skill: tech-mentor-backend
status: stub
---

# API (Application Programming Interface)

Uma **interface de programação**: o conjunto de operações que um software expõe para outro usar, com regras de entrada e saída, sem mostrar como funciona por dentro. É um [[wiki/concepts/contrato-de-api|contrato]].

## Tipos

- **API de linguagem ou biblioteca:** métodos de `String`, `Array`, `JSON` em JavaScript; a biblioteca padrão de qualquer linguagem.
- **API do ambiente:** o [[wiki/concepts/dom]] e as Web APIs do navegador (`fetch`, `localStorage`, [[wiki/concepts/geolocation-api]]); as APIs do sistema operacional ([[wiki/concepts/windows-api]]).
- **API web (remota):** operações expostas por um servidor pela rede, quase sempre sobre HTTP ([[wiki/concepts/requisicao-http]], [[wiki/concepts/metodos-http]]) com corpo em [[wiki/concepts/json]]. Os estilos mais comuns são [[wiki/concepts/api-rest]], GraphQL e gRPC.

## API web: o essencial

- **Endpoint** = método + URL (`GET https://api.github.com/users/octocat`).
- **Acesso:** público (aberto, às vezes com [[wiki/concepts/api-key]] gratuita) ou autenticado e autorizado ([[wiki/concepts/autenticacao-e-autorizacao]]). Costuma ter limite de taxa ([[wiki/concepts/github-search-api-limites]]).
- **No navegador**, uma API de outra origem só pode ser lida se o servidor liberar com [[wiki/concepts/cors]].
- **Desenho:** `[skill: tech-mentor-backend]` expõe recursos e casos de uso, não o schema do banco; versiona ([[wiki/concepts/api-versioning]]) e documenta ([[wiki/concepts/documentacao-api-swagger]]).

## No FrontPUSH, JavaScript aula 13

Em [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]], [[wiki/entities/nasser|Násser]] define a API como o meio da requisição entre front e back ("como eu vou me comunicar? Ah, eu vou construir uma API"), acessada "via URL", pública ou com autenticação, e mostra a API do [[wiki/entities/github|GitHub]]. Diz que ela "reflete o banco de dados", o que é um anti-padrão de desenho. Na [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this|aula 05]] ele já tinha chamado os métodos de string de "API", que é o sentido de API de linguagem.

Em [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]], a API do GitHub vira código: `XHR.open('GET', <URL>)` devolve o usuário em JSON, com avatar, bio, blog, company e "as outras APIs" (os campos `*_url`, links para outros recursos).

## Key sources

- [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]]: FrontPUSH, JavaScript aula 13: API como meio da comunicação front × back; API pública e do GitHub
- [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]]: FrontPUSH, JavaScript aula 14: API do GitHub consumida com XHR
