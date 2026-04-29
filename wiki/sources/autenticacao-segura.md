---
type: source
title: "Autenticação Segura"
aliases: ["autenticacao segura", "bcrypt argon2", "mfa totp", "passkeys webauthn", "password hashing"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/autenticacao-segura.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [autenticacao, bcrypt, argon2id, mfa, totp, passkeys, webauthn, jwt, oauth, session-management, account-lockout]
skill: tech-mentor-security
status: stable
---

## TL;DR

Autenticação vs Autorização: authn = quem você é, authz = o que pode fazer. Senhas: bcrypt 12 rounds ou Argon2id (mais resistente a GPU). JWT: Access Token 1h httpOnly, Refresh Token 7d httpOnly Secure. MFA: TOTP é o mínimo, Passkeys/WebAuthn é o futuro. Checklist de 15 pontos cobre os principais vetores.

## Key Claims

**Claim:** Argon2id supera bcrypt contra ataques de GPU — recomendação OWASP 2024+.
**Evidence:** bcrypt é CPU-bound mas paralelizável em GPU. Argon2id usa memória intensiva (64MB por hash) — GPUs têm menos memória por core que CPUs. Custo de cracking 10× maior vs bcrypt equivalente em tempo.
**Confidence:** alta

**Claim:** MD5/SHA256 direto para senhas é inaceitável — vulnerável a rainbow tables e GPU cracking.
**Evidence:** SHA256(senha) sem salt: rainbow table pré-computada resolve em milissegundos. Com salt: GPU com 10B hash/s quebra 8 chars em < 1h. bcrypt com cost 12: mesmo GPU leva anos. O fator de custo é a diferença crítica.
**Confidence:** alta

**Claim:** Passkeys/WebAuthn é o padrão de autenticação do futuro — phishing-resistant por design.
**Evidence:** Passkey usa par de chaves criptográficas vinculado ao domain. Phishing em domain diferente = chave diferente = autenticação falha. Sem senha para roubar ou interceptar. Suporte > 95% dos browsers em 2025.
**Confidence:** alta

**Claim:** timingSafeEqual é obrigatório para comparação de tokens — string comparison vaza timing.
**Evidence:** Comparação `===` retorna mais cedo quando bytes iniciais diferem. Atacante mede microssegundos de diferença para descobrir prefixo correto. `crypto.timingSafeEqual()` compara em tempo constante independente do ponto de diferença.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/bcrypt]]
- [[concepts/argon2id]]
- [[concepts/totp]]
- [[concepts/passkeys]]
- [[concepts/webauthn]]
- [[concepts/jwt]]
- [[concepts/timing-attack]]
- [[concepts/session-management]]

## Open Questions

- Passkeys na web: como lidar com usuários sem dispositivo compatível (fallback para senha sem degradar segurança)?
- Account lockout vs brute force: lockout muito agressivo pode virar DoS. Qual o threshold correto?
