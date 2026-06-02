---
type: source
title: "Estruturas de Dados na Prática — Array, Hashmap, Fila, Pilha e Árvore"
aliases: []
date_created: 2026-06-01
date_updated: 2026-06-01
source_count: 0
tags: [cs-fundamentals, estruturas-de-dados, array, hashmap, fila, pilha, arvore, performance, big-o]
skill: cs-fundamentals
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore.md
source_url: ""
author: "desconhecido (canal parceiro da Rocket City)"
date_published: ""
date_ingested: 2026-06-01
---

# Estruturas de Dados na Prática — Array, Hashmap, Fila, Pilha e Árvore

## TL;DR

Toda decisão de armazenamento de dados é uma escolha de estrutura — e essa escolha define performance, manutenibilidade e fragilidade do sistema. Este vídeo introduz as cinco estruturas mais usadas na prática com três perguntas de decisão: (1) acesso por posição ou identificador? (2) a ordem de processamento importa? (3) os dados têm hierarquia natural?

---

## Argumento Central

A escolha errada de estrutura de dados em um sistema pequeno pode passar despercebida. Em um sistema com mais de 1.000 usuários, vai parar o sistema. A maioria dos devs toma essa decisão sem perceber que está tomando.

---

## As Cinco Estruturas

### Array

Coleção ordenada onde cada elemento tem um índice numérico. Acesso por índice é O(1) — você sabe exatamente onde o elemento está. Fraqueza: inserção e remoção no meio são O(n) — todos os elementos subsequentes precisam ser deslocados.

### Hashmap

Acesso por chave (string, ID, e-mail) em vez de posição numérica. Busca em O(1) independente do tamanho — 10 ou 1 milhão de registros, o tempo é praticamente o mesmo. Fraqueza: não preserva ordem; não eficiente para intervalos.

### Fila (Queue)

FIFO — primeiro a entrar, primeiro a sair. Inserção no fim, remoção do início. Exemplos: filas de jobs, mensageria, impressão.

### Pilha (Stack)

LIFO — último a entrar, primeiro a sair. Inserção e remoção no topo. Exemplos: Ctrl+Z, call stack de execução.

### Árvore

Estrutura hierárquica onde cada nó pode ter filhos. Busca em O(log n) — elimina metade das possibilidades a cada passo. Exemplos: índices de banco de dados (B-tree), sistema de arquivos, AST.

---

## As Três Perguntas de Decisão

```
1. Acesso por POSIÇÃO ou IDENTIFICADOR?
   → Posição: Array
   → Identificador: Hashmap

2. ORDEM de processamento importa?
   → Primeiro chegou, primeiro processa: Fila
   → Mais recente tem prioridade: Pilha

3. Dados têm HIERARQUIA NATURAL?
   → Sim: Árvore
   → Não: Array ou Hashmap resolvem
```

---

## Conceitos Tocados

- [[wiki/concepts/array]] — novo conceito
- [[wiki/concepts/hashmap]] — novo conceito
- [[wiki/concepts/fila]] — novo conceito (estrutura de dados; diferente de [[event-sourcing]] ou filas de mensageria)
- [[wiki/concepts/pilha]] — novo conceito
- [[wiki/concepts/arvore]] — novo conceito
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — fonte primária enriquecida com conceitos individuais

---

## Questões em Aberto

1. O vídeo anuncia continuação sobre Big O — como formalizar as intuições de O(1) e O(n) apresentadas aqui?
2. Linked lists, deques e heaps não foram cobertas — onde se encaixam no framework das três perguntas?
3. Como escolher entre array e linked list quando inserção no meio é frequente?
