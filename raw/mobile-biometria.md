---
date: 2026-04-23
tags: [tech-mentor, mobile, biometria, face-id, touch-id, fingerprint, react-native, flutter, ios, android]
skill: tech-mentor-mobile/references/biometria
level: intermediário
---

# Biometria — Face ID / Touch ID / Fingerprint

## Contexto
Biometria é a forma mais natural de autenticação mobile: sem digitar senha, sem token físico. O padrão moderno não é substituir a senha por biometria — é usar biometria para desbloquear uma credencial armazenada com segurança (no Keychain/Keystore), que autentica o usuário na sessão. Assim, a biometria não viaja pela rede, e o fallback é a senha master.

## Como Funciona

### Fluxo seguro

```
Login inicial: usuário + senha → backend valida → retorna refresh_token
Armazenamento: refresh_token é salvo no Keychain/Keystore (criptografado)
Próximos acessos: biometria → biometria ok → libera acesso ao Keychain → lê refresh_token → troca por access_token
```

A biometria não substitui a senha no backend — ela protege o acesso ao token local.

### React Native — react-native-biometrics

```typescript
import ReactNativeBiometrics, { BiometryTypes } from "react-native-biometrics";

const rnBiometrics = new ReactNativeBiometrics({ allowDeviceCredentials: true });

// Verificar disponibilidade
export async function checkBiometrics(): Promise<{
  available: boolean;
  type: string | null;
}> {
  const { available, biometryType } = await rnBiometrics.isSensorAvailable();
  return {
    available,
    type: biometryType ?? null // FaceID | TouchID | Biometrics (Android)
  };
}

// Autenticar usuário
export async function authenticateWithBiometrics(): Promise<boolean> {
  const { success } = await rnBiometrics.simplePrompt({
    promptMessage: "Confirme sua identidade",
    cancelButtonText: "Usar senha",
    fallbackPromptMessage: "Use sua senha ou PIN"
  });
  return success;
}

// Assinar um payload (mais seguro — prova criptográfica)
export async function signWithBiometrics(payload: string): Promise<string | null> {
  const { publicKey } = await rnBiometrics.createKeys();
  // Registrar publicKey no backend uma vez
  await http.post("/biometrics/register", { publicKey });

  const { success, signature } = await rnBiometrics.createSignature({
    promptMessage: "Autenticar",
    payload
  });

  return success && signature ? signature : null;
}
```

```typescript
// Integração com Keychain para armazenar token
import * as Keychain from "react-native-keychain";

const BIOMETRIC_SERVICE = "com.yourapp.biometric";

export async function saveTokenWithBiometricProtection(token: string): Promise<void> {
  await Keychain.setGenericPassword("token", token, {
    service: BIOMETRIC_SERVICE,
    accessControl: Keychain.ACCESS_CONTROL.BIOMETRY_CURRENT_SET,
    accessible: Keychain.ACCESSIBLE.WHEN_UNLOCKED_THIS_DEVICE_ONLY
  });
}

export async function getTokenWithBiometrics(): Promise<string | null> {
  try {
    const credentials = await Keychain.getGenericPassword({
      service: BIOMETRIC_SERVICE,
      authenticationPrompt: { title: "Autenticar para continuar" }
    });
    return credentials ? credentials.password : null;
  } catch {
    return null; // biometria cancelada ou falhou
  }
}
```

### Flutter — local_auth

```dart
import "package:local_auth/local_auth.dart";

class BiometricService {
  final _auth = LocalAuthentication();

  Future<bool> isAvailable() async {
    final canAuth = await _auth.canCheckBiometrics;
    final isDeviceSupported = await _auth.isDeviceSupported();
    return canAuth && isDeviceSupported;
  }

  Future<List<BiometricType>> getAvailableTypes() async {
    return _auth.getAvailableBiometrics();
    // [BiometricType.face, BiometricType.fingerprint, BiometricType.strong, BiometricType.weak]
  }

  Future<bool> authenticate({String reason = "Confirme sua identidade"}) async {
    try {
      return await _auth.authenticate(
        localizedReason: reason,
        options: const AuthenticationOptions(
          biometricOnly: false, // permite PIN como fallback
          stickyAuth: true      // mantém prompt se app vai para background
        ),
      );
    } on PlatformException catch (e) {
      console.log({ message: "Erro biometria", error: e.message });
      return false;
    }
  }
}

// Uso no Provider
final biometricProvider = Provider<BiometricService>((_) => BiometricService());

// Widget
class BiometricLoginButton extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return ElevatedButton(
      onPressed: () async {
        final bio = ref.read(biometricProvider);
        final authenticated = await bio.authenticate();
        if (authenticated) {
          // liberar acesso ao token no secure storage
          final token = await SecureStorage.read("refresh_token");
          ref.read(authProvider.notifier).loginWithToken(token!);
        }
      },
      child: const Text("Entrar com biometria"),
    );
  }
}
```

### iOS — LocalAuthentication (Swift)

```swift
import LocalAuthentication

class BiometricManager {
  let context = LAContext()

  func isAvailable() -> Bool {
    var error: NSError?
    return context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error)
  }

  func authenticate(reason: String) async -> Bool {
    do {
      return try await context.evaluatePolicy(
        .deviceOwnerAuthentication, // inclui PIN como fallback
        localizedReason: reason
      )
    } catch {
      return false
    }
  }
}

// Armazenar no Keychain com proteção biométrica
func saveSecureToken(_ token: String) throws {
  let access = SecAccessControlCreateWithFlags(
    nil,
    kSecAttrAccessibleWhenUnlockedThisDeviceOnly,
    .biometryCurrentSet, // invalida se biometria mudar
    nil
  )!

  let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrService as String: "com.yourapp.token",
    kSecValueData as String: token.data(using: .utf8)!,
    kSecAttrAccessControl as String: access
  ]

  SecItemDelete(query as CFDictionary)
  SecItemAdd(query as CFDictionary, nil)
}
```

### Android — BiometricPrompt

```kotlin
class BiometricManager(private val activity: FragmentActivity) {
  private val biometricManager = BiometricManager.from(activity)

  fun isAvailable(): Boolean {
    return biometricManager.canAuthenticate(
      BiometricManager.Authenticators.BIOMETRIC_STRONG or
      BiometricManager.Authenticators.DEVICE_CREDENTIAL
    ) == BiometricManager.BIOMETRIC_SUCCESS
  }

  fun authenticate(
    onSuccess: (BiometricPrompt.AuthenticationResult) -> Unit,
    onError: (String) -> Unit
  ) {
    val executor = ContextCompat.getMainExecutor(activity)
    val prompt = BiometricPrompt(activity, executor,
      object : BiometricPrompt.AuthenticationCallback() {
        override fun onAuthenticationSucceeded(result: BiometricPrompt.AuthenticationResult) {
          onSuccess(result)
        }
        override fun onAuthenticationError(errorCode: Int, errString: CharSequence) {
          onError(errString.toString())
        }
      }
    )

    val info = BiometricPrompt.PromptInfo.Builder()
      .setTitle("Autenticar")
      .setSubtitle("Use sua biometria ou PIN")
      .setAllowedAuthenticators(
        BiometricManager.Authenticators.BIOMETRIC_STRONG or
        BiometricManager.Authenticators.DEVICE_CREDENTIAL
      )
      .build()

    prompt.authenticate(info)
  }
}
```

## Trade-offs

| Aspecto | simplePrompt | createSignature | Keychain protegido |
|---|---|---|---|
| Segurança | Média (local only) | Alta (prova criptográfica) | Alta (hardware-backed) |
| Complexidade | Baixa | Alta | Média |
| Backend necessário | Não | Sim (verificar assinatura) | Não |
| Uso ideal | Desbloquear sessão local | Transações financeiras | Proteger token de sessão |

## Quando Usar / Quando Evitar

**Sempre combine biometria + Keychain/Keystore** — biometria sem storage seguro é inútil (o token fica em texto plano).

**Use `BIOMETRY_CURRENT_SET`** para invalidar o acesso se o usuário adicionar nova biometria — previne que um atacante com acesso físico ao device adicione seu fingerprint.

**Implemente fallback para senha** — usuários com biometria não cadastrada ou que a desativam não devem ser bloqueados.

**Nunca:** enviar o dado biométrico para o backend (viola LGPD/GDPR), usar biometria para transações financeiras sem assinatura criptográfica adicional.

## Conceitos Relacionados
[[mobile-armazenamento-local]] · [[mobile-seguranca]] · [[mobile-permissoes]] · [[autenticacao-segura]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
