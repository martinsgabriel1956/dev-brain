---
type: concept
title: "Buffer Pool"
aliases: ["buffer pool", "cache de páginas", "page cache do banco"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [banco-de-dados, buffer-pool, cache, postgresql, database-internals]
skill: tech-mentor-data
status: stub
---

# Buffer Pool

Memória interna do banco de dados reservada para páginas de dados. É o cache entre a query e o disco: antes de buscar uma página no armazenamento, o banco procura primeiro no buffer pool.

## Buffer hit vs. miss

- **Buffer hit** — a página já está na memória. Resposta rápida, sem I/O de disco.
- **Buffer miss** — a página não está lá. O banco busca no disco e carrega a página no buffer antes de responder.

É por isso que a mesma query costuma ficar mais rápida na segunda execução: as páginas necessárias já estão carregadas.

## Dirty pages

Quando o buffer pool enche, o banco precisa escolher o que sai. Páginas só lidas podem sair sem problema — a cópia em disco já é igual. Mas uma página modificada em memória (**dirty page**) não pode simplesmente ser descartada: a versão em disco ainda está desatualizada. Ela só pode sair depois de ser persistida no arquivo de dados — e essa persistência acontece de forma assíncrona, depois que a mudança já está garantida no [[wiki/concepts/write-ahead-log]].

## Por que a página, não a linha

O banco não busca uma linha isolada — ele busca a página que a contém, um bloco com várias linhas. Consultas que leem linhas fisicamente próximas na mesma página são muito mais baratas que ler o mesmo número de linhas espalhadas em páginas diferentes. Isso é o motivo prático por trás da importância de modelagem e [[wiki/concepts/database-index|índices]]: eles reduzem quantas páginas precisam ser tocadas para satisfazer uma query. Ver [[wiki/concepts/page-splitting]] para o que acontece quando uma página fica cheia e precisa se dividir.

## Relação com outros conceitos

- [[wiki/concepts/write-ahead-log]] — garante durabilidade de uma dirty page antes dela ser persistida
- [[wiki/concepts/database-index]] — índice existe para reduzir quantas páginas o banco precisa tocar
- [[wiki/concepts/arvore]] — B-tree organiza a busca dentro/entre páginas
- [[wiki/concepts/page-splitting]] — o que acontece quando uma página do índice enche

## Key Sources

- [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]] — buffer hit/miss, dirty page, e por que ler linhas próximas fisicamente é mais barato
