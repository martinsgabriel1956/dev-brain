---
type: concept
title: "Chat Distribuído"
aliases: ["cross-server chat", "chat distribuído", "websocket routing"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, chat, websocket, redis, kafka, distribuído]
skill: tech-mentor-system-design
status: stable
---

# Chat Distribuído

Problema de roteamento de mensagem quando sender e receiver estão conectados em chat servers diferentes.

## O Problema

```
Chat Server 1 (usuário A)  ←?→  Chat Server 2 (usuário B)
Cada server conhece apenas suas conexões WebSocket locais.
```

## Solução: Message Broker

```
Chat Server 1 (A) → publica: channel:user_B_id
Chat Server 2 (B) → subscreveu: channel:user_B_id → recebe → envia via WS para B
```

## Redis Pub-Sub vs Kafka

| | Redis Pub-Sub | Kafka |
|---|---|---|
| Latência | Sub-ms | Alguns ms |
| Persistência | Não (fire and forget) | Sim (log persistente) |
| Ideal para | Mensagens diretas online | Grupos grandes, garantia de entrega |

- **1:1 online**: Redis Pub-Sub — baixa latência, sem necessidade de persistência
- **Grupos com 256 membros**: Kafka com topic por grupo — fan-out escalável
- **Chat Server cai**: mensagens no Redis Pub-Sub podem ser perdidas → Kafka resolve com offset replay

## Reconexão

Client cai → reconecta em outro Chat Server → busca pending_messages no Cassandra → ACKs em ordem.

## Key Sources

- [[sources/case-whatsapp]]
