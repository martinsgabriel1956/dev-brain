---
type: source
title: "Criptografia — Fundamentos"
aliases: ["criptografia", "aes gcm", "envelope encryption", "kdf", "pki", "assinatura digital", "ed25519"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/criptografia-fundamentos.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [criptografia, aes-gcm, envelope-encryption, kdf, argon2, pki, x509, ocsp, assinatura-digital, ed25519, hmac, tde, column-encryption]
skill: tech-mentor-security
status: stable
---

## TL;DR

Criptografia fundamental: hash (irreversível), encryption (reversível com chave), simétrica (mesma chave), assimétrica (par público/privado). AES-256-GCM é o padrão para criptografia simétrica em repouso. Envelope Encryption (KMS + DEK) para dados em escala. KDF (Argon2id, bcrypt) para derivar chaves de senhas. Ed25519 para assinaturas digitais.

## Key Claims

**Claim:** Hash ≠ Encryption — hash é irreversível, encryption é reversível com chave.
**Evidence:** SHA-256(dados) → sempre o mesmo resultado, sem chave para reverter. AES-256(dados, chave) → criptografado, descriptografável com a mesma chave. Erro crítico: armazenar senhas como AES (descriptografável se chave vazar) em vez de bcrypt/Argon2 (irreversível).
**Confidence:** alta

**Claim:** Envelope Encryption é o padrão para criptografar dados em escala com KMS.
**Evidence:** KEK (Key Encryption Key) fica no KMS (AWS/GCP). DEK (Data Encryption Key) é gerada por operação, criptografada com a KEK, armazenada junto ao dado. Para descriptografar: KMS descriptografa a DEK, DEK descriptografa o dado. Rotação de KEK não requer re-encriptar todos os dados.
**Confidence:** alta

**Claim:** AES-256-GCM é o padrão — nunca reutilizar IV (nonce), nunca usar ECB.
**Evidence:** GCM fornece authenticated encryption (AEAD) — confidencialidade + integridade em um. IV reutilizado com GCM = chave comprometida (two-time pad). ECB: blocos iguais → ciphertext igual (revela padrões). CBC: vulnerável a padding oracle.
**Confidence:** alta

**Claim:** Ed25519 é o algoritmo preferido para assinaturas digitais em 2026 — seguro e rápido.
**Evidence:** Ed25519 usa curva elíptica Curve25519. Assinatura 64 bytes (vs RSA 256+ bytes). Mais rápido que RSA 2048 em verificação. Resistente a ataques de timing por design. Recomendado pelo NIST para novos sistemas.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/aes-gcm]]
- [[concepts/envelope-encryption]]
- [[concepts/kdf]]
- [[concepts/pki]]
- [[concepts/x509]]
- [[concepts/ed25519]]
- [[concepts/hmac]]
- [[concepts/tde]]

## Open Questions

- Post-Quantum Cryptography (CRYSTALS-Kyber, Dilithium) — quando migrar sistemas existentes? Qual o prazo real?
- Column-level encryption vs application-level encryption: quando cada um é melhor para compliance?
