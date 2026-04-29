---
type: source
title: "Presence System — Online/Offline em Tempo Real"
aliases: ["presence", "online offline", "heartbeat", "typing indicator"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [presence-system, heartbeat, redis-ttl, websocket, typing-indicator, real-time, system-design]
skill: tech-mentor-system-design
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/presence-system.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# Presence System — Online/Offline em Tempo Real

## TL;DR

Sistema de presença (online/offline) usa Heartbeat + Redis TTL: cliente envia ping a cada 15s, servidor atualiza `presence:{userId}` com SETEX 30s. Se TTL expirar, usuário está offline. Para múltiplos nodes, Redis Pub/Sub propaga mudanças de presença. Typing indicator usa TTL curto (~3s) com debounce no cliente. Desafio de escala: propagar para contatos relevantes sem fan-out excessivo.

## Key Claims

| Claim | Evidência |
|---|---|
| Heartbeat a cada 15s com TTL 30s — dobro garante tolerância a 1 falha | Padrão documentado |
| Redis TTL é o mecanismo de offline detection — nenhum evento explícito necessário | SETEX renova; expiração = offline |
| Reconexão automática no cliente: onclose dispara setTimeout(3000) | Reconecta sem intervenção do usuário |
| Typing indicator: TTL 3s + debounce 1s no cliente evita flood | Emite `typing` no keydown, não em cada tecla |
| Multi-node: Redis Pub/Sub para propagar presença entre nodes de WebSocket | Cada node subscreve ao canal de presença dos usuários conectados nele |

## Conceitos

- [[concepts/presenca-online]] — já existe no index
- [[concepts/websocket-vs-polling]] — transporte do heartbeat
- [[concepts/chat-distribuido]] — context de uso do presence system
- [[concepts/redis-geo]] — complemento para presença geolocalizada

## Key Sources

_Este é o documento primário._
