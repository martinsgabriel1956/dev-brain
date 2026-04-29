---
type: source
title: "OAuth2, OIDC e JWT"
aliases: ["oauth2", "oidc", "jwt", "authorization code pkce", "client credentials", "refresh token rotation"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/oauth2-oidc-jwt.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [oauth2, oidc, jwt, pkce, authorization-code, client-credentials, device-flow, refresh-token-rotation, session-management, jwks]
skill: tech-mentor-security
status: stable
---

## TL;DR

OAuth2: protocolo de autorização (delegação de acesso). OIDC: camada de autenticação sobre OAuth2 (quem é o usuário). Authorization Code + PKCE é o único flow correto para web/mobile. JWT: token auto-contido assinado — validar algoritmo, `exp`, `iss`, `aud`. Access Token curto (1h) + Refresh Token longo em httpOnly cookie.

## Key Claims

**Claim:** Authorization Code + PKCE é o único flow correto para SPAs e mobile em 2026.
**Evidence:** Implicit Flow: access token na URL (vulnerável a leaking no history/logs). Client Credentials: sem user context. Authorization Code + PKCE: code na URL (curto prazo), trocado por token via POST (server-to-server). PKCE impede que code interceptado seja usado sem o `code_verifier` original.
**Confidence:** alta

**Claim:** JWT deve ser validado em 5 dimensões — assinatura + algoritmo + exp + iss + aud.
**Evidence:** `alg: none` exploit: token sem assinatura aceito por libraries antigas. `exp` expirado: token válido indefinidamente. `iss` não validado: token de outro provedor aceito. `aud` não validado: token para outro cliente aceito. Todas as 5 verificações são obrigatórias.
**Confidence:** alta

**Claim:** Refresh Token Rotation é obrigatório para detecção de roubo de token.
**Evidence:** A cada uso do refresh token, um novo é emitido e o antigo é invalidado. Se o token roubado for usado: o legítimo também falha → detecção de comprometimento → revogar todos. Sem rotation: token roubado é válido indefinidamente.
**Confidence:** alta

**Claim:** Access Token em memória (não localStorage) + Refresh Token em httpOnly cookie é o padrão seguro para SPAs.
**Evidence:** localStorage: acessível via XSS. sessionStorage: perdido ao fechar aba. Memory: acessível apenas no JS da página atual, perdido ao recarregar (mas renovado via refresh token em httpOnly cookie). Sem httpOnly: XSS pode roubar o refresh token também.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/oauth2]]
- [[concepts/oidc]]
- [[concepts/jwt]]
- [[concepts/pkce]]
- [[concepts/refresh-token-rotation]]
- [[concepts/session-management]]

## Open Questions

- Como lidar com refresh token rotation em múltiplas abas simultâneas (race condition)?
- JWT Keys Rotation: como fazer rotação de chaves de assinatura sem invalidar tokens ativos?
