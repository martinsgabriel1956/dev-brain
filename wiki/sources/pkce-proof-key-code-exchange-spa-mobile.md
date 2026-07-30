---
type: source
title: "PKCE — Como Proteger Autenticação em SPAs e Apps Mobile"
aliases: ["pkce", "proof key for code exchange", "code_verifier", "code_challenge", "rfc 7636"]
date_created: 2026-07-30
date_updated: 2026-07-30
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/pkce-proof-key-code-exchange-spa-mobile.md
source_url: ""
author: "Bernardo Lobato"
date_published: ""
date_ingested: 2026-07-30
source_count: 0
tags: [pkce, oauth2, oidc, implicit-flow, authorization-code, code-verifier, code-challenge, rfc-7636, oauth2-1, bff, mtls, dpop, seguranca]
skill: tech-mentor-security
status: stable
---

## TL;DR

PKCE (RFC 7636, 2015) resolve o problema de client secret dinâmico para clientes que não têm onde esconder segredo (SPA, mobile): o cliente gera um `code_verifier` aleatório, manda o hash dele (`code_challenge`) na etapa de autorização, e só revela o `code_verifier` na troca do authorization code por token — o Authorization Server valida reaplicando o hash. Substitui o Implicit Flow (deprecated, expunha token na URL) e, no OAuth 2.1, é obrigatório para todos os clients, inclusive backends robustos.

## Key Claims

**Claim:** O Implicit Flow falhou porque expunha access token e dados de controle diretamente na URL de redirecionamento.
**Evidence:** Token no fragmento da URL fica salvo no histórico do navegador; é interceptável por extensões maliciosas, proxies e apps espiões (man-in-the-middle); por ser canal inseguro, boas práticas proibiam refresh tokens nesse fluxo, forçando reautenticação frequente; e, principalmente, o servidor não tinha como provar que quem recebia o token era quem tinha iniciado o pedido (falta de prova de posse).
**Confidence:** alta — consistente com [[wiki/concepts/oauth2]] e com [[wiki/sources/oauth2-oidc-jwt]], que já documentam o Implicit Flow como deprecated.

**Claim:** PKCE resolve o problema do client secret estático em clientes públicos usando um par `code_verifier`/`code_challenge` descartável a cada tentativa de login.
**Evidence:** Passo a passo: (1) client gera `code_verifier` (string randômica grande); (2) aplica hash SHA-256 → `code_challenge`; (3) envia `code_challenge` + credenciais de login ao Authorization Server; (4) Authorization Server armazena o `code_challenge`; (5) usuário autentica, recebe `authorization_code`; (6) client troca o `authorization_code` pelo token enviando agora o `code_verifier` original; (7) Authorization Server reaplica o hash e compara — bate, libera token; não bate, `401`. Mesmo que um atacante intercepte o `authorization_code`, não consegue trocá-lo por token sem o `code_verifier` correspondente.
**Confidence:** alta — mecanismo técnico verificável e consistente com a implementação documentada em `references/identity-iam.md` do skill tech-mentor-security (`code_challenge_method=S256`, exchange com `code_verifier`).

**Claim:** No OAuth 2.1, PKCE é obrigatório para todos os clients — não só para clientes públicos — inclusive backends robustos.
**Evidence:** O nome original do RFC 7636 é "Proof Key for Code Exchange by OAuth Public Clients", focado inicialmente em clientes públicos (SPA, mobile), mas a recomendação evoluiu para uso universal no OAuth 2.1, mesmo quando o cliente já tem capacidade de guardar segredo.
**Confidence:** alta — confirma o que já está registrado em [[wiki/sources/identity-iam-avancado]] ("PKCE obrigatório para todos os flows, não só public clients") e em [[wiki/sources/oauth2-oidc-jwt]].

**Claim:** DPoP, mTLS e BFF são alternativas/complementos ao PKCE para prova de posse em clientes complexos.
**Evidence:** Citados de passagem como opções que evoluíram com foco em clientes mais independentes do backend — sem detalhamento técnico no vídeo (promete vídeos futuros dedicados, incluindo um sobre arquitetura BFF stateless/stateful híbrida).
**Confidence:** média-baixa — apenas nomeados, sem mecanismo explicado nesta fonte; mecanismo de cada um já documentado em [[wiki/concepts/bff-pattern]] (não no contexto de auth) e no skill tech-mentor-security (`references/identity-iam.md`, seção DPoP).

## Entities & Concepts Touched

- [[wiki/concepts/pkce]]
- [[wiki/concepts/oauth2]]
- [[wiki/concepts/bff-pattern]]
- [[wiki/entities/bernardo-lobato]]

## Open Questions

- O vídeo promete um vídeo futuro detalhando BFF stateless vs. stateful como solução híbrida para o mesmo problema de proof-of-possession — ainda não ingerido nesta wiki.
- DPoP e mTLS são citados só pelo nome nesta fonte, sem mecanismo explicado — mecanismo já coberto no skill (`identity-iam.md`), mas ainda sem fonte de vídeo dedicada na wiki para justificar página própria de DPoP.
