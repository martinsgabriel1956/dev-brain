---
type: concept
title: "Page Splitting — B+ Tree"
aliases: ["page split", "page splitting", "b tree rebalancing"]
date_created: 2026-04-23
date_updated: 2026-07-29
source_count: 2
tags: [page-splitting, btree, mysql, primary-key, performance, storage]
skill: tech-mentor-data
status: stub
---

# Page Splitting

Operação interna do B+ Tree quando uma página (page) está cheia e precisa ser dividida para acomodar um novo valor.

**Com chaves sequenciais (auto-increment):** MySQL preenche cada página a ~94% antes de criar uma nova. Inserts vão sempre para o lado direito da árvore — sem necessidade de rebalanceamento.

**Com chaves aleatórias (UUIDv4):** cada insert vai para uma posição aleatória. A página correspondente pode estar cheia → MySQL divide a página e rebalanceia a árvore. Efeitos:
- Páginas ficam com ~50% de utilização (vs 94%) → dobro do storage necessário
- Mais operações de I/O para trazer páginas do disco
- Performance de insert até 10x pior em tabelas grandes

**Solução:** usar PKs sequenciais ou pseudo-sequenciais (UUIDv7, ULID, Snowflake ID).

## Buffer Pool: Páginas Também Vivem em Memória, Não Só no Disco

Antes de uma página cheia precisar se dividir, ela normalmente já passou pelo [[wiki/concepts/buffer-pool]] — o cache de páginas em memória do banco. O banco busca a página (não a linha isolada) primeiro na memória; só recorre ao disco em caso de *buffer miss*. Ver [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]] para o fluxo completo de como uma página chega à memória, é modificada e eventualmente persistida.

## Key Sources

- [[sources/uuid-primary-key-mysql]]
- [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]] — contexto mais amplo de por que o banco organiza dado em páginas e busca por página, não por linha isolada
