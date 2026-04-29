---
type: concept
title: "ACK Triplo"
aliases: ["triple ack", "message delivery ack", "enviado entregue lido", "ack de mensagem"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, chat, mensagens, protocolo, idempotencia, whatsapp]
skill: tech-mentor-system-design
status: stable
---

# ACK Triplo

Protocolo de confirmação de entrega em 3 estados: enviado, entregue, lido. Base do modelo ✓ / ✓✓ / ✓✓ azul do WhatsApp.

## Fluxo

```
[1] A envia mensagem
    Client gera client_message_id (UUID local)
    Envia via WebSocket para Chat Server

[2] Chat Server persiste no Cassandra
    Gera server_message_id (Snowflake ID)
    Retorna ACK → { client_id, server_id }
    → A mostra ✓ (tick cinza = enviado)

[3] Chat Server entrega para B
    B online  → envia via WS diretamente
    B offline → pending_messages + push notification (FCM/APNs)

[4] B recebe → envia ACK de entrega
    → A mostra ✓✓ (dois ticks cinzas = entregue)

[5] B abre a conversa → lê → envia ACK de leitura
    → A mostra ✓✓ azul (lido)
```

## Idempotência com client_message_id

Se WebSocket cair entre envio e ACK do server, client reenvia a mensagem. Server usa `client_message_id` como chave de idempotência — evita duplicatas no Cassandra.

```
INSERT INTO messages (...) IF NOT EXISTS  -- Cassandra lightweight transaction
WHERE client_message_id = :uuid
```

## Offline: Push Notification

FCM (Android) / APNs (iOS) acorda o app quando há mensagens pendentes. App abre WebSocket, busca pending_messages, envia ACKs em ordem cronológica (Snowflake ID).

## Key Sources

- [[sources/case-whatsapp]]
