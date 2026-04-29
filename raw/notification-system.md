---
date: 2026-04-17
tags: [tech-mentor, system-design, notificacao, realtime, fanout]
skill: tech-mentor-system-design/references/design-cases
level: avançado
---

# Notification System Design

## Contexto
Sistema de notificações é um dos casos clássicos de system design — aparece em entrevistas e na prática. O desafio central é **fan-out**: um evento gera N notificações para N usuários por M canais.

## Arquitetura

```
Event Source (order.shipped, comment.added, etc.)
        │
        ▼
┌───────────────────┐
│  Notification     │  ← determina quem receber e por qual canal
│  Service          │
└────────┬──────────┘
         │
    ┌────┴─────────────────────────────┐
    ▼          ▼          ▼            ▼
┌───────┐ ┌───────┐ ┌──────────┐ ┌────────┐
│ Push  │ │ Email │ │ In-App   │ │  SMS   │
│(FCM/  │ │(Resend│ │(SSE/     │ │(Twilio)│
│ APNs) │ │/SES)  │ │WebSocket)│ │        │
└───────┘ └───────┘ └──────────┘ └────────┘
```

## Fan-out: Write vs. Read

**Fan-out on Write:** ao publicar o evento, gera e persiste notificações para todos os destinatários imediatamente.

```
OrderShipped → gera 1 notificação na tabela → para o dono do pedido ✓
CommentOnPost → gera N notificações → para cada seguidor do post ✗ (se N = 10M)
```

**Fan-out on Read:** armazena apenas o evento; ao usuário consultar, agrega dinamicamente.

**Regra de ouro:** para destinatários pequenos (< 1000), fan-out on write. Para conteúdo viral com muitos destinatários (Twitter, Instagram), fan-out on read — ou híbrido: usuários comuns usam fan-out on write, celebridades usam fan-out on read.

## Implementação

```typescript
// Schema
// notifications: id, user_id, type, title, body, data, channel, read_at, sent_at, created_at
// user_preferences: user_id, channel, enabled, quiet_hours_start, quiet_hours_end

// Notification Service
class NotificationService {
  async send(event: DomainEvent) {
    const recipients = await this.resolveRecipients(event);
    
    for (const userId of recipients) {
      const prefs = await this.prefsRepo.findByUser(userId);
      const channels = this.determineChannels(event.type, prefs);

      for (const channel of channels) {
        await this.queue.add(`send:${channel}`, {
          userId,
          eventType: event.type,
          payload: event.payload
        });
      }
    }
  }

  private async resolveRecipients(event: DomainEvent): Promise<string[]> {
    switch (event.type) {
      case "order.shipped":
        return [event.payload.customerId];
      case "post.comment":
        return [event.payload.postAuthorId, ...event.payload.otherCommenters];
      default:
        return [];
    }
  }
}
```

## Deduplicação

O mesmo evento pode ser processado mais de uma vez (at-least-once delivery). Sem deduplicação, o usuário recebe a mesma notificação múltiplas vezes.

```typescript
async function sendWithDedup(userId: string, eventId: string, channel: string) {
  const dedupKey = `notif:sent:${userId}:${eventId}:${channel}`;
  const alreadySent = await redis.set(dedupKey, "1", { NX: true, EX: 86400 });
  
  if (!alreadySent) return; // já enviado — skip

  await this.sendToChannel(userId, channel);
}
```

## Push — FCM (Android) e APNs (iOS)

```typescript
import admin from "firebase-admin";

async function sendPush(userId: string, notification: PushNotification) {
  const tokens = await deviceTokenRepo.findByUser(userId);
  
  const results = await admin.messaging().sendEachForMulticast({
    tokens,
    notification: { title: notification.title, body: notification.body },
    data: notification.data,
    apns: { payload: { aps: { badge: await getUnreadCount(userId) } } }
  });

  // Limpar tokens inválidos (dispositivo desinstalou o app)
  results.responses.forEach((result, idx) => {
    if (result.error?.code === "messaging/registration-token-not-registered") {
      deviceTokenRepo.delete(tokens[idx]);
    }
  });
}
```

## Quiet Hours e User Preferences

```typescript
function shouldSend(prefs: UserPreferences, channel: string): boolean {
  if (!prefs.channels[channel]?.enabled) return false;

  const now = new Date();
  const hour = now.getHours();
  const { quietStart, quietEnd } = prefs.channels[channel];

  if (quietStart < quietEnd) {
    return hour < quietStart || hour >= quietEnd; // janela simples (ex: 22-8)
  }
  return hour >= quietEnd && hour < quietStart; // cruza meia-noite (ex: 22-8)
}
```

## Email Bounce Handling

```typescript
// Webhook do Resend/SES para bounces
app.post("/webhooks/email", async (req, res) => {
  const { type, email } = req.body;

  if (type === "bounce" || type === "complaint") {
    // Marcar email como inválido — não tentar mais
    await userRepo.markEmailBounced(email);
    await this.unsubscribeFromEmail(email);
  }

  res.sendStatus(200);
});
```

## Conceitos Relacionados
[[websocket-sse-realtime]] · [[kafka]] · [[rate-limiting]] · [[redis-avancado]] · [[background-jobs]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
