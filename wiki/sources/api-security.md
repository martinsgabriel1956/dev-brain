---
type: source
title: "API Security"
aliases: ["api security", "bola idor", "rate limiting api", "graphql security", "grpc security"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/api-security.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [api-security, bola, idor, mass-assignment, rate-limiting, sliding-window, graphql-security, grpc-security, credential-stuffing]
skill: tech-mentor-security
status: stable
---

## TL;DR

API Security é o subconjunto do OWASP focado em APIs. BOLA (IDOR) é o #1 — verificar `user_id` em toda query por ID. Rate limiting é defesa contra brute force e credential stuffing — sliding window com Redis. GraphQL: depth limiting + query complexity. gRPC: mTLS para service-to-service + interceptor de authn.

## Key Claims

**Claim:** BOLA é o vuln #1 em APIs — ausência de verificação de ownership por objeto.
**Evidence:** `GET /orders/456` sem `WHERE user_id = req.user.id` permite que qualquer usuário autenticado acesse o pedido de qualquer outro usuário. Solução: toda query por ID deve incluir `AND user_id = $currentUserId`.
**Confidence:** alta

**Claim:** Sliding Window é o algoritmo de rate limiting mais preciso para APIs.
**Evidence:** Fixed Window tem burst no boundary (99 req no final do minuto + 99 no início = 198 em 2 segundos). Sliding Window calcula a janela a partir do timestamp do primeiro request — sem burst. Trade-off: mais memória (guarda timestamp de cada request).
**Confidence:** alta

**Claim:** Credential stuffing contorna rate limit por IP — requer defesa em camadas.
**Evidence:** Atacantes usam milhares de IPs diferentes (botnets). Rate limit por IP não ajuda. Defesas adicionais: device fingerprinting, análise comportamental (taxa de sucesso baixa = stuffing), serviços especializados (Cloudflare Bot Management).
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/bola]]
- [[concepts/idor]]
- [[concepts/rate-limiting]]
- [[concepts/sliding-window-rate-limit]]
- [[concepts/credential-stuffing]]
- [[concepts/graphql-security]]
- [[concepts/owasp]]

## Open Questions

- Como implementar rate limiting granular por usuário + IP + endpoint sem criar muitas keys no Redis?
- GraphQL persisted queries como defesa de segurança — como implementar sem quebrar desenvolvimento?
