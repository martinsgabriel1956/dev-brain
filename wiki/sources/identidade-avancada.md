---
type: source
title: "Identidade Avançada — SSO, MFA, Workload Identity, IAM, Casbin, SCIM"
aliases: ["identidade avancada", "sso", "mfa totp", "passkeys webauthn", "workload identity spiffe", "casbin", "jit access"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/identidade-avancada.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [sso, mfa, totp, passkeys, webauthn, workload-identity, spiffe, spire, casbin, scim, jit-access]
skill: tech-mentor-security
status: stable
---

## TL;DR

Identidade avançada: SSO com OIDC/SAML para autenticação centralizada. MFA: TOTP como baseline, WebAuthn/Passkeys como gold standard (phishing-resistant). SPIFFE/SPIRE para workload identity em K8s. IAM Just-in-Time: zero standing privilege — acesso temporário aprovado por demanda. Casbin como policy engine flexível. SCIM para provisionamento automático.

## Key Claims

**Claim:** Passkeys (WebAuthn) são phishing-resistant — TOTP não é, SMS não é.
**Evidence:** TOTP: usuário pode ser phished para digitar o código em site falso (real-time MITM). SMS: SIM swapping. Passkeys: challenge é vinculado à origem (domínio) do site — chave privada nunca sai do dispositivo, impossível de phish em site diferente. FIDO2/WebAuthn é o único MFA que elimina phishing de credenciais.
**Confidence:** alta

**Claim:** SPIFFE/SPIRE fornece identidade criptográfica para workloads — substitui credenciais estáticas entre serviços.
**Evidence:** Sem SPIFFE: `order-service` se autentica com `API_KEY=secret123` hardcoded. Com SPIFFE: SPIRE agent emite SVID (X.509 ou JWT) com identidade `spiffe://cluster.local/ns/default/sa/order-service`. Certificados rotacionados automaticamente. mTLS entre serviços com identidade verificável.
**Confidence:** alta

**Claim:** Just-in-Time Access elimina standing privilege — ninguém tem acesso permanente a sistemas críticos.
**Evidence:** Standing privilege: DBA tem acesso root ao banco de produção 24/7. Se conta for comprometida, atacante tem acesso imediato. JIT: acesso solicitado → aprovado por peer → credencial temporária (TTL 1h) → sessão gravada no audit log → credencial expirada automaticamente. HashiCorp Boundary, CyberArk, AWS IAM Identity Center implementam JIT.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/sso]]
- [[concepts/mfa]]
- [[concepts/passkeys]]
- [[concepts/webauthn]]
- [[concepts/spiffe]]
- [[entities/spire]]
- [[concepts/jit-access]]
- [[entities/casbin]]

## Open Questions

- Passkeys em aplicações web B2B — como lidar com devices corporativos que não suportam biometria?
- SPIFFE em multi-cluster K8s — como federar trust domains entre clusters de diferentes cloud providers?
