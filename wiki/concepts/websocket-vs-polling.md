---
type: concept
title: "WebSocket vs Polling"
aliases: ["websocket", "long polling", "http polling", "sse"]
date_created: 2026-04-22
date_updated: 2026-07-03
source_count: 3
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

Alternativa unidirecional (server → client apenas). Mais simples que WebSocket para casos de notificação/feed. Usa HTTP/2 nativamente. Não substitui WebSocket quando o client também precisa enviar dados com baixa latência. Implementação prática, formato de mensagem, escala com Redis Pub/Sub e erros comuns de produção → [[wiki/concepts/server-sent-events]].

## Quando Usar

- WebSocket: chat, gaming, colaboração em tempo real, tracking
- SSE: notificações, dashboards de métricas, feeds
- Long Polling: fallback quando WebSocket não é suportado

## Polling não é uma escolha inferior — é uma escolha de escala

Para sistemas com poucos usuários simultâneos e tolerância a delay de segundos (relatório pronto para download, notificação não-crítica), polling simples é a resposta correta em entrevista: menor complexidade, sem infraestrutura extra, sem WebSocket. O erro comum é o oposto — meter WebSocket num sistema de baixa escala só para "parecer" mais robusto. Ver [[wiki/sources/updates-tempo-real-polling-sse-websocket]] para a moldura completa de "que pergunta o entrevistador está realmente fazendo" (escala horizontal, comunicação entre servidores, usuário offline) e por que WebSocket exige [[wiki/concepts/load-balancer|load balancer de camada 4]], nunca de camada 7.

## Key Sources

- [[sources/case-whatsapp]]
- [[wiki/sources/server-sent-events-sse-tempo-real]] — implementação prática de SSE e long polling, erros comuns de produção
- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] — quando polling é a resposta certa em entrevista; LB L4 vs L7; erros mais comuns
