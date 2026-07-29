---
type: concept
title: "Full-Text Search"
aliases: ["busca full text", "FULLTEXT INDEX", "match against", "tsvector tsquery", "busca por relevância em SQL"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 2
tags: [banco-de-dados, full-text-search, mysql, postgresql, sql, performance, relevancia, gin]
skill: tech-mentor-data
status: stable
---

# Full-Text Search

Técnica de busca textual em banco de dados relacional que resolve, ao mesmo tempo, dois problemas do operador [[wiki/concepts/like-wildcard|`LIKE`]]: falta de relevância semântica (`LIKE` compara substring de caracteres, não palavras) e falta de performance (`LIKE '%termo%'` força um full table scan). Funciona construindo um [[wiki/concepts/indice-invertido|índice invertido]] dedicado sobre o texto — palavra → lista de registros onde ela ocorre — em vez de examinar a tabela linha a linha a cada busca.

## Problema que Resolve

`LIKE '%termo%'` é a primeira intuição de quase todo programador para implementar um campo de busca, e está estruturalmente errada:

- **Relevância:** busca por substring de caracteres, não por palavra. `'%Ana%'` também casa com "Luciana"; `'%anel%'` também casa com "panela". Remover o wildcard inicial (`'termo%'`) só desloca o problema (`'Maria%'` ainda casa com "Mariana").
- **Performance:** `EXPLAIN ANALYZE` numa query com `LIKE '%termo%'` mostra table scan (`Seq Scan` no Postgres) sobre a tabela inteira, e o custo escala com tamanho-da-tabela × número de buscas concorrentes.

## MySQL — FULLTEXT INDEX + MATCH ... AGAINST

```sql
CREATE FULLTEXT INDEX search_idx ON products (name, description);

SELECT * FROM products
WHERE MATCH(name, description) AGAINST('fone bluetooth');
```

`MATCH` recebe as colunas cobertas pelo índice full-text; `AGAINST` recebe o termo pesquisado. O resultado vem ranqueado por relevância — os IDs retornados saem fora de ordem sequencial porque o critério é relevância textual, não ordem física da tabela.

## PostgreSQL — tsvector, tsquery e índice GIN

```sql
-- Índice: converte nome+descrição num tsvector e indexa com GIN
CREATE INDEX search_idx ON products
USING GIN (
  to_tsvector('portuguese', coalesce(name, '') || ' ' || coalesce(description, '') || ' ')
);

-- Consulta
SELECT * FROM products
WHERE to_tsvector('portuguese', coalesce(name, '') || ' ' || coalesce(description, '') || ' ')
      @@ to_tsquery('portuguese', 'capa & dura');
```

- `to_tsvector(idioma, texto)` — converte o texto em lexemas indexáveis.
- `to_tsquery(idioma, termo)` / `plainto_tsquery` — converte o termo pesquisado, resolvendo fronteira entre palavras compostas.
- `@@` — operador de correspondência entre `tsvector` e `tsquery`.
- `GIN` (Generalized Inverted Index) — o tipo de índice que estrutura o índice invertido por baixo dos panos; é o mesmo tipo de índice usado para `JSONB`/arrays (ver [[wiki/concepts/database-index]]).

**Sem o índice GIN, a query roda mais lenta que o próprio `LIKE`** (139ms vs. 4,9ms no exemplo da fonte) porque o `tsvector` é recalculado em tempo de execução a cada chamada. Com o índice: ~0,3–0,8ms, ordens de grandeza mais rápido, e o plano deixa de mostrar `Seq Scan`.

## Stemming e Lexemas (diferencial do Postgres)

PostgreSQL reduz variações morfológicas ao mesmo lexema automaticamente — "programador", "programando", "programação" e "programadores" viram um único token de raiz; "prata" e "prateado" retornam o mesmo resultado; buscar "cadernos" (plural) encontra "caderno" (singular) sem essa forma existir literalmente no texto. MySQL tem suporte a idioma mais limitado nesse eixo (claim de confiança média — não demonstrado ao vivo na fonte, apenas comparado em tabela).

## Tesauros (Sinônimos)

"Tesauro", no jargão do Postgres, é sinônimo configurável: é possível fazer com que "carro", "automóvel" e "veículo" sejam tratados como equivalentes na busca. Recurso disponível no Postgres; não no MySQL.

## Além da Fonte — Recursos Não Demonstrados no Vídeo

A fonte cita a existência, mas não demonstra ao vivo, os seguintes recursos avançados do Postgres (calibrados pela skill `tech-mentor-data`, `references/databases/postgresql.md`):

- **`pg_trgm` (trigram similarity)** — busca fuzzy com tolerância a erro de digitação, via `CREATE EXTENSION pg_trgm` + índice GIN com `gin_trgm_ops` + operador `%` de similaridade. Resolve um problema que o Full-Text Search por lexema não cobre (typo, não variação morfológica).
- **`ts_rank` + `setweight`** — ranking de relevância com peso configurável por campo (ex.: match no título vale mais que match na descrição), usando `setweight(to_tsvector(...), 'A')` combinado via `||`.
- **Quando migrar para Elasticsearch** — ver [[wiki/sources/elasticsearch-opensearch]]: acima de ~10M de documentos, ou quando a necessidade é de facets/aggregations complexas, autocomplete sofisticado (`completion` suggester) ou algoritmo BM25, o Full-Text Search nativo do Postgres deixa de ser suficiente.

## Índice Invertido — o Mecanismo Comum

Tanto `FULLTEXT INDEX` (MySQL) quanto o índice `GIN` sobre `tsvector` (PostgreSQL) implementam a mesma ideia estrutural: tokenização (quebra em palavras, remoção de stop words) seguida de um [[wiki/concepts/indice-invertido|índice invertido]] palavra → lista de IDs. Buscas compostas retornam a interseção dos IDs de cada termo. Ver [[wiki/concepts/indice-invertido]] para o mecanismo isolado da técnica de busca.

## Key Sources

- [[wiki/sources/full-text-search-mysql-postgresql]] — fonte principal: LIKE vs. Full-Text Search, MySQL FULLTEXT/MATCH AGAINST, PostgreSQL tsvector/tsquery/GIN, lexemas
- [[wiki/sources/elasticsearch-opensearch]] — próximo degrau quando o Full-Text Search nativo não é mais suficiente (BM25, facets, >10M docs)
