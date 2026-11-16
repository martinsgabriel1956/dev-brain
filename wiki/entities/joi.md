---
type: entity
title: "Joi (e celebrate)"
aliases: ["joi", "@hapi/joi", "celebrate", "Joi.object"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [validacao, nodejs, express, schema, biblioteca]
skill: lang-dynamic
status: stub
---

# Joi (e celebrate)

Biblioteca de validação de schema para JavaScript, nascida no ecossistema hapi: `Joi.object({ name: Joi.string().required(), email: Joi.string().email() })`. O **celebrate** a integra ao [[wiki/entities/express]] como [[wiki/concepts/middleware]] por segmento da requisição (`body`, `query`, `params`, `headers`, `cookies`), e o `errors()` formata as falhas como 400.

No Ecoleta ([[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]): o `celebrate({ body: Joi.object().keys({...}) }, { abortEarly: false })` fica entre o upload e o controller, e devolve todos os erros de uma vez ("Name is required, email is required..."). Para [[wiki/entities/diego-fernandes]], o celebrate "não se preocupa com as regras de validação", só integra o Joi ao Express. No front-end, ele indica o Yup, de API parecida.

**Notas:**

- **Pacote:** `@hapi/joi` voltou a ser `joi` e traz os próprios tipos, o que dispensou o `@types/hapi__joi` da aula `[external]` (https://github.com/hapijs/joi).
- **Hoje:** `[skill: lang-dynamic]` Zod (ou Valibot/ArkType via Standard Schema) dá um schema só para front e back, com tipos TypeScript inferidos. No Fastify, a validação nativa é JSON Schema.
- **Validar não é sanitizar:** regras como `uf: max(2)` aceitam "s" ou "sc". Ver [[wiki/concepts/validacao-de-entrada]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: validação do POST /points
