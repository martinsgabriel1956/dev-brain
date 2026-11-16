---
type: concept
title: "Post/Redirect/Get (PRG)"
aliases: ["PRG pattern", "redirect after post", "303 see other"]
date_created: 2026-07-09
date_updated: 2026-11-16
source_count: 2
tags: [http, formularios, ux, double-submit]
skill: tech-mentor-backend
status: stub
---

# Post/Redirect/Get (PRG)

Padrão web onde, após um `POST` bem-sucedido, o servidor responde com um redirect (tipicamente `303 See Other`) para uma URL de `GET` em vez de renderizar a resposta diretamente.

```
POST /subscribe (email) → 303 See Other → GET /thank-you
```

Como o navegador não reenvia o `POST` original ao seguir o redirect, e o usuário sai da página do formulário, o padrão evita reenvio acidental de formulário (ex.: usuário aperta F5 na página de resposta, ou clica duas vezes no botão de submit) sem precisar de nenhuma lógica extra no servidor.

## Limitação

PRG só protege contra o usuário bem-intencionado navegando pelo browser. Não protege contra um cliente que reenvia o `POST` diretamente (script, `curl`, API client) ignorando o navegador — para isso é necessário [[wiki/concepts/idempotencia]] no servidor e/ou uma constraint de unicidade no banco.

## Quando é suficiente sozinho

Quando a duplicidade é inócua e facilmente identificável no banco (ex.: um cadastro em lista de e-mail, protegido por `email UNIQUE`), PRG combinado com uma unique constraint já resolve — não compensa a complexidade de uma Idempotency Key nesse cenário.

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], o cadastro do Ecoleta faz `res.render(..., { saved: true })` direto na resposta do POST. Um Ctrl+R pede "resubmeter o formulário" e insere de novo, e [[wiki/entities/mayk-brito|Mayk Brito]] usa isso como atalho para testar. É o caso de manual para PRG: `res.redirect(303, '/create-point?saved=1')`.

## Key Sources

- [[wiki/sources/double-spend-double-submit]] — documento primário
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: POST sem redirect no Ecoleta: reload duplica
