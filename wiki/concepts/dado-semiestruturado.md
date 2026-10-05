---
type: concept
title: "Dado Semiestruturado"
aliases: ["semi-structured data","modelo de documento","sem esquema não é sem modelagem"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [banco-de-dados, nosql, documento, modelagem]
skill: tech-mentor-data
status: draft
---

# Dado Semiestruturado

Dado que **tem estrutura, mas ela pode variar de registro para registro** — o caso típico é o JSON de um catálogo: todo produto tem nome, preço, categoria e disponibilidade; depois notebook tem processador/memória, camiseta tem tamanho/cor, livro tem autor/ISBN. O modelo de documento ([[wiki/concepts/mongodb]]) deixa cada registro carregar só os campos que fazem sentido, em vez de uma migração de esquema por tipo novo de produto. Ver [[wiki/sources/cinco-tipos-de-armazenamento-de-dados-qual-usar-codigo-fonte-tv]].

## Armadilha: "sem esquema" ≠ "sem modelagem"

O banco deixar de cobrar o formato não faz o formato deixar de existir — **a aplicação continua dependendo dele**. Se metade dos produtos usa `preco` e a outra `valor`, quem quebra é o código. Fugir de migration não é, sozinho, motivo para NoSQL; o critério é a estrutura variar o bastante para justificar flexibilidade. O relacional também consegue modelar isso (colunas opcionais, tabelas auxiliares, e [external] JSONB), só que pode virar "lutar contra a estrutura".

Relacionado: [[wiki/concepts/nosql]] (guarda-chuva: documento, colunas largas como Cassandra/Bigtable), [[wiki/concepts/relational-vs-nosql]], [[wiki/concepts/schema-evolution]], [[wiki/concepts/modelagem-de-dados]], [[wiki/concepts/persistencia-poliglota]].

## Key Sources

- [[wiki/sources/cinco-tipos-de-armazenamento-de-dados-qual-usar-codigo-fonte-tv]]
