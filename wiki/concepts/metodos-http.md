---
type: concept
title: "Métodos HTTP"
aliases: ["http methods", "get post put delete", "verbos http"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [http, api, rest, idempotencia]
skill: tech-mentor-networking
status: stub
---

# Métodos HTTP

O método comunica a **intenção** da [[wiki/concepts/requisicao-http]]; é parte da mensagem, não a operação inteira.

| Método | Intenção | [[wiki/concepts/idempotencia\|Idempotente]]? |
|---|---|---|
| GET | obter um recurso | sim |
| POST | enviar/criar algo no servidor | **não** — duas chamadas podem criar dois registros |
| PUT | alterar/substituir um recurso | sim |
| DELETE | remover um recurso | sim |

## Por que idempotência importa

Escolher o método muda o comportamento em retries e cliques duplos: um POST repetido numa tela de pagamento pode cobrar duas vezes, por isso se adiciona trava contra clique duplo (e, no servidor, chave de idempotência — ver [[wiki/concepts/idempotencia]]).

- [external] A idempotência é definida sobre o *estado do servidor*, não sobre a resposta: um DELETE repetido pode retornar 404 sem deixar de ser idempotente (https://www.rfc-editor.org/rfc/rfc9110#name-idempotent-methods).
- [external] Existem também PATCH, HEAD e OPTIONS (usado no preflight de [[wiki/concepts/cors]]); não cobertos na fonte.

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — GET/PUT/DELETE idempotentes, POST não
