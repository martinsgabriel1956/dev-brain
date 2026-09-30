---
type: concept
title: "Recurso (REST)"
aliases: ["resource", "pensar em recursos", "rest resource"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [rest, api, recurso, design-de-api]
skill: tech-mentor-networking
status: stub
---

# Recurso (REST)

Ideia central de uma API REST: a URL identifica um **recurso** (`/usuarios/42`) e o [[wiki/concepts/metodos-http|método]] expressa o que fazer com ele. Mentalidade: "qual recurso estou acessando?" em vez de "qual função chamo?" — isso torna REST intuitivo.

Relacionado: [[wiki/concepts/requisicao-http]], [[wiki/concepts/contrato-de-api]], [[wiki/concepts/api-versioning]].

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — mudança de mentalidade função → recurso
