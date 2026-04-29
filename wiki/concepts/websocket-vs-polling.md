---
type: concept
title: "WebSocket vs Polling"
aliases: ["websocket", "long polling", "http polling", "sse"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, websocket, realtime, protocolo, chat]
skill: tech-mentor-system-design
status: stable
---

# WebSocket vs Polling

Três formas de receber dados do servidor em tempo real — com trade-offs bem diferentes.

## Comparativo

```
HTTP Polling:
  Client pergunta a cada Ns → "tem mensagem?" → "não" / "não" / "sim"
  Latência = intervalo de polling
  Overhead: 1 request HTTP por pergunta

Long Polling:
  Client abre request → Server segura até ter dado ou timeout → responde → client reabre
  Melhor latência, mas overhead HTTP por mensagem permanece

WebSocket:
  Handshake HTTP → upgrade → conexão bidirecional persistente
  Server empurra dados ao client sem solicitação
  ✅ Latência mínima (dezenas de ms)
  ✅ Full-duplex: client e server enviam a qualquer momento
  ✅ 1 socket por usuário (vs múltiplas conexões HTTP)
```

## Problema do WebSocket: Estado

Chat server mantém estado de conexão — qual socket pertence a qual usuário. Isso torna escala horizontal não trivial. → [[concepts/chat-distribuido]]

## SSE (Server-Sent Events)

Alternativa unidirecional (server → client apenas). Mais simples que WebSocket para casos de notificação/feed. Usa HTTP/2 nativamente. Não substitui WebSocket quando o client também precisa enviar dados com baixa latência.

## Quando Usar

- WebSocket: chat, gaming, colaboração em tempo real, tracking
- SSE: notificações, dashboards de métricas, feeds
- Long Polling: fallback quando WebSocket não é suportado

## Key Sources

- [[sources/case-whatsapp]]
