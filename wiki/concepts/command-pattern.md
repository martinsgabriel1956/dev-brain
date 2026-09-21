---
type: concept
title: "Command Pattern"
aliases: ["command", "padrão comando"]
date_created: 2026-05-05
date_updated: 2026-09-21
source_count: 5
tags: [design-patterns, behavioral, command, gof, undo-redo, xunit, testes]
skill: tech-mentor-backend
status: stub
---

# Command Pattern

Padrão [[behavioral-patterns|comportamental]] que **encapsula uma solicitação como um objeto**, permitindo parametrizar clientes com diferentes pedidos, enfileirar ou registrar solicitações e suportar operações que podem ser desfeitas (undo/redo).

## Definição formal (GOF, via xUnitPatterns.com)

[[wiki/sources/command-xunitpatterns]] cita o texto canônico do GOF: "Objectify a request so that it can be executed via a standard interface" / "Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations." A aplicação ao [[wiki/concepts/testcase-object|Testcase Object]] (abaixo) usa apenas a faceta de "objetificar uma chamada" — não usa queue, log nem undo/redo, que são motivações centrais da definição geral do padrão.

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

## Parente próximo: Pluggable Block

[[wiki/sources/pluggable-behavior-xunitpatterns]] descreve o **Pluggable Block**, uma das duas variações do padrão [[wiki/concepts/pluggable-behavior|Pluggable Behavior]] (Kent Beck, *Smalltalk Best Practice Patterns*): quem cria um objeto injeta um bloco de código arbitrário para ser executado depois — conceitualmente próximo do Command (objetificar comportamento), mas sem a ênfase do GOF em parametrizar clientes, enfileirar/logar ou suportar undo/redo. A outra variação do mesmo padrão, **Pluggable (Method) Selector**, é a que o [[wiki/concepts/testcase-object|Testcase Object]] usa abaixo — nenhum bloco de código é passado, apenas o nome de um método já existente.

## Semelhança com Unit of Work

[[wiki/concepts/unit-of-work]] também encapsula operações como objeto antes de executá-las, mas com propósito diferente: Command foca em parametrizar/enfileirar/desfazer *uma* ação individual; Unit of Work foca em agrupar *várias* operações heterogêneas (inserções, updates, deleções) num commit atômico único.

## Aplicação concreta: cada teste xUnit é um Command

[[wiki/sources/testcase-object-xunitpatterns]] (xUnitPatterns.com, Meszaros) descreve o [[wiki/concepts/testcase-object|Testcase Object]] como uma aplicação direta e nomeada do Command Pattern: cada [[wiki/concepts/test-method|Test Method]] a executar é encapsulado como um objeto Command, com um método `run` padrão que o [[wiki/concepts/test-runner|Test Runner]] chama sem precisar conhecer a interface específica de cada teste. Isso não é sobre undo/redo (a motivação mais comum do padrão) — a motivação aqui é permitir que testes sejam mantidos em coleções ([[wiki/concepts/test-suite-object|Test Suite Object]]), inspecionados, contados e invocados uniformemente, exatamente a capacidade que um **Graphical Test Runner** (ex.: JUnit no Eclipse) precisa para deixar o usuário navegar numa árvore de testes.

## Key Sources

- [[sources/design-pattern-strategy]] — mencionado nas relações com Strategy
- [[sources/design-pattern-observer]] — mencionado nas relações: conexão unidirecional remetente→destinatário
- [[wiki/sources/unit-of-work-padrao-de-design]] — comparação explícita entre Unit of Work e Command como padrões que encapsulam operação(ões) em objeto(s) antes da execução
- [[wiki/sources/testcase-object-xunitpatterns]] — aplicação do Command Pattern ao Testcase Object da família xUnit: cada teste é um Command com método `run` padrão
- [[wiki/sources/command-xunitpatterns]] — fonte primária isolada da definição formal do GOF, em inglês, citada por Meszaros no verbete de External Patterns
- [[wiki/sources/pluggable-behavior-xunitpatterns]] — Pluggable Block (Kent Beck, SBPP), padrão vizinho conceitualmente próximo do Command
