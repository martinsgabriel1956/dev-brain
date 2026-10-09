---
type: concept
title: "Read Model (Banco de Leitura Desnormalizado)"
aliases: ["modelo de leitura", "banco de leitura", "query side", "projeção de leitura"]
date_created: 2026-09-30
date_updated: 2026-10-09
source_count: 2
tags: [cqrs, read-model, desnormalizacao, nosql, projecao]
skill: tech-mentor-backend
status: draft
---

# Read Model

## TL;DR

O lado de consulta do [[wiki/concepts/cqrs]]: um armazenamento próprio, **desnormalizado**, que guarda os dados já no formato que a tela/cliente consome. A consulta vira praticamente "ler uma linha/documento", sem os joins de várias tabelas que o modelo relacional normalizado exigiria.

## Como a fonte descreve

- Geralmente um banco **NoSQL** ([[wiki/concepts/nosql]]) com documentos **JSON** "muito próximos do que vai ser consumido" na UI: se a tela precisa de cinco informações, persiste-se um documento com as cinco.
- No SQL normalizado seriam necessários inner joins com duas ou três tabelas até para trazer a descrição de códigos.
- A camada de consulta conversa direto com esse banco, sem passar pelo domínio nem pelo [[wiki/concepts/command-bus]].
- É populado assincronamente por um [[wiki/concepts/event-handler]] que consome eventos do lado de escrita; daí o delay de [[wiki/concepts/eventual-consistency]].
- Fonte: [[wiki/sources/cqrs-desbalanco-leitura-escrita-banco-de-leitura-eventos]].

## Variações [skill]

NoSQL não é obrigatório. Um read model pode ser [[wiki/concepts/read-replicas]] (mesmo schema), [[wiki/concepts/materialized-view]] na mesma base, um índice de busca (Elasticsearch), ou Redis ([[wiki/concepts/cqrs]], seção "Redis como Read Layer"). A escolha depende do formato das consultas. Com [[wiki/concepts/event-sourcing]], o read model é uma projeção reconstruível a partir dos eventos.

## Key sources

- [[wiki/sources/cqrs-desbalanco-leitura-escrita-banco-de-leitura-eventos]] — banco de leitura desnormalizado (JSON/NoSQL), alimentado por eventos via fila
- [[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] — alternativas de read model (replicas, views, Elasticsearch)

## Key sources (adição 2026-10-09)

- [[wiki/sources/cqrs-quando-faz-sentido-cqs-bernardo-lobato]] — read model como modelo feito para a tela (extrato, pedido consolidado), mais simples e desnormalizado; várias projeções do mesmo dado (usuário, dashboard, relatório, integração)
