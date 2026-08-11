---
type: concept
title: "Database per Service"
aliases: ["banco por serviço", "database-per-service pattern", "polyglot persistence"]
date_created: 2026-07-30
date_updated: 2026-08-10
source_count: 2
tags: [microsservicos, banco-de-dados, deadlock, arquitetura]
skill: tech-mentor-backend
status: stub
---

# Database per Service

Cada microsserviço possui seu próprio banco de dados, isolado dos demais — nenhum outro serviço acessa esse banco diretamente.

## Problema que Resolve: Deadlock por Banco Compartilhado

Quando múltiplos serviços (ex.: payments e shipping) compartilham o mesmo banco (**shared database**), uma escrita de um serviço bloqueia o outro para manter consistência de dados — gerando [[wiki/concepts/deadlock]]. Isolar o banco por serviço elimina esse deadlock específico, porque as escritas passam a acontecer em bancos independentes, em paralelo. Ver [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]].

## Novo Problema Introduzido: Atomicidade entre Serviços

Isolar os bancos resolve o deadlock mas cria um problema de consistência distribuída: quando um serviço orquestrador (ex.: orders) precisa atualizar dois bancos separados (payments e shipping) como parte de uma única operação lógica, não há mais uma transação única que garanta atomicidade. Se payments falha depois que shipping já foi atualizado, o sistema fica num estado inconsistente (pedido despachado sem pagamento confirmado). Isso motiva [[wiki/concepts/two-phase-commit]] e, em escala maior, [[wiki/concepts/saga-pattern]].

## Key Sources

- [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]] — banco por serviço como solução ao deadlock de banco compartilhado, e como origem do problema de atomicidade que motiva 2PC/Saga
- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]] — "cada serviço com seu próprio banco" citado como custo dos microsserviços (um request pode consultar 4 bancos), com ressalva explícita do autor ao consenso
