---
type: concept
title: "Amazon RDS"
aliases: ["RDS", "Relational Database Service"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
tags: ["aws", "rds", "banco-de-dados", "relacional", "infra", "cloud"]
skill: tech-mentor-infra
status: stub
---

# Amazon RDS (Relational Database Service)

Serviço gerenciado da AWS para rodar bancos de dados relacionais (SQL) — MySQL, PostgreSQL, MariaDB, entre outros. O próprio nome descreve o escopo: **r**elational **d**atabase **s**ervice — não cobre NoSQL (para isso a AWS oferece [[wiki/concepts/dynamodb]]).

Oferece as features esperadas de um banco gerenciado: observabilidade, opção de escalar, backups automáticos — todas com custo adicional proporcional. Faz sentido dentro do ecossistema AWS; fora dele, raramente é a escolha natural.

## Relação com outros conceitos

- [[wiki/concepts/dynamodb]] — contraparte NoSQL da AWS
- [[wiki/concepts/read-replicas]]
- [[wiki/concepts/replicacao-de-banco]]

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
