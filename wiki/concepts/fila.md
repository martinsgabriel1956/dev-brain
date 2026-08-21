---
type: concept
title: "Fila (Queue)"
aliases: ["queue", "FIFO", "fila de dados"]
date_created: 2026-06-01
date_updated: 2026-08-14
source_count: 5
tags: [cs-fundamentals, estruturas-de-dados, fila, queue, fifo]
skill: cs-fundamentals
status: draft
---

# Fila (Queue)

Estrutura de dados **FIFO** — *First In, First Out*: o primeiro elemento a entrar é o primeiro a sair. Inserção ocorre no final (*enqueue*), remoção ocorre no início (*dequeue*).

## Operações e Complexidade

| Operação | Complexidade |
|---|---|
| Enqueue (inserir no fim) | O(1) |
| Dequeue (remover do início) | O(1) |
| Peek (ver o primeiro sem remover) | O(1) |
| Busca por valor | O(n) |

## Analogia

Uma fila de pessoas. A primeira a chegar é a primeira a ser atendida. Ninguém fura a fila.

Ou: mensagens no celular — chegam na ordem em que foram enviadas.

## Onde Aparece na Prática

- **Filas de jobs** (background processing): tarefa mais antiga processa primeiro
- **Mensageria** (Kafka, RabbitMQ, SQS): consumidores processam mensagens na ordem de chegada
- **Filas de impressão**: documento enviado primeiro imprime primeiro
- **BFS** (Busca em Largura em grafos): usa fila internamente

## Quando Usar

- Processamento em ordem de chegada é um requisito
- Você precisa desacoplar produtor de consumidor ([[wiki/concepts/buffer]])
- Load leveling: absorver picos de trabalho sem perder requisições

## Nota: Fila como Estrutura vs. Filas de Mensageria

Esta página trata da **estrutura de dados** fila. Sistemas de mensageria como Kafka e RabbitMQ implementam conceitos de fila em nível distribuído — mesma lógica FIFO, mas com garantias adicionais de durabilidade, particionamento e reprocessamento.

## Relação com outros conceitos

- [[pilha]] — estrutura inversa: LIFO em vez de FIFO
- [[array]] — uma fila pode ser implementada sobre um array circular
- [[event-sourcing]] — eventos são consumidos em ordem; fila é o mecanismo subjacente
- [[wiki/concepts/filas-e-workers]] — o padrão arquitetural de processamento assíncrono construído sobre esta estrutura
- [[wiki/concepts/bullmq]] — implementação concreta dessa estrutura sobre Redis, com producer/worker como processos independentes

## Key sources

- [[wiki/sources/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore]]
- [[wiki/sources/pub-sub-message-queue-bullmq-na-pratica]]
- [[wiki/sources/estruturas-de-dados-algoritmos-big-o-como-escolher]] — "pegar o próximo job" como exemplo canônico de operação onde a ordem de chegada é o critério de escolha da estrutura
- [[wiki/sources/cache-vs-buffer-diferenca-conceitual]] — a fila como mecanismo de [[wiki/concepts/buffer]] que absorve picos e desacopla produtor de consumidor
- [[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]] — por que a fila precisa ser **bounded** (limitada): sem limite, itens envelhecem e o uso de memória pode crescer até crashar o sistema
