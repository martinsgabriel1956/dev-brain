---
type: concept
title: "Command Pattern"
aliases: ["command", "padrão comando"]
date_created: 2026-05-05
date_updated: 2026-08-19
source_count: 2
tags: [design-patterns, behavioral, command, gof, undo-redo]
skill: tech-mentor-backend
status: stub
---

# Command Pattern

Padrão [[behavioral-patterns|comportamental]] que **encapsula uma solicitação como um objeto**, permitindo parametrizar clientes com diferentes pedidos, enfileirar ou registrar solicitações e suportar operações que podem ser desfeitas (undo/redo).

## Mecanismo

A operação e seus parâmetros são transformados em campos de um objeto Command. Isso permite:
- Atrasar a execução
- Enfileirar operações
- Armazenar histórico de comandos (undo/redo)
- Enviar comandos para serviços remotos

## Distinção do Strategy

Ambos parametrizam um objeto com uma ação, mas com propósitos diferentes:

| | Command | [[strategy-pattern]] |
|---|---|---|
| Propósito | Operação como objeto (undo, queue, log) | Variantes do mesmo algoritmo |
| Histórico? | Sim — pode armazenar e reverter | Não |
| Mesmo resultado? | Não necessariamente | Sim — mesmo objetivo, método diferente |

## Quando usar

- Editor com undo/redo
- Fila de tarefas assíncronas
- Transações que podem ser revertidas
- GUI onde botões/atalhos disparam as mesmas operações

## Semelhança com Unit of Work

[[wiki/concepts/unit-of-work]] também encapsula operações como objeto antes de executá-las, mas com propósito diferente: Command foca em parametrizar/enfileirar/desfazer *uma* ação individual; Unit of Work foca em agrupar *várias* operações heterogêneas (inserções, updates, deleções) num commit atômico único.

## Key Sources

- [[sources/design-pattern-strategy]] — mencionado nas relações com Strategy
- [[sources/design-pattern-observer]] — mencionado nas relações: conexão unidirecional remetente→destinatário
- [[wiki/sources/unit-of-work-padrao-de-design]] — comparação explícita entre Unit of Work e Command como padrões que encapsulam operação(ões) em objeto(s) antes da execução
