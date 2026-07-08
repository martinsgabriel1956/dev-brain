---
type: concept
title: "MySQL"
aliases: ["mysql", "innodb"]
date_created: 2026-07-07
date_updated: 2026-07-07
source_count: 2
tags: [mysql, banco-de-dados, sql, innodb, gap-locking, skip-locked, backend]
skill: tech-mentor-backend
status: draft
---

# MySQL

Banco relacional (SQL) — engine padrão de armazenamento é o **InnoDB**. Comparado ao [[wiki/concepts/postgresql-avancado|PostgreSQL]], compartilha boa parte dos mesmos padrões de concorrência (MVCC, locks, transações ACID), mas com diferenças importantes de comportamento de lock.

## Estoque como Linhas, Não Como Coluna

Modelagem clássica: uma coluna `estoque` numa tabela de produto, atualizada por `UPDATE ... SET estoque = estoque - 1`. Sob alta concorrência, isso gera contenção na mesma linha.

Alternativa usada pela Shopify em escala: cada unidade física de estoque vira **uma linha própria** na tabela. Reservar N unidades = mover N linhas específicas para o carrinho, tudo numa única transação atômica — em vez de decrementar um contador compartilhado. Ver [[wiki/concepts/skip-locked]] para como workers pegam linhas sem se bloquear.

## Gap Locking

Por padrão, o InnoDB do MySQL bloqueia não só a linha lida, mas também **os espaços vazios ("gaps") ao redor dela** — para evitar phantom reads em nível `REPEATABLE READ`. Isso pode travar muito mais do que o necessário: análogo a um segurança de condomínio que fecha o corredor inteiro em vez de só a porta do apartamento.

Em sistemas de alta concorrência com muitas inserções/deleções na mesma faixa de índice, gap locking mal compreendido é uma causa comum de [[wiki/concepts/deadlock]] e de contenção que não aparece como "query lenta" — aparece como fila de espera por lock.

## SKIP LOCKED

`SELECT ... FOR UPDATE SKIP LOCKED` é suportado desde o **MySQL 8.0** (2018) — mesma semântica do PostgreSQL 9.5+: pula linhas já travadas por outra transação em vez de esperar. Ver [[wiki/concepts/skip-locked]].

## Diagnóstico de Gargalo: Tempo de Conexão, Não Latência de Query

Uma armadilha de diagnóstico: otimizar queries individuais (menor tempo de execução) não resolve gargalos causados por **conexões seguradas por tempo desproporcional** em alguma parte do código — mesmo com CPU baixa e latência de query aceitável, o sistema pode não escalar porque o pool de conexões está saturado por operações que seguram a conexão aberta por mais tempo do que deveriam. Instrumentar por **tempo de conexão por operação** (não por query) expõe esse tipo de gargalo. Ver [[wiki/concepts/connection-pooling]].

## Key Sources

- [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]]
- [[wiki/sources/uuid-primary-key-mysql]] — UUID como PK degrada performance de índice B-tree no InnoDB
