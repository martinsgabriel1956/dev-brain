---
type: concept
title: "Datomic"
aliases: ["datomic db", "immutable database"]
date_created: 2026-05-31
date_updated: 2026-09-15
source_count: 4
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

Datomic é essencialmente [[concepts/event-sourcing]] no nível do banco de dados. A diferença: em Event Sourcing você design seus próprios eventos; Datomic gerencia isso internamente com datoms.

## Arquitetura Interna: Transactor + Peers

A arquitetura do Datomic separa leitura de escrita: um **transactor** processa todas as escritas (garantindo consistência e ordenação total das transações), enquanto múltiplos **peers** fazem a leitura, escalando horizontalmente e independente do transactor. O storage físico por trás dos datoms pode ser DynamoDB, um banco relacional, ou outro backend — Datomic é uma camada de semântica (imutabilidade, time-travel, Datalog) sobre um storage substituível. Esse desenho resolve o par clássico de sistemas distribuídos: escrita que precisa de consistência forte vs. leitura que precisa de performance/escala — ao separar os dois caminhos fisicamente, cada um escala pela própria dimensão. Ver [[wiki/sources/nubank-arquitetura-escala-122-milhoes-clientes]] (detalhe não presente na fonte original desta página).

## Linguagem de Query: Datalog em vez de SQL

Datomic é citado em [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]] como exemplo concreto de que a camada 2 de um banco de dados (comunicação/query) não precisa ser SQL — Datomic usa **Datalog**. Isso ilustra o ponto central da fonte: SQL é uma escolha de linguagem de query entre várias possíveis, não uma parte obrigatória do que é "um banco de dados".

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
- [[wiki/sources/cqrs-event-sourcing-full-cycle-wesley-williams]] — usado como exemplo didático de banco imutável ao explicar Event Sourcing
- [[wiki/sources/nubank-arquitetura-escala-122-milhoes-clientes]] — arquitetura interna transactor (escrita) + peers (leitura horizontal), storage backend substituível (DynamoDB, relacional, outro)
