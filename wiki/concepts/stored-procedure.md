---
type: concept
title: "Stored Procedure"
aliases: ["procedure", "sp", "function de banco", "trigger"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 1
tags: [banco-de-dados, sql, stored-procedure, trigger, regra-de-negocio, arquitetura]
skill: tech-mentor-backend
status: stub
---

# Stored Procedure

Bloco de lógica (SQL ou linguagem procedural do banco) armazenado e executado dentro do próprio banco de dados, em vez de na aplicação. Functions e triggers são variações do mesmo mecanismo: functions retornam valor e podem ser chamadas dentro de queries; triggers disparam automaticamente em resposta a eventos (`INSERT`/`UPDATE`/`DELETE`).

## Quando Faz Sentido

Mover regra de negócio para o banco compensa quando a alternativa é extrair um volume muito grande de dados para a aplicação só para agregar (soma, contagem, apuração). Exemplo: calcular inadimplência sobre 1 milhão de faturas — trazer as linhas para a memória da aplicação para depois somar não escala; deixar o banco agregar sim.

## Por Que Usar com Moderação

Regra de negócio dentro do banco fica fora do controle de versão da aplicação, fora dos testes unitários do domínio, e acopla a lógica a um SGBD específico. À medida que o número de stored procedures, functions e triggers cresce, a aplicação perde visibilidade sobre onde a regra realmente vive — um efeito parecido com o de [[wiki/concepts/acoplamento|acoplamento oculto]]. Um meio-termo é usar [[wiki/concepts/materialized-view]] em vez de lógica procedural completa.

## Trade-off

| Mover para o banco | Manter na aplicação |
|---|---|
| Agregação sobre volume muito grande | Regra que muda com frequência |
| Constraint de integridade (`UNIQUE`, `CHECK`) | Lógica testável em isolamento |
| Operação que economiza I/O de rede | Lógica versionada junto com o domínio |

## Key Sources

- [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]]
