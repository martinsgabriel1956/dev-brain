---
type: source
title: "REST e OpenAPI 3.1 — Design, Contratos e API-First"
aliases: ["rest", "openapi", "openapi 3.1", "api first", "api design", "status codes", "hateoas", "sunset policy"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/rest-openapi.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [rest, openapi, api-design, api-first, status-codes, versioning, hateoas, sunset-policy, mock-server]
skill: tech-mentor-backend
status: stable
---

## TL;DR

REST: recursos via HTTP com semântica de verbos e status codes. OpenAPI 3.1: spec como contrato — API-First significa escrever a spec antes do código. Nomenclatura: substantivos plurais no plural (`/users`, `/orders`). Status codes semânticos: 200/201/204, 400/401/403/404/422, 500. Versionamento via URL path (`/v1/`). Sunset Policy (RFC 8594) para deprecação. HATEOAS é opcional na prática.

## Key Claims

**Claim:** API-First com OpenAPI inverte o fluxo — spec é o contrato compartilhado antes de qualquer implementação.
**Evidence:** Fluxo tradicional: implementa código → gera docs da implementação. API-First: escreve OpenAPI spec → time de frontend usa mock server (Prism) para integrar em paralelo → backend implementa contra a spec. Benefício: desacoplamento de equipes, contrato explícito, validação automática da implementação contra a spec.
**Confidence:** alta

**Claim:** Status codes semânticos corretos são essenciais — 400 vs 422 vs 500 têm semânticas distintas para clientes.
**Evidence:** 400 Bad Request: request malformada (JSON inválido, campo obrigatório ausente). 422 Unprocessable Entity: request válida mas regra de negócio violada (email já cadastrado). 401: não autenticado. 403: autenticado mas sem permissão. 404: recurso não existe. 500: erro interno — nunca expor detalhes. Clients implementam retry em 5xx, não em 4xx.
**Confidence:** alta

**Claim:** Sunset Policy (RFC 8594) é o padrão correto para deprecação de versões de API — comunica prazo para clientes.
**Evidence:** Header: `Sunset: Tue, 01 Jan 2026 00:00:00 GMT` + `Deprecation: true` + `Link: <https://api.example.com/v2/users>; rel="successor-version"`. Clientes que monitoram headers recebem aviso automático. Sem Sunset: clientes descobrem deprecação quando a versão para de funcionar. RFC 8594 é o padrão — documentado, previsível.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/rest]]
- [[concepts/openapi]]
- [[concepts/api-first]]
- [[concepts/api-versioning]]
- [[concepts/status-codes]]
- [[concepts/sunset-policy]]
- [[concepts/hateoas]]

## Open Questions

- OpenAPI 3.1 vs AsyncAPI para sistemas event-driven — como usar ambos em um sistema híbrido REST + Kafka?
- HATEOAS na prática — quais casos de uso realmente se beneficiam de hypermedia em vez de complicar o cliente?
