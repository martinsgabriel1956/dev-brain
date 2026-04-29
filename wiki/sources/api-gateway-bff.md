---
type: source
title: "API Gateway & BFF"
aliases: ["api gateway", "bff", "backend for frontend", "api gateway bff", "aggregation layer"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/api-gateway-bff.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [api-gateway, bff, backend-for-frontend, aggregation, rate-limiting, service-mesh, north-south-traffic]
skill: tech-mentor-backend
status: stable
---

## TL;DR

API Gateway controla tráfego norte-sul (externo → sistema): authn/authz, rate limiting, routing. BFF (Backend for Frontend) é um backend dedicado por tipo de cliente (Web, Mobile, Parceiro) que agrega chamadas a serviços internos e entrega exatamente o que aquele cliente precisa. API Gateway ≠ Service Mesh: gateway controla o que entra, mesh controla tráfego interno (leste-oeste). BFF resolve over-fetching e under-fetching sem mudar os serviços internos.

## Key Claims

**Claim:** BFF por tipo de cliente resolve over-fetching e under-fetching sem exigir mudanças nos serviços internos.
**Evidence:** API genérica retorna 40 campos, mobile usa 8 (over-fetching). Montar tela de resumo exige 4 chamadas separadas (under-fetching). BFF Mobile: `Promise.all([usuarioService.buscarPerfil(), pedidosService.listarRecentes(), saldo()])` → uma chamada do cliente, múltiplas internas, resposta formatada para aquela tela. Serviços internos permanecem genéricos; cada BFF adapta para seu cliente.
**Confidence:** alta

**Claim:** API Gateway e Service Mesh são complementares — gateway para norte-sul, mesh para leste-oeste.
**Evidence:** API Gateway (Kong, AWS API GW, Traefik): borda do sistema, tráfego externo. Responsabilidades: authn/authz, rate limiting, routing, SSL termination. Service Mesh (Istio, Linkerd): dentro do cluster, tráfego entre serviços. Responsabilidades: mTLS, circuit breaking, retries, observabilidade. Erro comum: tentar fazer o API Gateway fazer circuit breaking entre serviços internos — isso é responsabilidade do mesh.
**Confidence:** alta

**Claim:** Rate limiting no API Gateway deve ser por usuário/token, não por IP — IP-based rate limiting é trivialmente contornável.
**Evidence:** IP-based: usuário com muitos IPs (NAT, VPN, proxies) não é limitado; usuário legítimo atrás de NAT corporativo é limitado injustamente. Token-based: limita por `Authorization` header ou API key — identifica o consumidor real. Sliding window em Redis: `INCR user:{id}:window:{minute}` com TTL. Retornar `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` para transparência.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/api-gateway]]
- [[concepts/bff-pattern]]
- [[concepts/rate-limiting]]
- [[concepts/north-south-traffic]]
- [[concepts/east-west-traffic]]
- [[concepts/service-mesh]]
- [[concepts/aggregation-layer]]

## Open Questions

- BFF vs GraphQL — quando GraphQL elimina a necessidade de múltiplos BFFs?
- API Gateway como single point of failure — estratégias de HA e fallback quando o gateway cai?
