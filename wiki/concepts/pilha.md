---
type: concept
title: "Pilha (Stack)"
aliases: ["stack", "LIFO", "call stack"]
date_created: 2026-06-01
date_updated: 2026-08-18
source_count: 2
tags: [cs-fundamentals, estruturas-de-dados, pilha, stack, lifo]
skill: cs-fundamentals
status: draft
---

# Pilha (Stack)

Estrutura de dados **LIFO** — *Last In, First Out*: o último elemento a entrar é o primeiro a sair. Inserção e remoção ocorrem sempre no topo (*push* e *pop*).

## Operações e Complexidade

| Operação | Complexidade |
|---|---|
| Push (inserir no topo) | O(1) |
| Pop (remover do topo) | O(1) |
| Peek (ver o topo sem remover) | O(1) |
| Busca por valor | O(n) |

## Analogia

Uma pilha de pratos. Você coloca o novo prato em cima e é o primeiro a ser retirado. Nunca vai buscar o prato do fundo.

## Onde Aparece na Prática

- **Ctrl+Z (undo)**: a última modificação é a primeira a ser desfeita
- **Call stack**: quando `funcaoA` chama `funcaoB`, o frame de `funcaoB` vai para o topo — e é o primeiro a ser resolvido. Exemplo concreto: em `fatorial(5)` recursivo, cada chamada empilha um frame pendente (`5 × fatorial(4)`, `4 × fatorial(3)`...) até `fatorial(1)` retornar — daí os frames se resolvem de cima para baixo, na ordem inversa em que foram empilhados (LIFO) — ver [[wiki/sources/recursao-fatorial-fibonacci-javascript]]
- **Avaliação de expressões matemáticas**: parsers usam pilha para respeitar precedência de operadores
- **Histórico de navegação**: botão "voltar" remove o item do topo da pilha de páginas visitadas
- **DFS** (Busca em Profundidade em grafos): usa pilha (ou recursão, que usa a call stack) internamente

## Quando Usar

- O elemento mais recente tem prioridade de processamento
- Você precisa de desfazer operações (undo/redo)
- Você precisa rastrear estado aninhado (chamadas de função, tags XML)

## Relação com outros conceitos

- [[fila]] — estrutura inversa: FIFO em vez de LIFO
- [[excecao-vs-erro]] — stack trace é a representação da call stack no momento da exceção

## Key sources

- [[wiki/sources/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore]]
- [[wiki/sources/recursao-fatorial-fibonacci-javascript]] — trace passo a passo do desenrolar da call stack em fatorial e Fibonacci recursivos
