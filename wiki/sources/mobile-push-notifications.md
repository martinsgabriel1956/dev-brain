---
type: source
title: "Push Notifications — FCM, APNs, OneSignal"
aliases: ["push notifications mobile", "fcm firebase", "apns ios push", "onesignal"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-push-notifications.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, push-notifications, fcm, apns, onesignal, deep-links, quiet-hours]
skill: tech-mentor-mobile
status: stable
---

# Push Notifications — Mobile

## TL;DR

FCM (Firebase Cloud Messaging) para Android e iOS (via APNs bridge). Token FCM é por dispositivo/app — armazenar no servidor com userId. Payload máximo: 4KB (FCM) / 4KB (APNs). Quiet hours e frequência controlada no servidor — não no cliente. Deep link em notificação exige handling de cold start (app fechado) e warm start (app em background).

## Claims Principais

| Claim | Confiança |
|---|---|
| Token FCM muda em reinstall/clear data — listener `onTokenRefresh` obrigatório | Alta |
| APNs requer certificado p8 ou p12 — p8 (AuthKey) não expira, preferível | Alta |
| Payload > 4KB silenciosamente ignorado — comprimir dados ou usar data-only notification | Alta |
| Notificação no cold start: `getInitialNotification()` antes de `setBackgroundMessageHandler` | Alta |
| Quiet hours no servidor — respeitar fuso horário do usuário, não do servidor | Alta |

## Conceitos Abordados

- [[mobile-push-notifications]] · [[mobile-deep-links]] · [[mobile-navegacao]] · [[mobile-permissoes]]
