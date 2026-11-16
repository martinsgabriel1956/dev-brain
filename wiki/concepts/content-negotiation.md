---
type: concept
title: "Content negotiation"
aliases: ["negociação de conteúdo", "content negotiation", "header Accept", "representação de recurso"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [http, rest, api, accept, content-type, representacao, tech-mentor-backend]
skill: tech-mentor-backend
status: stub
---

# Content negotiation

Um mesmo recurso HTTP pode ter várias **representações** (HTML, JSON, XML, CSV, idiomas diferentes). O cliente diz o que aceita em headers como `Accept`, `Accept-Language` e `Accept-Encoding`; o servidor escolhe uma, avisa em `Content-Type` e, se a escolha variar por header, manda `Vary: Accept` para os caches não misturarem respostas `[external]` https://www.rfc-editor.org/rfc/rfc9110#name-content-negotiation. Sem nada aceitável, responde 406 Not Acceptable.

```http
GET /products HTTP/1.1
Accept: application/json

HTTP/1.1 200 OK
Content-Type: application/json
Vary: Accept
```

É o "R" de REST (*Representational* State Transfer): o servidor não manda o recurso, manda uma representação do seu estado. Ver [[wiki/concepts/api-rest]] e [[wiki/concepts/recurso-rest]].

Na prática, quase toda API de hoje só fala JSON e ignora o `Accept`; a negociação aparece mais em `Accept-Encoding` (gzip, br) e em servidores que servem HTML ao navegador e JSON ao `fetch` na mesma rota.

## No JStack (aula 02)

Em [[wiki/sources/jstack-http-e-apis-rest]], [[wiki/entities/mateus-silva]] contrapõe o HTML montado (❌) ao JSON (✅) como "representação do estado". A wiki corrige: os dois são representações do mesmo recurso, e a escolha pode ser feita por negociação. O ponto válido é servir dados neutros para clientes que "não entendem HTML", como o React Native.

## Key sources

- [[wiki/sources/jstack-http-e-apis-rest]]: HTML × JSON como "representação do estado"
