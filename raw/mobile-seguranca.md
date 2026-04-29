---
date: 2026-04-23
tags: [tech-mentor, mobile, segurança, certificate-pinning, keychain, keystore, owasp, jailbreak]
skill: tech-mentor-mobile/references/seguranca
level: avançado
---

# Segurança Mobile — Certificate Pinning, Keychain/Keystore, OWASP Mobile Top 10, Jailbreak Detection

## Contexto
Apps mobile têm superfície de ataque única: o binário roda no device do usuário (potencialmente comprometido), a rede pode ser interceptada (MITM), e o storage local pode ser lido em devices rooteados. O OWASP Mobile Top 10 define os vetores mais explorados. A postura correta é defense-in-depth: múltiplas camadas, nenhuma como silver bullet.

## Como Funciona

### 1. Certificate Pinning

Pinning valida que o certificado TLS recebido corresponde ao esperado — impede ataques MITM mesmo com certificados CA válidos instalados por atacantes.

```typescript
// React Native — react-native-ssl-pinning
import { fetch } from "react-native-ssl-pinning";

async function secureApiCall(endpoint: string, body: unknown) {
  return fetch(`${API_URL}${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
    sslPinning: {
      certs: ["api-cert-prod", "api-cert-backup"] // arquivos .cer em assets
    },
    timeoutInterval: 10000
  });
}
```

```swift
// iOS — URLSession com URLSessionDelegate
class PinnedURLSessionDelegate: NSObject, URLSessionDelegate {
  // Hash SHA-256 da public key (mais robusto que pinning do certificado completo)
  private let pinnedKeys = [
    "base64EncodedPublicKeyHash1==",
    "base64EncodedPublicKeyHash2==" // backup key — sempre ter ao menos 2
  ]

  func urlSession(
    _ session: URLSession,
    didReceive challenge: URLAuthenticationChallenge,
    completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void
  ) {
    guard challenge.protectionSpace.authenticationMethod == NSURLAuthenticationMethodServerTrust,
          let serverTrust = challenge.protectionSpace.serverTrust,
          let certificate = SecTrustGetCertificateAtIndex(serverTrust, 0),
          let publicKey = SecCertificateCopyKey(certificate),
          let publicKeyData = SecKeyCopyExternalRepresentation(publicKey, nil) as? Data
    else {
      completionHandler(.cancelAuthenticationChallenge, nil)
      return
    }

    let keyHash = sha256(publicKeyData).base64EncodedString()
    if pinnedKeys.contains(keyHash) {
      completionHandler(.useCredential, URLCredential(trust: serverTrust))
    } else {
      completionHandler(.cancelAuthenticationChallenge, nil)
    }
  }
}
```

```kotlin
// Android — OkHttp CertificatePinner
val certificatePinner = CertificatePinner.Builder()
  .add("api.yourapp.com", "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")
  .add("api.yourapp.com", "sha256/BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=") // backup
  .build()

val okHttpClient = OkHttpClient.Builder()
  .certificatePinner(certificatePinner)
  .build()

// Gerar o hash para usar acima:
// openssl s_client -connect api.yourapp.com:443 | openssl x509 -pubkey -noout |
//   openssl pkey -pubin -outform der | openssl dgst -sha256 -binary | base64
```

**Cuidado com pinning:** se o certificado expirar e você não atualizar o app, o app quebra para todos os usuários. Sempre pinar 2+ chaves (uma de produção, uma de backup/emergência).

### 2. Keychain (iOS) / Keystore (Android)

Hardware-backed secure storage — o sistema operacional gerencia a criptografia.

```typescript
// React Native — react-native-keychain
import * as Keychain from "react-native-keychain";

const KEYCHAIN_SERVICE = "com.yourapp.credentials";

// Salvar token com proteção biométrica
async function saveSecureToken(token: string): Promise<void> {
  await Keychain.setGenericPassword("token", token, {
    service: KEYCHAIN_SERVICE,
    accessible: Keychain.ACCESSIBLE.WHEN_UNLOCKED_THIS_DEVICE_ONLY,
    // Requer biometria para ler (iOS)
    accessControl: Keychain.ACCESS_CONTROL.BIOMETRY_CURRENT_SET_OR_DEVICE_PASSCODE,
    securityLevel: Keychain.SECURITY_LEVEL.SECURE_HARDWARE // Android Keystore
  });
}

// Ler — dispara prompt biométrico se configurado
async function getSecureToken(): Promise<string | null> {
  try {
    const credentials = await Keychain.getGenericPassword({
      service: KEYCHAIN_SERVICE,
      authenticationPrompt: { title: "Confirmar identidade" }
    });
    return credentials ? credentials.password : null;
  } catch {
    return null;
  }
}

// Limpar no logout
async function clearSecureStorage(): Promise<void> {
  await Keychain.resetGenericPassword({ service: KEYCHAIN_SERVICE });
}
```

### 3. OWASP Mobile Top 10 — Checklist

```
M1 - Improper Credential Usage
□ Tokens em Keychain/Keystore, não em AsyncStorage/SharedPreferences
□ Sem credenciais hardcoded no código
□ Verificar: grep -r "password\|secret\|apikey" src/ --include="*.ts"

M2 - Inadequate Supply Chain Security
□ Lock files commitados (package-lock.json, Podfile.lock)
□ Auditoria de dependências: npm audit, bundle audit
□ Sem pacotes sem manutenção com CVEs conhecidos

M3 - Insecure Authentication/Authorization
□ Access tokens com expiração (máx 1h)
□ Refresh tokens com rotação
□ Biometria vinculada ao Keychain (não autenticação standalone)

M4 - Insufficient Input/Output Validation
□ Zod para todos os inputs de usuário
□ Sanitizar dados antes de exibir (XSS em WebViews)
□ Validar deep link params antes de usar em queries

M5 - Insecure Communication
□ HTTPS obrigatório (ATS no iOS, Network Security Config no Android)
□ Certificate pinning em endpoints críticos
□ Sem dados sensíveis em query params (aparecem em logs)

M6 - Inadequate Privacy Controls
□ Sem PII em logs
□ Analytics opt-out implementado
□ Dados biométricos nunca saem do device

M7 - Insufficient Binary Protections
□ Ofuscação habilitada (ProGuard/R8 no Android)
□ Sem chaves de API no bundle JS (usar env vars do servidor)
□ Detecção de debugging em produção

M8 - Security Misconfiguration
□ Sem modo debug em builds de produção
□ CORS configurado no backend
□ Sem endpoints de debug expostos

M9 - Insecure Data Storage
□ Sem dados sensíveis em logs
□ Clipboard limpo após cópia de senha
□ Backups do Android não incluem dados sensíveis

M10 - Insufficient Cryptography
□ bcrypt 12+ rounds para senhas
□ Sem MD5/SHA1 para dados sensíveis
□ IV único para cada operação AES
```

### 4. Jailbreak / Root Detection

```typescript
// React Native — react-native-device-info
import DeviceInfo from "react-native-device-info";

export async function checkDeviceIntegrity(): Promise<{
  isCompromised: boolean;
  reason: string | null;
}> {
  const [isJailBroken, isEmulator] = await Promise.all([
    DeviceInfo.isEmulator(),
    // iOS: testa presença de arquivos de jailbreak
    // Android: testa acesso root e apps de root conhecidos
    checkJailbreakIndicators()
  ]);

  if (isEmulator && !__DEV__) {
    return { isCompromised: true, reason: "Emulator detected in production" };
  }

  return { isCompromised: false, reason: null };
}

async function checkJailbreakIndicators(): Promise<boolean> {
  if (Platform.OS === "ios") {
    const jailbreakFiles = [
      "/Applications/Cydia.app",
      "/private/var/lib/apt/",
      "/usr/bin/ssh"
    ];
    // Tentar acessar arquivos — em device limpo, falha com ENOENT
    return jailbreakFiles.some(file => {
      try {
        require("react-native-fs").existsSync(file);
        return true;
      } catch {
        return false;
      }
    });
  }
  return false;
}
```

```kotlin
// Android — Play Integrity API (mais confiável que detecção local)
val integrityManager = IntegrityManagerFactory.create(context)

suspend fun checkPlayIntegrity(): IntegrityVerdict {
  val nonce = generateNonce() // enviar ao backend para validar
  val tokenResponse = integrityManager.requestIntegrityToken(
    IntegrityTokenRequest.builder()
      .setNonce(nonce)
      .build()
  ).await()

  // Enviar token ao backend — backend valida com Google
  val verdict = backendApi.verifyIntegrity(tokenResponse.token())
  return verdict
}
```

```swift
// iOS — DeviceCheck / App Attest
import DeviceCheck

// App Attest — verifica que o app não foi modificado
func attestKey() async throws -> String {
  let service = DCAppAttestService.shared
  guard service.isSupported else { throw AttestError.notSupported }

  let keyId = try await service.generateKey()
  // Registrar keyId com backend
  return keyId
}

func assertRequest(keyId: String, request: Data) async throws -> Data {
  let service = DCAppAttestService.shared
  let assertion = try await service.generateAssertion(keyId, clientDataHash: sha256(request))
  return assertion
}
```

### Android Network Security Config

```xml
<!-- res/xml/network_security_config.xml -->
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
  <!-- Produção: apenas HTTPS, sem CAs de usuário -->
  <base-config cleartextTrafficPermitted="false">
    <trust-anchors>
      <certificates src="system" />
      <!-- Remover "user" em produção — impede install de CAs para MITM -->
    </trust-anchors>
  </base-config>

  <!-- Debug: permitir CAs de usuário apenas em debug -->
  <debug-overrides>
    <trust-anchors>
      <certificates src="system" />
      <certificates src="user" />
    </trust-anchors>
  </debug-overrides>

  <!-- Pinning por domínio -->
  <domain-config>
    <domain includeSubdomains="true">api.yourapp.com</domain>
    <pin-set>
      <pin digest="SHA-256">AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=</pin>
      <pin digest="SHA-256">BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=</pin>
    </pin-set>
  </domain-config>
</network-security-config>
```

## Trade-offs

| Medida | Proteção | Custo de manutenção | Falsos positivos |
|---|---|---|---|
| Certificate Pinning | MITM | Alto (renovação de cert) | Nenhum |
| Keychain/Keystore | Storage local | Baixo | Raro |
| Jailbreak detection local | Reversing parcial | Médio | Alto |
| Play Integrity / App Attest | Root + adulteração | Médio | Baixo |
| Ofuscação (ProGuard) | Reversing parcial | Baixo | Nenhum |

## Quando Usar / Quando Evitar

**Certificate Pinning** em apps financeiros, de saúde, ou que transmitem PII. Para outros apps, o overhead de manutenção pode não compensar — HTTPS bem configurado já oferece boa proteção.

**Jailbreak detection** nunca bloqueie o app completamente — usuários legítimos (pesquisadores, devs) usam devices modificados. Use para downgrade de funcionalidade sensível (esconder balanço, exigir 2FA adicional).

**Play Integrity > detecção local de root** — é mais difícil de burlar pois a validação ocorre nos servidores do Google.

## Conceitos Relacionados
[[mobile-biometria]] · [[mobile-permissoes]] · [[mobile-armazenamento-local]] · [[autenticacao-segura]] · [[api-security]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
