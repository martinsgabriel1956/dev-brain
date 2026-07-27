---
type: concept
title: "Biometria Mobile — Face ID, Touch ID, Fingerprint"
aliases: ["biometria ios", "biometria android", "BiometricPrompt", "LocalAuthentication ios"]
date_created: 2026-04-24
date_updated: 2026-07-27
source_count: 2
tags: [mobile, biometria, face-id, touch-id, fingerprint, secure-enclave, keystore]
skill: tech-mentor-mobile
status: stable
---

# Biometria Mobile

Dados biométricos ficam no hardware do dispositivo — o app recebe apenas sucesso ou falha.

## Três Gerações de Biometria por Impressão Digital

1. **Minúcias**: sistema extrai pontos onde uma linha da digital termina ou se bifurca, guarda como lista de posições/ângulos (o *template*). Comparação exige realinhar as duas leituras (o dedo nunca toca exatamente na mesma posição) e contar coincidências acima de um threshold. Frágil: pressão do dedo (tecido mole) muda o padrão capturado.
2. **Vetor único**: em vez de só minúcias, incorpora direção de linhas, densidade e textura num vetor numérico único; compara por distância entre vetores. Mesmo problema de fundo permanece: biometria vazada não pode ser trocada como uma senha.
3. **Isolamento de hardware** (Secure Enclave / TEE): o problema deixa de ser algorítmico e passa a ser arquitetural — mover a verificação para um processador isolado do sistema operacional, para que malware no SO não intercepte o template biométrico. Na web, o fluxo passa a ser challenge-response: o site manda um challenge, o dispositivo pede biometria localmente, e só libera uma chave privada para assinar o challenge — o site nunca vê a biometria em si, só a assinatura. Ver [[wiki/concepts/webauthn-fido2-u2f]] para esse fluxo em detalhe.

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
- [[wiki/concepts/webauthn-fido2-u2f]] — biometria como liberador local da chave privada num fluxo challenge-response
- [[wiki/concepts/mfa-multifator-autenticacao]] — biometria implementa o fator "algo que você é"

## Key Sources

- [[wiki/sources/mobile-biometria]]
- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
