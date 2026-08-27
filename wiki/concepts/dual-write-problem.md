---
type: concept
title: "Dual Write Problem (Bug da Escrita Dupla)"
aliases: ["bug da escrita dupla", "dual write", "problema da escrita dupla"]
date_created: 2026-08-27
date_updated: 2026-08-27
source_count: 1
tags: [dual-write-problem, cqrs, event-driven-architecture, outbox-pattern, consistencia, sistemas-distribuidos]
skill: tech-mentor-backend
status: stub
---

# Dual Write Problem (Bug da Escrita Dupla)

Problema de atualizar dois sistemas (tipicamente: um banco de dados e um broker de eventos) de forma consistente sem uma transação distribuída. Se a escrita no banco e a publicação do evento não são atômicas, uma pode ter sucesso e a outra falhar — gerando inconsistência entre o estado persistido e o que foi comunicado a outros consumidores.

## Onde Aparece: Sincronização de CQRS via Eventos

[[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] nomeia esse risco diretamente ao descrever a sincronização write→read via [[wiki/concepts/event-driven-architecture|eventos]] em [[wiki/concepts/cqrs]]: o serviço de escrita grava na base **e** posta um evento — duas operações separadas. Se divergirem, o usuário passa a ver, na leitura, uma informação diferente da que ele efetivamente salvou. A fonte cita o problema nominalmente mas não detalha a solução, remetendo a outro vídeo do canal.

## Solução: Transactional Outbox

A solução padrão é o [[wiki/concepts/outbox-pattern]]: escrever o evento numa tabela outbox dentro da **mesma transação local** que grava o estado, e usar CDC (ex. Debezium) para publicar o evento a partir dessa tabela de forma assíncrona e garantida — eliminando a necessidade de uma transação distribuída entre banco e broker.

## Key Sources

- [[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] — citação nominal do bug da escrita dupla como risco de sincronizar CQRS via eventos
