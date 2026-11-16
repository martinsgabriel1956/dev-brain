---
type: concept
title: "Seed de banco de dados"
aliases: ["seed", "seeds", "seeding", "dados iniciais"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [banco-de-dados, migrations, dados-iniciais, desenvolvimento]
skill: lang-dynamic
status: stub
---

# Seed de banco de dados

Script que popula o banco com dados iniciais. Pode ser **dado de referência**, que a aplicação precisa para funcionar (categorias, tipos, papéis), ou **dado de exemplo** para desenvolvimento e testes. Ao contrário da [[wiki/concepts/database-migration|migration]], que muda a estrutura, o seed muda o conteúdo.

No Ecoleta ([[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]), os seis itens de coleta são "pré-estabelecidos pela nossa própria aplicação". O arquivo `seeds/create_items.ts` faz `await knex('items').insert([...])` e roda com `knex seed:run`. Na explicação de [[wiki/entities/diego-fernandes]], seeds servem "para a gente popular a nossa base de dados com alguns dados padrões".

**Cuidados:**

- **O seed do Knex não guarda histórico.** Ao contrário das migrations, todo `seed:run` roda de novo e duplica os itens, a menos que o script apague antes ou use `INSERT ... ON CONFLICT DO NOTHING` `[external]` (https://knexjs.org/guide/migrations.html#seed-files).
- **Dado de referência pode ir numa migration,** para garantir que exista em produção na ordem certa. Dado de exemplo nunca vai para produção.

Relacionado: [[wiki/concepts/schema-migration]], [[wiki/entities/knex]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: seed dos itens de coleta com SVG
