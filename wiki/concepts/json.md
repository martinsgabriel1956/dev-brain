---
type: concept
title: "JSON (JavaScript Object Notation)"
aliases: ["JSON", "JavaScript Object Notation", "res.json()"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 7
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

## Na NLW #2, dia 2 (Diego Fernandes)

"Um objeto escrito da mesma forma que a gente escreve no JavaScript", entendido por web e mobile; a lista é um array de objetos. Vírgula no fim do último item é erro em JSON. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## Na NLW #2, dia 5 (Diego Fernandes)

O AsyncStorage só guarda texto, então os favoritos vão com `JSON.stringify` e voltam com `JSON.parse`: "o mesmo JSON [...] entre o backend e frontend". Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: JSON x objeto JavaScript, resposta do IBGE
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: package.json como JSON
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: JSON como contrato entre API, React e React Native
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: body JSON e serialização
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: JSON x objeto JavaScript
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: JSON como formato da API REST
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: JSON no AsyncStorage
