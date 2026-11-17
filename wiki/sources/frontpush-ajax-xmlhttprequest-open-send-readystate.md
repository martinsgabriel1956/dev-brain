---
type: source
title: "AJAX na prática: XMLHttpRequest, open, send, readyState e JSON.parse (FrontPUSH)"
aliases: ["FrontPUSH AJAX", "módulo de JavaScript ES6, aula 14", "AJAX"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, ajax, xmlhttprequest, xhr, readystate, onreadystatechange, json-parse, github-api, devtools, network, classe, instancia, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/dev-brain/raw/frontpush-ajax-xmlhttprequest-open-send-readystate.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# AJAX na prática (FrontPUSH)

## TL;DR

Aula 14 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (diz o nome: "Ah, Násser, por que vai se chamar XHR?"). Primeira aula prática da sequência: junta as três anteriores ([[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono|assíncrono]], [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back|JSON]], [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete|API e HTTP]]) numa requisição à API do [[wiki/entities/github|GitHub]].

- **AJAX:** "Asynchronous JavaScript XML [...] é o uso do objeto XML HTTP request" para buscar dados do servidor sem "o clássico do F5". Ver [[wiki/concepts/ajax]].
- **Classe e instância:** `const XHR = new XMLHttpRequest()`. "Sempre quando você estiver definindo uma variável, espaço, new [...] você está instanciando uma classe"; a variável "vira um objeto [...] que herda todas essas propriedades". Ver [[wiki/concepts/xmlhttprequest]].
- **Requisição:** `XHR.open('GET', <URL da API do GitHub>)` e `XHR.send(null)`. Na aba Network, filtro XHR: a requisição sai logo depois da página, "de maneira assíncrona", e a resposta é JSON.
- **Resposta:** `XHR.onreadystatechange = function () { if (XHR.readyState == 4) console.log(JSON.parse(XHR.responseText)) }`. O `readyState` 4 vem "quando der certo"; o painel mostra Status Code 200, método GET e URL.
- O objeto traz avatar, bio, blog, company e "as outras APIs".

## Key Claims

### O que é AJAX

- "Ele significa Asynchronous JavaScript XML, se eu fosse falar para você, é simplesmente o JavaScript assíncrono."
- "É o uso do objeto XML HTTP request para se comunicar com os scripts do lado do servidor, quando você está requisitando, por meio de uma API, algum tipo de informação." Ver [[wiki/concepts/api]].
- "Ao invés de a gente recarregar a página inteira [...] que é o clássico do F5 [...] e forçar o JavaScript síncrono [...] eu posso requisitar uma nova informação do servidor de maneira assíncrona." Ver [[wiki/concepts/javascript-assincrono]].

### Classe, `new` e herança

- "Vou atribuir para eles uma classe chamada XMLHttpRequest."
- "Sempre quando você estiver definindo uma variável, espaço, new, e atribuindo um método, que você entende que isso aqui é um método, consegue identificar porque ele fica azulzinho, tem o abrir e o fechado parênteses, isso aqui você está instanciando uma classe."
- "Uma classe [...] tem um conceito muito parecido com um objeto. Dentro dele tem métodos e atributos específicos dessa classe, que quando você instancia ela em alguma variável, automaticamente essa variável vira um objeto [...] que herda todas essas propriedades." Ver [[wiki/concepts/programacao-orientada-a-objetos]] e [[wiki/concepts/objetos-javascript]].
- `XHR.` no autocomplete: "tem muita coisa que foi herdada porque eu instanciei a classe nela, então ele virou um objeto de XMLHttpRequest".
- Recapitula: a URL é a API, o HTTP é o protocolo "para enviar e receber dados", e "essa alguma coisa é o JSON".

### open, send e Network

- "Um método chamado open [...] dois parâmetros. O primeiro é o método de acesso, no caso, eu estou só pegando uma informação, então é o método get", e o segundo é "o endereço da URL do API [...] a própria do GitHub". Ver [[wiki/concepts/metodos-http]].
- "Eu tenho que definir aqui o send, onde como eu não tenho nenhum parâmetro, eu estou simplesmente querendo pegar essa informação, eu vou passar ele como null."
- "Abrir aqui o nosso console, mais especificamente na seção de network [...] esse carinha aqui, XHR." Ver [[wiki/concepts/debug-de-requisicao-http]].
- "Ela demora um pouquinho [...] não é instantâneo, ela executa a página e em seguida faz a requisição, só que como é muito rápido, parece que é instantâneo, mas ele fez essa requisição de maneira assíncrona."
- A resposta "é justamente um arquivo JSON [...] onde ele traz aqui as propriedades, se deu certo, se não deu, se essa requisição foi bem sucedida". Ver [[wiki/concepts/json]].

### onreadystatechange, readyState e parse

- "`XHR.onreadystatechange` [...] como o próprio nome já diz, verificar quando o estado mudar, e aí eu vou lá e disparo uma função." Ver [[wiki/concepts/callback-javascript]].
- O painel mostra "statusCode, está vendo que ele deu 200, requestMethod, get, ok, o requestUrl". Ver [[wiki/concepts/http-status-code]].
- "If [...] `XHR.readyState`, e aí ele vai me dar o código 4 quando der certo."
- "Lembre-se, ele me volta isso aqui como um texto [...] é interessante eu transformar ele para objeto, utilizando o objeto JSON, e aí eu faço o parse [...] `XHR.responseText`."
- Resultado: "esse JSON aqui em forma de objeto [...] qual é o meu avatar, minha bio, qual é o meu blog, a minha companhia, as outras APIs".
- "A gente fez tudo dos conceitos nesse simples exemplo aqui."

## Código reconstruído

Pela fala (a legenda não mostra a tela; o usuário do GitHub não é dito):

```javascript
const XHR = new XMLHttpRequest()

XHR.open("GET", "https://api.github.com/users/<usuario>")
XHR.send(null)

XHR.onreadystatechange = function () {
  if (XHR.readyState == 4) {
    console.log(JSON.parse(XHR.responseText))
  }
}
```

## Entities

- [[wiki/entities/nasser]]: instrutor (diz o nome; a legenda o chama de "Anasse").
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6, aula 14.
- [[wiki/entities/github]]: a API consultada.
- [[wiki/entities/javascript]]: assunto da aula.

## Concepts

- [[wiki/concepts/xmlhttprequest]] (criado neste ingest)
- [[wiki/concepts/ajax]]
- [[wiki/concepts/javascript-assincrono]]
- [[wiki/concepts/json]]
- [[wiki/concepts/api]]
- [[wiki/concepts/metodos-http]]
- [[wiki/concepts/http-status-code]]
- [[wiki/concepts/callback-javascript]]
- [[wiki/concepts/fetch-api]]
- [[wiki/concepts/programacao-orientada-a-objetos]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/debug-de-requisicao-http]]

## Precisões e tensões com a wiki

`⚠️` Sem arquivo de referência na skill lang-dynamic para XMLHttpRequest ou classes em JavaScript; as precisões vêm do MDN e da especificação XHR do WHATWG (`[external]`, sem fetch nesta sessão, confiança alta).

- **`readyState === 4` não quer dizer "deu certo".** 4 é `DONE`: a requisição terminou, com sucesso ou não. Um 404 ou um 500 também chegam a 4, e uma falha de rede chega a 4 com `status` 0. O teste certo é `readyState === 4 && XHR.status === 200` (ou `status` entre 200 e 299). Os estados são 0 `UNSENT`, 1 `OPENED`, 2 `HEADERS_RECEIVED`, 3 `LOADING`, 4 `DONE`. Ver [[wiki/concepts/xmlhttprequest]] e [[wiki/concepts/http-status-code]].
- **"Se deu certo" não está no JSON.** Status 200, método e URL ficam na aba Headers da requisição, não no corpo; o JSON da resposta só traz os dados do usuário. A fala junta os dois painéis do DevTools.
- **`new` chama um construtor, não "um método azulzinho".** O azul do editor não indica classe. `XMLHttpRequest` é uma função construtora (interface da Web API); a instância herda pela cadeia de protótipos (`XMLHttpRequest.prototype` → `XMLHttpRequestEventTarget` → `EventTarget`). Em JS, `class` é sintaxe sobre protótipos ([[wiki/concepts/objetos-javascript]], [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this|aula 05]]). Primeira vez que o curso fala em classe; a ideia de molde → instância está certa ([[wiki/concepts/programacao-orientada-a-objetos]]).
- **AJAX é *Asynchronous JavaScript and XML*.** Não é "simplesmente o JavaScript assíncrono": é a técnica de pedir dados ao servidor por script e atualizar só parte da página (nome de Jesse James Garrett, 2005). O XML do nome ficou para trás; hoje a resposta é quase sempre JSON. Ver [[wiki/concepts/ajax]].
- **`open` tem três parâmetros.** O terceiro, `async`, vale `true` por padrão. Com `false`, a chamada bloqueia a página, e o XHR síncrono na thread principal está obsoleto.
- **`send(null)`:** o argumento é o corpo da requisição, não "parâmetro". Num GET não há corpo, e `send()` sem nada basta.
- **Registrar o handler antes do `send`** é a ordem convencional. Na aula funciona depois porque a resposta só chega numa volta seguinte do [[wiki/concepts/event-loop-performance-js|event loop]], quando o código atual já terminou.
- **Forma moderna.** `XHR.onload` (dispara só em `DONE`) ou `XHR.responseType = "json"` dispensam o `readyState` e o `parse`. Hoje se usa [[wiki/concepts/fetch-api|fetch]] (`fetch(url).then(r => r.json())`) ou [[wiki/entities/axios|Axios]]. O handler é um [[wiki/concepts/callback-javascript|callback]] de evento, como os da [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown|aula 10]].
- **A aba Network é do DevTools, não do "console".** O filtro atual se chama "Fetch/XHR". Ver [[wiki/concepts/debug-de-requisicao-http]].
- **"Protocolo de transferência de arquivos"** é o FTP. HTTP é de hipertexto ([[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete|aula 13]]).
- **Recarregar a página não é "forçar o JavaScript síncrono".** O F5 é uma navegação inteira: o navegador baixa o HTML de novo e o JavaScript recomeça do zero.
- **"As outras APIs" são os links da resposta.** A API do GitHub devolve campos `*_url` (`repos_url`, `followers_url`): URLs de outros recursos, o estilo hipermídia do REST. Ver [[wiki/concepts/api-rest]].
- **`==` × `===`:** a aula não mostra qual comparador usa; o curso recomendou `===` na [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript|aula 03]].
- **Positivos:** o fluxo inteiro (API → HTTP → JSON → parse) em poucas linhas, a aba Network para ver que a requisição é assíncrona, e lembrar que `responseText` é texto.

## Open Questions

- Qual usuário do GitHub ele consulta? A legenda só diz "o meu".
- Ele compara com `==` ou `===`?
- As próximas aulas da lista (Axios, Promises, Fetch, async/await) vão reescrever este exemplo?

## Raw quotes

- "que é o clássico do F5"
- "parece que é instantâneo, mas ele fez essa requisição de maneira assíncrona"
- "ele me volta isso aqui como um texto"
