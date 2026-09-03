---
type: source
title: "Particionamento por LIST no PostgreSQL (playlist 'SQL em 30 Dias', dia 13)"
aliases: ["particionamento por list", "partition by list postgresql", "sql em 30 dias dia 13"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 0
tags: [postgresql, particionamento, partition-by-list, sql, banco-de-dados, performance]
skill: tech-mentor-data
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/particionamento-por-list-postgresql-sql-30-dias.md
source_url:
author:
date_published:
date_ingested: 2026-09-01
---

# Particionamento por LIST no PostgreSQL

## TL;DR

Décimo terceiro vídeo (autor não identificado) de uma playlist "como ser bom em SQL em 30 dias". Demonstra `PARTITION BY LIST` no PostgreSQL como alternativa ao `PARTITION BY RANGE` do "dia 12" (não ingerido nesta wiki): útil quando a coluna de particionamento tem um **conjunto conhecido e finito de valores** (ex.: UF/estado), ao contrário do RANGE, que serve a intervalos contínuos (ex.: datas). Demo prática com uma tabela `venda_estado` particionada por `uf`, partições nomeadas por estado (SC, RS, PR) e uma partição `DEFAULT` como catch-all para valores sem partição própria — sem ela, um INSERT de um estado não mapeado falha.

## Key Claims

| Claim | Evidência |
|---|---|
| `PARTITION BY LIST` é indicado quando existe um conjunto conhecido de valores discretos na coluna | Exemplo dado: vendas divididas por estado (UF) numa tabela com ~10 milhões de registros |
| Cada partição de LIST é criada individualmente com `FOR VALUES IN (...)`, diferente do "partition function" usado no RANGE (aula anterior) | Sintaxe demonstrada: `CREATE TABLE venda_estado_rs PARTITION OF venda_estado FOR VALUES IN ('RS')` |
| Sem uma partição `DEFAULT`, um INSERT para um valor sem partição própria falha | Comportamento citado explicitamente antes da demo (não reproduzido como erro na gravação, mas apresentado como regra) |
| A partição `DEFAULT` funciona como catch-all — qualquer valor não coberto pelas listas explícitas cai nela | Demo: INSERT de 'SP' (sem partição própria) foi parar em `venda_estado_outros` |
| Consultar a tabela "guarda-chuva" (partitioned table) com filtro na coluna de partição retorna o mesmo resultado que consultar a partição filha diretamente | `SELECT * FROM venda_estado WHERE uf = 'SC'` vs. `SELECT * FROM venda_estado_sc` |
| Chave primária de tabela particionada precisa incluir a coluna de particionamento | Exemplo usa `PRIMARY KEY (id, uf)`, não apenas `id` |

## Conceitos

- [[wiki/concepts/particionamento-de-tabela]] (novo) — LIST vs. RANGE, partição DEFAULT, chave primária composta
- [[wiki/concepts/postgresql]] — feature nativa do motor
- [[wiki/concepts/sharding]] — distinção entre particionamento lógico (mesmo banco) e sharding físico (múltiplos nós)
- [[wiki/concepts/database-index]] — mencionado como tema do "dia 12" (RANGE), mesma playlist

## Open Questions

- O vídeo do "dia 12" (particionamento por RANGE da mesma playlist, com função de partição e índices) não está ingerido nesta wiki — não foi possível verificar cruzado o exemplo específico citado ali (apenas a menção de que existe).
- Autor/canal do vídeo não identificado no texto da transcrição (não há nome de pessoa ou canal na fala, só menções a "like", "se inscrever" e "ativar o sino").
- Não fica claro no vídeo o que acontece exatamente se um INSERT chega para um valor sem partição correspondente E sem `DEFAULT` — a regra é citada, mas não demonstrada como erro ao vivo.

## Raw Quotes

> "o particionamento por lista [...] é interessante quando existe um conjunto conhecido de valores dentro da tua tabela"

> "se eu não tenho uma partição específica para um determinado estado pode dar problema durante a inserção de dados [...] a gente cria uma partição de full [DEFAULT] [...] se eu receber um insert de algum estado que não tá particionado vai cair por aqui"

## Key Sources

_Este é o documento primário._
