---
type: concept
title: "Isolation Levels (Níveis de Isolamento)"
aliases: ["níveis de isolamento", "isolation level", "read committed", "repeatable read", "serializable"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [banco-de-dados, isolation-level, mvcc, acid, postgresql, database-internals]
skill: tech-mentor-data
status: stub
---

# Isolation Levels (Níveis de Isolamento)

Configuração que responde a uma pergunta prática: **qual versão dos dados uma transação pode enxergar?** É a propriedade Isolation de [[wiki/concepts/acid]] tornada ajustável — o banco não impõe um único nível, oferece várias opções e deixa a aplicação escolher conforme o risco do fluxo.

## Níveis principais

- **Read Uncommitted** — lê dados de transações ainda não confirmadas (dirty read). Raramente usado.
- **Read Committed** (padrão do PostgreSQL) — cada comando enxerga apenas o que já foi confirmado antes dele rodar. Consequência prática: duas leituras dentro da mesma transação podem retornar valores diferentes, se outra transação confirmou uma mudança no meio do caminho (*non-repeatable read*).
- **Repeatable Read** — a transação mantém uma visão estável (snapshot) do início ao fim; a segunda leitura enxerga o mesmo valor que a primeira, mesmo que outra transação tenha confirmado uma mudança nesse meio tempo.
- **Serializable** — maior isolamento; transações se comportam como se rodassem uma de cada vez. Mais lento, mais chance de rollback por conflito — reservado para operações onde qualquer anomalia é inaceitável.

## O trade-off central

Mais isolamento reduz surpresa (menos chance de ler dado inconsistente), mas aumenta espera de lock e a chance de uma transação falhar e precisar tentar de novo. Por isso não existe "nível certo" universal: débito financeiro pede mais rigor (Repeatable Read ou Serializable); consultar um extrato antigo pode aceitar Read Committed.

## Nuance entre motores: PostgreSQL vs. MySQL

Em Repeatable Read, o PostgreSQL usa snapshot e por isso não sofre *phantom read*. O MySQL, sob o mesmo nome de nível, ainda pode sofrer phantom read em certos casos. O nome do nível é padronizado pelo SQL standard, mas a garantia exata por baixo varia por motor — vale conferir a documentação específica antes de assumir paridade de comportamento entre bancos.

## Relação com outros conceitos

- [[wiki/concepts/mvcc]] — o mecanismo que viabiliza níveis de isolamento sem lock pesado em toda leitura
- [[wiki/concepts/acid]] — Isolation é uma das quatro garantias; isolation level é o dial que a ajusta
- [[wiki/concepts/database-transactions]] — o nível de isolamento é configurado por transação/sessão
- [[wiki/concepts/concorrencia]] — trade-off entre isolamento e espera é uma instância do trade-off geral de concorrência

## Key Sources

- [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]] — Read Committed vs. Repeatable Read explicado via exemplo de saldo de Pix mudando (ou não) entre duas leituras da mesma transação
