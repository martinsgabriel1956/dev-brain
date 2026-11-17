---
type: source
title: "API e protocolo HTTP: API pública, GitHub, HTTPS e métodos (FrontPUSH)"
aliases: ["FrontPUSH API e HTTP", "módulo de JavaScript ES6, aula 13", "API & HTTP"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [api, http, https, metodos-http, get, post, put, delete, head, cors, autenticacao, github-api, crud, curso, frontend, javascript]
skill: tech-mentor-backend
status: draft
source_file: "/home/nemomartins/Documentos/dev-brain/raw/frontpush-api-e-protocolo-http-metodos-get-post-put-delete.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# API e protocolo HTTP (FrontPUSH)

## TL;DR

Aula 13 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (pela sequência; não diz o nome). "Uma aula mais conceitual" (cerca de 9 min) que prepara o AJAX da aula seguinte. Domínios secundários: frontend (`lang-dynamic`), networking.

- **API:** o front "constantemente precisa fazer" requisições ao back, e faz "por meio de uma API". Quem constrói um back-end se pergunta "como eu vou me comunicar? Ah, eu vou construir uma API". Acesso "via URL", com ou sem autenticação (chave, senha). Ver [[wiki/concepts/api]].
- **API pública:** a do tempo em Brasília (a cidade vai na URL e volta um JSON) e a do [[wiki/entities/github|GitHub]]: `api.github.com/users/<usuário>` devolve login, ID, node ID. O repositório "Public APIs" lista APIs com autenticação, HTTPS e [[wiki/concepts/cors|CORS]].
- **HTTP:** "Hypertext Transfer Protocol [...] para você enviar e receber dados na web, como se fosse um canal". **HTTPS** tem criptografia; sem ela, o navegador mostra o "cadeadinho aberto". Ver [[wiki/concepts/http-vs-https]].
- **Métodos** ([[wiki/concepts/metodos-http]]): GET pega ("o padrão"), POST cria ("remete ao CRUD"), PUT atualiza (o usuário 7 troca o e-mail), DELETE apaga, HEAD "puxa o cabeçalho" (metadados).

## Key Claims

### API

- "A gente está sempre tentando fazer uma requisição, ou seja, uma busca de informação do front-end para o back-end."
- "Requisição nada mais é do que as informações de padronização que você precisa para poder realizar a comunicação e aí você faz por meio de uma API." Ver [[wiki/concepts/requisicao-http]].
- "Sempre que você constrói [...] um back-end, você tem que sempre se perguntar como eu vou me comunicar? Ah, eu vou construir uma API."
- "Essa API, de certa forma, reflete o banco de dados e tem como você acessar essas informações por meio de regrinhas, por meio de documentos que têm uma padronização." Ver [[wiki/concepts/contrato-de-api]].
- "Você acessa via URL, pode ter autenticação ou não [...] mediante uma chave, mediante uma senha", "ou às vezes é uma API pública". Ver [[wiki/concepts/api-key]] e [[wiki/concepts/autenticacao-e-autorizacao]].
- Tempo em Brasília: "como eu tenho que colocar a informação Brasília dentro dessa URL para que ele me devolva o JSON". "Toda e qualquer pessoa pode fazer requisição [...] sem precisar de uma senha." Ver [[wiki/concepts/json]].
- "A API é a forma de como eu acesso a rede de comunicação daquele servidor para poder obter informações [...] um get, um post, um put."

### A API do GitHub e as Public APIs

- "A própria API do GitHub, que é muitíssimo utilizada nesses casos", será o exemplo das próximas aulas.
- A requisição a `.../users` traz "um arquivo do tipo JSON [...] eu tenho um login [...] o ID do meu usuário, o node ID e outras informações". Ver [[wiki/concepts/github-search-api-limites]].
- "É só colocar no Google Public APIs [...] ele vai falar de todas as APIs que são públicas, uma descrição, se tem autenticação ou não, se tem o protocolo HTTPS ou não, se tem o CORS."
- CORS: "basicamente é quando você faz uma requisição dentro de uma outra requisição, se ele permite isso ou não, porque geralmente isso é bloqueado dos navegadores para poder evitar [...] que você execute um script dentro de um outro lugar".

### HTTP e HTTPS

- "Hypertext Transfer Protocol, ou seja, é um protocolo de transferência [...] para você enviar e receber dados na web, como se fosse um canal, ele é utilizado para poder eu transferir arquivos."
- "O S vem de Security e é o mais amplamente utilizado justamente pela questão da segurança."
- Sem criptografia, o navegador mostra "um cadeadinho aberto, ele avisa que a conexão não é segura". Ver [[wiki/concepts/tls]].

### Métodos

- "O get é a maioria deles e ele é o padrão [...] vem de pegar a informação." O exemplo: "eu acessei a API do GitHub, estou acessando os usuários do GitHub, e aí eu especifiquei qual é o usuário que eu quero, que no caso é o meu".
- POST: o formulário com "nome, e-mail, endereço" vai ao back-end para cadastrar; "você não está mais pegando a informação, você está enviando [...] de create, que sempre remete ao CRUD". Ver [[wiki/concepts/crud]].
- PUT: "parecido com o método post, você vai atualizar a informação, então necessariamente você vai pegar um método get antes". O usuário 7 troca o e-mail e "você manda com o método put".
- DELETE: "quando você quer deletar alguma informação".
- HEAD: "vem de puxar o cabeçalho, ele não é muito importante por agora [...] quando você precisa dos metadados de alguma coisa". Ver [[wiki/concepts/http-headers]].
- Próxima aula: AJAX com requisição HTTP ([[wiki/concepts/ajax]], [[wiki/concepts/javascript-assincrono]]).

## Entities

- [[wiki/entities/nasser]]: instrutor (pela sequência do módulo).
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6, aula 13.
- [[wiki/entities/github]]: a API pública usada de exemplo.
- [[wiki/entities/javascript]]: módulo em que a aula está.

## Concepts

- [[wiki/concepts/api]] (criado neste ingest)
- [[wiki/concepts/api-rest]]
- [[wiki/concepts/contrato-de-api]]
- [[wiki/concepts/requisicao-http]]
- [[wiki/concepts/metodos-http]]
- [[wiki/concepts/http-vs-https]]
- [[wiki/concepts/tls]]
- [[wiki/concepts/http-headers]]
- [[wiki/concepts/crud]]
- [[wiki/concepts/cors]]
- [[wiki/concepts/api-key]]
- [[wiki/concepts/autenticacao-e-autorizacao]]
- [[wiki/concepts/github-search-api-limites]]
- [[wiki/concepts/json]]
- [[wiki/concepts/ajax]]
- [[wiki/concepts/javascript-assincrono]]

## Precisões e tensões com a wiki

`[skill: tech-mentor-backend]` Referência: `api-design.md` (tabela de métodos REST com idempotência, códigos de status). Resto da RFC 9110, do MDN e da documentação do GitHub como `[external]`, sem fetch nesta sessão (confiança alta, salvo onde indicado).

- **CORS está explicado errado.** Não é "uma requisição dentro de outra requisição". O navegador aplica a *same-origin policy*: uma página de `site-a.com` não pode ler a resposta de `api-b.com`. CORS é o mecanismo com que o servidor libera isso, mandando `Access-Control-Allow-Origin` (com preflight `OPTIONS` em alguns casos). O que ele impede é ler dados de outra origem com as credenciais do usuário; "executar um script dentro de um outro lugar" é [[wiki/concepts/xss]], outro problema. Na lista Public APIs, "CORS: yes" quer dizer que dá para chamar a API direto do front-end. Ver [[wiki/concepts/cors]] e [[wiki/concepts/cors-misconfiguration]].
- **"Public APIs" não são "as APIs do GitHub".** O repositório `public-apis/public-apis` fica no GitHub, mas lista APIs gratuitas de vários provedores (clima, filmes, governo), com as colunas Auth, HTTPS e CORS. A API do GitHub é só uma delas. (A confusão parece vir de a lista estar hospedada no GitHub; inferência.)
- **A API não deve "refletir o banco de dados".** `[skill: tech-mentor-backend]` Uma boa API expõe recursos e casos de uso e esconde o schema; espelhar tabelas acopla o cliente ao banco e vaza campos internos. Ver [[wiki/concepts/contrato-de-api]] e [[wiki/concepts/api-e-consequencia-nao-ponto-de-partida]].
- **API é mais que rede.** A definição da aula ("a forma de como eu acesso a rede de comunicação daquele servidor") é a de API web. API é qualquer interface de programação: o DOM e os métodos de string que a [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this|aula 05]] já chamava de "API" também são. Ver [[wiki/concepts/api]].
- **Requisição é a mensagem, não "as informações de padronização".** Uma requisição HTTP tem método, URL, cabeçalhos e corpo; o padrão é o protocolo (e o contrato da API). Ver [[wiki/concepts/requisicao-http]].
- **"O S vem de Security".** É *Secure* (HTTP Secure), e o S é HTTP sobre [[wiki/concepts/tls|TLS]]: criptografia, integridade e autenticação do servidor por certificado. Os navegadores atuais mostram "Não seguro" na barra em vez do cadeado aberto, e o Chrome trocou o cadeado por outro ícone em 2023 (`[external]`, confiança média).
- **HTTP não é só para "transferir arquivos".** Transfere representações de recursos: HTML, JSON, imagens, respostas geradas na hora. É pedido-resposta e sem estado (*stateless*), sobre TCP (ou QUIC no HTTP/3). Ver [[wiki/concepts/protocolo-de-rede]].
- **GET não é "a maioria" dos métodos.** É o mais usado e o padrão da navegação e do `fetch` sem opções. É seguro (não muda estado) e idempotente.
- **PUT não pede GET antes.** O cliente só precisa saber o ID. PUT substitui o recurso inteiro e é idempotente; trocar só o e-mail é caso de PATCH, que a aula não cita. `[skill: tech-mentor-backend]` `api-design.md`: "PUT /users/123 → substituir completo (idempotente); PATCH → atualizar parcial". Ver [[wiki/concepts/metodos-http]] e [[wiki/concepts/idempotencia]].
- **HEAD é um GET sem corpo.** Devolve os mesmos cabeçalhos que o GET (`Content-Type`, `Content-Length`, `Last-Modified`): serve para saber se um recurso existe ou mudou sem baixá-lo. Não são metadados "inerentes ao servidor" em geral. Faltam também PATCH e OPTIONS.
- **Mapa CRUD:** Create = POST, Read = GET, Update = PUT/PATCH, Delete = DELETE ([[wiki/concepts/crud]]). Bate com a [[wiki/sources/jstack-http-e-apis-rest|aula 02 do JStack]].
- **A API do GitHub sem token tem limite.** `[external]` Sem autenticação, cerca de 60 requisições por hora por IP; com token, 5.000. Vale saber antes de usá-la nas próximas aulas. Ver [[wiki/concepts/github-search-api-limites]].
- **API pública ≠ sem chave.** Muitas APIs públicas (como várias de clima) pedem uma [[wiki/concepts/api-key]] gratuita; "pública" quer dizer aberta a qualquer um, não necessariamente anônima.
- **Positivos:** a API do GitHub como exemplo real e gratuito, o par método ↔ intenção, CRUD ligado aos métodos, o HTTPS como padrão.

## Open Questions

- Há 9 s sem legenda (00:03:02–00:03:11) antes de ".users": é quando ele digita a URL da API do GitHub. O nome do usuário não aparece; a legenda só diz "que no caso é o meu".
- Qual API de tempo ele mostra? Não diz o nome (OpenWeather e HG Brasil pedem chave).
- "Como eu escrevi aqui": há um slide ou texto na tela com a tradução de HTTP que a legenda não mostra.

## Raw quotes

- "como eu vou me comunicar? Ah, eu vou construir uma API"
- "como se fosse um canal"
- "de create, que sempre remete ao CRUD"
