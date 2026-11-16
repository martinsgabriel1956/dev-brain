---
type: concept
title: "Permissões Runtime — Mobile"
aliases: ["runtime permissions android", "ios permissions", "privacy manifest apple"]
date_created: 2026-04-24
date_updated: 2026-11-16
source_count: 2
tags: [mobile, permissoes, runtime-permissions, privacy-manifest, ios, android]
skill: tech-mentor-mobile
status: stable
---

# Permissões Runtime — Mobile

## Princípio: Pedir no Contexto

Pedir permissão no momento de uso — não no launch. Taxa de concessão 3x maior quando o usuário entende o motivo.

```ts
// ❌ Anti-pattern — pedir no launch
useEffect(() => { requestCameraPermission(); }, []);

// ✅ Correto — pedir quando o usuário tenta tirar foto
async function handleCameraButton() {
    const granted = await PermissionsAndroid.request(CAMERA);
    if (granted === 'granted') openCamera();
}
```

## iOS — Info.plist

```xml
<key>NSCameraUsageDescription</key>
<string>Para tirar foto do produto para review</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>Para encontrar lojas próximas</string>
```

Descrição clara e específica — Apple rejeita apps com strings genéricas ("necessário para funcionar").

**Privacy Manifest** (obrigatório desde maio 2024):

```xml
<!-- PrivacyInfo.xcprivacy -->
<key>NSPrivacyAccessedAPITypes</key>
<array>
    <dict>
        <key>NSPrivacyAccessedAPIType</key>
        <string>NSPrivacyAccessedAPICategoryUserDefaults</string>
        <key>NSPrivacyAccessedAPITypeReasons</key>
        <array><string>CA92.1</string></array>
    </dict>
</array>
```

## Android — Runtime Permission

```kotlin
val requestPermissionLauncher = registerForActivityResult(
    ActivityResultContracts.RequestPermission()
) { isGranted ->
    if (isGranted) openCamera()
    else showPermissionDeniedDialog()
}

fun handleCameraButton() {
    when {
        ContextCompat.checkSelfPermission(this, CAMERA) == GRANTED -> openCamera()
        shouldShowRequestPermissionRationale(CAMERA) -> showRationaleDialog()
        else -> requestPermissionLauncher.launch(CAMERA)
    }
}
```

## Permissão Negada Permanentemente

Direcionar para Settings — sem loop de pedidos:

```ts
Linking.openSettings(); // abre configurações do app
```

## Ver também

- [[wiki/concepts/mobile-seguranca]] — permissões como parte da postura de segurança
- [[wiki/concepts/mobile-biometria]] — permissão de biometria

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], `Location.requestPermissionsAsync()` (hoje `requestForegroundPermissionsAsync`) e `Alert` quando a permissão é negada. O app fica sem mapa porque não há alternativa à recusa.

## Key Sources

- [[wiki/sources/mobile-permissoes]]
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: permissão de localização sem fallback
