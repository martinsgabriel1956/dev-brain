---
type: source
title: "Particionamento por HASH no PostgreSQL (playlist 'SQL em 30 Dias')"
aliases: ["particionamento por hash", "partition by hash postgresql", "sql em 30 dias hash"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 0
tags: [postgresql, particionamento, partition-by-hash, sql, banco-de-dados, sharding]
skill: tech-mentor-data
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/particionamento-por-hash-postgresql-sql-30-dias.md
source_url:
author:
date_published:
date_ingested: 2026-09-14
---

# Particionamento por HASH no PostgreSQL

## TL;DR

Vídeo curto (autor não identificado) da mesma playlist "como ser bom em SQL em 30 dias" que já rendeu [[wiki/sources/particionamento-por-list-postgresql-sql-30-dias]] (LIST) e menciona um vídeo anterior de RANGE ("full das tabelas", não ingerido). Ensina `PARTITION BY HASH` no PostgreSQL: útil quando **não existe separação natural** por período (RANGE) ou por conjunto de valores conhecido (LIST), mas a tabela é grande e o autor quer que o próprio banco distribua os registros em um número fixo de partições. Demo com tabela `evento_usuario` particionada por `id_usuario`, quatro partições criadas com `MODULUS 4` / `REMAINDER 0..3`. O vídeo enfatiza explicitamente que HASH **não distribui fisicamente** entre servidores — continua sendo uma única instância Postgres — e usa a palavra "sharding" apenas como analogia pedagógica, corrigindo-se em seguida para não confundir com [[wiki/concepts/sharding]] real. Fecha com queries de introspecção (`pg_partition_tree` via `pg.relname`/`pg_get_expr`) para listar partições existentes de qualquer estratégia (RANGE, LIST ou HASH) e menciona particionamento multi-nível (ano → estado) como próximo passo não demonstrado.

## Key Claims

| Claim | Evidência |
|---|---|
| `PARTITION BY HASH` serve para distribuir registros em partições de tamanho fixo quando não há separação natural por período ou lista | Frase de abertura do vídeo, contrastando explicitamente com RANGE e LIST das aulas anteriores |
| Sintaxe de criação de cada partição de HASH usa `FOR VALUES WITH (MODULUS n, REMAINDER i)`, diferente de `FOR VALUES FROM/TO` (RANGE) ou `FOR VALUES IN (...)` (LIST) | Demo: `CREATE TABLE evento_usuario_p0 PARTITION OF evento_usuario FOR VALUES WITH (MODULUS 4, REMAINDER 0)`, repetido para p1/p2/p3 |
| O PostgreSQL calcula o hash da coluna de particionamento internamente e roteia cada linha automaticamente para a partição cujo `REMAINDER` corresponde | Comparação feita pelo autor com o cálculo de um load balancer (ex.: escalonador do Kubernetes escolhendo o servidor com menos memória) |
| Particionamento por HASH **não** distribui os dados entre servidores/nós diferentes — todas as partições continuam na mesma instância Postgres | Correção explícita do autor logo após usar a palavra "sharding": "o hash não significa que o banco vai estar distribuído entre vários servidores [...] as partições vão continuar normalmente dentro de uma única instância do Postgres" |
| Uma query com `WHERE` sobre a coluna de particionamento (ex.: `WHERE id_usuario = 100`) permite ao planner identificar e usar diretamente a partição correta | Exemplo: `SELECT * FROM evento_usuario WHERE id_usuario = 100` |
| Chave primária de tabela particionada por HASH precisa incluir a coluna de particionamento, assim como em LIST | `PRIMARY KEY (id_evento, id_usuario)`, não apenas `id_evento` |
| É possível combinar múltiplos níveis de particionamento (ex.: por ano e, dentro de cada ano, por estado) | Exemplo verbal dado (venda 2025 SC / venda 2025 RS), não demonstrado em SQL na gravação |
| Uma query contra o catálogo do Postgres (`pg_partition_tree`/tabelas de sistema com filtro opcional por `parent.relname`) lista todas as partições existentes de uma tabela, ou de todas as tabelas particionadas do banco se o filtro for omitido | Demonstrado ao vivo, mostrando as partições de `evento_usuario` (HASH) e `venda` (RANGE, do vídeo anterior) na mesma listagem |
| A função `pg_get_expr` permite visualizar o limite/definição de cada partição (`MODULUS`/`REMAINDER` para HASH, `FROM`/`TO` para RANGE) numa mesma query de introspecção | Demonstrado com exemplo comparando saída de uma partição HASH e de partições RANGE lado a lado |

## Conceitos

- [[wiki/concepts/particionamento-de-tabela]] — nova estratégia HASH somada a RANGE/LIST já documentados
- [[wiki/concepts/postgresql]] — feature nativa do motor, mesma família de RANGE/LIST
- [[wiki/concepts/sharding]] — autor usa o termo por analogia e se corrige explicitamente: HASH particiona dentro de uma única instância, não distribui fisicamente entre nós
- [[wiki/concepts/database-index]] — não central nesta fonte, mas citado en passant na comparação com RANGE

## Open Questions

- O vídeo de RANGE ("full das tabelas") da mesma playlist não está ingerido nesta wiki — não foi possível comparar a sintaxe de `FOR VALUES FROM/TO` citada aqui de segunda mão com a demo original.
- Particionamento multi-nível (ano → estado) foi apenas descrito verbalmente, sem SQL demonstrado; não há claim técnico verificável sobre a sintaxe exata de particionamento aninhado nesta fonte.
- Autor/canal não identificado no texto da transcrição, mesma situação da fonte irmã sobre LIST.
- A query exata de introspecção (`pg_partition_tree`, `parent.relname`, `pg_get_expr`) foi descrita pelo autor em termos aproximados na fala, sem o SQL completo ser lido em voz alta — reconstruída aqui a partir do comportamento demonstrado (nomes das colunas/função podem diferir ligeiramente do exato usado na gravação).

## Raw Quotes

> "a ideia dele é distribuir os registros em quantidades fixas de partições [...] muito útil quando não existe essa separação natural por período ou por lista [...] mas você deseja distribuir uma tabela que é muito grande e quer que o banco gerencie essa partição para você"

> "o hash não significa que o banco vai estar distribuído entre vários servidores, tá, as partições elas vão continuar normalmente dentro de uma única instância do Postgres [...] eu falei é um exemplo de sharding, tá, mas eh só para vocês se associarem [...] não me entendam errado"

## Key Sources

_Este é o documento primário._
