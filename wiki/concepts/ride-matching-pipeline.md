---
type: concept
title: "Ride Matching Pipeline"
aliases: ["matching pipeline", "driver matching", "pipeline de matching"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, matching, uber, pipeline, latencia]
skill: tech-mentor-system-design
status: stable
---

# Ride Matching Pipeline

Pipeline de 5 etapas para encontrar o melhor motorista para um passageiro em <1s.

## Fluxo

```
[1] Passageiro solicita corrida
    → Location Service: GEOSEARCH raio 2km
    → candidatos com distância euclidiana

[2] ETA Calculation Service
    → Top 10 por distância
    → Routing Service (OSRM self-hosted ou Google Maps)
    → ETA real considerando tráfego — distância ≠ ETA

[3] Ranking
    → Score = f(ETA, rating do motorista, tipo do veículo)
    → Ordena candidatos por score

[4] Oferta ao melhor candidato
    → Push notification + WebSocket para app do motorista
    → Timeout: 10s para aceitar

[5] Aceite/Rejeição
    → Aceite: match confirmado, lock permanece
    → Rejeição/timeout: libera lock, oferta para próximo
    → Lista esgotada: expande raio para 4km, repete
```

## Race Condition no Passo 4

Dois passageiros podem receber oferta do mesmo motorista. → [[concepts/distributed-lock]]

## ETA vs Distância Euclidiana

GEOSEARCH retorna distância em linha reta. ETA real depende de tráfego, ruas de mão única, semáforos. Routing Service é obrigatório para ranking preciso.

## Scale

278 matches/s × 10 ETA calls = 2.780 routing req/s. OSRM self-hosted suporta ~5k req/s por nó — 1-2 nós suficientes.

## Key Sources

- [[sources/case-uber]]
