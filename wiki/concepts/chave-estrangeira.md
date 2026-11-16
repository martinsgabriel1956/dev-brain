---
type: concept
title: "Chave estrangeira"
aliases: ["foreign key", "FK", "integridade referencial", "references"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [banco-de-dados, sql, integridade, modelagem]
skill: tech-mentor-data
status: stub
---

# Chave estrangeira

Coluna que aponta para a [[wiki/concepts/chave-primaria]] de outra tabela, com o banco garantindo a integridade referencial: não se insere um valor inexistente do outro lado, e apagar o pai segue uma regra (`RESTRICT`, `CASCADE`, `SET NULL`).

No Ecoleta ([[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]), `point_items.point_id` faz `.references('id').inTable('points')` e `item_id` aponta para `items`. Na explicação de [[wiki/entities/diego-fernandes]], "todo point_id [...] precisa ser um id válido dentro da tabela points".

**A pegadinha do SQLite:** as chaves estrangeiras vêm **desligadas** por padrão, por compatibilidade, e só passam a valer com `PRAGMA foreign_keys = ON` em cada conexão `[external]` (https://www.sqlite.org/foreignkeys.html#fk_enable). Sem isso, inserir `item_id = 9` inexistente funciona, e é por isso que o "teste de rollback" da aula não provava a transação. No Knex, liga-se em `pool: { afterCreate: (conn, done) => conn.run('PRAGMA foreign_keys = ON', done) }`. Ver [[wiki/concepts/sqlite]].

Relacionado: [[wiki/concepts/relacionamento-muitos-para-muitos]], [[wiki/concepts/database-transactions]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: references/inTable na pivô; teste com item 9
