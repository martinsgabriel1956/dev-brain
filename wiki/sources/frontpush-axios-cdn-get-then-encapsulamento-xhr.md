---
type: source
title: "Axios: encapsulamento do XMLHttpRequest, CDN e axios.get com then (FrontPUSH)"
aliases: ["FrontPUSH Axios", "módulo de JavaScript ES6, aula 16", "Axios"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, axios, cliente-http, xmlhttprequest, promise, then, cdn, npm, yarn, github-api, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/dev-brain/raw/frontpush-axios-cdn-get-then-encapsulamento-xhr.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Axios (FrontPUSH)

## TL;DR

Aula 16 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (diz o nome: "Ah, Násser, não estou entendendo"). Curta (cerca de 5 min): refaz a requisição à API do [[wiki/entities/github|GitHub]] das aulas [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate|14]] e [[wiki/sources/frontpush-promises-resolve-reject-then-catch|15]] com o [[wiki/entities/axios|Axios]].

- **O que é:** "um encapsulamento do XML HTTP request [...] a mesma coisa que a gente fez na aula passada, só que de maneira bem mais enxuta". Já "suporta uma API de promise".
- **Instalação:** existe via npm e yarn, mas "como a gente ainda não configurou o nosso ambiente de desenvolvimento", ele carrega o código "via CDN", que "tem que ser declarado primeiro". Ver [[wiki/concepts/cdn]] e [[wiki/concepts/carregamento-de-scripts]].
- **Código:** "toda aquela parafernália" (a Promise com XHR, `readyState`, status, `JSON.parse`) vira `axios.get(url).then(...)`. Há também `.put`, `.delete` e `.post`.
- **Resposta "mais completa":** além dos dados (`data`), traz `config`, os cabeçalhos (cache-control) e o `request`.

## Key Claims

### O Axios

- "Desde lá da aula de AJAX, a gente está sempre tratando do mesmo assunto, só que a gente está refinando a forma de como a gente faz a requisição." Ver [[wiki/concepts/ajax]].
- "O axios, simplesmente, é um encapsulamento do XML HTTP request, ou seja, ele vai fazer exatamente a mesma coisa que a gente fez na aula passada, só que de maneira bem mais enxuta." Ver [[wiki/concepts/xmlhttprequest]].
- "Ele já é baseado aqui em HTTP request e já é uma promise [...] ele já suporta uma API de promise." Ver [[wiki/concepts/promise-javascript]].

### CDN

- "Você pode instalar aqui via npm, yarn, só que como a gente ainda não configurou o nosso ambiente de desenvolvimento [...] eu prefiro fazer isso quando eu estou literalmente utilizando algum tipo de framework, a gente pode utilizar o código via CDN." Ver [[wiki/concepts/gerenciador-de-pacotes]].
- "É o código em si do axios, a gente está passando esse código para o nosso navegador ler para quando a gente utilizar os métodos do axios dentro do nosso JavaScript, sendo que ele tem que ser declarado primeiro."

### axios.get

- "Vou literalmente apagar a promise." A versão anterior fica comentada: "olha só o tamanho da parafernália".
- "Definir simplesmente o axios e utilizar o .get, a gente pode passar a nossa URL diretamente por aqui [...] eu posso aplicar o .then direto nela, porque ela já é uma promise e eu já estou passando qual é o método e já estou passando a URL."
- "Eu poderia muito bem colocar aqui o método .put, método .delete, método .post, só que no caso é o .get mesmo." Ver [[wiki/concepts/metodos-http]].
- "Se eu quisesse colocar um outro parâmetro aqui, eu colocaria ele aqui, mas no caso não é necessário, nós vamos explorar ele um pouquinho depois."
- "Ele vai funcionar da mesmíssima forma que a gente estabeleceu antes, ele já tem todos os tratamentos."

### A resposta

- "Ele me voltou o objeto mais completo ainda, porque ele me voltou o config [...] antes ele só me voltava a data."
- "O cache control, ou seja, meio que são as configurações de metadata e o próprio request." Ver [[wiki/concepts/http-headers]] e [[wiki/concepts/http-caching]].
- "Além dele me voltar mais informações, ser mais completo, ele é mais enxuto em questão de código, em questão de verbosidade."

## Código reconstruído

Pela fala (a legenda não mostra a tela; a URL da CDN e o usuário do GitHub não são ditos):

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script src="app.js"></script>
```

```javascript
axios
  .get("https://api.github.com/users/<usuario>")
  .then(function (response) {
    console.log(response) // { data, status, statusText, headers, config, request }
  })
```

## Entities

- [[wiki/entities/nasser]]: instrutor (diz o nome).
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6, aula 16.
- [[wiki/entities/axios]]: assunto da aula.
- [[wiki/entities/github]]: a API consultada.
- [[wiki/entities/javascript]]: módulo em que a aula está.

## Concepts

- [[wiki/concepts/xmlhttprequest]]
- [[wiki/concepts/promise-javascript]]
- [[wiki/concepts/fetch-api]]
- [[wiki/concepts/metodos-http]]
- [[wiki/concepts/http-status-code]]
- [[wiki/concepts/http-headers]]
- [[wiki/concepts/http-caching]]
- [[wiki/concepts/json]]
- [[wiki/concepts/cdn]]
- [[wiki/concepts/carregamento-de-scripts]]
- [[wiki/concepts/gerenciador-de-pacotes]]
- [[wiki/concepts/ajax]]

## Precisões e tensões com a wiki

`⚠️` Sem arquivo de referência para o Axios nas skills lang-dynamic e tech-mentor-frontend; as precisões vêm da documentação do Axios e do MDN (`[external]`, sem fetch nesta sessão, confiança alta).

- **Os dados agora estão em `response.data`.** O objeto "mais completo" é o envelope do Axios: `{ data, status, statusText, headers, config, request }`. Na aula 15 o `resolve` entregava o JSON já parseado; aqui o usuário do GitHub fica em `response.data`, e quem copiar o `console.log(response)` para usar os campos precisa lembrar disso. O Axios faz o `JSON.parse` sozinho.
- **Cache-control é cabeçalho de resposta, não `config`.** O `config` é a configuração da requisição feita (URL, método, timeout, headers enviados). O `cache-control` está em `response.headers`, com o que o servidor diz sobre cache ([[wiki/concepts/http-caching]]). `request` é o próprio XHR por baixo.
- **"Já tem todos os tratamentos" vale para o erro também, mas falta o `catch`.** O Axios rejeita a Promise quando o status sai de 2xx (`validateStatus`), e o erro traz `error.response.status`. A aula não mostra o `.catch`, que a aula 15 tinha; sem ele, um 404 vira *unhandled rejection*. É diferente do [[wiki/concepts/fetch-api|fetch]], que só rejeita em falha de rede. Ver [[wiki/concepts/http-status-code]] e [[wiki/entities/axios]].
- **"O .then e o .get"** deve ser lapso para `.then` e `.catch`. O `.get` é o método da requisição; `then` e `catch` são da Promise que ele devolve.
- **O Axios não "é uma promise".** `axios.get(...)` devolve uma Promise. `axios` é uma função com métodos (`get`, `post`, `create`).
- **"Outro parâmetro" depende do método.** `axios.get(url, config)` recebe um objeto de configuração (`params`, `headers`, `timeout`); `axios.post(url, data, config)` e `put` recebem o corpo como segundo argumento, que o Axios serializa em JSON. Ver [[wiki/concepts/metodos-http]].
- **Encapsulamento do XHR só no navegador.** No Node, o Axios usa o módulo `http`. As versões recentes também têm um adaptador opcional para `fetch` (`[external]`, confiança média).
- **CDN não é instalar.** A tag `<script>` baixa o arquivo a cada visita (ou do cache) e cria a variável global `axios`; "declarado primeiro" quer dizer que essa tag vem antes do `app.js` ([[wiki/concepts/carregamento-de-scripts]]). Fixe a versão na URL (e use SRI) para o código não mudar sozinho. Em projeto real, npm ou yarn mais um bundler ([[wiki/concepts/gerenciador-de-pacotes]]). A [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes|aula de ambiente]] do curso já tinha instalado Node e yarn.
- **"Mais enxuto" compara com o XHR à mão.** Com o `fetch` nativo a requisição também cabe em uma linha, sem dependência (`fetch(url).then(r => r.json())`); o que o Axios acrescenta é rejeitar em 4xx/5xx, JSON automático, interceptors, `baseURL` e timeout.
- **Lapso literal no raw:** "XHTML HTTP request" é o `XMLHttpRequest`.
- **Positivos:** a progressão XHR → Promise → Axios mostra o que a biblioteca esconde; o `config` e os `headers` aparecem no console; o aviso de que o npm vem depois, com framework.

## Open Questions

- Há 16 s sem legenda (00:01:03–00:01:19): é quando ele abre a página do Axios (README ou site). "Entendo como é instalar, o exemplo, a API do axios" vem logo depois, e a frase está truncada.
- Qual CDN ele usa (jsDelivr, unpkg)? E com versão fixa?
- A próxima aula é `fetch` ou `async/await`? A lista da [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono|aula 12]] tinha os dois.

## Raw quotes

- "um encapsulamento do XML HTTP request"
- "olha só o tamanho da parafernália"
- "ele já suporta uma API de promise"
