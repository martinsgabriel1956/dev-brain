---
type: source
title: "Auth Avançado — Sessions, MFA, WebAuthn/Passkeys e Workload Identity"
aliases: ["sessions", "server side sessions", "jwt stateless", "redis sessions", "auth avancado"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/sessions.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [sessions, redis, jwt, mfa, totp, webauthn, passkeys, spiffe, workload-identity, auth]
skill: tech-mentor-security
status: stable
---

## TL;DR

JWT stateless: impossível revogar antes do TTL. Sessions server-side com Redis: revogação imediata ao custo de state. MFA TOTP: mínimo aceitável. WebAuthn/Passkeys: padrão futuro sem senha, phishing-resistant. Workload Identity via SPIFFE/SPIRE: serviço-a-serviço sem segredos compartilhados, certificados X.509 com TTL de horas.

## Key Claims

**Claim:** JWT stateless é irrevogável antes do TTL — Session + Redis permite revogação imediata.
**Evidence:** JWT: token válido por 1h. Se usuário for banido ou credencial comprometida, o token continua válido por até 1h. Sem como invalidar. Session + Redis: `DEL session:{sessionId}` no Redis invalida imediatamente. Todas as requisições checam o Redis → session não existe → 401. Custo: Redis como dependência de disponibilidade para autenticação.
**Confidence:** alta

**Claim:** SPIFFE/SPIRE resolve autenticação serviço-a-serviço sem segredos compartilhados — certificados rotacionados automaticamente.
**Evidence:** Sem SPIFFE: `order-service` usa `API_KEY=abc123` para autenticar no `payment-service`. Se vazado, acesso permanente. Com SPIFFE: cada workload recebe SVID (X.509) com identidade `spiffe://cluster.local/ns/prod/sa/order-service`. TTL: 1h. SPIRE Agent rotaciona automaticamente. mTLS entre serviços com identidade verificável sem segredos na config.
**Confidence:** alta

**Claim:** MFA com TOTP é o mínimo aceitável — mas ainda phishable em real-time MITM. Passkeys resolvem isso.
**Evidence:** TOTP: código de 6 dígitos a cada 30s. Phishing sofisticado: site falso captura TOTP em tempo real e usa imediatamente. WebAuthn: challenge vinculado ao domínio — `paypa1.com` não consegue usar credencial de `paypal.com`. Para sistemas com dados sensíveis, investir em passkeys elimina o vetor de phishing completamente.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/session-management]]
- [[concepts/jwt]]
- [[concepts/redis]]
- [[concepts/mfa]]
- [[concepts/totp]]
- [[concepts/passkeys]]
- [[concepts/spiffe]]
- [[entities/spire]]

## Open Questions

- Sessions em microserviços com múltiplos serviços — como compartilhar sessão entre serviços sem criar acoplamento no Redis?
- JWT com short TTL (5min) + refresh token long TTL — é equivalente a sessions em termos de segurança?
