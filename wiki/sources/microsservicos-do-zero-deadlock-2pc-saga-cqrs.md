---
type: source
title: "Microsserviços do Zero — Deadlock, Atomicidade, 2PC, Saga Pattern, CQRS"
aliases: ["microsserviços do zero", "glossário de microsserviços", "aula completa de microsserviços"]
date_created: 2026-07-30
date_updated: 2026-07-30
source_count: 1
tags: [microsservicos, deadlock, atomicidade, two-phase-commit, saga-pattern, cqrs, event-driven, rabbitmq, acid, read-replicas]
skill: tech-mentor-backend
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/microsservicos-do-zero-deadlock-2pc-saga-cqrs.md
source_url: ""
author: "transcrição de aula (pt-BR), autor não identificado no material"
date_published: ""
date_ingested: 2026-07-30
status: stable
---

# Microsserviços do Zero — Deadlock, Atomicidade, 2PC, Saga Pattern, CQRS

## TL;DR

Aula constrói incrementalmente, problema-por-problema, o percurso clássico de microsserviços: banco compartilhado → [[wiki/concepts/deadlock|deadlock]] → banco por serviço → quebra de [[wiki/concepts/acid|atomicidade]] entre serviços → [[wiki/concepts/two-phase-commit|two-phase commit]] → gargalo de coordenação com N serviços → [[wiki/concepts/saga-pattern|Saga Pattern]] via fila ([[wiki/entities/rabbitmq|RabbitMQ]]) e [[wiki/concepts/event-driven-architecture|event-driven architecture]] → separação de banco de leitura/escrita ([[wiki/concepts/cqrs|CQRS]]) com o trade-off de lag de replicação. Didática mas informal — cada solução é apresentada como resposta ao problema criado pela anterior, sem cobrir profundamente escolha entre choreography/orchestration ou detalhes de implementação de compensação.

## Key Claims

- **Banco de dados compartilhado entre microsserviços causa deadlock** — dois serviços (payments, shipping) escrevendo/lendo o mesmo banco: enquanto um atualiza, o outro fica bloqueado, porque o banco precisa manter consistência de dados. → [[concepts/deadlock]]
- **Banco de dados por serviço (database-per-service) elimina esse deadlock específico** — mas introduz um problema novo quando um serviço adicional (orders) orquestra chamadas a outros dois (payments, shipping) sem transação distribuída.
- **Atomicidade exige que toda operação seja reversível (rollback)** — se o pagamento falha depois que o envio já foi autorizado, o pedido é despachado sem ter sido pago; isso viola o princípio de atomicidade, que a fonte atribui ao "A" do [[concepts/acid]]. → [[concepts/acid]]
- **Two-phase commit (2PC) resolve isso via fase de aprovação antes da fase de execução** — orders só libera shipping depois que payments confirma sucesso; a fonte cita a sintaxe de `PREPARE TRANSACTION`/rollback do Postgres como exemplo real do padrão. → [[concepts/two-phase-commit]]
- **2PC não escala para muitos serviços** — cada serviço adicional na cadeia de aprovação aumenta o tempo de espera e a fragilidade da coordenação central; a fonte identifica isso como o gargalo que motiva o Saga Pattern.
- **Saga Pattern substitui a coordenação síncrona por uma fila de mensagens** (a fonte usa RabbitMQ como exemplo) — cada serviço publica na fila, que garante ordem e evita gargalo; em caso de falha, os serviços que já processaram precisam de rollback manual (compensação). → [[concepts/saga-pattern]]
- **Saga é caracterizada como "muito difícil de implementar"** — o custo citado é que cada serviço precisa implementar manualmente sua própria lógica de compensação/rollback; a fonte não detalha a distinção formal entre choreography e orchestration.
- **Essa arquitetura de fila é chamada de event-driven** — porque toda a coordenação passa a acontecer em reação a eventos publicados na fila, não a chamadas diretas síncronas. → [[concepts/event-driven-architecture]]
- **Banco de dados também escala separando leitura de escrita** — duplicar o banco em uma instância de escrita (write) e uma (ou mais) de leitura (read), escalando cada lado independentemente; a fonte chama isso de CQRS (Command Query Responsibility Segregation). → [[concepts/cqrs]] [[concepts/read-replicas]]
- **Trade-off do read/write split é replication lag** — a fonte estima 1-3 segundos de delay entre escrita no banco de escrita e propagação para o banco de leitura; sistemas que exigem resposta imediata e de baixíssima latência não toleram esse delay, o que explica por que nem toda arquitetura adota esse padrão.
- **Escalabilidade não é sinônimo de mais performance de resposta ao usuário** — a fonte define escalabilidade como escolher a arquitetura e os padrões corretos para a necessidade do sistema, não necessariamente reduzir latência.

## Entities

- [[entities/rabbitmq]]

## Concepts

[[concepts/deadlock]] · [[concepts/acid]] · [[concepts/two-phase-commit]] · [[concepts/saga-pattern]] · [[concepts/event-driven-architecture]] · [[concepts/cqrs]] · [[concepts/read-replicas]] · [[concepts/microsservicos]] · [[concepts/database-per-service]] · [[concepts/postgresql]]

## Open Questions

- A fonte não distingue choreography vs. orchestration para o Saga Pattern — ver `references/saga-pattern.md` da skill `tech-mentor-backend` para o detalhamento formal (state machine, Temporal.io, pivot transaction) que a aula não cobre.
- A fonte trata "fila" e "event-driven" como praticamente sinônimos; vale reforçar no wiki a diferença entre message queue (RabbitMQ, ponto-a-ponto/work queue) e broker de eventos (Kafka, log distribuído replayable) — a aula não faz essa distinção.
- Quando a fonte diz "2PC não escala para vários serviços", não menciona que 2PC clássico já é evitado em microsserviços por natureza (acoplamento síncrono, SPOF do coordinator) mesmo com poucos serviços — ver [[wiki/concepts/two-phase-commit]] seção "Quando Evitar".

## Raw Quotes

> "Toda operação ela tem que ter um rollback, toda operação ela tem que poder ser revertida. Isso é um princípio da engenharia de software."

> "Saga é muito difícil da gente implementar, porque dá muito trabalho... cada um desses serviços vai ter que implementar manualmente o rollback deles."

> "Escalabilidade não necessariamente significa mais performance pro seu usuário na resposta para ele... escalabilidade significa você escolher a arquitetura certa e os padrões corretos."

> "O seu banco de escrita, enquanto ele tá sendo atualizado, o seu banco de leitura ainda não tem a informação que o banco de escrita já tem — vai demorar sei lá 2 segundos de latência."
