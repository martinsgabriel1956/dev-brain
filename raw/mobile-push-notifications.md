---
date: 2026-04-23
tags: [tech-mentor, mobile, push-notifications, apns, fcm, firebase, react-native, flutter]
skill: tech-mentor-mobile/references/push-notifications
level: intermediário
---

# Push Notifications — APNs + FCM

## Contexto
Push notifications são o canal de retenção mais direto de um app mobile. A complexidade está na diferença entre iOS (APNs — Apple Push Notification service) e Android (FCM — Firebase Cloud Messaging), no tratamento de foreground/background, e na gestão de tokens de dispositivo. Um sistema de push robusto vai além de "mandar notificação" — inclui segmentação, entrega garantida e rastreamento de abertura.

## Como Funciona

### Arquitetura geral

```
Seu Backend → FCM/APNs → Sistema Operacional → App
```

O backend nunca fala direto com o device. FCM é o broker para Android (e opcionalmente iOS). APNs é obrigatório para iOS em produção — FCM faz o relay para APNs.

```
Backend → FCM HTTP v1 API → APNs → iPhone
                          → Android Device diretamente
```

### React Native — Expo Notifications (Managed Workflow)

```typescript
import * as Notifications from "expo-notifications";
import * as Device from "expo-device";

// Configurar handler (foreground)
Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,
    shouldPlaySound: true,
    shouldSetBadge: true
  })
});

// Registrar e obter token
export async function registerForPushNotifications(): Promise<string | null> {
  if (!Device.isDevice) {
    console.log({ message: "Push notifications requerem device físico" });
    return null;
  }

  const { status: existingStatus } = await Notifications.getPermissionsAsync();
  let finalStatus = existingStatus;

  if (existingStatus !== "granted") {
    const { status } = await Notifications.requestPermissionsAsync();
    finalStatus = status;
  }

  if (finalStatus !== "granted") return null;

  const token = await Notifications.getExpoPushTokenAsync({
    projectId: process.env.EXPO_PUBLIC_PROJECT_ID
  });

  // Salvar no backend associado ao usuário
  await http.post("/devices/register", { token: token.data });

  return token.data;
}

// Listeners
export function useNotificationListeners() {
  useEffect(() => {
    // App em foreground recebeu notificação
    const foregroundSub = Notifications.addNotificationReceivedListener(notification => {
      console.log({ message: "Notificação recebida em foreground", notification });
    });

    // Usuário tocou na notificação
    const responseSub = Notifications.addNotificationResponseReceivedListener(response => {
      const data = response.notification.request.content.data;
      // navegar para tela correta via deep link
      handleNotificationTap(data);
    });

    return () => {
      foregroundSub.remove();
      responseSub.remove();
    };
  }, []);
}
```

### React Native — FCM direto (bare workflow / react-native-firebase)

```typescript
import messaging from "@react-native-firebase/messaging";

export async function setupFCM() {
  // Solicitar permissão (iOS)
  const authStatus = await messaging().requestPermission();
  const enabled =
    authStatus === messaging.AuthorizationStatus.AUTHORIZED ||
    authStatus === messaging.AuthorizationStatus.PROVISIONAL;

  if (!enabled) return;

  // Token FCM
  const fcmToken = await messaging().getToken();
  await http.post("/devices/register", { token: fcmToken, platform: Platform.OS });

  // Refresh de token
  messaging().onTokenRefresh(newToken => {
    http.post("/devices/register", { token: newToken, platform: Platform.OS });
  });
}

// Background message handler — FORA do componente, no index.js
messaging().setBackgroundMessageHandler(async remoteMessage => {
  console.log({ message: "Notificação em background", data: remoteMessage.data });
});

// Foreground
const unsubscribe = messaging().onMessage(async remoteMessage => {
  // Exibir local notification pois FCM não mostra UI em foreground
  await displayLocalNotification(remoteMessage);
});
```

### Flutter — firebase_messaging

```dart
// main.dart
@pragma("vm:entry-point")
Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  await Firebase.initializeApp();
  // processar mensagem em background/terminated
}

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
  FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);
  runApp(const App());
}

// Serviço de notificação
class PushNotificationService {
  final FirebaseMessaging _messaging = FirebaseMessaging.instance;

  Future<void> initialize() async {
    final settings = await _messaging.requestPermission(
      alert: true,
      badge: true,
      sound: true,
    );

    if (settings.authorizationStatus == AuthorizationStatus.authorized) {
      final token = await _messaging.getToken();
      await _registerToken(token!);
      _messaging.onTokenRefresh.listen(_registerToken);
    }

    // Foreground
    FirebaseMessaging.onMessage.listen(_handleForegroundMessage);

    // App aberto via notificação (background → foreground)
    FirebaseMessaging.onMessageOpenedApp.listen(_handleNotificationTap);

    // App aberto via notificação (terminated)
    final initialMessage = await _messaging.getInitialMessage();
    if (initialMessage != null) _handleNotificationTap(initialMessage);
  }

  void _handleForegroundMessage(RemoteMessage message) {
    // Exibir flutter_local_notifications
  }

  void _handleNotificationTap(RemoteMessage message) {
    final route = message.data["route"] as String?;
    if (route != null) router.go(route);
  }
}
```

### Backend — Envio via FCM HTTP v1

```typescript
import { GoogleAuth } from "google-auth-library";

const FCM_ENDPOINT = "https://fcm.googleapis.com/v1/projects/PROJECT_ID/messages:send";

async function sendPushNotification(
  tokens: string[],
  title: string,
  body: string,
  data?: Record<string, string>
) {
  const auth = new GoogleAuth({ scopes: ["https://www.googleapis.com/auth/firebase.messaging"] });
  const client = await auth.getClient();
  const accessToken = await client.getAccessToken();

  // FCM suporta até 500 tokens por batch
  const batches = chunk(tokens, 500);

  for (const batch of batches) {
    await Promise.all(
      batch.map(token =>
        fetch(FCM_ENDPOINT, {
          method: "POST",
          headers: {
            Authorization: `Bearer ${accessToken.token}`,
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            message: {
              token,
              notification: { title, body },
              data: data ?? {},
              android: { priority: "high" },
              apns: {
                headers: { "apns-priority": "10" },
                payload: { aps: { sound: "default", badge: 1 } }
              }
            }
          })
        })
      )
    );
  }
}
```

## Trade-offs

| Aspecto | Expo Notifications | react-native-firebase | firebase_messaging (Flutter) |
|---|---|---|---|
| Setup | Mínimo | Médio | Médio |
| Token | Expo Push Token | FCM Token | FCM Token |
| Background | Automático | Manual (index.js) | Manual (top-level handler) |
| Customização | Limitada | Total | Total |
| Enterprise | Não recomendado | Sim | Sim |

## Quando Usar / Quando Evitar

**Use Expo Notifications** para MVPs e apps Managed Workflow — zero config de certificados.

**Use firebase_messaging direto** quando precisar de: notificações silenciosas, data-only messages, customização de ícone/som Android, ou quando você tem um backend que fala FCM diretamente.

**Sempre implemente:** token refresh (tokens expiram/mudam), remoção de token no logout, e o handler de notificação quando o app estava terminated (não só background).

**Nunca:** guardar token FCM sem associar ao usuário no backend, ignorar o estado de permissão (usuário pode revogar a qualquer momento).

## Conceitos Relacionados
[[mobile-deep-links]] · [[mobile-permissoes]] · [[mobile-armazenamento-local]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
