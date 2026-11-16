---
type: concept
title: "SQLite"
aliases: ["sqlite3", "banco embarcado"]
date_created: 2026-07-27
date_updated: 2026-11-16
source_count: 5
tags: [sqlite, banco-de-dados, embarcado, mobile, backend]
skill: tech-mentor-backend
status: stub
---

# SQLite

Não é um servidor de banco de dados — é uma biblioteca C incluída diretamente no projeto, sem processo próprio, sem instância, sem configuração de rede. O banco inteiro é um único arquivo no disco.

## Limites Técnicos

Tamanho teórico de até 281 TB; na prática, manter abaixo de 1 TB. Leitura extremamente rápida por ser tudo local, sem latência de rede.

## O Limite Que Importa: Concorrência de Escrita

SQLite usa lock global do banco para escrita — uma transação de escrita bloqueia o banco inteiro. Leituras simultâneas funcionam bem em modo **WAL** (Write-Ahead Logging), mas escritas concorrentes são serializadas. Regra objetiva: se mais de dois ou três processos precisam escrever simultaneamente, não use SQLite.

## Quem Usa (Surpreendente)

Todo app Android e iOS tem um SQLite interno. Chrome e Firefox guardam histórico, bookmarks e cookies em SQLite. O gerenciador de pacotes npm usa SQLite. Aviões Airbus usam SQLite em sistemas de aviônica, citado como certificado pela norma **DO-178C** — a certificação mais rigorosa de software embarcado aeronáutico do mundo (claim não verificada nesta ingestão, ver open question na fonte).

## Quando Usar

App mobile/desktop com usuário único, protótipos de MVPs rápidos, testes automatizados onde não se quer subir um servidor, sistemas embarcados.

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] anuncia o SQLite como o banco do Ecoleta, "amanhã eu explico melhor". O back-end precisa guardar dados porque não dá para comparar um CPF que não está cadastrado.

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa o pacote `sqlite3` (`require('sqlite3').verbose()`, `new sqlite3.Database('./src/database/database.db')`) para o CRUD do Ecoleta: `db.serialize`, `db.run` para CREATE, INSERT e DELETE, e `db.all` para SELECT. As vantagens que ele cita: é open source, "muito facinho de configurar" e "reside na própria aplicação". Os pontos fracos: segurança (sem login) e "alguns conflitos". `[skill: tech-mentor-data]` Os conflitos são de concorrência, uma escrita por vez; em servidor, use WAL e `busy_timeout`.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]], o SQLite é escolhido para não instalar nada ("um arquivo físico mesmo") e usado via [[wiki/entities/knex]] com `useNullAsDefault`. Ele vem com chaves estrangeiras desligadas; ver [[wiki/concepts/chave-estrangeira]].

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], o Proffy usa o pacote `sqlite-async` (`Database.open(__dirname + "/database.sqlite")`, `exec`, `run`, `all`, `lastID`), com três tabelas. O SQLite aceita as aspas duplas da aula como texto só por compatibilidade, não valida chaves estrangeiras sem `PRAGMA foreign_keys = ON` e não altera tabela existente com `CREATE TABLE IF NOT EXISTS`.

## Key Sources

- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]]
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: anunciado para o dia 5
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: CRUD com sqlite3 no Ecoleta; concorrência
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: SQLite via Knex; FKs desligadas por padrão
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: sqlite-async, três tabelas, aspas duplas
