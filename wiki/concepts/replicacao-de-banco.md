---
type: concept
title: "Replicação de Banco de Dados"
aliases: ["read replica", "replicação", "database replication", "replica set"]
date_created: 2026-06-26
date_updated: 2026-08-24
source_count: 5
tags: [system-design, banco-de-dados, replicacao, escalabilidade, leitura, alta-disponibilidade]
skill: tech-mentor-system-design
status: draft
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

## Implementação concreta: roteamento read/write no ORM ou no cluster

Duas formas comuns de implementar o roteamento write→primário / read→réplicas na prática, sem escrever lógica de roteamento manual:

- **No ORM/framework**: no Laravel, por exemplo, a configuração de conexão de banco aceita uma chave `read` com uma lista de hosts de réplica e uma chave `write` com o host primário — todo insert/update/delete é roteado automaticamente para `write`, todo select para `read`, com balanceamento entre os hosts de leitura feito pelo próprio framework. A maioria dos ORMs maduros oferece mecanismo equivalente.
- **No provedor cloud**: o Amazon Aurora expõe um cluster com um único endereço de conexão de leitura — a aplicação não precisa saber quantas réplicas existem nem escolher entre elas; o balanceamento entre réplicas de leitura acontece por trás desse endereço único.

Ver [[wiki/sources/escalando-aplicacao-zero-a-um-milhao-usuarios-renato-augusto]].

## Réplica em Standby (HA) vs. Réplica Ativa (Tolerância a Falha)

O tipo mais comum de réplica descrito nesta página serve leitura enquanto fica pronta para promoção em caso de falha — é a réplica "secundária" da topologia ativo-passivo de [[wiki/concepts/alta-disponibilidade|HA]]. [[wiki/sources/ha-vs-ft-alta-disponibilidade-tolerancia-a-falha]] descreve um segundo padrão: réplica como "clone" já ativo, servindo tráfego em paralelo (ativo-ativo), característico de [[wiki/concepts/tolerancia-a-falha]] — nesse caso não há promoção porque o lado replicado já estava operando.

## Key sources

- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
- [[wiki/sources/ha-vs-ft-alta-disponibilidade-tolerancia-a-falha]] — réplica em standby (HA) vs. réplica ativa em paralelo (Tolerância a Falha)
- [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]] — replicação como escalonamento de leitura "quase infinito" (adicionar réplicas), com replication lag de até segundos como tradeoff central
- [[wiki/sources/escalar-para-um-milhao-de-usuarios]] — write/read split motivado por evitar inconsistência/race condition ao escrever em dois bancos, e a **promoção** de uma réplica de leitura a banco de escrita como resposta ao SPOF do primário
- [[wiki/sources/escalando-aplicacao-zero-a-um-milhao-usuarios-renato-augusto]] — primeiro exemplo de configuração concreta na wiki para este padrão: chaves `read`/`write` no Laravel e cluster do Amazon Aurora com endereço único de leitura
