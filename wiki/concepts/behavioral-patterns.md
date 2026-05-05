---
type: concept
title: "Behavioral Patterns"
aliases: ["padrões comportamentais", "comportamentais"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [design-patterns, gof, behavioral]
skill: tech-mentor-backend
status: stable
---

# Behavioral Patterns (Padrões Comportamentais)

Uma das três categorias dos 23 padrões [[gang-of-four]]. Tratam de **como objetos se comunicam e distribuem responsabilidades** entre si — algoritmos, fluxos de controle e delegação de tarefas.

## Os 11 Padrões Comportamentais GoF

| Padrão | Problema que resolve |
|---|---|
| [[strategy-pattern]] | Algoritmos intercambiáveis sem if/else |
| [[observer-pattern]] | Notificação automática de dependentes |
| Command | Encapsula operação como objeto (undo/redo, queue) |
| Chain of Responsibility | Passa request por cadeia de handlers (middleware) |
| Template Method | Esqueleto de algoritmo na base, etapas nas subclasses |
| State | Comportamento muda com o estado interno |
| Iterator | Percorre coleção sem expor sua estrutura |
| Mediator | Centraliza comunicação entre objetos |
| Memento | Captura e restaura estado de objeto (undo) |
| Visitor | Operação sobre elementos sem mudar suas classes |
| Interpreter | Gramática para linguagem simples |

## Nota sobre Chain of Responsibility

É a base do padrão de middleware: `authMiddleware → rateLimitMiddleware → validationMiddleware → routeHandler`. Cada handler decide processar ou passar adiante.

## Key Sources

- [[sources/sete-padroes-de-design-de-software]]
- [[sources/design-pattern-strategy]]
- [[sources/design-pattern-observer]]
