---
type: concept
title: "Query string"
aliases: ["query string", "query strings", "parâmetros de URL", "req.query", "URLSearchParams"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 8
tags: [http, url, formulario, backend, web]
skill: lang-dynamic
status: stub
---

# Query string

É a parte da [[wiki/concepts/url|URL]] depois do `?`: pares `chave=valor` separados por `&`, com codificação percentual (espaço vira `+` ou `%20`, vírgula vira `%2C`).

É onde um formulário com `method="get"` põe os campos, usando o `name` de cada input. No navegador, `URLSearchParams` lê esses pares; no [[wiki/entities/express]], eles chegam em `req.query`. Servem para busca, filtros e paginação.

Não são lugar para dado sensível: a URL fica no histórico, em logs e no cabeçalho `Referer`. Para cadastros, usa-se POST com o dado no corpo. Ver [[wiki/concepts/metodos-http]].

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] lê em voz alta a URL do cadastro enviado por GET (`?name=...&image=...&uf=15&state=Pará...`): "o nome disso aqui é query strings". Mostra `req.query` no terminal.

Depois muda o formulário para POST, porque "não é assim que a gente faz, que a gente envia formulários pela internet". A busca por cidade continua em GET: `req.query.search`.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: `?search=on` filtra uma lista e `?city=Rio do Sul&uf=SC&items=1,2` filtra os pontos. Query params são "opcionais, para filtros, paginação" e podem se repetir e virar array. Ver [[wiki/concepts/parametros-de-requisicao]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], `api.get('points', { params: { city, uf, items } })` vira `items[]=1&items[]=2`, e o filtro do back-end só funciona porque o `qs` do Express 4 o converte em array.

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], o formulário sem `action` envia para a própria página; por ser `get` por padrão, os campos aparecem na URL: "ele adicionou isso daqui".

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], os filtros da página study chegam como `?subject=1&weekday=0&time=08%3A00` ("%3A é a substituição [...] dos dois pontinhos") e o Express os entrega em `req.query`, um objeto vazio quando não há filtro. O cadastro de give-classes também vai pela query string, o que Mayk diz ser "ruim deixar dados expostos assim".

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], o redirect monta `?subject=...&weekday=...&time=...` concatenando `req.body` à mão; os valores são números e horas, mas texto livre pediria `URLSearchParams` ou `encodeURIComponent`. A busca lê os mesmos nomes em `req.query`.

## Na NLW #2, dia 2 (Diego Fernandes)

`GET /classes?week_day=1&subject=Matemática&time=9:00`; o Insomnia monta a query pela aba Query. O valor chega como string (daí `Number(week_day)`) e pode chegar como array. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## Na NLW #2, dia 3 (Diego Fernandes)

No Axios, os filtros do GET vão em `{ params: { subject, week_day, time } }`, porque o segundo argumento direto só vale para POST/PUT. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## Key sources

- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: req.query no Express; GET x POST no formulário do Ecoleta
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: filtros e paginação; repetição vira array
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: arrays em query string por acaso compatíveis
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: form sem action manda os campos na URL
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: req.query nos filtros e no cadastro
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: query string montada para o redirect
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: filtros de aulas na query
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: params do Axios
