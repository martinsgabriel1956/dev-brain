---
type: source
title: "Segurança Mobile — Keychain, Keystore, Certificate Pinning, Frida"
aliases: ["mobile seguranca", "certificate pinning mobile", "keychain ios security", "android keystore security"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-seguranca.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, seguranca, keychain, keystore, certificate-pinning, ssl-pinning, frida, obfuscation]
skill: tech-mentor-mobile
status: stable
---

# Segurança Mobile

## TL;DR

Secrets no Keychain (iOS) / Keystore (Android) — nunca em SharedPreferences ou AsyncStorage. Certificate pinning para APIs críticas (financeiro/saúde) com backup pin para rotação. SSL pinning pode ser bypassado com Frida em dispositivos rooteados — defense in depth obrigatório. ProGuard/R8 (Android) e bitcode (iOS) para ofuscação. Nunca hardcoded API keys no código.

## Claims Principais

| Claim | Confiança |
|---|---|
| SharedPreferences/AsyncStorage em texto plano — acessível via ADB backup em Android | Alta |
| Certificate pinning com 2 pins: pin ativo + pin de backup para rotação sem downtime | Alta |
| SSL pinning bypassed com Frida em dispositivos root — não é única linha de defesa | Alta |
| API keys hardcoded no código são extraíveis com strings/decompile — nunca fazer | Alta |
| Jailbreak/root detection como sinal de risco — bloquear funcionalidades sensíveis | Média |

## Conceitos Abordados

- [[mobile-seguranca]] · [[mobile-biometria]] · [[mobile-armazenamento-local]] · [[mobile-chamadas-http]] · [[mobile-security]]
