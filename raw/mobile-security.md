---
date: 2026-04-23
tags: [tech-mentor, security, mobile, ios, android, owasp-mobile]
skill: tech-mentor-security/references/mobile-security
level: avançado
---

# Mobile Security

## Contexto

Apps mobile operam em ambientes hostis que web não enfrenta: o dispositivo pode ser roubado, rootado/jailbroken, ter apps maliciosos instalados, e estar em redes não confiáveis. O código roda no cliente sem controle do servidor — binários são reversiáveis, comunicação pode ser interceptada e armazenamento local é acessível com acesso físico.

OWASP Mobile Top 10 captura as vulnerabilidades mais críticas. A maioria das brechas móveis não são exploits sofisticados — são armazenamento incorreto de secrets, comunicação insegura, e falta de validação no servidor.

## Como Funciona

### OWASP Mobile Top 10 (2023)

| # | Vulnerabilidade | Exemplo |
|---|---|---|
| M1 | Improper Credential Usage | API key hardcoded no código fonte |
| M2 | Inadequate Supply Chain Security | SDK de terceiros comprometido |
| M3 | Insecure Authentication/Authorization | JWT sem validação no servidor |
| M4 | Insufficient Input/Output Validation | SQL injection via input mobile |
| M5 | Insecure Communication | HTTP sem TLS, certificate não validado |
| M6 | Inadequate Privacy Controls | PII em logs, clipboard, analytics |
| M7 | Insufficient Binary Protections | App sem ofuscação, debuggável em prod |
| M8 | Security Misconfiguration | Backup habilitado, permissões excessivas |
| M9 | Insecure Data Storage | Credentials em SharedPreferences/NSUserDefaults |
| M10 | Insufficient Cryptography | DES/MD5, chave hardcoded |

### Armazenamento Seguro de Dados

**Android:**
```kotlin
// ERRADO — SharedPreferences é texto claro
val prefs = getSharedPreferences("config", Context.MODE_PRIVATE)
prefs.edit().putString("api_key", apiKey).apply()  // visível com root

// CORRETO — EncryptedSharedPreferences (Jetpack Security)
val masterKey = MasterKey.Builder(context)
  .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
  .build()

val encryptedPrefs = EncryptedSharedPreferences.create(
  context,
  "secure_config",
  masterKey,
  EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
  EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
)
encryptedPrefs.edit().putString("api_key", apiKey).apply()

// Para secrets críticos (tokens de auth): Android Keystore
val keyStore = KeyStore.getInstance("AndroidKeyStore")
```

**iOS:**
```swift
// ERRADO — UserDefaults não é criptografado
UserDefaults.standard.set(token, forKey: "auth_token")

// CORRETO — Keychain Services
import Security

func saveToKeychain(key: String, value: String) -> Bool {
  let data = value.data(using: .utf8)!
  let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrAccount as String: key,
    kSecValueData as String: data,
    kSecAttrAccessible as String: kSecAttrAccessibleWhenUnlockedThisDeviceOnly
  ]
  SecItemDelete(query as CFDictionary)  // remover se existir
  return SecItemAdd(query as CFDictionary, nil) == errSecSuccess
}
```

### Certificate Pinning

Impede ataques MITM mesmo com certificado CA válido instalado no dispositivo.

```kotlin
// Android — OkHttp com Certificate Pinning
val certificatePinner = CertificatePinner.Builder()
  .add("api.example.com", "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")
  .add("api.example.com", "sha256/BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=") // backup pin
  .build()

val client = OkHttpClient.Builder()
  .certificatePinner(certificatePinner)
  .build()
```

```swift
// iOS — URLSession com certificate pinning
class PinnedSessionDelegate: NSObject, URLSessionDelegate {
  func urlSession(_ session: URLSession,
                  didReceive challenge: URLAuthenticationChallenge,
                  completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
    guard
      challenge.protectionSpace.authenticationMethod == NSURLAuthenticationMethodServerTrust,
      let serverTrust = challenge.protectionSpace.serverTrust,
      let certificate = SecTrustGetCertificateAtIndex(serverTrust, 0)
    else {
      completionHandler(.cancelAuthenticationChallenge, nil)
      return
    }

    let pinnedPublicKeyHash = "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
    let serverPublicKeyHash = getPublicKeyHash(certificate)

    if serverPublicKeyHash == pinnedPublicKeyHash {
      completionHandler(.useCredential, URLCredential(trust: serverTrust))
    } else {
      completionHandler(.cancelAuthenticationChallenge, nil)
    }
  }
}
```

**Atenção:** certificate pinning complica renovação de certificado — sempre incluir backup pin e implementar atualização de pin via OTA antes de expirar.

### Proteções de Binário

```kotlin
// Android — configurações no build.gradle
android {
  buildTypes {
    release {
      minifyEnabled true        // remove código não usado
      shrinkResources true
      proguardFiles getDefaultProguardFile("proguard-android-optimize.txt"),
                   "proguard-rules.pro"
      debuggable false          // NUNCA true em release
    }
  }
}

// AndroidManifest.xml
<application
  android:debuggable="false"     // redundante com debuggable false, mas explícito
  android:allowBackup="false"    // impede backup de dados pelo sistema
  android:networkSecurityConfig="@xml/network_security_config">
```

```xml
<!-- res/xml/network_security_config.xml -->
<network-security-config>
  <base-config cleartextTrafficPermitted="false">  <!-- bloqueia HTTP -->
    <trust-anchors>
      <certificates src="system"/>  <!-- apenas CAs do sistema, não user-installed -->
    </trust-anchors>
  </base-config>
</network-security-config>
```

### Análise Dinâmica com Frida

Frida é um framework de instrumentação dinâmica — injetado em apps em runtime para inspecionar comportamento, bypassar proteções e interceptar chamadas.

```javascript
// Frida script — interceptar chamadas de criptografia
Java.perform(function() {
  // Monitorar SharedPreferences
  var SharedPreferences = Java.use("android.app.SharedPreferencesImpl");
  SharedPreferences.getString.overload("java.lang.String", "java.lang.String")
    .implementation = function(key, defValue) {
      var result = this.getString(key, defValue);
      console.log(`SharedPreferences.getString("${key}") = "${result}"`);
      return result;
    };

  // Bypassar certificate pinning (para teste)
  var OkHttpClient = Java.use("okhttp3.OkHttpClient$Builder");
  OkHttpClient.certificatePinner.implementation = function(pinner) {
    console.log("Certificate pinning bypassed");
    return this;
  };
});
```

```bash
# Rodar script Frida em dispositivo conectado
frida -U -f com.example.app -l intercept.js --no-pause
```

**MobSF (Mobile Security Framework):** análise estática e dinâmica automatizada.
```bash
docker run -it --rm -p 8000:8000 opensecurity/mobile-security-framework-mobsf
# Upload APK/IPA → análise automática: permissões, hardcoded secrets, libs vulneráveis
```

### Permissões — Princípio do Mínimo

```xml
<!-- AndroidManifest.xml — solicitar apenas o necessário -->
<!-- ERRADO — solicitar permissões amplas sem necessidade -->
<uses-permission android:name="android.permission.READ_CONTACTS"/>
<uses-permission android:name="android.permission.CAMERA"/>
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>

<!-- CORRETO — especificar o máximo granular -->
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
<!-- Se só precisar de localização aproximada para a feature -->
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Certificate pinning | Bloqueia MITM com CA comprometida | Complexidade de renovação de cert |
| Keychain/Keystore | Dados seguros mesmo com root | API mais verbosa |
| Ofuscação de código | Dificulta reversing | Não impede — só atrasa |
| Biometria nativa | UX excelente, hardware-backed | Não disponível em todos os dispositivos |
| Jailbreak/root detection | Reduz superfície em devices comprometidos | Falsos positivos, contornável |

## Quando Usar / Quando Evitar

**Keychain/Keystore:** sempre para tokens, chaves e credentials. `UserDefaults`/`SharedPreferences` para dados não sensíveis apenas.

**Certificate pinning:** apps financeiros, de saúde, e-commerce com dados de cartão. Verificar processo de pin rotation antes de ativar em produção.

**Jailbreak/root detection:** considerar o trade-off — não é impermeável e pode bloquear usuários legítimos com root para personalização. Logs + risk score é melhor que block hard.

## Conceitos Relacionados

[[autenticacao-segura]] · [[criptografia-fundamentos]] · [[api-security]] · [[owasp-top10]] · [[secrets-management]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-23*
