---
type: concept
title: "Push Notifications Mobile — FCM, APNs"
aliases: ["fcm push", "apns push ios", "firebase cloud messaging", "onesignal mobile"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, push-notifications, fcm, apns, onesignal, deep-links]
skill: tech-mentor-mobile
status: stable
---

# Push Notifications Mobile

## Arquitetura

```
Seu Servidor → FCM/APNs → Dispositivo
                ↑
         Token FCM/APNs (por dispositivo)
```

## FCM Setup (React Native)

```ts
// Obter e salvar token
const token = await messaging().getToken();
await api.updateDeviceToken(user.id, token);

// Token muda — listener obrigatório
messaging().onTokenRefresh(newToken => {
    api.updateDeviceToken(user.id, newToken);
});

// Foreground
messaging().onMessage(async remoteMessage => {
    showLocalNotification(remoteMessage);
});

// Background/killed — handler fora do componente
messaging().setBackgroundMessageHandler(async remoteMessage => {
    // processar silenciosamente
});

// Cold start — app aberto via notificação
const initialNotification = await messaging().getInitialNotification();
if (initialNotification) navigateToScreen(initialNotification.data);
```

## APNs — iOS

Certificado `.p8` (AuthKey) preferível ao `.p12` — não expira. Upload em Firebase Console ou APNs direto.

```
Payload máximo: 4KB
Priority: 10 (imediato) ou 5 (conserve bateria)
```

## Payload

```json
{
  "notification": { "title": "Pedido confirmado!", "body": "Seu pedido #1234 foi aceito." },
  "data": { "type": "ORDER_CONFIRMED", "orderId": "1234", "deepLink": "/orders/1234" },
  "apns": { "payload": { "aps": { "sound": "default", "badge": 1 } } }
}
```

## Quiet Hours

Implementar no servidor — considerar fuso horário do usuário:

```ts
function shouldSend(user: User, now: Date): boolean {
    const userTime = toZonedTime(now, user.timezone);
    const hour = userTime.getHours();
    return hour >= 8 && hour < 22;
}
```

## Ver também

- [[mobile-deep-links]] — deep link no payload de notificação
- [[mobile-permissoes]] — solicitar permissão de notificação

## Key Sources

- [[wiki/sources/mobile-push-notifications]]
