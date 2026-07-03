---
type: concept
title: "DSL (Domain-Specific Language)"
aliases: ["dsl", "linguagem específica de domínio", "domain specific language"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 1
tags: [dsl, sql, kotlin, linguagem, abstracao, banco-de-dados]
skill: tech-mentor-backend
status: stub
---

# DSL (Domain-Specific Language)

Linguagem criada para resolver um domínio específico de problema, em vez de ser genérica como uma linguagem de programação completa. No contexto de bancos de dados, uma DSL permite manipular dados de forma declarativa e tipada, sem escrever SQL literal no código.

## Onde Aparece

- **Kotlin, Java, TypeScript, Rust** suportam construir DSLs internas para modelar queries como código (ex: jOOQ em Java)
- **SQL em si** é uma DSL — uma linguagem específica para o domínio de consulta a dados relacionais
- **Datalog** (usado pelo [[wiki/concepts/datomic]]) é uma DSL alternativa ao SQL para o mesmo domínio: consultar dados

## A Pegadinha

Uma DSL para banco de dados, na prática, quase sempre é um **wrapper em cima do SQL** — ela não elimina a linguagem SQL, apenas muda a sintaxe que o desenvolvedor escreve. Por baixo, o motor do banco ainda parseia, planeja e executa SQL (ou algo equivalente). Ver discussão completa em [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]].

## Relação com ORM

Um [[wiki/concepts/orm]] tipicamente expõe uma DSL (métodos encadeados, builders) para montar queries sem escrever SQL cru — mas a distinção é sutil: DSL é sobre a forma da linguagem, ORM é sobre o mapeamento objeto↔tabela. As duas coisas frequentemente coexistem na mesma biblioteca.

## Key Sources

- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
