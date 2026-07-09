---
type: concept
title: "Post/Redirect/Get (PRG)"
aliases: ["PRG pattern", "redirect after post", "303 see other"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
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

## Key Sources

- [[wiki/sources/double-spend-double-submit]] — documento primário
