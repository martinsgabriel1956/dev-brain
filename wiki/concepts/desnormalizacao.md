---
type: concept
title: "Desnormalização"
aliases: ["denormalization"]
date_created: 2026-10-08
date_updated: 2026-10-09
source_count: 2
tags: [banco-de-dados, sharding, trade-off]
skill: tech-mentor-system-design
status: draft
---

# Desnormalização

Duplicar dados (ou referências) para acelerar leituras. Em sharding: ao comentar no post de outro usuário, grava-se também no shard de quem comentou, para listar "todos os comentários da Joana" sem varrer N shards. Trade-off: leitura rápida, escrita em dois lugares (mais complexa, risco de divergência). Vale quando a consulta é feature central. Ver [[wiki/concepts/cross-shard-query]].

## Key Sources

- [[wiki/sources/sharding-milhoes-de-escritas-partition-key-consistent-hashing-pedro-camaforte]]

## Key Sources (adição 2026-10-09)

- [[wiki/sources/cqrs-quando-faz-sentido-cqs-bernardo-lobato]] — read model mais desnormalizado, com estrutura própria diferente do write model
