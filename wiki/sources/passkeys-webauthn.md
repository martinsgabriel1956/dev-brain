---
type: source
title: "Passkeys & WebAuthn"
aliases: ["passkeys", "webauthn", "fido2", "passkey registration", "passkey authentication", "simplewebauthn"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/passkeys-webauthn.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [passkeys, webauthn, fido2, phishing-resistant, biometria, asymmetric-key, simplewebauthn]
skill: tech-mentor-security
status: stable
---

## TL;DR

Passkeys (WebAuthn/FIDO2): autenticação phishing-resistant sem senha. Chave privada fica no dispositivo (Secure Enclave/TPM), nunca sai. Challenge é vinculado à origem (domínio) — impossível de usar em site falso. Biblioteca `@simplewebauthn/server` para backend Node.js. Schema: tabela `passkey_credentials` com `credential_id`, `public_key`, `counter`. UX: biometria nativa (Face ID, fingerprint).

## Key Claims

**Claim:** Passkeys são phishing-resistant por design — challenge é vinculado ao RP ID (domínio), não funciona em domínio diferente.
**Evidence:** Phishing clássico: site falso `paypa1.com` captura usuário/senha ou TOTP. WebAuthn: authenticator verifica que o challenge foi gerado por `paypal.com` (RP ID). Em `paypa1.com`, o authenticator rejeita silenciosamente — credencial do site correto não funciona em domínio diferente. Ataque de phishing é fisicamente impossível.
**Confidence:** alta

**Claim:** Chave privada nunca sai do dispositivo — servidor armazena apenas a chave pública.
**Evidence:** Registro: dispositivo gera par EC P-256. Chave privada: armazenada no Secure Enclave (iOS) ou TPM (Android/Windows). Chave pública: enviada ao servidor e armazenada. Autenticação: dispositivo assina o challenge com chave privada. Servidor verifica a assinatura com chave pública. Mesmo que servidor seja comprometido, chave privada não vaza.
**Confidence:** alta

**Claim:** `counter` previne ataques de replay de authenticators clonados — incrementa a cada uso.
**Evidence:** Authenticator mantém contador de uso. Server armazena o valor anterior. Na autenticação, se `counter_atual <= counter_armazenado`, o server rejeita — indica authenticator clonado (dois devices usando a mesma chave). Passkeys sincronizadas (iCloud Keychain, Google Password Manager) desativam counter (todos os devices compartilham a mesma chave).
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/passkeys]]
- [[concepts/webauthn]]
- [[concepts/fido2]]
- [[concepts/phishing-resistant]]
- [[concepts/secure-enclave]]
- [[entities/simplewebauthn]]

## Open Questions

- Passkeys em enterprise com dispositivos corporativos gerenciados — como lidar com backup e recuperação de acesso quando o dispositivo é trocado?
- WebAuthn com enterprise SSO (SAML/OIDC) — como integrar passkeys como segundo fator em fluxos de federação existentes?
