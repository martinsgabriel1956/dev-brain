---
type: source
title: "WebSocket Avançado e SSE"
aliases: ["websocket", "sse", "server-sent events", "realtime", "websocket cluster", "redis pubsub realtime"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/websocket-sse-realtime.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [websocket, sse, server-sent-events, realtime, redis-pubsub, heartbeat, socket-io]
skill: tech-mentor-backend
status: stable
---

## TL;DR

SSE para unidirecional (servidor → cliente): `Last-Event-ID` dá reconexão automática gratuita, simples sobre HTTP/1.1. WebSocket para bidirecional: full-duplex, mas stateful — problema em cluster. Solução cluster: Redis Pub/Sub como bus entre nodes (socket.io-redis-adapter). Autenticação: token no handshake (não em headers após upgrade). Heartbeat obrigatório para detectar conexões zumbis.

## Key Claims

**Claim:** SSE é superior ao WebSocket para comunicação unidirecional — reconexão automática via `Last-Event-ID` elimina lógica de retry no cliente.
**Evidence:** SSE: browser reconecta automaticamente com `Last-Event-ID: <último evento recebido>`. Server resume a partir desse ID. WebSocket: aplicação precisa implementar reconnect logic, backoff exponencial, e estado de reconexão manualmente. Para casos unidirecionais (notificações, feeds, status updates), SSE é mais simples, funciona sobre HTTP/1.1, e o browser faz o trabalho pesado.
**Confidence:** alta

**Claim:** WebSocket em cluster exige Redis Pub/Sub como bus — sem isso, mensagens não chegam a clientes em outros nodes.
**Evidence:** WebSocket é stateful: conexão persiste em um processo específico. Com múltiplos nodes: Node A tem conexão com Client 1, Node B com Client 2. Mensagem publicada no Node A não alcança Client 2. Solução: `socket.io-redis-adapter` → Node A faz `PUBLISH "channel" payload` no Redis, Node B (subscrito) recebe e entrega para Client 2. `io.to("room:xyz").emit()` funciona transparentemente em qualquer topologia de nodes.
**Confidence:** alta

**Claim:** Heartbeat é obrigatório para detectar conexões zumbis — sem ele, sockets mortos acumulam e travam recursos.
**Evidence:** Conexão zumbi: cliente desconecta sem fechar o socket (queda de rede, crash de processo). TCP não detecta imediatamente sem dados trafegando. Resultado: server mantém socket "aberto" indefinidamente, memória vaza. Heartbeat: server envia `ping` a cada 30s, cliente responde `pong`. Sem `pong` em X segundos → server fecha o socket. socket.io tem heartbeat nativo (`pingInterval`, `pingTimeout`).
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/websocket]]
- [[concepts/server-sent-events]]
- [[concepts/redis-pubsub]]
- [[concepts/heartbeat-protocol]]
- [[concepts/stateful-connections]]
- [[entities/socket-io]]

## Open Questions

- WebSocket vs WebRTC para colaboração em tempo real — quando a latência P2P do WebRTC justifica a complexidade (STUN/TURN/ICE)?
- Scaling WebSocket para 100k conexões simultâneas — quando socket.io-redis-adapter não é suficiente e precisa de solução dedicada (Ably, Pusher)?
