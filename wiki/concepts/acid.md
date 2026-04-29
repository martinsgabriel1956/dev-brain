---
type: concept
title: "ACID"
aliases: ["atomicity", "consistency isolation durability", "acid properties"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
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

## Key Sources

- [[sources/banco-de-dados]]
