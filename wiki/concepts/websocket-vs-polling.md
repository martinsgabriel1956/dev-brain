---
type: concept
title: "WebSocket vs Polling"
aliases: ["websocket", "long polling", "http polling", "sse"]
date_created: 2026-04-22
date_updated: 2026-11-10
source_count: 9
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

Chat server mantém estado de conexão — qual socket pertence a qual usuário. Isso torna escala horizontal não trivial. → [[wiki/concepts/chat-distribuido]]

## SSE (Server-Sent Events)

Alternativa unidirecional (server → client apenas). Mais simples que WebSocket para casos de notificação/feed. Usa HTTP/2 nativamente. Não substitui WebSocket quando o client também precisa enviar dados com baixa latência. Implementação prática, formato de mensagem, escala com Redis Pub/Sub e erros comuns de produção → [[wiki/concepts/server-sent-events]].

## Quando Usar

- WebSocket: chat, gaming, colaboração em tempo real, tracking
- SSE: notificações, dashboards de métricas, feeds
- Long Polling: fallback quando WebSocket não é suportado

## Polling não é uma escolha inferior — é uma escolha de escala

Para sistemas com poucos usuários simultâneos e tolerância a delay de segundos (relatório pronto para download, notificação não-crítica), polling simples é a resposta correta em entrevista: menor complexidade, sem infraestrutura extra, sem WebSocket. O erro comum é o oposto — meter WebSocket num sistema de baixa escala só para "parecer" mais robusto. Ver [[wiki/sources/updates-tempo-real-polling-sse-websocket]] para a moldura completa de "que pergunta o entrevistador está realmente fazendo" (escala horizontal, comunicação entre servidores, usuário offline) e por que WebSocket exige [[wiki/concepts/load-balancer|load balancer de camada 4]], nunca de camada 7.

## WebSocket em produção: segurança e backpressure

[[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]: WebSocket é contínuo/stateful (vs. request/response stateless), o que muda a autenticação ([[wiki/concepts/ticket-de-uso-unico-websocket]]) e exige **backpressure** entre WebSocket e SSH; o terminal web envia cada tecla e resize como mensagem ([[wiki/concepts/terminal-web-broker-websocket-ssh]]).

## Polling como Forma de Assíncrono

Polling de um endpoint de status com um ID de operação é uma das três formas de [[wiki/concepts/comunicacao-assincrona]] em [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]]; ver [[wiki/concepts/async-request-reply]].

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]] — WebSocket com ticket, sem cookies; backpressure WebSocket↔SSH
- [[wiki/sources/presence-system]] — Sistema de presença (online/offline) usa Heartbeat + Redis TTL: cliente envia ping a cada 15s, servidor atualiza `presence:{userId}` com SETEX 30s. Se TTL expirar, usuário está offline. Para...
- [[wiki/sources/case-whatsapp]]
- [[wiki/sources/server-sent-events-sse-tempo-real]] — implementação prática de SSE e long polling, erros comuns de produção
- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] — quando polling é a resposta certa em entrevista; LB L4 vs L7; erros mais comuns
- [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]] — WhatsApp citado como exemplo de arquitetura que exige LB de camada 4 por usar WebSocket (vídeo dedicado à arquitetura completa ainda não ingerido)
- [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]] — polling por ID de operação como forma de assíncrono
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — HTTP = pergunta/resposta pontual; WebSocket = conexão aberta bidirecional, ambos iniciados por negociação parecida

## Regra de escalada: polling → SSE → WebSocket (2026-11-10)

[[wiki/sources/polling-sse-websocket-comunicacao-em-tempo-real]] ordena as três técnicas da mais simples à mais poderosa e fecha com uma heurística: só vá para o WebSocket se polling e SSE não resolverem, porque ele traz gestão de conexão, perda de mensagem e limite em serverless. O polling descrito é *short polling* com cursor (timestamp da última alteração reenviado a cada pergunta), e o custo é aritmético: 1000 clientes a cada 2 s dão cerca de 500 req/s, quase todas vazias. Intervalo de 30 s a 1 min serve para dados lentos, como status de atividade.

**Ressalva sobre LB:** a regra "WebSocket exige LB de camada 4, nunca 7" acima vem de uma única fonte. A skill de backend faz proxy de WebSocket no nginx, que é camada 7, repassando `Upgrade`/`Connection` `[skill: tech-mentor-backend]`, e a RFC 6455 define o handshake como um HTTP Upgrade com resposta `101` ([external](https://datatracker.ietf.org/doc/html/rfc6455)). A leitura mais segura é que o LB L7 precisa suportar upgrade e conexões longas, não que seja proibido.

## Key sources (adição 2026-11-10)

- [[wiki/sources/polling-sse-websocket-comunicacao-em-tempo-real]] — regra de escalada polling → SSE → WebSocket; polling com cursor; custo 500 req/s; WebSocket não é bala de prata
