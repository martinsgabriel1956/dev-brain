---
type: concept
title: "Amazon RDS"
aliases: ["RDS", "Relational Database Service"]
date_created: 2026-08-04
date_updated: 2026-08-17
source_count: 2
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

## Multi-AZ e Read Replicas

**Multi-AZ**: instância primária numa Availability Zone, standby em outra AZ, replicação **síncrona** entre elas. Se a primária cai (hardware, rede, ou a AZ inteira), o failover é automático — o DNS aponta pro standby. A standby **não recebe tráfego de leitura**, existe só para disponibilidade. **Read Replicas** escalam leitura: escritas vão pro primário, leituras vão pras réplicas (até 5 no RDS). Para failover mais rápido (<30s vs. ~60-120s do Multi-AZ tradicional), mais réplicas (até 15) ou storage auto-scaling, ver Aurora — a AWS trata RDS como escolha padrão para workload pequeno/dev, e Aurora quando performance/escala exige mais. Ver [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]].

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — Multi-AZ (failover automático, standby não serve leitura), read replicas (até 5), e a heurística RDS vs. Aurora
