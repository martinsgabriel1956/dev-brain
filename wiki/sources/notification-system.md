---
type: source
title: "Notification System Design"
aliases: ["notification system", "sistema de notificação", "fanout", "push notifications"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 0
tags: [system-design, notificacao, fanout, push, fcm, apns, deduplicacao, quiet-hours]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-study/raw/notification-system.md
source_url: ""
author: ""
date_published: 2026-04-17
date_ingested: 2026-04-22
---

# Notification System Design

## TL;DR

Fan-out é o desafio central: um evento → N usuários × M canais. Regra: fan-out on write para < 1000 destinatários; fan-out on read (ou híbrido) para conteúdo viral. Deduplicação via Redis SET NX é obrigatória em at-least-once delivery. Tokens FCM inválidos devem ser deletados imediatamente.

## Key Claims

**Claim:** Fan-out on write é preferível para audiências pequenas; fan-out on read para conteúdo viral com muitos destinatários.
**Evidence:** Fan-out on write: gera e persiste notificações para todos os destinatários no momento do evento — simples, mas impraticável para 10M seguidores. Fan-out on read: armazena só o evento, agrega dinamicamente na consulta. Híbrido: usuários comuns = write, celebridades = read (Twitter/Instagram).
**Confidence:** alta

**Claim:** Deduplicação via Redis SET NX é obrigatória em sistemas com at-least-once delivery.
**Evidence:** `redis.set(dedupKey, "1", { NX: true, EX: 86400 })` — se já enviado, NX falha e skip. Sem isso, retry de queue envia a mesma notificação múltiplas vezes para o usuário.
**Confidence:** alta

**Claim:** Tokens FCM inválidos (`messaging/registration-token-not-registered`) devem ser deletados imediatamente para evitar acúmulo de dead tokens.
**Evidence:** `sendEachForMulticast` retorna resultado por token. Erro `registration-token-not-registered` = app desinstalado. Manter token = tentar entregar para dispositivo que não tem mais o app.
**Confidence:** alta

**Claim:** Quiet hours requer lógica especial para janelas que cruzam meia-noite.
**Evidence:** Janela simples (22h–08h): `hour < quietStart || hour >= quietEnd`. Janela que cruza meia-noite inverte a lógica. Sem esse tratamento, notificações chegam no horário errado para usuários em timezones específicos.
**Confidence:** alta

**Claim:** Bounce handling de email via webhook é obrigatório — ignorar bounces leva à penalização do domínio por provedores de email.
**Evidence:** Resend/SES enviam webhook `bounce`/`complaint`. Sem tratamento: IP/domínio vai para blacklist, deliverability cai globalmente. Ação: marcar email como inválido e desinscrever.
**Confidence:** alta

## Concepts & Entities Touched

[[concepts/notification-system]] · [[concepts/fanout-pattern]] · [[concepts/idempotencia]] · [[concepts/distributed-lock]] · [[concepts/ack-triplo]] · [[concepts/presenca-online]]

## Open Questions

- Fan-out híbrido — onde fica o threshold exato (1000? 10000 seguidores)?
- Notification batching (agrupar N notificações em 1) — como modelar no schema?
- Timezone-aware quiet hours em escala global — banco de timezone por usuário?
