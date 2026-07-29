---
type: concept
title: "LIKE / Wildcard Search (Antipattern)"
aliases: ["like wildcard", "operador like", "busca por substring sql", "percent wildcard sql"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [sql, banco-de-dados, performance, antipattern, full-text-search]
skill: tech-mentor-data
status: stub
---

# LIKE / Wildcard Search (Antipattern)

`LIKE '%termo%'` é a primeira intuição de quase todo programador para implementar busca textual — receber o texto digitado pelo usuário e comparar contra as colunas com o operador `LIKE` e os wildcards `%` (coringa). Funciona para protótipos pequenos, mas quebra em dois eixos assim que o sistema precisa de busca real: relevância e performance. Ver [[wiki/concepts/full-text-search]] para a alternativa correta.

## Por Que Falha em Relevância

`LIKE` compara **substring de caracteres**, não palavras — ele não entende fronteira de palavra, idioma ou vocabulário:

- `'%Ana%'` também casa com "Luciana", "Adriana", "Vanessa" (a sequência "a-n-a" aparece em qualquer posição).
- Remover o wildcard inicial (`'Ana%'`) não é uma correção estrutural: resolve esse caso, mas `'Maria%'` ainda casa com "Mariana", e `'capa%'` ainda casa com "capacete".
- Busca composta (`'%anel prata%'`) frequentemente não encontra nada, porque a ordem exata das palavras no texto raramente coincide com a ordem digitada pelo usuário.

## Por Que Falha em Performance

`LIKE '%termo%'` não pode usar um [[wiki/concepts/database-index|índice B-tree]] de forma eficiente quando o wildcard inicial está presente — o padrão de referência do próprio material de banco de dados desta wiki já registra isso: `B-tree` serve bem para `LIKE 'abc%'` (prefixo fixo), mas não para `LIKE '%abc%'` (substring em qualquer posição). O resultado é um full table scan (`Seq Scan`/table scan) sobre a tabela inteira, com custo que escala com o tamanho da tabela × número de buscas concorrentes.

## A Saída

[[wiki/concepts/full-text-search]] — índice invertido dedicado (`FULLTEXT INDEX`/`MATCH AGAINST` no MySQL, `tsvector`/`GIN` no PostgreSQL) resolve os dois problemas: busca por palavra com ranking de relevância, e consulta ao índice em vez de varredura da tabela.

## Key Sources

- [[wiki/sources/full-text-search-mysql-postgresql]] — demonstração completa do problema (relevância + `EXPLAIN ANALYZE` mostrando table scan) e da migração para Full-Text Search
