---
type: source
title: "Case: WhatsApp"
aliases: ["whatsapp system design", "chat em tempo real", "case whatsapp"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, cases, whatsapp, websocket, mensagens, presença, cassandra]
skill: tech-mentor-system-design
source_file: /home/gabriel-martins/Documentos/dev-study/raw/case-whatsapp.md
source_url: ""
author: "tech-mentor skill"
date_published: 2026-03-29
date_ingested: 2026-04-22
status: stable
---

# Case: WhatsApp

## TL;DR

Chat expõe os limites de arquitetura stateless: WebSocket exige estado de conexão por usuário, cross-server delivery requer broker (Redis Pub-Sub), e presença real-time não escala para todos os contatos — só para quem está ativamente na conversa. Cassandra para escrita intensa com TTL nativo. ACK triplo com idempotência via client_message_id.

## Key Claims

- **WebSocket, não HTTP polling** — full-duplex, baixa latência, 1 conexão por usuário. Polling tem latência = intervalo; Long Polling tem overhead HTTP por mensagem. → [[concepts/websocket-vs-polling]]
- **Cross-server delivery via Redis Pub-Sub** — A e B podem estar em chat servers diferentes. Redis Pub-Sub roteia via channel:{user_id}. Para grupos grandes: Kafka por tópico de grupo. → [[concepts/chat-distribuido]]
- **ACK triplo com idempotência** — enviado ✓, entregue ✓✓, lido ✓✓ azul. client_message_id garante idempotência em reconexão. → [[concepts/ack-triplo]]
- **Presença escalável: só contatos ativos na tela** — propagar para todos os 500 contatos de cada usuário com 1B DAU é inviável. Demais recebem last_seen no próximo acesso. → [[concepts/presenca-online]]
- **Cassandra para storage de mensagens** — 1.15M writes/s, TTL nativo, scale linear, sem joins necessários. partition_key = conversation_id, clustering_key = Snowflake ID DESC. → [[concepts/cassandra-schema]]
- **Mídia via presigned URL + S3** — não passa pelo Chat Server. Client sobe direto para S3, mensagem carrega CDN URL. → [[concepts/media-upload-pattern]]
- **Delivery offline: pending_messages com TTL 30 dias** — push notification (FCM/APNs) acorda o app, reconexão faz flush da fila.

## Scale Numbers

```
2B usuários registrados
1B DAU
100B mensagens/dia = 1.15M msg/s
48GB/s de mídia uploaded = ~4PB/dia
Latência entrega online: < 100ms p99
```

## Entities

- [[entities/cassandra]]
- [[entities/redis]]
- [[entities/kafka]]
- [[entities/whatsapp]]

## Concepts

[[concepts/websocket-vs-polling]] · [[concepts/chat-distribuido]] · [[concepts/ack-triplo]] · [[concepts/presenca-online]] · [[concepts/cassandra-schema]] · [[concepts/media-upload-pattern]] · [[concepts/snowflake-id]]

## Open Questions

- Signal Protocol end-to-end: como ACK de leitura funciona sem o servidor ler o conteúdo?
- Fan-out em grupos de 256 — threshold para trocar Redis Pub-Sub por Kafka?

## Raw Quotes

> "Chat em tempo real expõe os limites de arquiteturas stateless."

> "Presença: propagar para todos os contatos é inviável. Só para quem está ativamente na tela."

> "client_message_id como chave de idempotência — evita duplicatas no DB em reconexão."
