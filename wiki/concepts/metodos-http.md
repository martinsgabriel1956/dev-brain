---
type: concept
title: "Métodos HTTP"
aliases: ["http methods", "get post put delete", "verbos http"]
date_created: 2026-09-30
date_updated: 2026-11-16
source_count: 4
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

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]]: "GET é um verbo HTTP", uma das regras do protocolo; acessar uma URL faz um GET, e "Cannot GET /" quer dizer que não há rota. O POST, "quando a gente vai enviar um formulário", fica para o dia seguinte. O formulário de busca envia por GET para `/search`.

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] completa o dia 4. O formulário passa de GET (dados na URL, `req.query`) para `method="post"` (dados no corpo, `req.body` com `express.urlencoded`). Diz que o POST envia "de uma maneira um pouco mais escondida", mas sem HTTPS o corpo também viaja exposto. Digitar uma URL na barra "só será o verbo get", por isso `/savepoint` dá Cannot GET. Ver [[wiki/concepts/query-string]].

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — GET/PUT/DELETE idempotentes, POST não
- [[wiki/sources/csrf-cross-site-request-forgery]] — POST de troca de e-mail explorado por CSRF
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: GET em rotas Express; Cannot GET /; POST adiado
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: GET x POST; req.query x req.body
