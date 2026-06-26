---
type: concept
title: "Replicação de Banco de Dados"
aliases: ["read replica", "replicação", "database replication", "replica set"]
date_created: 2026-06-26
date_updated: 2026-06-26
source_count: 1
tags: [system-design, banco-de-dados, replicacao, escalabilidade, leitura, alta-disponibilidade]
skill: tech-mentor-system-design
status: stub
---

# Replicação de Banco de Dados

Estratégia de criar **cópias do banco primário** para distribuir carga de leitura e aumentar disponibilidade. Escritas vão para o primário; leituras podem ir para qualquer réplica.

```
       WRITES ↓          READS ↓ ↓ ↓
    [Primário] ──sync──► [Réplica 1]
                    └──► [Réplica 2]
                    └──► [Réplica 3]
```

## Por que replicação

- **Escala leituras** — a maioria dos sistemas tem muito mais reads do que writes (ex: redes sociais, e-commerces)
- **Alta disponibilidade** — se o primário cair, uma réplica pode ser promovida
- **Análises sem impacto** — queries pesadas de BI/analytics vão para réplica dedicada, sem afetar produção

## Tipos

| Tipo | Como funciona | Trade-off |
|---|---|---|
| **Síncrona** | Write confirma após réplica confirmar | Consistência forte; latência maior |
| **Assíncrona** | Write confirma imediatamente; réplica atualiza depois | Latência menor; réplica pode estar atrasada (replication lag) |

## Replication Lag

Em replicação assíncrona, há um delay entre o write no primário e a atualização na réplica. Leituras de réplica podem retornar dados desatualizados. Solução: leituras críticas pós-write vão para o primário.

## Limitações

- **Só escala reads** — writes ainda vão todos para um único primário
- **Não aumenta capacidade de armazenamento** — cada réplica tem uma cópia completa dos dados
- Para escalar writes ou armazenamento → [[sharding]]

## Quando usar

- Workload com muito mais reads do que writes
- Queries analíticas que não podem afetar a produção
- Necessidade de alta disponibilidade com failover automático

## Relação com outros conceitos

- [[sharding]] — complementar; sharding escala writes e armazenamento
- [[cap-theorem]] — replicação assíncrona implica consistência eventual
- [[escalabilidade-horizontal]] — replicação é escala horizontal específica para a camada de dados
- [[gargalo]] — a replicação alivia o gargalo de leitura no banco

## Key sources

- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
