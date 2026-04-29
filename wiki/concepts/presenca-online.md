---
type: concept
title: "Presença Online"
aliases: ["presence", "online status", "last seen", "indicador de presença"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, chat, presença, redis, kafka, escala]
skill: tech-mentor-system-design
status: stable
---

# Presença Online

Indicar se um usuário está online/offline e quando foi visto pela última vez. Um dos problemas mais caros de escalar em chat.

## Detecção

```
WebSocket conectado → usuário online
Client envia heartbeat a cada 10s → Chat Server atualiza Redis:
  key:   presence:{user_id}
  value: { status: "online", server_id: "chat-3", last_seen: timestamp }
  TTL:   30s

Ausência de heartbeat → TTL expira → offline automaticamente
```

## Propagação

```
Connect/disconnect → Chat Server publica no Kafka: topic presence.updates
  payload: { user_id, status, timestamp }

Presence Service consome:
  → Para cada contato: notifica via WS se estiver online
  → Atualiza last_seen no PostgreSQL
```

## O Problema de Escala

1B DAU × 500 contatos × N connects/disconnects/dia = volume explosivo de propagação.

**Solução pragmática**: propagar apenas para contatos **ativamente na tela de conversa** com o usuário. Demais contatos recebem `last_seen` no próximo acesso — sem push em tempo real.

## Trade-off

Consistência eventual aceitável para presença — atraso de alguns segundos no status é tolerável. Precisão absoluta exigiria coordenação inviável em escala.

## Key Sources

- [[sources/case-whatsapp]]
