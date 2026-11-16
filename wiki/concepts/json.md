---
type: concept
title: "JSON (JavaScript Object Notation)"
aliases: ["JSON", "JavaScript Object Notation", "res.json()"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
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

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: JSON x objeto JavaScript, resposta do IBGE
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: package.json como JSON
