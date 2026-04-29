---
type: concept
title: "Segurança Mobile"
aliases: ["mobile certificate pinning", "mobile ssl pinning", "mobile keychain security", "mobile obfuscation"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, seguranca, keychain, keystore, certificate-pinning, ssl-pinning, frida]
skill: tech-mentor-mobile
status: stable
---

# Segurança Mobile

## Hierarquia de Armazenamento Seguro

```
Segredos críticos (chaves privadas, tokens biométricos)
    → Keychain (iOS Secure Enclave) / Keystore (Android hardware-backed)

Tokens de sessão, credenciais
    → MMKV com encryptionKey (AES) ou Keychain/Keystore

Preferências, flags
    → MMKV sem criptografia

NUNCA:
    → SharedPreferences / AsyncStorage sem criptografia para dados sensíveis
    → Código-fonte com API keys hardcoded
```

## Certificate Pinning

```kotlin
// OkHttp
val certificatePinner = CertificatePinner.Builder()
    .add("api.example.com", "sha256/AAAA...") // pin ativo
    .add("api.example.com", "sha256/BBBB...") // backup pin para rotação
    .build()

val client = OkHttpClient.Builder()
    .certificatePinner(certificatePinner)
    .build()
```

**Sempre ter 2 pins:** ativo + backup. Rotacionar: ativar backup, atualizar ativo, remover antigo.

SSL pinning pode ser bypassado com Frida em dispositivos root — não é única linha de defesa.

## Checklist de Segurança

- [ ] API keys em variáveis de ambiente, não no código-fonte
- [ ] Certificate pinning para APIs financeiras/saúde
- [ ] Tokens em Keychain/Keystore, não AsyncStorage
- [ ] Jailbreak/root detection para operações sensíveis
- [ ] ProGuard/R8 habilitado em release build (Android)
- [ ] App Transport Security (iOS) — sem `NSAllowsArbitraryLoads`
- [ ] SSL pinning com backup pin

## Frida e Defense in Depth

Frida pode fazer SSL unpinning e modificar lógica de validação de receipt. Defense in depth:

1. Certificate pinning (primeira barreira)
2. Validação server-side de todos os dados críticos
3. Root/jailbreak detection
4. Ofuscação de código

## Ver também

- [[mobile-biometria]] — Keychain/Keystore integrado com biometria
- [[mobile-armazenamento-local]] — onde guardar cada tipo de dado
- [[mobile-monetizacao]] — receipt validation server-side

## Key Sources

- [[wiki/sources/mobile-seguranca]]
