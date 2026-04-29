---
date: 2026-03-29
tags: [tech-mentor, system-design, cases, uber, geolocalização, matching, geohash]
skill: tech-mentor-system-design/references/system-design-cases
level: arquiteto
---

# Case: Ride-sharing (Uber)

## Contexto

Ride-sharing concentra dois problemas de system design que raramente aparecem juntos: **geolocalização em tempo real com escrita intensa** (5M motoristas atualizando posição a cada 4s) e **matching eficiente** (encontrar o motorista certo para um passageiro em milissegundos). A solução exige estruturas de dados especializadas para busca geoespacial e uma pipeline de decisão que equilibra latência com qualidade do match.

---

## Requisitos

**Funcionais:**
- Passageiro solicita corrida com origem e destino
- Sistema encontra motoristas disponíveis próximos
- Calcula ETA para cada motorista candidato
- Oferece corrida ao melhor match; motorista aceita ou rejeita
- Tracking da corrida em tempo real (passageiro vê motorista no mapa)

**Não-funcionais:**
```
5M motoristas ativos simultâneos
Atualização de posição: a cada 4 segundos por motorista
5M × (86.400 / 4) = 108M location updates/dia
Matching latência: < 1s do pedido ao motorista receber a oferta
Disponibilidade: 99,99% (corrida bloqueada = receita perdida diretamente)
```

---

## O Problema de Localização

### Escrita intensa de posição

```
5M motoristas × 1 update/4s = 1.25M writes/segundo

Opções de storage:
  PostgreSQL + PostGIS: ótimo para queries geoespaciais, write throughput limitado
  Redis GEO: estrutura nativa para lat/lng + busca por raio, O(N+log M) para range queries
              writes de 1.25M/s → Redis cluster suporta facilmente
```

Redis é a escolha para o estado atual de localização dos motoristas — dados quentes, altamente voláteis, não precisam de durabilidade forte.

### Geohash — Indexação Geoespacial

Busca "todos os motoristas em raio de 1km" via latitude/longitude bruta requer calcular distância para cada um dos 5M motoristas — inviável.

**Geohash** divide o mapa em células de tamanho progressivo, representadas como strings. Células geograficamente próximas compartilham prefixo da string.

```
Precisão do geohash:
  4 chars → ~39km × 20km  (escala de cidade)
  5 chars → ~4.9km × 4.9km
  6 chars → ~1.2km × 0.6km  ← usado para matching (raio de ~1km)
  7 chars → ~150m × 150m   ← usado para tracking em tempo real
  8 chars → ~38m × 19m

Exemplo:
  Av. Paulista, SP: -23.5617, -46.6558 → geohash "6gyf4m"
  Rua próxima 200m de distância        → geohash "6gyf4m" (mesmo prefixo!)
```

**Busca por raio**: pegar geohash da célula do passageiro + 8 células adjacentes → filtrar motoristas nessas células. Sem calcular distância para todos os 5M.

```python
# Redis GEO commands
import redis

r = redis.Redis()

# Motorista atualiza posição (a cada 4s)
r.geoadd("drivers:active", -46.6558, -23.5617, "driver:42")

# Buscar motoristas em raio de 2km, ordenado por distância
nearby = r.geosearch(
    "drivers:active",
    longitude=-46.6558,
    latitude=-23.5617,
    radius=2,
    unit="km",
    withcoord=True,
    withdist=True,
    sort="ASC",
    count=20
)
# → [("driver:42", 0.3, (-46.6558, -23.5617)), ...]
```

---

## Pipeline de Matching

```
[1] Passageiro solicita corrida
    → Location Service: encontrar motoristas em raio de 2km
      → Redis GEOSEARCH → lista de candidatos com distância euclidiana

[2] ETA Calculation Service
    → Para cada candidato (top 10 por distância):
      → Routing Service (Google Maps API ou OSRM self-hosted)
      → Calcula ETA real considerando tráfego em tempo real
      → Distância em linha reta ≠ ETA real (trânsito, ruas de mão única)

[3] Ranking
    → Score = f(ETA, rating do motorista, tipo do veículo)
    → Ordenar candidatos por score

[4] Oferta ao melhor candidato
    → Push notification + WebSocket para o app do motorista
    → Timeout: 10 segundos para aceitar

[5] Aceite → match confirmado
    Rejeição ou timeout → oferecer para próximo da lista
    Lista esgotada → expandir raio para 4km → repetir
```

---

## Tracking em Tempo Real

Depois do match, passageiro acompanha o motorista no mapa.

```
Motorista app → WebSocket → Location Service
  → Atualiza Redis GEO: geoadd drivers:active ...
  → Publica no Kafka: topic ride.{ride_id}.location
        ↓
  Passenger app (subscrito via WebSocket)
  → Recebe update de posição a cada 4s
  → Renderiza no mapa

Precisão:
  Geohash de 7 chars (150m × 150m) suficiente para o mapa do passageiro
  Geohash de 8 chars (38m × 19m) para chegada final (detectar "chegou")
```

---

## Surge Pricing — Decisão Arquitetural

Preço dinâmico baseado em demanda/oferta na região.

```
Demand signal:
  Kafka stream de pedidos de corrida → agregado por geohash (5 chars = ~5km)
  Janela de 5 minutos → requests/min por célula

Supply signal:
  Redis GEO → contar motoristas disponíveis por célula

Surge multiplier:
  ratio = demand / supply
  ratio > 2.0 → 1.5×
  ratio > 3.0 → 2.0×
  ratio > 5.0 → 3.0× (cap máximo)

Atualização: a cada 30s por célula
Cacheado no Redis com TTL de 30s → Pricing Service serve sem query ao stream
```

---

## Consistência no Matching — Race Condition

Dois passageiros podem solicitar corrida ao mesmo tempo e ambos receber oferta do mesmo motorista.

```
Problema:
  Passageiro A solicita → candidatos: [driver:42, driver:7]
  Passageiro B solicita → candidatos: [driver:42, driver:15]
  Ambos oferecem driver:42 → driver:42 aceita ambos → conflito

Solução — Distributed Lock:
  Ao selecionar driver:42 como candidato:
    Redis SET lock:driver:42 {ride_id} NX EX 15
    NX = só seta se não existir (atomic)
    EX 15 = expira em 15s (timeout do motorista)

  Se lock adquirido: oferecer corrida
  Se lock existe: driver:42 já está sendo ofertado → pular, tentar próximo

  Motorista aceita → lock permanece até corrida finalizar
  Motorista rejeita / timeout → DEL lock:driver:42 → libera para outros pedidos
```

---

## Estimativas de Escala

```
Location updates:
  5M motoristas × 1 update/4s = 1.25M writes/s
  Redis cluster com 10 shards por geohash prefix: cada shard ~125k writes/s

Matching requests:
  1M corridas/hora (pico) = 278 req/s
  Cada match: ~10 ETA calls ao Routing Service = 2.780 routing req/s
  OSRM self-hosted: suporta ~5k req/s por nó → 1-2 nós suficientes

Kafka (location stream):
  1.25M msg/s × 50 bytes = ~60MB/s de throughput
  10 partitions no tópico de location → 6MB/s por partition (dentro do limite)

Redis GEO memory:
  5M motoristas × ~70 bytes (lat, lng, member) = ~350MB
  Cabe em uma instância Redis confortavelmente
```

---

## Trade-offs

| Decisão | Escolha | Por quê |
|---|---|---|
| Storage de posição | Redis GEO | 1.25M writes/s, dados voláteis, busca geoespacial nativa |
| Indexação geoespacial | Geohash | Busca por prefixo eficiente, sem calcular distância para 5M |
| ETA | Routing Service externo | Distância euclidiana não reflete tráfego real |
| Race condition | Redis SET NX | Lock atômico e distribuído sem coordenação pesada |
| Surge pricing | Kafka stream + Redis cache | Tempo real mas sem bloquear o caminho crítico do match |
| Tracking | WebSocket + Kafka | Push em tempo real, desacoplado do Location Service |

---

## Problemas a Aprofundar em Entrevista

**"E se o Redis de localização cair?"**
Redis Sentinel ou Redis Cluster com replicação. Dados de localização são efêmeros — em 4s, todos os motoristas reenviam posição. Perda de alguns segundos de posição é tolerável (degradação de UX, não de correção).

**"Como lidar com motoristas em fronteiras de células de geohash?"**
Geohash tem problema de fronteira: dois pontos a 100m de distância podem ter prefixos diferentes se estiverem em células adjacentes. Solução: sempre buscar a célula do passageiro **e as 8 células adjacentes** — cobertura total sem duplicatas.

**"Como escalar para 50M motoristas?"**
Sharding do Redis GEO por região geográfica (prefixo de 2 chars do geohash). Cada cluster Redis cuida de uma macrorregião. Location Service faz roteamento por prefixo antes de chamar o Redis.

---

## Conceitos Relacionados

[[cache]] · [[mensageria]] · [[rate-limiting]] · [[horizontal-vs-vertical-scaling]] · [[db-sharding]] · [[circuit-breaker]]

---

*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-29*
