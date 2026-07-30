---
type: concept
title: "Geohash"
aliases: ["geohash", "indexação geoespacial", "spatial index"]
date_created: 2026-04-22
date_updated: 2026-07-29
source_count: 2
tags: [system-design, geoespacial, geohash, redis, localização]
skill: tech-mentor-system-design
status: stable
---

# Geohash

Divide o mapa em células de tamanho progressivo, representadas como strings. Células geograficamente próximas compartilham prefixo — permite busca por proximidade via comparação de string, sem calcular distância para todos os pontos.

## Precisão

```
4 chars → ~39km × 20km   (escala de cidade)
5 chars → ~4.9km × 4.9km
6 chars → ~1.2km × 0.6km  ← matching (raio ~1km)
7 chars → ~150m × 150m    ← tracking em tempo real
8 chars → ~38m × 19m      ← detecção de chegada
```

## Exemplo

```
Av. Paulista, SP: -23.5617, -46.6558 → "6gyf4m"
Rua 200m de distância                → "6gyf4m" (mesmo prefixo!)
```

## Busca por Raio

Pegar geohash da célula do passageiro + **8 células adjacentes** → filtrar motoristas nessas células. Sem calcular distância para os 5M motoristas.

## Boundary Problem

Dois pontos a 100m podem ter prefixos diferentes se estiverem em células adjacentes. Por isso a busca inclui sempre as 8 células adjacentes — garante cobertura total sem duplicatas.

## Relação com Índice Espacial

Geohash é a técnica concreta por trás do que [[wiki/concepts/database-index|índice de banco de dados]] chama genericamente de **índice espacial** — estrutura útil só para geolocalização/coordenadas, "perfeitamente inútil" fora desse caso de uso. Ver [[wiki/sources/indice-de-banco-de-dados]].

## Redis GEO

Redis usa geohash internamente no `GEOADD`/`GEOSEARCH`. → [[concepts/redis-geo]]

## Escala para 50M Motoristas

Sharding do Redis GEO por prefixo de 2 chars do geohash — cada cluster Redis cuida de uma macrorregião. Location Service roteia por prefixo.

## Key Sources

- [[sources/case-uber]]
- [[wiki/sources/indice-de-banco-de-dados]] — menção ao índice espacial como categoria de índice de banco de dados
