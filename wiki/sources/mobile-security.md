---
type: source
title: "Mobile Security"
aliases: ["mobile security", "certificate pinning", "keychain", "keystore", "jailbreak detection", "frida", "owasp mobile top 10"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-security.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [mobile-security, certificate-pinning, keychain, keystore, jailbreak-detection, frida, owasp-mobile, android-security, ios-security]
skill: tech-mentor-security
status: stable
---

## TL;DR

Mobile Security: OWASP Mobile Top 10 (2023) guia o que proteger. Armazenamento seguro: Keychain (iOS) e Keystore (Android) para segredos — nunca SharedPreferences ou UserDefaults para dados sensíveis. Certificate Pinning previne MITM mesmo com CA comprometida — inclua backup pin para renovação. Ofuscação dificulta reversing (não impede). Frida é a ferramenta principal de análise dinâmica.

## Key Claims

**Claim:** Certificate Pinning requer backup pin e processo de atualização OTA — sem isso, renovação de certificado quebra o app.
**Evidence:** App com pin único: certificado expira ou é rotacionado → todas as versões antigas do app param de funcionar. Solução: sempre incluir 2+ pins (current + backup). Processo: antes de expirar, publicar nova versão com backup pin como primary. Rotação: quando nova versão está em >95% dos devices, remover pin antigo.
**Confidence:** alta

**Claim:** Dados sensíveis devem usar Keychain (iOS) e Keystore (Android) — nunca UserDefaults ou SharedPreferences.
**Evidence:** UserDefaults/SharedPreferences: armazenados em plist/XML no filesystem, acessíveis com root ou em backup. Keychain (iOS): criptografado pelo OS, protegido por Secure Enclave, configurável por `kSecAttrAccessible`. Keystore (Android): chaves armazenadas em TEE (Trusted Execution Environment) ou hardware security module. Impossível extrair a chave mesmo com root (hardware-backed).
**Confidence:** alta

**Claim:** Jailbreak/Root detection reduz superfície de ataque mas não é barreira definitiva — complemento, não substituto.
**Evidence:** Detecção: verificar presença de Cydia, substrates, caminhos de binários suspeitos. Ferramentas como Frida ou Objection contornam detecções básicas. Valor: eleva o custo para atacantes, útil para aplicações financeiras/healthcare. Não depender exclusivamente: toda lógica sensível deve estar no backend.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/certificate-pinning]]
- [[concepts/keychain]]
- [[concepts/keystore]]
- [[concepts/jailbreak-detection]]
- [[entities/frida]]
- [[concepts/owasp-mobile]]

## Open Questions

- Certificate pinning com Let's Encrypt (90 dias de validade) — como automatizar a rotação de pin sem forçar app update?
- Frida bypass de certificate pinning em produção — quais técnicas modernas de pinning são resistentes?
