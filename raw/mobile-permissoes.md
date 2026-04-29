---
date: 2026-04-23
tags: [tech-mentor, mobile, permissoes, camera, localizacao, notifications, react-native, flutter]
skill: tech-mentor-mobile/references/permissoes
level: intermediário
---

# Permissões — Câmera, Localização, Notificações (Runtime)

## Contexto
Permissões mobile são solicitadas em runtime desde Android 6 e iOS 8. O sistema as gerencia — o app não pode conceder permissões a si mesmo. O erro mais comum é solicitar todas as permissões na abertura do app: o usuário nega por reflexo, e o app nunca mais consegue pedir de volta (estado "denied permanently"). A regra é: solicitar no contexto certo, no momento em que faz sentido.

## Como Funciona

### Fluxo correto de permissão

```
1. Verificar status atual (não solicitar se já foi granted)
2. Se "not determined": mostrar explicação contextual (educacional) → então solicitar
3. Se "denied": mostrar mensagem com link para Ajustes do sistema
4. Se "granted": usar o recurso
```

### React Native — expo-permissions / react-native-permissions

```typescript
import {
  check,
  request,
  openSettings,
  PERMISSIONS,
  RESULTS,
  Permission
} from "react-native-permissions";

type PermissionStatus = "granted" | "denied" | "blocked" | "unavailable";

async function checkPermission(permission: Permission): Promise<PermissionStatus> {
  const result = await check(permission);

  switch (result) {
    case RESULTS.GRANTED: return "granted";
    case RESULTS.DENIED: return "denied"; // pode pedir novamente
    case RESULTS.BLOCKED: return "blocked"; // precisa ir em Ajustes
    case RESULTS.UNAVAILABLE: return "unavailable";
    default: return "denied";
  }
}

async function requestPermission(permission: Permission): Promise<PermissionStatus> {
  const result = await request(permission);

  if (result === RESULTS.BLOCKED) {
    // Única forma de desbloquear é o usuário ir manualmente em Ajustes
    return "blocked";
  }

  return result === RESULTS.GRANTED ? "granted" : "denied";
}

// Câmera — solicitar quando usuário toca em "Tirar foto"
export async function requestCameraPermission(): Promise<boolean> {
  const permission = Platform.select({
    ios: PERMISSIONS.IOS.CAMERA,
    android: PERMISSIONS.ANDROID.CAMERA
  })!;

  const status = await checkPermission(permission);
  if (status === "granted") return true;

  if (status === "blocked") {
    Alert.alert(
      "Câmera bloqueada",
      "Habilite o acesso à câmera em Ajustes > Privacidade.",
      [
        { text: "Cancelar", style: "cancel" },
        { text: "Abrir Ajustes", onPress: openSettings }
      ]
    );
    return false;
  }

  const finalStatus = await requestPermission(permission);
  return finalStatus === "granted";
}

// Localização — foreground vs background
export async function requestLocationPermission(): Promise<"always" | "whenInUse" | "denied"> {
  // Sempre solicitar "when in use" primeiro
  const whenInUse = Platform.select({
    ios: PERMISSIONS.IOS.LOCATION_WHEN_IN_USE,
    android: PERMISSIONS.ANDROID.ACCESS_FINE_LOCATION
  })!;

  const result = await request(whenInUse);
  if (result !== RESULTS.GRANTED) return "denied";

  // Solicitar "always" apenas se feature realmente precisar (ex: rastreamento de entrega)
  // iOS: só funciona depois de "when in use" já concedido
  if (needsBackgroundLocation) {
    const always = await request(PERMISSIONS.IOS.LOCATION_ALWAYS);
    return always === RESULTS.GRANTED ? "always" : "whenInUse";
  }

  return "whenInUse";
}
```

### React Native — Expo (Managed Workflow)

```typescript
import { Camera } from "expo-camera";
import * as Location from "expo-location";
import * as Notifications from "expo-notifications";
import * as MediaLibrary from "expo-media-library";

// Câmera
export function CameraScreen() {
  const [permission, requestPermission] = Camera.useCameraPermissions();

  if (!permission) return <LoadingScreen />;

  if (!permission.granted) {
    return (
      <View>
        <Text>Precisamos de acesso à câmera para fotografar seus produtos.</Text>
        <Button title="Conceder acesso" onPress={requestPermission} />
      </View>
    );
  }

  return <Camera style={{ flex: 1 }} />;
}

// Localização com granularidade
async function getCurrentLocation() {
  const { status } = await Location.requestForegroundPermissionsAsync();
  if (status !== "granted") return null;

  const location = await Location.getCurrentPositionAsync({
    accuracy: Location.Accuracy.Balanced
  });

  return location.coords;
}
```

### Flutter — permission_handler

```dart
import "package:permission_handler/permission_handler.dart";

class PermissionService {
  Future<bool> requestCamera() async {
    final status = await Permission.camera.status;

    if (status.isGranted) return true;

    if (status.isPermanentlyDenied) {
      await openAppSettings(); // abre Ajustes do sistema
      return false;
    }

    final result = await Permission.camera.request();
    return result.isGranted;
  }

  Future<bool> requestLocation() async {
    // Android: verificar se location services estão ativados
    final serviceEnabled = await Permission.location.serviceStatus.isEnabled;
    if (!serviceEnabled) return false;

    final status = await Permission.locationWhenInUse.request();
    return status.isGranted;
  }

  Future<bool> requestNotifications() async {
    // Android 13+ requer permissão explícita
    if (await Permission.notification.isDenied) {
      final status = await Permission.notification.request();
      return status.isGranted;
    }
    return await Permission.notification.isGranted;
  }

  // Solicitar múltiplas de uma vez (mostrar um dialog de contexto antes)
  Future<Map<Permission, PermissionStatus>> requestMultiple() async {
    return await [
      Permission.camera,
      Permission.microphone,
      Permission.photos
    ].request();
  }
}
```

### iOS — NSUsageDescription (Info.plist)

Toda permissão iOS precisa de uma string descritiva no Info.plist — sem ela, o app é rejeitado na App Store:

```xml
<key>NSCameraUsageDescription</key>
<string>Usamos a câmera para você fotografar produtos para venda.</string>

<key>NSLocationWhenInUseUsageDescription</key>
<string>Sua localização é usada para encontrar lojas próximas.</string>

<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>Usamos sua localização em segundo plano para rastreamento de entregas.</string>

<key>NSPhotoLibraryUsageDescription</key>
<string>Acesse sua galeria para escolher fotos de perfil.</string>

<key>NSMicrophoneUsageDescription</key>
<string>O microfone é usado para mensagens de voz.</string>
```

### Android — AndroidManifest.xml

```xml
<!-- Permissões normais (não requerem runtime request) -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.VIBRATE" />

<!-- Permissões perigosas (requerem runtime request) -->
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.READ_MEDIA_IMAGES" /> <!-- Android 13+ -->
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" /> <!-- Android 13+ -->

<!-- Background location requer justificativa adicional na Play Store -->
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

## Modelo de Request por Plataforma

| Permissão | iOS comportamento | Android comportamento |
|---|---|---|
| Câmera | 1 prompt, se negar → settings | 2 prompts antes de "never ask again" |
| Localização | "While using" obrigatório antes de "Always" | Fine/Coarse, background separado |
| Notificações | iOS 10+: 1 prompt | Android 13+: 1 prompt |
| Fotos | iOS 14+: acesso parcial disponível | READ_MEDIA_IMAGES Android 13+ |
| Microfone | 1 prompt | 2 prompts |

## Trade-offs

| Abordagem | UX | Conversão | Risco |
|---|---|---|---|
| Pedir tudo no launch | Ruim | Baixa | Usuário nega tudo |
| Pedir no contexto | Boa | Alta | Mais código condicional |
| Pedir com educação prévia | Ótima | Mais alta | Um passo a mais na UX |

## Quando Usar / Quando Evitar

**Solicite no momento exato de uso** — câmera quando o usuário toca em "Câmera", localização quando abre mapa.

**Mostre contexto educacional antes** de solicitar para permissões críticas (localização, câmera) — aumenta a taxa de concessão.

**Implemente o estado "blocked"** — link direto para Ajustes, nunca mostrar o dialog de permissão novamente (iOS não mostra mais, você ficará pedindo infinitamente sem sucesso).

**Localização background** — exige revisão manual na App Store/Play Store. Use apenas quando absolutamente necessário (entregador, rastreamento de corrida).

## Conceitos Relacionados
[[mobile-push-notifications]] · [[mobile-biometria]] · [[mobile-seguranca]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
