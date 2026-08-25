---
type: entity
title: "IETF — Internet Engineering Task Force"
aliases: ["Internet Engineering Task Force"]
date_created: 2026-07-27
date_updated: 2026-08-24
source_count: 2
tags: [ietf, padronizacao, rfc, autenticacao, oauth2]
skill: tech-mentor-security
status: stub
---

# IETF — Internet Engineering Task Force

Organização responsável por padronizar protocolos de internet via RFCs. No histórico de autenticação, padronizou o [[wiki/concepts/otp-hotp-totp|HOTP]] (RFC 4226, 2005) — que eliminou a dependência de relógio sincronizado dos tokens de hardware proprietários como o [[wiki/entities/rsa-security|SecurID]] ao basear o código em um contador — e depois o TOTP (RFC 6238), que reintroduziu o tempo como base, mas de forma pública e especificada, ao invés de um segredo proprietário.

## Publicação do OAuth 1.0 e OAuth 2.0

Publicou a **RFC 5849** (abril de 2010), especificando o [[wiki/concepts/oauth2|OAuth]] 1.0 — versão complexa (assinatura criptográfica por requisição) que caiu em desuso — e depois a **RFC 6749** (2012), o OAuth 2.0, que se tornou o padrão de fato de autorização delegada na indústria. Ver [[wiki/sources/historia-oauth2-antipadrao-senha-bernardo-lobato]].

## Key sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
- [[wiki/sources/historia-oauth2-antipadrao-senha-bernardo-lobato]] — publicação da RFC 5849 (OAuth 1.0) e RFC 6749 (OAuth 2.0)
