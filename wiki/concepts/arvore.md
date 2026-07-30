---
type: concept
title: "Árvore (Tree)"
aliases: ["tree", "árvore binária", "binary tree", "BST", "B-tree"]
date_created: 2026-06-01
date_updated: 2026-07-29
source_count: 6
tags: [cs-fundamentals, estruturas-de-dados, arvore, tree, hierarquia, big-o]
skill: cs-fundamentals
status: draft
---

# Árvore (Tree)

Estrutura de dados **hierárquica** onde cada elemento (chamado **nó**) pode ter zero ou mais filhos. Há um único nó raiz no topo; nós sem filhos são chamados folhas. A hierarquia cria uma estrutura de busca muito eficiente.

## Operações e Complexidade (Árvore Balanceada)

| Operação | Complexidade |
|---|---|
| Busca | **O(log n)** |
| Inserção | O(log n) |
| Remoção | O(log n) |

A chave do O(log n): a cada passo, **metade das possibilidades é eliminada**. Para encontrar 1 registro entre 1 bilhão: ~30 comparações.

## Analogia

O sistema de arquivos do computador. Uma pasta-raiz contém subpastas, que contêm arquivos. Você não percorre todos os arquivos — navega pela hierarquia.

## Tipos Relevantes

| Tipo | Uso principal |
|---|---|
| **BST** (Binary Search Tree) | Estrutura básica; cada nó tem até 2 filhos |
| **AVL / Red-Black Tree** | BST auto-balanceada; mantém O(log n) garantido |
| **B-Tree / B+Tree** | Índices de banco de dados; otimizada para disco |
| **Trie** | Busca de strings com prefixo; autocompletar |
| **AST** (Abstract Syntax Tree) | Representação de código-fonte pelos compiladores |

## Onde Aparece na Prática (sem construir do zero)

- **Índices de banco de dados**: PostgreSQL e MySQL usam B-trees nos índices. Um `SELECT WHERE id = X` percorre a árvore em O(log n) — encontra 1 registro em bilhões em milissegundos
- **Sistema de arquivos**: hierarquia de diretórios
- **Parsers de código**: compiladores e linters constroem uma AST para analisar e transformar o código
- **DNS hierarchy**: raiz → TLD (`.com`) → domínio → subdomínio

Entender árvores te ajuda a entender por que `SELECT` em coluna sem índice varre a tabela inteira (O(n)) e `SELECT` em coluna com índice é instantâneo (O(log n)).

## Quando Usar

- Os dados têm hierarquia natural (categorias, comentários aninhados, menus, org charts)
- Você precisa de busca eficiente em grandes volumes
- Você está modelando relacionamentos pai-filho

## Quando Não Usar

- Os dados são planos e simples — [[array]] ou [[hashmap]] resolvem com menos complexidade
- Você precisa de acesso por posição ou chave exata — array ou hashmap são O(1)

## Relação com outros conceitos

- [[hashmap]] — alternativa para busca exata O(1); árvore é melhor para intervalos e ordenação
- [[array]] — alternativa para dados planos com acesso sequencial
- [[event-sourcing]] — árvores de Merkle são usadas para verificar integridade de logs de eventos
- [[wiki/concepts/algoritmos-de-grafo]] — árvore é um caso particular de grafo (acíclico e conectado); DFS/BFS percorrem ambos da mesma forma

## Key sources

- [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]] — B-tree como estrutura por trás do índice, dentro do fluxo completo de escrita de um banco (páginas → buffer pool → WAL → commit)
- [[wiki/sources/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore]]
- [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]]
- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]] — B-tree como uma das duas coisas que uma base de dados "deve fazer" (armazenamento), junto com WAL/páginas
- [[wiki/sources/indice-de-banco-de-dados]] — demonstração visual passo a passo: inserção sequencial de IDs reordenando a B-tree, e busca do ID 7 resolvida em 3 comparações via percurso binário (>4? >6?) em vez de 7 comparações lineares
