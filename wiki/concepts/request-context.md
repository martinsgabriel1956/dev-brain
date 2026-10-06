---
type: concept
title: "Request Context"
aliases: ["contexto da requisição", "request scope"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [request-context, backend, frameworks, debugging]
skill: tech-mentor-backend
status: draft
---

# Request Context

Padrão em que cada requisição agrupa seu contexto (usuário, ids, parâmetros) e o **passa adiante** a quem precisar, em vez de guardá-lo em global. Facilita logar, depurar e reproduzir ([[wiki/concepts/reprodutibilidade-de-bugs]]); muitos frameworks e codebases o adotam.

Frameworks request/response (FastAPI, Hono, Express) **induzem** a não compartilhar contexto entre requests: seguindo o tutorial, o dev tende a não cometer [[wiki/concepts/estado-global-em-servidor]]. Não é garantia.

Alternativa para esconder o contexto sem global: armazenamento por requisição (ex.: `AsyncLocalStorage` em Node; ver uso em multi-tenancy na skill) — **[external/skill, não coberto pelo vídeo]**. Relacionado: [[wiki/concepts/dependency-injection]], [[wiki/concepts/stateless]], [[wiki/concepts/requisicao-http]].

## Key sources

- [[wiki/sources/estado-global-stateless-side-effects-reprodutibilidade-galego]]
