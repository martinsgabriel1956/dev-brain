---
type: source
title: "Elasticsearch / OpenSearch"
aliases: ["elasticsearch", "opensearch", "full text search", "bm25", "lucene", "faceted search", "search engine"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/elasticsearch-opensearch.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [elasticsearch, opensearch, full-text-search, bm25, lucene, faceted-search, aggregations, mapping]
skill: tech-mentor-data
status: stable
---

## TL;DR

Elasticsearch/OpenSearch: motor de busca distribuído baseado em Lucene. BM25 como algoritmo de relevância (supera TF-IDF). Mapping define schema de índice (analyzer, field types). Sync com PostgreSQL: CDC + Debezium ou dual-write. Use quando: >10M documentos, relevância customizada, facets/aggregations complexas, autocomplete sofisticado. OpenSearch é o fork AWS pós-mudança de licença do Elastic.

## Key Claims

**Claim:** Elasticsearch resolve o que PostgreSQL FTS não resolve em escala: relevância, facets e autocomplete sofisticado.
**Evidence:** PostgreSQL FTS: `tsvector` + GIN index, relevância básica (`ts_rank`), sem facets nativas. Elasticsearch: BM25 com boost por campo, aggregations para facets em tempo real, `completion` suggester para autocomplete, `more_like_this` para recomendação. Para >10M docs com queries complexas, ES/OS é 10-100x mais rápido.
**Confidence:** alta

**Claim:** Mapping deve ser definido antes de indexar — dinâmico é conveniente mas perigoso em produção.
**Evidence:** Dynamic mapping: ES detecta tipo automaticamente. Problema: campo `price` como string em um documento → ES mapeia como `keyword`. Próximo documento com `price: 99.9` → erro de mapping conflict. Produção: definir mapping explícito (`"price": { "type": "float" }`) antes de indexar. Reindex é caro para índices grandes.
**Confidence:** alta

**Claim:** Sincronização com PostgreSQL via CDC (Debezium) é mais robusta que dual-write — sem risco de inconsistência.
**Evidence:** Dual-write: salva no PostgreSQL, depois indexa no ES. Se ES estiver down → dado no banco mas não no índice. CDC + Debezium: lê o WAL do PostgreSQL, publica no Kafka, consumer indexa no ES. Garantia at-least-once. Reindex automático se ES ficar temporariamente indisponível (replay do Kafka).
**Confidence:** alta

## Entities & Concepts Touched

- [[entities/elasticsearch]]
- [[entities/opensearch]]
- [[concepts/bm25]]
- [[wiki/concepts/full-text-search]]
- [[concepts/faceted-search]]
- [[concepts/cdc]]
- [[entities/lucene]]

## Open Questions

- OpenSearch vs Elasticsearch — diferenças técnicas relevantes em 2026 após anos de fork independente?
- Elasticsearch com kNN (vector search) para hybrid search — como balancear relevância BM25 + similaridade semântica?

## Ver também

- [[wiki/sources/full-text-search-mysql-postgresql]] — o degrau anterior: Full-Text Search nativo em MySQL (`FULLTEXT`/`MATCH AGAINST`) e PostgreSQL (`tsvector`/`GIN`), com o mesmo mecanismo de índice invertido descrito aqui de forma mais elementar; a claim "PostgreSQL FTS: sem facets nativas" registrada acima é consistente com o que essa fonte demonstra (stemming e sinônimo via tesauro, mas nenhuma agregação/facet)
