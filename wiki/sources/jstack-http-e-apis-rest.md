---
type: source
title: "JStack, aula 02: HTTP e APIs REST"
aliases: ["JStack aula 02", "HTTP e APIs REST", "Primeiros passos no Node.js: HTTP e APIs REST"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [api, api-rest, rest, http, requisicao-http, url, endpoint, query-string, metodos-http, http-headers, custom-headers, content-type, authorization, jwt, multi-tenancy, body, json, base64, multipart-form-data, status-code, https, http2, devtools, representacao-de-estado, content-negotiation, jstack, iniciante, tech-mentor-networking]
skill: tech-mentor-backend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/jstack-http-e-apis-rest.md"
source_url: ""
author: "Mateus Silva (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# JStack, aula 02: HTTP e APIs REST

## TL;DR

Segunda aula (cerca de 15 min) do módulo "Primeiros passos no Node.js" do [[wiki/entities/jstack]], com [[wiki/entities/mateus-silva]] (autoria inferida; o JSON do slide traz `"name": "Mateus"`). Todas as APIs do curso serão REST em [[wiki/entities/nodejs|Node.js]], consumidas por React e React Native. A aula vai em cinco partes:

1. **API.** Algo "no meio" que conecta front-end web, mobile, desktop e outras APIs à "mesma fonte de dados". Ver [[wiki/concepts/api-rest]] e [[wiki/concepts/arquitetura-cliente-servidor]].
2. **Request.** Cinco blocos (slide): URL/endpoint (identifica o recurso), [[wiki/concepts/query-string|query params]], [[wiki/concepts/metodos-http|método]] (GET, POST, PUT, DELETE), [[wiki/concepts/http-headers|headers]] (chave: valor, case-insensitive, `Authorization: Bearer`, custom com `X-`, como `X-Org-ID`) e body ([[wiki/concepts/json]] ou [[wiki/concepts/multipart-form-data]] para arquivos; [[wiki/concepts/base64-encoding|Base64]] é "gambiarrinha"). Ver [[wiki/concepts/requisicao-http]].
3. **Response.** Headers, Content-Type, [[wiki/concepts/http-status-code|status code]] (famílias pelo primeiro dígito; 200, 201, 204, 400, 401/403, 404, 405, 409, 500) e body.
4. **Exemplo e DevTools.** `GET /products` pelo navegador devolve `200`, `content-length: 197`, `content-type: text/html` e uma lista em `<ul><li>`. Para ver tudo, a aba Network do Chrome.
5. **REST.** "Um padrão para construção de APIs que utiliza o protocolo HTTP" e "retorna uma representação do estado". Recursos no plural (`GET /products`, `GET /products/10`, `POST /products`, `PUT /products/10`, `DELETE`). Em vez do HTML montado (❌ no slide), devolve JSON (✅), que web e mobile interpretam cada um a seu modo.

A estrutura é boa para iniciante. As imprecisões estão em "Tensões e precisões": REST tratado como "padrão HTTP + JSON", HTML ❌ como se não fosse representação, body "só em POST e PUT", status code como "header", 401 = 403, prefixo `X-` como boa prática (desaconselhado desde 2012) e `content-length` em "caracteres".

## Key Claims

### O que é uma API

- **Definição.** API é "um acrônimo para Application Programming Interface", explicada no sentido web: "permite que a gente conecte várias aplicações de diferentes tipos em uma mesma fonte de dados". O slide mostra uma engrenagem "API" ligada a FRONT END, MOBILE, DESKTOP e outra API.
- **No curso.** As APIs são "escritas em Node.js", logo "executam do lado do servidor", e são consumidas por web em React e mobile em React Native "através de HTTP, requisições HTTP".

### HTTP: request e response

- **Troca de mensagens.** "O protocolo HTTP é basicamente uma troca de mensagens entre duas pontas." O cliente é "literalmente qualquer tipo de programa ou dispositivo que consiga fazer requisições HTTP". Slide: "Hypertext Transfer Protocol", com setas Request → e ← Response.
- **Aviso.** "Agora vai vir muita informação em cima de você", mas "quando a gente for para a prática, [...] as peças vão começar a se encaixar".

### Request: URL, endpoint e query params

- **Slide:** `https://mywebsite.com/products?page=3&orderBy=name`, com URL (`https://mywebsite.com`), Endpoint (`/products`) e Query Params (`?page=3&orderBy=name`).
- **Endpoint** é "tudo que vem depois do nosso domínio": "onde a gente fala para o back-end qual é o recurso que a gente está tentando acessar". Ver [[wiki/concepts/url]] e [[wiki/concepts/recurso-rest]].
- **Query params** são "parâmetros adicionais": "eu quero que você me traga os produtos da página 3 e ordenados pelo nome". Ver [[wiki/concepts/query-string]].

### Request: métodos

- **Slide:** "GET: consulta de dados; POST: criação de registros; PUT: alteração de registros; DELETE: deleção de registros." "Existem alguns outros", mas "esses são os principais".
- **Navegador = GET.** Acessar a URL na barra "a requisição é sempre GET"; "pelo JavaScript [...] a gente consegue sim, pelo HTML também" fazer outros métodos. Ver [[wiki/concepts/metodos-http]].

### Request: headers

- **Slide:** "Usados para trocar informações adicionais entre client e server"; "Existem headers pré definidos porém também podemos criar headers customizados".
- **Formato.** "Chave e valor separados por dois pontos": `Content-Type: application/json`. O `Content-Type` diz o tipo do corpo, na request e na response.
- **Case-insensitive.** `content-type` em minúsculas funciona igual. `authorization: Bearer usertoken` leva o "token JWT de autenticação do usuário". Ver [[wiki/concepts/http-headers]] e [[wiki/concepts/jwt]].
- **Custom headers.** "Uma boa prática é sempre a gente colocar um X na frente" (slide: "sempre começam com X"). Exemplo: `X-Org-ID: 1123`, trocado quando o usuário muda a organização selecionada na interface. Ver [[wiki/concepts/multi-tenancy]].

### Request: body

- **Só em POST e PUT.** "Ele só está presente em requisições do método post e put, tá? Nas outras, a gente não envia body." (Slide: "Apenas para requisições do tipo POST e PUT.")
- **JSON.** "JavaScript Object Notation", "poderoso": quase toda linguagem lê, e aceita "string, array, objetos aninhados, números". O slide mostra `user` com `id`, `name`, `roles` e `address` aninhado. Ver [[wiki/concepts/json]].
- **Binários.** Imagens, PDFs, áudios e vídeos não vão em JSON, salvo pela "gambiarrinha" de converter para Base64, que "acaba pesando mais a nossa requisição". Para arquivos, multipart/form-data, "composto por chave e valor". Ver [[wiki/concepts/base64-encoding]] e [[wiki/concepts/multipart-form-data]].

### Response

- **Slide:** Headers ("Informações adicionais"), Content Type ("Tipo do conteúdo da resposta"), Status Code ("Indica o que aconteceu com a request") e Body ("Dados que foram requisitados").
- **Status code como "outro header".** "A gente também tem um outro header, que é o Status Code", que diz "o que aconteceu com ela? Deu certo? Deu errado? [...] Foi um erro de autorização? Foi um erro no servidor?"
- **Famílias.** "O que indica a categoria é o primeiro dígito": 1xx informação, 2xx sucesso, 3xx redirecionamento, 4xx erro do cliente, 5xx erro do servidor. "O que mais interessa para a gente são os códigos com o dígito 2, 4 e 5." Slide dos principais: 200 OK, 201 Created, 204 No Content, 400 Bad Request, "401/403: Unauthorized", 404 Not Found, 405 Method Not Allowed, 409 Conflict, 500 Internal Server Error. Ver [[wiki/concepts/http-status-code]].

### Exemplo prático e DevTools

- **Request.** Nos headers aparecem o `path` (`/products`), o método (GET) e o `scheme` ("HTTPS, o S de Security"). Ver [[wiki/concepts/http-vs-https]].
- **DevTools.** "Abrir aí no teu Google Chrome a Developer Tools, vai ter uma abinha Network": dá para ver todas as requisições da página, com headers e bodies.
- **Response.** `status: 200`, `content-length: 197` ("uma contagem de quantos caracteres estão sendo enviados dentro do corpo"), `content-type: text/html` e o HTML "já todo populado" com iPhone 11 Pro (R$ 6.999,00) e iPad Pro (R$ 8.499,00).

### REST e representação do estado

- **Slide:** "Padrão REST: Representational State Transfer. Um padrão para construção de APIs; Usa o protocolo HTTP; Retorna uma representação do estado."
- **Definição falada.** "O REST não passa de um padrão para construção de APIs que utiliza o protocolo HTTP. Simples assim."
- **Nomes de endpoints.** "Usar o nome dos recursos sempre no plural": `GET /products`, `GET /products/10` (o `/10` "é o que a gente chama de parâmetros"), `POST /products`, `PUT /products/10` e `DELETE` com o ID na URL.
- **Representação do estado.** O HTML com os produtos em `li` "vai funcionar muito bem na web", mas o React Native "não entende HTML". Então, "ao invés de a gente retornar esse HTML já todo montado", a API "retorna uma representação desses dados" em JSON (slide: HTML com ❌, JSON com ✅).
- **Formato.** "Poderia, por exemplo, ser um XML", mas o JSON "é o mais usado na web". A web injeta os dados no HTML com JavaScript, o mobile "não vai ser com LI": "os dados ficam acessíveis de uma forma genérica". Ver [[wiki/concepts/api-rest]] e [[wiki/concepts/content-negotiation]].

## Tensões e precisões

- **REST não é "um padrão que usa HTTP".** É um estilo arquitetural de [[wiki/entities/roy-fielding|Roy Fielding]] (tese de 2000) definido por restrições: cliente-servidor, sem estado, cache, interface uniforme, sistema em camadas e código sob demanda opcional `[external]` https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm. HTTP é a implementação mais comum, não a definição. Plural nos recursos é convenção de mercado `[skill: tech-mentor-backend]`, não regra do REST.
- **HTML também é representação.** "Representational State Transfer" fala em transferir *representações* do estado de um recurso, e o HTML do slide ❌ é uma delas. Na tese, o hipertexto (links que guiam o próximo passo, o HATEOAS) é parte central do estilo, e o HTML é o exemplo clássico. O mesmo `/products` pode servir HTML ou JSON conforme o header `Accept` do cliente ([[wiki/concepts/content-negotiation]]). O ponto da aula, desacoplar dados de tela para vários clientes, está certo; o erro é chamar isso de "a grande sacada do REST".
- **Body não é "só POST e PUT".** PATCH também leva body. Em DELETE e GET o body não tem semântica definida e costuma ser ignorado ou rejeitado `[external]` https://www.rfc-editor.org/rfc/rfc9110#name-get. E toda response pode ter body, inclusive a de GET.
- **PUT não é "editar" genérico.** PUT substitui o recurso inteiro e é idempotente; a edição parcial é PATCH `[skill: tech-mentor-backend]`. A aula não cita PATCH. Ver [[wiki/concepts/metodos-http]] e [[wiki/concepts/idempotencia]].
- **Status code não é header.** No HTTP/1.1 ele vem na linha de status (`HTTP/1.1 200 OK`), antes dos headers. A confusão tem origem real: no HTTP/2 o DevTools mostra `:status`, `:path`, `:method` e `:scheme` como **pseudo-headers**, que são exatamente o `path`, o método e o `scheme` que a aula lista "dentro dos headers" `[external]` https://www.rfc-editor.org/rfc/rfc9113#name-request-pseudo-header-field. Ver [[wiki/concepts/http2]].
- **401 ≠ 403.** O slide junta "401/403: Unauthorized". 401 é "não autenticado" (falta credencial ou ela é inválida); 403 Forbidden é "sei quem você é, mas não pode" `[skill: tech-mentor-backend]`.
- **Prefixo `X-` desaconselhado.** A RFC 6648 (2012) recomenda não criar headers novos com `X-`, porque o nome vira problema quando o header é padronizado (o caso `X-Forwarded-For` → `Forwarded`) `[external]` https://www.rfc-editor.org/rfc/rfc6648. O `X-` continua comum na prática; o "sempre começam com X" do slide é convenção, não regra. No exemplo de organização, o servidor precisa validar se o usuário pertence à organização do header, ou qualquer cliente troca o ID e acessa outro tenant ([[wiki/concepts/multi-tenancy]]).
- **`content-length` conta bytes, não caracteres.** Em UTF-8, "ç" ou "é" ocupam 2 bytes. Importa no exemplo, que tem "R$" e acentos.
- **HTTPS: o S é de Secure**, não "Security": HTTP sobre TLS. Ver [[wiki/concepts/http-vs-https]] e [[wiki/concepts/tls]].
- **Base64 custa cerca de 33% a mais** (3 bytes viram 4 caracteres). O "em alguns casos nem conseguimos" é o limite de tamanho de body e de memória ao montar a string inteira ([[wiki/concepts/base64-encoding]]).
- **"Pelo HTML também", só em parte.** Formulários HTML enviam apenas GET e POST; PUT e DELETE exigem JavaScript (`fetch`) ou um override de método no servidor ([[wiki/concepts/formulario-html]]).
- **Domínio do exemplo.** A fala diz ".com.br" e "mywebsite.com.br products", e o slide mostra `mywebsite.com/products`. O "parâmetros" do `/10` é o que frameworks chamam de *route params* ou *path params*, diferentes dos query params.

## Entities

- [[wiki/entities/jstack]]: o curso
- [[wiki/entities/mateus-silva]]: instrutor (inferido)
- [[wiki/entities/nodejs]]: linguagem das APIs do curso
- [[wiki/entities/roy-fielding]]: autor do REST (na correção)

## Concepts

- [[wiki/concepts/api-rest]]
- [[wiki/concepts/requisicao-http]]
- [[wiki/concepts/recurso-rest]]
- [[wiki/concepts/url]]
- [[wiki/concepts/query-string]]
- [[wiki/concepts/metodos-http]]
- [[wiki/concepts/http-headers]]
- [[wiki/concepts/http-status-code]]
- [[wiki/concepts/json]]
- [[wiki/concepts/base64-encoding]]
- [[wiki/concepts/multipart-form-data]]
- [[wiki/concepts/content-negotiation]]
- [[wiki/concepts/http-vs-https]]
- [[wiki/concepts/http2]]
- [[wiki/concepts/jwt]]
- [[wiki/concepts/multi-tenancy]]
- [[wiki/concepts/arquitetura-cliente-servidor]]

## Open Questions

- O curso vai usar PATCH, ou PUT para edições parciais também?
- Como o curso valida o `X-Org-ID` (ou equivalente) contra o usuário autenticado, se chegar a usar multi-organização?
- O `/products/10` vira `request.params` no código; a próxima aula diferencia route params de query params?

## Raw quotes

> "O REST não passa de um padrão para construção de APIs que utiliza o protocolo HTTP. Simples assim, bem fácil, né?"

> "Ao invés de a gente retornar esse HTML já todo montado com os produtos ali dentro, a gente retorna uma representação desses dados."

> "Os dados ficam acessíveis de uma forma genérica."
