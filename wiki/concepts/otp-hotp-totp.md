---
type: concept
title: "OTP — HOTP e TOTP"
aliases: ["one-time password", "HOTP", "TOTP", "código de seis dígitos", "app autenticador"]
date_created: 2026-07-27
date_updated: 2026-08-03
source_count: 2
tags: [otp, hotp, totp, mfa, autenticacao, seguranca]
skill: tech-mentor-security
status: draft
---

# OTP — HOTP e TOTP

Senha de uso único (One-Time Password), gerada a partir de uma *seed* secreta compartilhada entre cliente e servidor. É o mecanismo por trás do fator "algo que você tem" em [[wiki/concepts/mfa-multifator-autenticacao|MFA]].

## Geração 1 — proprietária (RSA SecurID)

Token de hardware com seed gravada de fábrica + relógio interno. Servidor guarda cópia da seed. A cada 30-60s, código de 6 dígitos = f(seed, tempo atual). Problemas: seed vazada = token clonável; exige relógio sincronizado entre dispositivo e servidor. Ver [[wiki/entities/rsa-security]].

## HOTP (2005, IETF RFC 4226)

Troca o relógio por um **contador**. A cada uso, o token e o servidor incrementam o mesmo contador — código = f(seed, contador). Elimina o problema de sincronização de relógio, mas desalinha se o token é usado sem o servidor saber (ex.: apertar o botão sem logar).

## TOTP (IETF RFC 6238) — padrão dos apps autenticadores

Volta a usar o **tempo** como HOTP de primeira geração, mas agora com especificação pública em vez de segredo proprietário. Quando você escaneia o QR Code de um serviço, o que é transferido é a seed secreta. A partir daí:

```
código = TOTP(seed, tempo_atual)
```

Calculado independentemente no app e no servidor — eles não trocam mensagens, só precisam concordar sobre a hora atual e a seed.

## TOTP É Vulnerável a Phishing

Diferente de [[wiki/concepts/webauthn-fido2-u2f|WebAuthn]], o código TOTP não é vinculado ao domínio do site. Um site falso pode simplesmente pedir o código de 6 dígitos e repassá-lo em tempo real ao site real (phishing man-in-the-middle) — a vítima digita o código válido no lugar errado, e o atacante o usa antes que expire. É a principal limitação do TOTP frente a métodos baseados em criptografia de chave pública.

## Relação com outros conceitos

- [[wiki/concepts/mfa-multifator-autenticacao]] — OTP é uma implementação do fator "algo que você tem"
- [[wiki/entities/rsa-security]] — geração proprietária que antecedeu o padrão IETF
- [[wiki/entities/ietf]] — órgão que padronizou HOTP e TOTP
- [[wiki/concepts/webauthn-fido2-u2f]] — evolução seguinte, baseada em criptografia assimétrica em vez de segredo compartilhado

## Key Sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] — vulnerabilidade do TOTP a phishing, em contraste com WebAuthn
