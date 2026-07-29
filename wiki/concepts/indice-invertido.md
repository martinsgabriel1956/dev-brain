---
type: concept
title: "Índice Invertido"
aliases: ["inverted index", "índice reverso", "índice remissivo"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [algoritmos-e-estruturas-de-dados, banco-de-dados, full-text-search, performance, indice]
skill: tech-mentor-data
status: draft
---

# Índice Invertido

Estrutura de dados que mapeia cada termo (palavra) à lista de registros/documentos onde ele ocorre — o inverso de uma tabela normal, que mapeia registro → conteúdo. É o mecanismo por baixo de qualquer [[wiki/concepts/full-text-search|Full-Text Search]], tanto em bancos relacionais (`FULLTEXT INDEX` do MySQL, índice `GIN` do PostgreSQL) quanto em motores de busca dedicados (Lucene/Elasticsearch).

## Como é Construído

1. **Tokenização** — o texto de cada registro é quebrado em palavras individuais; preposições e palavras de baixo valor semântico (stop words) são descartadas.
2. **Inversão** — para cada token único, o motor mantém a lista de IDs de registro em que ele aparece. Exemplo simplificado: o token "anel" aponta para os registros 1 e 2; o token "capacete" aponta para os registros 8, 9 e 10.
3. **Consulta por interseção** — uma busca composta (ex.: "panela de pressão") descarta stop words ("de") e busca a interseção dos registros que contêm "panela" **e** "pressão" — não uma varredura sequencial da tabela.

## Por Que é Rápido

Uma busca textual sem índice invertido (via [[wiki/concepts/like-wildcard|`LIKE`]] ou `tsvector` recalculado em tempo de execução) precisa examinar registro por registro — um [[wiki/concepts/database-index|table scan/Seq Scan]]. Com o índice invertido pré-computado, o motor nunca mais olha para a tabela original durante a busca: ele consulta diretamente a estrutura palavra→IDs.

**Analogia:** procurar uma palavra num livro sem índice = ler página por página até encontrar. Com índice invertido = ir direto ao índice remissivo no final do livro, que já lista em quais páginas a palavra aparece.

## Onde Aparece

- **MySQL** — `CREATE FULLTEXT INDEX` constrói o índice invertido internamente; consultado via `MATCH ... AGAINST`.
- **PostgreSQL** — índice `GIN` (Generalized Inverted Index) sobre uma expressão `to_tsvector(...)` é a implementação explícita de índice invertido do Postgres; o mesmo tipo de índice também serve para `JSONB`/arrays (ver [[wiki/concepts/database-index]]).
- **Motores de busca dedicados** — Lucene (base do Elasticsearch/OpenSearch) usa índice invertido como estrutura central, combinado com BM25 para ranking de relevância. Ver [[wiki/sources/elasticsearch-opensearch]].

## Key Sources

- [[wiki/sources/full-text-search-mysql-postgresql]] — explicação do mecanismo com exemplo simplificado de 10 registros, e demonstração de custo antes/depois de indexar
