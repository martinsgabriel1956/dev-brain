---
type: concept
title: "Particionamento de Tabela"
aliases: ["table partitioning", "partition by range", "partition by list", "partition by hash", "particionamento lógico"]
date_created: 2026-09-01
date_updated: 2026-09-14
source_count: 2
tags: [postgresql, particionamento, banco-de-dados, performance, sql]
skill: tech-mentor-data
status: stub
---

# Particionamento de Tabela

Divide uma tabela logicamente em várias tabelas filhas ("partições") dentro do **mesmo banco de dados**, com base no valor de uma ou mais colunas. Diferente de [[wiki/concepts/sharding]] (que distribui dados fisicamente entre **nós/bancos diferentes**), o particionamento continua sendo uma única instância de banco — o motor apenas roteia cada linha para a partição correta e pode ignorar (*partition pruning*) as partições irrelevantes numa query filtrada pela coluna de particionamento.

## Estratégias

| Estratégia | Quando usar | Exemplo |
|---|---|---|
| `PARTITION BY RANGE` | Intervalos contínuos, tipicamente temporais | Data de criação por trimestre/ano |
| `PARTITION BY LIST` | Conjunto conhecido e finito de valores discretos | UF/estado, categoria, tenant, status |
| `PARTITION BY HASH` | Distribuir uniformemente sem critério lógico natural | Balanceamento de carga entre partições |

## Particionamento por LIST

```sql
CREATE TABLE venda_estado (
  id BIGINT GENERATED ALWAYS AS IDENTITY,
  uf CHAR(2) NOT NULL,
  dt_venda DATE NOT NULL,
  vl_total NUMERIC(12,2) NOT NULL,
  PRIMARY KEY (id, uf)
) PARTITION BY LIST (uf);

CREATE TABLE venda_estado_rs PARTITION OF venda_estado FOR VALUES IN ('RS');
CREATE TABLE venda_estado_sc PARTITION OF venda_estado FOR VALUES IN ('SC');

-- Catch-all: sem ela, INSERT de valor não mapeado falha
CREATE TABLE venda_estado_outros PARTITION OF venda_estado DEFAULT;
```

- A **chave primária** (ou qualquer índice único) de uma tabela particionada precisa incluir a coluna de particionamento — daí `PRIMARY KEY (id, uf)`, não apenas `id`.
- Consultar a tabela guarda-chuva com filtro na coluna de partição (`WHERE uf = 'SC'`) é equivalente a consultar a partição filha diretamente — o planner já roteia.
- Ver [[wiki/sources/particionamento-por-list-postgresql-sql-30-dias]].

## Particionamento por RANGE

Voltado a intervalos contínuos (datas é o caso mais comum), permitindo *partition pruning* por range e `DETACH`/`DROP` instantâneo de partições antigas — muito mais rápido que `DELETE`, que é lento e gera bloat. Ver exemplo em [[wiki/concepts/postgresql]] (seção Hot/Warm/Cold Storage Tiering) `[skill: tech-mentor-data]`.

## Particionamento por HASH

Indicado quando **não existe separação natural** por período (RANGE) nem por conjunto conhecido de valores (LIST), mas a tabela é grande e o objetivo é só distribuir os registros em um número fixo de partições, deixando o próprio banco gerenciar o roteamento — o autor da fonte compara ao cálculo de um load balancer (ex.: escalonador do Kubernetes escolhendo o servidor com menos memória).

```sql
CREATE TABLE evento_usuario (
  id_evento BIGSERIAL,
  id_usuario BIGINT NOT NULL,
  dt_evento TIMESTAMP NOT NULL,
  descricao TEXT,
  PRIMARY KEY (id_evento, id_usuario)
) PARTITION BY HASH (id_usuario);

CREATE TABLE evento_usuario_p0 PARTITION OF evento_usuario FOR VALUES WITH (MODULUS 4, REMAINDER 0);
CREATE TABLE evento_usuario_p1 PARTITION OF evento_usuario FOR VALUES WITH (MODULUS 4, REMAINDER 1);
CREATE TABLE evento_usuario_p2 PARTITION OF evento_usuario FOR VALUES WITH (MODULUS 4, REMAINDER 2);
CREATE TABLE evento_usuario_p3 PARTITION OF evento_usuario FOR VALUES WITH (MODULUS 4, REMAINDER 3);
```

- Sintaxe própria: `FOR VALUES WITH (MODULUS n, REMAINDER i)`, em vez de `FROM/TO` (RANGE) ou `IN (...)` (LIST) — `n` é a quantidade total de partições e `i` o índice daquela partição (0-based).
- Assim como em LIST, a **chave primária** precisa incluir a coluna de particionamento (`PRIMARY KEY (id_evento, id_usuario)`).
- Uma query filtrada pela coluna de particionamento (`WHERE id_usuario = 100`) permite ao planner ir direto à partição correta, igual RANGE/LIST.
- **HASH não é sharding físico**: o autor usa a palavra "sharding" como analogia pedagógica e se corrige explicitamente em seguida — todas as partições continuam dentro de uma **única instância** do Postgres; não há distribuição entre nós/servidores. Ver [[wiki/concepts/sharding]] para a distinção formal.
- Suporta **particionamento multi-nível** (ex.: por ano e, dentro de cada ano, por estado), mencionado mas não demonstrado em SQL na fonte.
- Uma query de introspecção sobre o catálogo do Postgres (via `pg_partition_tree`/tabelas de sistema, opcionalmente filtrada por `parent.relname`, mais `pg_get_expr` para ver o limite/definição de cada partição) lista as partições existentes de qualquer estratégia — RANGE, LIST ou HASH — no mesmo formato.
- Ver [[wiki/sources/particionamento-por-hash-postgresql-sql-30-dias]].

## Open Questions

- A fonte que cobre RANGE em detalhe (função de partição, índices) faz parte da mesma playlist ("dia 12") mas não foi ingerida nesta wiki ainda — este stub cobre RANGE apenas pelo conhecimento geral da skill `tech-mentor-data`, marcado como `[skill: tech-mentor-data]`, não por uma fonte primária própria.

## Key Sources

- [[wiki/sources/particionamento-por-list-postgresql-sql-30-dias]] — LIST, partição DEFAULT, chave primária composta
- [[wiki/sources/particionamento-por-hash-postgresql-sql-30-dias]] — HASH via `MODULUS`/`REMAINDER`, distinção explícita entre HASH e sharding físico, introspecção de partições via catálogo
