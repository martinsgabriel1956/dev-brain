---
type: concept
title: "Métodos HTTP"
aliases: ["http methods", "get post put delete", "verbos http"]
date_created: 2026-09-30
date_updated: 2026-11-17
source_count: 14
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

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: GET busca, POST cria, PUT atualiza, DELETE remove, com o Insomnia para testar. Diego diz que "o navegador não sabe fazer outras requisições", mas isso vale só para a barra de endereço; formulários fazem POST e `fetch` usa qualquer método. PUT substitui o recurso inteiro; atualização parcial é PATCH.

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], GET é "o padrão desse verbo" ao digitar uma URL; "Cannot GET /" quer dizer que não há rota. POST fica para o dia 5, como "o jeito de esconder os dados", o que é impreciso: só tira os dados da URL.

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], o cadastro passa a `method="post"` com `server.post("/save-classes")`. POST "quer dizer [...] eu vou criar um conteúdo". A aula diz que só o formulário acessa "essa rota escondida", mas qualquer cliente HTTP (curl, fetch) envia POST.

## No JStack, aula 02

Em [[wiki/sources/jstack-http-e-apis-rest]]: GET consulta, POST cria, PUT altera, DELETE remove (slide); pela barra do navegador "a requisição é sempre GET". A aula não cita PATCH: PUT substitui o recurso inteiro e é idempotente, PATCH altera parte `[skill: tech-mentor-backend]`. Formulários HTML só enviam GET e POST.

## Na NLW #2, dia 2 (Diego Fernandes)

GET busca ou lista, POST cria, PUT atualiza e DELETE apaga; o navegador "sempre" faz GET, daí o Insomnia. O mesmo recurso com métodos diferentes são rotas diferentes (`GET`/`POST /users`). Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## No JStack, aula 05

Em [[wiki/sources/jstack-criando-a-primeira-rota-da-api]], `request.method` vem em maiúsculas (`'GET'`), e pela barra do navegador é sempre GET. A rota compara método e caminho; método errado numa rota existente deveria dar 405, mas a aula usa 404 "para facilitar".

Em [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]], GET pega ("o padrão"), POST cria ("remete ao CRUD"), PUT atualiza (o usuário 7 troca o e-mail), DELETE apaga e HEAD "puxa o cabeçalho". Precisões: PUT não exige GET antes e substitui o recurso inteiro (troca parcial é PATCH, não citado); HEAD é GET sem corpo; faltam PATCH e OPTIONS.

Em [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]], o método é o primeiro argumento de `XHR.open`: "eu estou só pegando uma informação, então é o método get".

Em [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]], cada método vira um método do Axios: `.get` na aula, e "eu poderia muito bem colocar aqui o método .put, método .delete, método .post". `post` e `put` recebem o corpo como segundo argumento.

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — GET/PUT/DELETE idempotentes, POST não
- [[wiki/sources/csrf-cross-site-request-forgery]] — POST de troca de e-mail explorado por CSRF
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: GET em rotas Express; Cannot GET /; POST adiado
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: GET x POST; req.query x req.body
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: GET/POST/PUT/DELETE; "o navegador só faz GET" (só a barra de endereço)
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: GET e o "Cannot GET"
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: POST para criar; não é só formulário
- [[wiki/sources/jstack-http-e-apis-rest]]: GET/POST/PUT/DELETE; navegador sempre GET; sem PATCH
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: GET/POST/PUT/DELETE e o Insomnia
- [[wiki/sources/jstack-criando-a-primeira-rota-da-api]]: request.method; 405 citado, 404 usado
- [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]]: FrontPUSH, JavaScript aula 13: GET, POST, PUT, DELETE, HEAD
- [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]]: FrontPUSH, JavaScript aula 14: GET no XHR.open
- [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]]: FrontPUSH, JavaScript aula 16: axios.get/post/put/delete
- [[wiki/sources/frontpush-spa-metodos-tradicional-vs-spa-json-api-multiplos-clientes]]: FrontPUSH, React aula 04: GET confundido com a query string
