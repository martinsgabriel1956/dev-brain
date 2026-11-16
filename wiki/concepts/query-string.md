---
type: concept
title: "Query string"
aliases: ["query string", "query strings", "parâmetros de URL", "req.query", "URLSearchParams"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
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

## Key sources

- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: req.query no Express; GET x POST no formulário do Ecoleta
