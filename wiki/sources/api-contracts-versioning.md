---
type: source
title: "API Contracts e Versioning"
aliases: ["api contracts", "api versioning", "typespec", "openapi", "backward compatible"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/api-contracts-versioning.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [api-contracts, api-versioning, typespec, spectral, openapi, breaking-changes, sunset-policy, microcks, consumer-driven]
skill: tech-mentor-backend
status: stable
---

## TL;DR

API contract é o contrato formal entre produtor e consumidor — define o que muda é breaking change. TypeSpec gera OpenAPI de forma agnóstica. Spectral faz linting de contratos. Estratégias de versioning: URL path (/v1/), header, content negotiation. Sunset Policy (RFC 8594) para deprecação com prazo. Microcks para contract testing em CI.

## Key Claims

**Claim:** Breaking changes vs non-breaking — a distinção define se o versioning é necessário.
**Evidence:** Non-breaking (backward compatible): adicionar campo opcional, novo endpoint, novo valor em enum não obrigatório. Breaking: remover campo, mudar tipo, mudar semântica de campo existente, remover endpoint. Breaking change = nova versão major.
**Confidence:** alta

**Claim:** TypeSpec é a abordagem design-first mais agnóstica — gera OpenAPI, gRPC, JSON Schema a partir de uma spec.
**Evidence:** Microsoft TypeSpec define a API em DSL agnóstica de protocolo. Emitters geram OpenAPI 3.x, .proto, JSON Schema. Evita manter múltiplos formatos sincronizados manualmente.
**Confidence:** média-alta

**Claim:** Sunset Policy (RFC 8594) é o padrão para deprecação com prazo definido.
**Evidence:** Header `Sunset: Sat, 01 Jan 2027 00:00:00 GMT` informa quando a versão será desativada. Permite que consumidores planejem migração. Documentar em OpenAPI via `x-sunset` extension.
**Confidence:** alta

**Claim:** Microcks permite contract testing automatizado em CI — mock server + validator.
**Evidence:** Importa OpenAPI, gera mock server automaticamente. Roda contract tests contra a implementação real. Detecta breaking changes em PRs antes de merge.
**Confidence:** média

## Entities & Concepts Touched

- [[concepts/api-versioning]]
- [[concepts/breaking-changes]]
- [[concepts/contract-testing]]
- [[concepts/sunset-policy]]
- [[entities/typespec]]

## Open Questions

- Como versionar APIs em GraphQL onde o schema é evolutivo por natureza?
- Sunset policy — o que fazer quando consumidores ignoram o header e continuam usando após o prazo?
