---
type: concept
title: "Middleware"
aliases: ["middlewares", "pedágio da requisição"]
date_created: 2026-09-30
date_updated: 2026-11-16
source_count: 3
tags: [backend, http, middleware, autenticacao, validacao]
skill: tech-mentor-networking
status: stub
---

# Middleware

Camada entre a **rota** e o **controller** por onde a [[wiki/concepts/requisicao-http]] passa antes de chegar à regra de negócio — "um pedágio no meio do caminho". Verificações típicas:

- o token de autenticação é válido? ([[wiki/concepts/jwt]], [[wiki/concepts/autenticacao-e-autorizacao]])
- o usuário tem permissão para esta rota?
- o corpo está no formato esperado?

Se falhar, o servidor responde já ali ([[wiki/concepts/http-status-code|401/403]]), e o código do controller/service nunca executa — explicação comum para "a requisição parece certa mas não chega no meu código".

Fluxo: rota → middleware → controller → service → banco ([[wiki/concepts/arquitetura-em-3-camadas]]). Outros usos comuns [external]: logging, [[wiki/concepts/rate-limiting]], CORS ([[wiki/concepts/cors]]), parsing de body.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]], `app.use(express.json())` é "como se fosse [...] um plugin": sem ele, o `request.body` chega vazio. `cors()` e `express.static` também entram por `app.use`.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]], a rota encadeia `upload.single('image')`, `celebrate(...)` e o controller. A ordem importa: o Multer grava o arquivo antes da validação recusar o body.

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — middleware como pedágio
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: app.use como "plugin": express.json, cors, static
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: ordem upload → validação → controller
