---
type: concept
title: "WebAuthn, FIDO2 e U2F"
aliases: ["U2F", "Universal Second Factor", "WebAuthn", "FIDO2", "passkeys", "YubiKey"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [webauthn, fido2, u2f, passkeys, criptografia-assimetrica, mfa, autenticacao]
skill: tech-mentor-security
status: draft
---

# WebAuthn, FIDO2 e U2F

Linha evolutiva de autenticação por hardware baseada em **criptografia de chave pública** em vez de segredo compartilhado (como [[wiki/concepts/otp-hotp-totp|OTP]]). Resolve o problema estrutural do segredo compartilhado: se a seed do OTP vaza do servidor, o atacante pode gerar códigos válidos; se a chave privada nunca sai do dispositivo, vazar o servidor não compromete nada.

## U2F (2014)

Primeiro padrão comercial em dispositivos físicos (ex.: YubiKey).

```
Registro:
1. Dispositivo gera par de chaves exclusivo para aquele serviço
2. Chave pública é enviada e armazenada no servidor

Login:
1. Servidor envia um challenge (valor aleatório)
2. Dispositivo assina o challenge com a chave privada
3. Servidor verifica a assinatura com a chave pública armazenada
```

Mesmo princípio de prova-de-posse sem transmissão de segredo usado em [[wiki/concepts/ssh]] e descrito em [[wiki/concepts/criptografia]] (assinatura digital: assina com chave privada, verifica com chave pública).

**Por que é phishing-resistant**: o protocolo vincula o challenge à origem (domínio) do site. Um site falso não consegue obter uma assinatura válida porque o dispositivo verifica contra qual domínio está assinando.

## FIDO2 / WebAuthn / Passkeys

Evolução do U2F para um padrão W3C usável diretamente no browser, sem hardware dedicado — a chave privada pode ficar protegida por biometria ou PIN local no próprio dispositivo (ver [[wiki/concepts/mobile-biometria]]), não só em um token físico. "Passkey" é o nome comercial dado a essa credencial WebAuthn quando sincronizável entre dispositivos (iCloud Keychain, Google Password Manager).

## Por que supera senha e OTP

- Chave privada nunca sai do dispositivo — não vaza em breach de servidor
- Phishing-resistant por design (challenge vinculado ao domínio)
- Elimina credential stuffing — não há senha para reutilizar entre sites

## Relação com outros conceitos

- [[wiki/concepts/mfa-multifator-autenticacao]] — implementação do fator "algo que você tem"
- [[wiki/concepts/otp-hotp-totp]] — geração anterior, baseada em segredo compartilhado em vez de par de chaves
- [[wiki/concepts/mobile-biometria]] — biometria libera a chave privada localmente no dispositivo
- [[wiki/concepts/ssh]] — mesmo princípio de assinatura de challenge com chave privada, sem transmiti-la
- [[wiki/concepts/criptografia]] — fundamento de assinatura digital com par de chaves assimétrico

## Key Sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
