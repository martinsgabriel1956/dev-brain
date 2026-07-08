---
type: concept
title: "Database Index"
aliases: ["índice de banco de dados", "índice composto", "índice parcial"]
date_created: 2026-04-22
date_updated: 2026-07-03
source_count: 5
tags: [banco-de-dados, performance, postgresql, index, system-design]
skill: tech-mentor-system-design
status: stable
---

# Database Index

Estrutura de dados que acelera queries ao custo de overhead em escritas.

## Tipos

```sql
-- Simples
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- Composto — otimiza WHERE user_id = ? AND status = ?
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- Parcial — indexa apenas subset dos dados
CREATE INDEX idx_orders_pending ON orders(created_at)
WHERE status = 'pending';
```

## Diagnóstico

```sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = '123';
-- Seq Scan       → full table scan → precisa de índice
-- Index Scan     → usando índice → OK
-- Index Only Scan → resposta direto do índice → melhor caso
```

## Regra

Indexe colunas em `WHERE`, `JOIN ON`, `ORDER BY`, `GROUP BY`. **Índice tem custo**: cada `INSERT`/`UPDATE`/`DELETE` atualiza todos os índices. Tabela com 15 índices faz 15x mais trabalho por escrita.

## A Estrutura Por Baixo

Índices em PostgreSQL/SQLite são implementados como [[wiki/concepts/arvore]] (B-tree por padrão). Entender essa estrutura explica por que criar/atualizar índices tem custo em escrita e por que a indexação é uma das partes genuinamente difíceis de reimplementar caso alguém tentasse construir um banco de dados do zero. Ver [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]].

## Índice Como Custo da Consistência

Um exemplo concreto de por que índice tem custo: garantir uma constraint `UNIQUE` (ex.: e-mail de usuário) exige que o banco consulte um índice — tipicamente hash — antes de confirmar cada escrita, para saber se o valor já existe. Sem esse índice, a alternativa seria varrer todos os registros a cada escrita. Isso ilustra a contrapartida de performance que garantias de [[wiki/concepts/acid|consistência forte]] impõem. Ver [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]].

## SQL Direto e Certeza sobre o Índice

Uma vantagem prática de escrever SQL diretamente em vez de depender de um ORM: quem escreve a query sabe com certeza se ela está batendo o índice ou não, em vez de confiar no que o ORM gerou por baixo. Ver [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]].

## Operador vs. Engenheiro no Uso do Índice

[[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] resume a diferença de forma direta: "o operador de CRUD usa o índice, o engenheiro sabe por que ele existe" — citado como exemplo do tipo de conhecimento que fica invisível atrás de um ORM ou ferramenta que "só funciona".

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
- [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]] — índice hash como mecanismo de garantia de unicidade (e-mail único)
- [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]]
- [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] — "operador usa o índice, engenheiro sabe por que ele existe"
