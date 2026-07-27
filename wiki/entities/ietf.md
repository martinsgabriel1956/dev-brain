---
type: entity
title: "IETF — Internet Engineering Task Force"
aliases: ["Internet Engineering Task Force"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [ietf, padronizacao, rfc, autenticacao]
skill: tech-mentor-security
status: stub
---

# IETF — Internet Engineering Task Force

Organização responsável por padronizar protocolos de internet via RFCs. No histórico de autenticação, padronizou o [[wiki/concepts/otp-hotp-totp|HOTP]] (RFC 4226, 2005) — que eliminou a dependência de relógio sincronizado dos tokens de hardware proprietários como o [[wiki/entities/rsa-security|SecurID]] ao basear o código em um contador — e depois o TOTP (RFC 6238), que reintroduziu o tempo como base, mas de forma pública e especificada, ao invés de um segredo proprietário.

## Key sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
