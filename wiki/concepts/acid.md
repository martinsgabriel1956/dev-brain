---
type: concept
title: "ACID"
aliases: ["atomicity", "consistency isolation durability", "acid properties"]
date_created: 2026-04-22
date_updated: 2026-07-03
source_count: 3
tags: [banco-de-dados, acid, transactions, postgresql, system-design]
skill: tech-mentor-system-design
status: stable
---

# ACID

Propriedades que garantem confiabilidade em transações de bancos de dados relacionais.

- **Atomicity** — transação toda ocorre ou nada ocorre. Não existe "cobrou mas não criou o pedido".
- **Consistency** — banco nunca fica em estado inválido. Constraints, foreign keys e checks sempre respeitados.
- **Isolation** — transações concorrentes não interferem entre si. Dois usuários comprando o último item — só um vence.
- **Durability** — dado commitado sobrevive a falha de hardware. Gravado no WAL antes de confirmar.

## Relação com Transações

ACID é o **contrato** que o banco oferece. `$transaction` é como o código o invoca. Sem transação explícita, operações dependentes violam Atomicity. → [[concepts/database-transactions]]

## NoSQL e ACID

A maioria dos bancos NoSQL oferece consistência eventual, não ACID completo. Para operações financeiras e inventário crítico, use banco relacional. → [[concepts/relational-vs-nosql]]

O contraponto formal de ACID é [[wiki/concepts/base-basically-available-soft-state-eventual|BASE]] (Basically Available, Soft State, Eventual Consistency) — garantias mais fracas, mas com maior disponibilidade e escalabilidade.

## O Custo de Consistência: Exemplo do E-mail Único

Garantir uma constraint como "e-mail único" (Consistency) não é gratuito: o banco precisa, a cada escrita, ou varrer todos os registros existentes ou consultar um [[wiki/concepts/database-index|índice]] (tipicamente hash) antes de confirmar. Essa é a contrapartida de performance que a consistência forte impõe — e por isso escalar um sistema fortemente consistente para milhões de usuários é mais difícil do que escalar um sistema BASE. Ver [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]].

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]] — contraponto com BASE e custo de performance da consistência forte
