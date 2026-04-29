---
type: concept
title: "Notification System"
aliases: ["sistema de notificação", "notification system", "push email sms in-app"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, notificacao, fanout, push, fcm, apns, redis, filas]
skill: tech-mentor-system-design
status: stable
---

# Notification System

Case clássico de system design. Desafio central: **fan-out** — um evento gera N notificações para N usuários por M canais (Push/FCM/APNs, Email, In-App/SSE, SMS/Twilio).

## Arquitetura

```
Event Source (order.shipped, comment.added)
        │
        ▼
  Notification Service  ← resolve destinatários + preferências
        │
   ┌────┴──────────────────────────┐
   ▼         ▼         ▼          ▼
 Push      Email    In-App       SMS
(FCM/APNs)(Resend) (SSE/WS)   (Twilio)
```

## Fan-out: Write vs Read

Ver [[concepts/fanout-pattern]] para decisão de quando usar cada um.

**Regra rápida:**
- < 1000 destinatários → fan-out on write
- Conteúdo viral (Twitter, Instagram) → fan-out on read ou híbrido

## Deduplicação (obrigatória em at-least-once)

```typescript
async function sendWithDedup(userId: string, eventId: string, channel: string) {
  const dedupKey = `notif:sent:${userId}:${eventId}:${channel}`;
  const alreadySent = await redis.set(dedupKey, "1", { NX: true, EX: 86400 });
  if (!alreadySent) return;
  await this.sendToChannel(userId, channel);
}
```

## Push — FCM + Limpeza de Tokens

```typescript
const results = await admin.messaging().sendEachForMulticast({ tokens, notification, data });

results.responses.forEach((result, idx) => {
  if (result.error?.code === "messaging/registration-token-not-registered") {
    deviceTokenRepo.delete(tokens[idx]); // app desinstalado — limpar imediatamente
  }
});
```

## Quiet Hours

```typescript
function shouldSend(prefs: UserPreferences, channel: string): boolean {
  if (!prefs.channels[channel]?.enabled) return false;
  const hour = new Date().getHours();
  const { quietStart, quietEnd } = prefs.channels[channel];

  if (quietStart < quietEnd) {
    return hour < quietStart || hour >= quietEnd; // janela simples: 22h–08h
  }
  return hour >= quietEnd && hour < quietStart;   // cruza meia-noite
}
```

## Email Bounce Handling

```typescript
app.post("/webhooks/email", async (req, res) => {
  const { type, email } = req.body;
  if (type === "bounce" || type === "complaint") {
    await userRepo.markEmailBounced(email);
    await this.unsubscribeFromEmail(email);
  }
  res.sendStatus(200);
});
```

Ignorar bounces = IP/domínio na blacklist = deliverability cai globalmente.

## Schema Mínimo

```
notifications:       id, user_id, type, title, body, data, channel, read_at, sent_at, created_at
user_preferences:    user_id, channel, enabled, quiet_hours_start, quiet_hours_end
device_tokens:       user_id, token, platform (fcm|apns), created_at
```

## Key Sources

- [[sources/notification-system]]
