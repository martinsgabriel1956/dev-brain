---
type: concept
title: "Biometria Mobile — Face ID, Touch ID, Fingerprint"
aliases: ["biometria ios", "biometria android", "BiometricPrompt", "LocalAuthentication ios"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, biometria, face-id, touch-id, fingerprint, secure-enclave, keystore]
skill: tech-mentor-mobile
status: stable
---

# Biometria Mobile

Dados biométricos ficam no hardware do dispositivo — o app recebe apenas sucesso ou falha.

## iOS — LocalAuthentication

```swift
let context = LAContext()
var error: NSError?

guard context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error) else {
    // fallback para PIN
    return
}

context.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics,
    localizedReason: "Autenticar para continuar") { success, error in
    if success {
        // abrir Keychain com chave protegida por biometria
    }
}
```

Secure Enclave processa a verificação — chave privada nunca sai do hardware.

## Android — BiometricPrompt

```kotlin
val biometricPrompt = BiometricPrompt(activity, executor,
    object : BiometricPrompt.AuthenticationCallback() {
        override fun onAuthenticationSucceeded(result: AuthenticationResult) {
            val cipher = result.cryptoObject?.cipher
            // usar cipher para descriptografar Keystore key
        }
    }
)

biometricPrompt.authenticate(
    BiometricPrompt.PromptInfo.Builder()
        .setTitle("Verificar identidade")
        .setNegativeButtonText("Usar PIN")
        .build()
)
```

## Regras

- Sempre oferecer fallback PIN/senha — biometria falha em condições físicas
- `setUserAuthenticationRequired(true)` no Keystore — chave inutilizável sem biometria
- Não usar biometria como única camada de auth — defense in depth

## Ver também

- [[mobile-seguranca]] — Keychain/Keystore para armazenamento de chaves
- [[mobile-armazenamento-local]] — onde guardar tokens protegidos por biometria
- [[autenticacao-segura]] — padrões gerais de autenticação

## Key Sources

- [[wiki/sources/mobile-biometria]]
