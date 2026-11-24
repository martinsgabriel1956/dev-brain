---
type: concept
title: "Relacionamento muitos para muitos (N:N)"
aliases: ["N para N", "many-to-many", "tabela pivô", "tabela associativa", "join table"]
date_created: 2026-11-16
date_updated: 2026-11-24
source_count: 2
tags: [banco-de-dados, sql, modelagem, relacionamento]
skill: tech-mentor-data
status: stub
---

# Relacionamento muitos para muitos (N:N)

Quando cada linha de A se liga a várias de B e cada linha de B a várias de A. Bancos relacionais representam isso com uma terceira tabela, a pivô (associativa), com uma [[wiki/concepts/chave-estrangeira]] para cada lado.

No Ecoleta ([[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]), um ponto de coleta coleta vários itens e um item é coletado por vários pontos, então nasce `point_items (point_id, item_id)`. Para [[wiki/entities/diego-fernandes]], o nome deve ser "derivado do nome das outras duas tabelas" e "o mais semântico possível".

- **Escrita:** insere o ponto, pega o id e insere um par por item, na mesma [[wiki/concepts/database-transactions|transação]].
- **Leitura:** `JOIN point_items ON points.id = point_items.point_id`, mais `DISTINCT` quando o filtro por vários itens duplicaria linhas.
- **Restrição que falta na aula:** a chave primária composta `(point_id, item_id)` (ou um `UNIQUE`) impede o mesmo par duas vezes. Ela também serve de índice para o join. Ver [[wiki/concepts/chave-primaria]] e [[wiki/concepts/database-index]].
- **"Todos os itens" x "algum item":** `WHERE item_id IN (...)` acha pontos com *qualquer* item; "todos" pede `GROUP BY point_id HAVING COUNT(DISTINCT item_id) = n`.

## Venda × curso

Na [[wiki/sources/frontpush-dashboards-levantamento-de-requisitos-dashclass|aula 06 do módulo de dashboards]], o curso recebe um "id do comprador". Como um curso é vendido a muitos alunos e uma venda pode ter vários cursos, o certo é uma tabela de itens (venda_id, curso_id, preço) e, para o acesso, uma de matrícula (aluno_id, curso_id).

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: points, items, point_items; join, whereIn e distinct
- [[wiki/sources/frontpush-dashboards-levantamento-de-requisitos-dashclass]]: FrontPUSH, dashboards aula 06: produto com id do comprador
