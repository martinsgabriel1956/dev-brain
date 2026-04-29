---
type: concept
title: "Realtime Tracking"
aliases: ["tracking em tempo real", "location tracking", "websocket tracking"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, websocket, kafka, realtime, localização, uber]
skill: tech-mentor-system-design
status: stub
---

# Realtime Tracking

Propagação de posição do motorista para o passageiro em tempo real após o match.

## Fluxo

```
Motorista app → WebSocket → Location Service
  → Redis GEOADD: atualiza posição ativa
  → Kafka publish: topic ride.{ride_id}.location
        ↓
  Passenger app (subscrito via WebSocket)
  → Recebe update a cada 4s
  → Renderiza no mapa
```

## Precisão por Contexto

- **Durante corrida (mapa do passageiro):** geohash 7 chars (~150m × 150m)
- **Detecção de chegada:** geohash 8 chars (~38m × 19m)

## Por que Kafka e Não WebSocket Direto

Kafka desacopla Location Service do Passenger WebSocket Service. Se o Passenger Service reiniciar, retoma a partir do offset do tópico. Location Service não precisa saber quantos passageiros estão ouvindo.

## Key Sources

- [[sources/case-uber]]
