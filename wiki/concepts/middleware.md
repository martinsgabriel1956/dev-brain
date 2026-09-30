---
type: concept
title: "Middleware"
aliases: ["middlewares", "pedágio da requisição"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
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

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — middleware como pedágio
