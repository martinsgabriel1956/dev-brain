---
type: concept
title: "MySQL"
aliases: ["mysql", "innodb"]
date_created: 2026-07-07
date_updated: 2026-07-27
source_count: 3
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

## Conexão Simultânea ≠ Usuário Online

Distinção crítica de capacity planning: a maioria dos usuários navegando numa aplicação web está lendo/pensando, sem conexão ativa no banco — a conexão é aberta, usada em milissegundos e fechada só no momento do write. Na prática, ~600 usuários simultâneos geram tipicamente 20–50 conexões reais no MySQL, não 600. O que de fato ocupa uma conexão por tempo desproporcional é query longa, transação aberta não comitada, ou vazamento de conexão por bug — o mesmo padrão de diagnóstico já descrito acima em "Diagnóstico de Gargalo".

## Limites Documentados de Conexão (Instância Única)

Padrão de fábrica sem alterar `my.cnf`: 151 conexões. Em servidores com 128–256 GB de RAM, 5.000–10.000 conexões são operacionalmente viáveis; configurações documentadas em 512 GB chegam a 100.000. Cada conexão consome ~1 MB de RAM só para gerenciar a thread — 10.000 conexões já são ~10 GB de overhead antes de processar qualquer linha de dado. Acima de ~5.000 conexões em instância única, context switching de threads costuma virar gargalo. Ao estourar o limite configurado, o MySQL não enfileira — retorna imediatamente o erro `1040 Too many connections`; uma conexão extra é reservada exclusivamente para `root`, para permitir diagnóstico mesmo com o limite esgotado. Ver [[wiki/concepts/cap-theorem]] para o porquê de bancos relacionais como o MySQL priorizarem recusar conexão a arriscar inconsistência.

## Key Sources

- [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]]
- [[wiki/sources/uuid-primary-key-mysql]] — UUID como PK degrada performance de índice B-tree no InnoDB
- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]] — limites reais de conexão em instância única e a distinção conexão vs. usuário online
