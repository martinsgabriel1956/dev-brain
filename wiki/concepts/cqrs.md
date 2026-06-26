---
type: concept
title: "CQRS — Command Query Responsibility Segregation"
aliases: ["command query responsibility segregation", "cqrs pattern"]
date_created: 2026-05-31
date_updated: 2026-06-26
source_count: 2
tags: [cqrs, arquitetura, event-sourcing, ddd, sistemas-distribuidos]
skill: tech-mentor-backend
status: draft
---

# CQRS

## TL;DR

Separar o modelo de **escrita** (Commands) do modelo de **leitura** (Queries). O lado de escrita processa comandos e emite eventos; o lado de leitura mantém projeções otimizadas para consulta.

## Modelo Mental

```
Command side (write):
  [SacarDinheiro command] → [BankHandler] → persiste evento no event log

Query side (read):
  [event log] → reaplica eventos → [Saldo projeção em memória ou read DB]
  → consulta rápida sem tocar o event log
```

O estado em memória (ex: saldo calculado) **nunca vai direto ao banco** — o banco só armazena eventos. O estado é derivado sob demanda.

## Por que Separar

- Modelos de leitura e escrita têm formatos diferentes — forçar um único modelo gera complexidade
- Reads são geralmente muito mais frequentes que writes → otimizar separadamente
- Allows múltiplas projeções do mesmo dado (ex: saldo por conta, saldo por produto, relatório mensal)

## Relação com Event Sourcing

[[event-sourcing]] e CQRS andam juntos mas são independentes:
- Event Sourcing: *como persistir* (eventos imutáveis)
- CQRS: *como separar leitura de escrita*

Em prática: events persistidos, projeções (read models) construídas por CQRS para queries rápidas.

## Uso no Nubank

O [[nubank]] utiliza CQRS em conjunto com [[event-sourcing]] e [[datomic]]. A separação permite que o estado atual (saldo, status) seja reconstruído a partir do event log sem poluir o modelo de domínio.

## Redis como Read Layer

[[redis]] é uma escolha comum como camada de leitura em CQRS: gravações vão ao SQL (fonte de verdade), leituras vão ao Redis (projeção otimizada). Um batch ou trigger sincroniza SQL → Redis.

```
[Domínio]
  ├── Write → [SQL]       ← fonte de verdade
  └── Read  → [Redis]     ← projeção rápida
                  ↑
          [Batch / Trigger de sync]
```

Esse padrão resolve o trade-off leitura/escrita sem abrir mão de consistência nas escritas.

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
