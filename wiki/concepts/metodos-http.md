---
type: concept
title: "Métodos HTTP"
aliases: ["http methods", "get post put delete", "verbos http"]
date_created: 2026-09-30
date_updated: 2026-11-03
source_count: 2
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

## Método e CSRF

No laboratório de [[wiki/sources/csrf-cross-site-request-forgery]], a troca de e-mail é um POST, e ainda assim um formulário de outro site consegue dispará-lo. POST sozinho não protege contra [[wiki/concepts/csrf]]. [external] Aceitar GET em ação que altera estado piora o caso: uma navegação top-level passa por `SameSite=Lax` ([PortSwigger](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions); ver [[wiki/concepts/samesite-cookie]]).

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — GET/PUT/DELETE idempotentes, POST não
- [[wiki/sources/csrf-cross-site-request-forgery]] — POST de troca de e-mail explorado por CSRF
