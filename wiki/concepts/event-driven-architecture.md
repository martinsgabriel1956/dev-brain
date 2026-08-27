---
type: concept
title: "Event-Driven Architecture (EDA)"
aliases: ["arquitetura orientada a eventos", "eda", "event driven"]
date_created: 2026-07-30
date_updated: 2026-08-27
source_count: 2
tags: [event-driven, mensageria, saga-pattern, cqrs, microsservicos, arquitetura]
skill: tech-mentor-backend
status: stub
---

# Event-Driven Architecture (EDA)

Estilo arquitetural onde componentes se comunicam publicando e reagindo a eventos, em vez de chamadas síncronas diretas. Um evento representa algo que já aconteceu (`OrderCreated`, `PaymentApproved`); quem produz o evento não sabe nem se importa quem vai consumi-lo.

## Relação com Saga Pattern e Filas

EDA é a base que viabiliza o [[wiki/concepts/saga-pattern|Saga Pattern]] coreografado: em vez de um coordinator central bloqueando serviços (como no [[wiki/concepts/two-phase-commit|two-phase commit]]), cada serviço publica eventos numa fila/broker (ex.: [[wiki/entities/rabbitmq]]) e reage a eventos de outros serviços. Isso elimina o gargalo de coordenação síncrona, ao custo de exigir compensação manual quando uma etapa falha. Ver [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]].

## Relação com CQRS

Também aparece como mecanismo de propagação em [[wiki/concepts/cqrs]]: ao invés de replicação de banco tradicional, uma atualização no lado de escrita dispara um evento/trigger que atualiza o lado de leitura — introduzindo o mesmo trade-off de consistência eventual (delay entre escrita e leitura refletida).

## Trade-off Central: Consistência Eventual

Ganha-se desacoplamento e ausência de gargalo síncrono; perde-se consistência imediata — sempre existe uma janela de tempo (a fonte cita 1-3 segundos como exemplo) entre o evento acontecer e todos os consumidores refletirem esse estado. Por isso EDA nem sempre é a escolha certa: sistemas que exigem resposta imediata de baixíssima latência não toleram esse delay.

## Risco Explícito no CQRS: o Bug da Escrita Dupla

[[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] nomeia diretamente o risco de usar eventos como mecanismo de sincronização em [[wiki/concepts/cqrs]]: escrever na base e publicar o evento não são atômicos por padrão — se as duas escritas divergirem, gera-se uma inconsistência entre o que foi salvo e o que foi lido. Ver [[wiki/concepts/dual-write-problem]] e a solução via [[wiki/concepts/outbox-pattern]].

## Key Sources

- [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]] — EDA como nome da arquitetura de fila usada para Saga Pattern, e como mecanismo de propagação write→read em CQRS, com o trade-off de latência/consistência eventual
- [[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] — eventos como opção de consistência eventual no CQRS que permite transformação livre do read model; nomeia explicitamente o bug da escrita dupla como risco
