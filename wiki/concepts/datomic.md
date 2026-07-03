---
type: concept
title: "Datomic"
aliases: ["datomic db", "immutable database"]
date_created: 2026-05-31
date_updated: 2026-07-03
source_count: 2
tags: [datomic, event-sourcing, imutabilidade, clojure, fintech, time-travel]
skill: tech-mentor-backend
status: draft
---

# Datomic

## TL;DR

Banco de dados imutável criado por [[rich-hickey]] (criador do [[clojure]]). Ao invés de sobrescrever dados, acumula fatos (datoms) em um log append-only. Oferece time-travel nativo, queries sobre o passado e snapshots imutáveis — superpoder para sistemas financeiros e de auditoria.

## Modelo de Dados

Datomic armazena **datoms**: tuplas `[entidade, atributo, valor, transação, adicionado?]`

```
[42, :conta/saldo, 1000, t1, true]   ← saldo criado como 1000
[42, :conta/saldo, 1000, t2, false]  ← saldo 1000 retracted
[42, :conta/saldo, 950,  t2, true]   ← saldo atualizado para 950
```

O histórico nunca é perdido. Você pode consultar o estado da entidade em qualquer ponto `t`.

## Time-Travel

```clojure
; Estado atual
(d/q '[:find ?saldo :where [?conta :conta/saldo ?saldo]] db)

; Estado em t=1000 (ontem)
(d/q '[:find ?saldo :where [?conta :conta/saldo ?saldo]] 
     (d/as-of db 1000))
```

## Por que o Nubank Escolheu

O [[nubank]] escolheu Datomic porque:
1. Banco tem requisitos de **auditoria e regulatórios** — histórico completo é obrigatório
2. **Time-travel** permite debugar e investigar disputas de transações em qualquer ponto do tempo
3. **Imutabilidade** elimina [[complexidade-acidental]] de estado mutável
4. **Integração nativa com [[clojure]]** — mesmo ecossistema

## Relação com Event Sourcing

Datomic é essencialmente [[event-sourcing]] no nível do banco de dados. A diferença: em Event Sourcing você design seus próprios eventos; Datomic gerencia isso internamente com datoms.

## Linguagem de Query: Datalog em vez de SQL

Datomic é citado em [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]] como exemplo concreto de que a camada 2 de um banco de dados (comunicação/query) não precisa ser SQL — Datomic usa **Datalog**. Isso ilustra o ponto central da fonte: SQL é uma escolha de linguagem de query entre várias possíveis, não uma parte obrigatória do que é "um banco de dados".

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
