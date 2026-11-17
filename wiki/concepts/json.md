---
type: concept
title: "JSON (JavaScript Object Notation)"
aliases: ["JSON", "JavaScript Object Notation", "res.json()"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 17
tags: [json, javascript, api, formato-de-dados]
skill: tech-mentor-frontend
status: stub
---

# JSON (JavaScript Object Notation)

Formato de texto para dados estruturados, com sintaxe derivada dos literais de objeto e array do JavaScript: chaves sempre entre aspas duplas, valores string, number, boolean, null, objeto ou array. É o formato padrão de APIs web. `JSON.parse` transforma texto em valor; `JSON.stringify` faz o contrário; `res.json()` da [[wiki/concepts/fetch-api]] faz o parse do corpo da resposta.

## Na NLW #1

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] mostra a resposta do [[wiki/entities/ibge]] (27 objetos com id, sigla, nome e região) e responde à dúvida "esse objeto tá escrito um pouquinho diferente": "esse daqui é um JSON. Isso daqui não é um objeto JavaScript", é "um textão que ele parece muito com JavaScript". Indica a extensão JSON Formatter para ler a resposta no navegador.

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] retoma o JSON ao abrir o `package.json`: "um jeito de você escrever textos que parece se assemelhar muito com o JavaScript", com todas as propriedades entre aspas duplas. Ver [[wiki/concepts/package-json]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]], o JSON é o formato da [[wiki/concepts/api-rest]]: a rota devolve os dados e não o HTML, e o mesmo JSON serve a web e o celular. No Express, `response.json()` aceita objeto ou array.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]], o body JSON do Insomnia só é lido depois de `app.use(express.json())`. A API devolve itens "serializados" com `image_url`.

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], JSON é "JavaScript Object Notation": chaves e valores com aspas duplas, vírgula só entre itens, colchetes para listas. No objeto JavaScript as aspas nas chaves "são facultativas".

## No JStack, aula 02

Em [[wiki/sources/jstack-http-e-apis-rest]], JSON é o formato do body e da resposta REST: quase toda linguagem lê, e aceita string, número, array e objetos aninhados. Não leva binário, salvo em [[wiki/concepts/base64-encoding|Base64]] ("gambiarrinha"); para arquivos, [[wiki/concepts/multipart-form-data]]. "Poderia [...] ser um XML", mas o JSON "é o mais usado na web".

## Na NLW #2, dia 2 (Diego Fernandes)

"Um objeto escrito da mesma forma que a gente escreve no JavaScript", entendido por web e mobile; a lista é um array de objetos. Vírgula no fim do último item é erro em JSON. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## Na NLW #2, dia 5 (Diego Fernandes)

O AsyncStorage só guarda texto, então os favoritos vão com `JSON.stringify` e voltam com `JSON.parse`: "o mesmo JSON [...] entre o backend e frontend". Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## No JStack, aula 05

Em [[wiki/sources/jstack-criando-a-primeira-rota-da-api]], `response.end(JSON.stringify(users))` com `Content-Type: application/json`, porque `end` não aceita array (aceita string ou Buffer). JSON é UTF-8 por definição, então "José" não precisa de `charset`.

Em [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]], JSON "basicamente são arrays, objetos" que vêm do back-end para o front-end mostrar. É texto com essa sintaxe; precisa de `JSON.parse` (ou `response.json()`) para virar objeto.

Em [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]], os dados do back-end "vão voltar em forma de objeto, seja em XML, seja em JSON". Chegam como texto e precisam de parse antes de virar array de objetos.

## No FrontPUSH, JavaScript aula 11

Em [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]], [[wiki/entities/nasser|Násser]] dedica a aula ao JSON como "linguagem unificada" entre front-end e back-end, com a analogia do inglês que o mundo todo aprendesse. Mostra a sintaxe num `produto.json` (array de objetos, aspas duplas, sem vírgula final, objeto e array aninhados) e o par `JSON.parse` ("transforma o texto JSON em objeto") e `JSON.stringify`. Esquece o `null` entre os tipos e chama o JSON de "linguagem de marcação"; a ideia de que o texto precisa estar "em uma linha" vem da string do JavaScript, não do JSON. Não entram `undefined`, funções, `Symbol` e `BigInt` (`TypeError`; `[skill: lang-dynamic]`).

## No FrontPUSH, JavaScript aula 12

Em [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]], a requisição HTTP "me devolve um JSON", que outra tarefa "transforma em um objeto". Esperar a resposta é assíncrono; o `JSON.parse` em si é síncrono ([[wiki/concepts/javascript-assincrono]]).

## No FrontPUSH, JavaScript aula 13

Em [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]], a API de tempo devolve "o JSON com essas informações" e a do GitHub "um arquivo do tipo JSON" com login, ID e node ID. Numa API o JSON é o corpo da resposta (`Content-Type: application/json`), não um arquivo.

## No FrontPUSH, JavaScript aula 14

Em [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]], a resposta da API do GitHub chega "como um texto" em `XHR.responseText` e vira objeto com `JSON.parse`, como na [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back|aula 11]]. Com `xhr.responseType = "json"` ou `response.json()` do fetch, o parse é automático ([[wiki/concepts/xmlhttprequest]]).

## No FrontPUSH, JavaScript aula 15

Em [[wiki/sources/frontpush-promises-resolve-reject-then-catch]], o `resolve` recebe `JSON.parse(XHR.responseText)`, e o `then` já ganha o objeto pronto.

## No FrontPUSH, JavaScript aula 16

Em [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]], o `JSON.parse` some: o Axios converte o corpo sozinho e entrega em `response.data`.

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: JSON x objeto JavaScript, resposta do IBGE
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: package.json como JSON
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: JSON como contrato entre API, React e React Native
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: body JSON e serialização
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: JSON x objeto JavaScript
- [[wiki/sources/jstack-http-e-apis-rest]]: JSON como body e representação; sem binário
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: JSON como formato da API REST
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: JSON no AsyncStorage
- [[wiki/sources/jstack-criando-a-primeira-rota-da-api]]: JSON.stringify no response.end
- [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]]: FrontPUSH, JavaScript aula 06: JSON do back-end como motivo para estudar arrays
- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: XML ou JSON vindos do back-end
- [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]]: FrontPUSH, JavaScript aula 11: linguagem unificada, sintaxe, parse e stringify
- [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]]: FrontPUSH, JavaScript aula 12: JSON na resposta da requisição assíncrona
- [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]]: FrontPUSH, JavaScript aula 13: JSON como resposta da API
- [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]]: FrontPUSH, JavaScript aula 14: JSON.parse(XHR.responseText)
- [[wiki/sources/frontpush-promises-resolve-reject-then-catch]]: FrontPUSH, JavaScript aula 15: JSON.parse dentro do resolve
- [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]]: FrontPUSH, JavaScript aula 16: parse automático do Axios
