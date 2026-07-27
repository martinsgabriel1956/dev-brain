---
type: entity
title: "RSA Security"
aliases: ["RSA SecurID", "SecurID"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [rsa-security, mfa, token-de-hardware, seguranca]
skill: tech-mentor-security
status: stub
---

# RSA Security

Empresa responsável pelo SecurID, o token de hardware que popularizou comercialmente em grande escala o segundo fator de autenticação nos anos 90. Cada token vinha gravado de fábrica com uma *seed* secreta e um relógio interno sincronizado com o servidor; a cada 30-60 segundos calculava um código de seis dígitos a partir da seed e do tempo atual — o antecessor direto do [[wiki/concepts/otp-hotp-totp|TOTP]] usado hoje em apps autenticadores.

Duas fragilidades motivaram a padronização posterior pela [[wiki/entities/ietf]]: (1) se a seed vazasse, o token era clonável; (2) dependia de relógio sincronizado entre dispositivo e servidor, algo operacionalmente difícil em escala.

## Key sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
