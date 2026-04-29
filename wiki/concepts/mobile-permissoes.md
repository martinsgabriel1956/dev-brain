---
type: concept
title: "Permissões Runtime — Mobile"
aliases: ["runtime permissions android", "ios permissions", "privacy manifest apple"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
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

- [[mobile-seguranca]] — permissões como parte da postura de segurança
- [[mobile-biometria]] — permissão de biometria

## Key Sources

- [[wiki/sources/mobile-permissoes]]
