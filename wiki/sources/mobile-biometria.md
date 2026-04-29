---
type: source
title: "Biometria — Face ID / Touch ID / Fingerprint"
aliases: ["biometria mobile", "face id ios", "fingerprint android", "BiometricPrompt"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-biometria.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, biometria, face-id, touch-id, fingerprint, BiometricPrompt, SecureEnclave, Keystore]
skill: tech-mentor-mobile
status: stable
---

# Biometria — Mobile

## TL;DR

iOS usa `LocalAuthentication` (LAContext) com Secure Enclave — chave privada nunca sai do hardware. Android usa `BiometricPrompt` unificando fingerprint/face/iris com chave no Android Keystore. Biometria deve ser segunda camada (fallback PIN/senha), nunca a única. Dados biométricos nunca saem do dispositivo — o app recebe apenas sucesso/falha.

## Claims Principais

| Claim | Confiança |
|---|---|
| Dados biométricos ficam no Secure Enclave (iOS) / Keystore (Android) — app recebe só sucesso/falha | Alta |
| BiometricPrompt unifica todos os métodos biométricos Android — sem API por tipo | Alta |
| Fallback PIN/senha obrigatório — biometria falha em mãos molhadas, óculos, máscara | Alta |
| Chave Keystore com `setUserAuthenticationRequired(true)` — inutilizável sem biometria | Alta |

## Conceitos Abordados

- [[mobile-biometria]] · [[mobile-seguranca]] · [[mobile-armazenamento-local]] · [[autenticacao-segura]]
