---
type: concept
title: "Desnormalização"
aliases: ["denormalization"]
date_created: 2026-10-08
date_updated: 2026-11-16
source_count: 3
tags: [banco-de-dados, sharding, trade-off]
skill: tech-mentor-system-design
status: draft
---

# Desnormalização

Duplicar dados (ou referências) para acelerar leituras. Em sharding: ao comentar no post de outro usuário, grava-se também no shard de quem comentou, para listar "todos os comentários da Joana" sem varrer N shards. Trade-off: leitura rápida, escrita em dois lugares (mais complexa, risco de divergência). Vale quando a consulta é feature central. Ver [[wiki/concepts/cross-shard-query]].

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], a pergunta "por que eu não cadastro tudo numa tabela só?" é o lado oposto: guardar professor, aula e horário juntos repetiria os dados do professor em cada linha. Ver [[wiki/concepts/normalizacao-de-dados]].

## Key Sources

- [[wiki/sources/sharding-milhoes-de-escritas-partition-key-consistent-hashing-pedro-camaforte]]
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: o contraexemplo da tabela única

## Key Sources (adição 2026-10-09)

- [[wiki/sources/cqrs-quando-faz-sentido-cqs-bernardo-lobato]] — read model mais desnormalizado, com estrutura própria diferente do write model
