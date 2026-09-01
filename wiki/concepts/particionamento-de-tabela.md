---
type: concept
title: "Particionamento de Tabela"
aliases: ["table partitioning", "partition by range", "partition by list", "partition by hash", "particionamento lógico"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 1
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

## Open Questions

- A fonte que cobre RANGE em detalhe (função de partição, índices) faz parte da mesma playlist ("dia 12") mas não foi ingerida nesta wiki ainda — este stub cobre RANGE apenas pelo conhecimento geral da skill `tech-mentor-data`, marcado como `[skill: tech-mentor-data]`, não por uma fonte primária própria.

## Key Sources

- [[wiki/sources/particionamento-por-list-postgresql-sql-30-dias]] — LIST, partição DEFAULT, chave primária composta
