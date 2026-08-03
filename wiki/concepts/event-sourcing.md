---
type: concept
title: "Event Sourcing"
aliases: ["event store", "append-only log", "eventsourcing"]
date_created: 2026-05-31
date_updated: 2026-08-03
source_count: 2
tags: [event-sourcing, arquitetura, cqrs, ddd, imutabilidade, fintech]
skill: tech-mentor-backend
status: stable
---

# Event Sourcing

## TL;DR

Em vez de persistir o **estado atual**, você persiste a **sequência de eventos que levou a esse estado**. O estado é sempre derivado por replay do log. Eventos são fatos imutáveis sobre o passado.

## Modelo Mental

```
Tradicional (state-based):
  saldo = 1000
  UPDATE conta SET saldo = 950 WHERE id = 1  ← destrói histórico

Event Sourcing (event-based):
  [DepositoCreditado: +1500]
  [PIXDebitado: -50]
  [CassinoDebitado: -100]
  [TED: -400]
  → saldo atual = replay de todos os eventos = 950
```

A conta bancária é a analogia canônica: o extrato é o event log, o saldo é o estado derivado.

## Propriedades dos Eventos

- **Imutáveis** — fatos sobre o passado não mudam
- **Append-only** — nunca UPDATE/DELETE no event log
- **Sequenciados** — cada evento tem posição no stream
- **Nomeados no passado** — `OrderShipped`, `PaymentConfirmed`, não `ShipOrder`

## Quando Usar

✅ Auditoria completa obrigatória (financeiro, compliance, regulatório)
✅ Time-travel: "qual era o estado em T?"
✅ Múltiplas projeções do mesmo dado ([[cqrs]])
✅ Replay: reconstruir projeções corrompidas ou criar novas
✅ Bugs 100% reproduzíveis (salva eventos, dá replay)
❌ Queries ad-hoc complexas — event sourcing não é OLAP
❌ Times sem experiência em [[ddd]] — complexidade alta

## Snapshots

Para aggregates com muitos eventos, replay completo fica lento. Solução: snapshots periódicos.

```
Snapshot em t=1000: { saldo: 950, versão: 1000 }
Replay: snapshot + eventos de t=1001 em diante
```

## Vantagens

- **Auditoria nativa** — trilha completa sem esforço extra
- **Bugs reproduzíveis** — salva o event log, dá play, reproduz 100%
- **Testes determinísticos** — dado input de eventos, output é previsível
- **Sem [[complexidade-acidental]]** de estado mutável
- **Time-travel** — ver estado em qualquer ponto do histórico ([[datomic]])

## Desvantagens

- Curva de aprendizado alta
- Event log cresce indefinidamente → precisa de snapshot strategy
- Queries sobre estado atual exigem projeções ([[cqrs]])
- Complexidade arquitetural — raramente usado fora de bancos/apostas/compliance

## Relação com CQRS

Event Sourcing e [[cqrs]] andam juntos mas são independentes:
- Event Sourcing resolve *como persistir*
- CQRS resolve *como separar leitura de escrita*

Em prática financeira: events persistidos no store, projeções (read models) construídas por [[cqrs]] para queries rápidas.

## Uso no Nubank

O [[nubank]] usa Event Sourcing + [[datomic]] como fundação. O Datomic é essencialmente um banco de dados que implementa event sourcing nativamente — append-only, com time-travel e snapshots imutáveis.

Adotar Event Sourcing como TO-BE de uma migração de arquitetura segue o mesmo ciclo de qualquer outra mudança arquitetural significativa — AS-IS entendido, POC validada na escala real, coexistência com o modelo anterior. Ver [[wiki/concepts/ciclo-de-mudanca-de-arquitetura]].

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/ciclo-de-mudanca-de-arquitetura]] — citado como exemplo de decisão de TO-BE que exige o ciclo AS-IS/POC/migração
