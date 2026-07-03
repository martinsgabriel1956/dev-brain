---
type: source
title: "SQL não é Banco de Dados: A Confusão da Galera no Twitter"
aliases: ["sql nao e banco de dados", "uncle bob sql demon spawn", "bob tables"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 0
tags: [sql, banco-de-dados, orm, dsl, sqlite, postgresql, arquitetura, database-internals, clean-code]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/sql-nao-e-banco-de-dados-uncle-bob.md
source_url: ""
author: "Criador de conteúdo brasileiro (não identificado no arquivo bruto), reagindo a thread de Robert C. Martin (Uncle Bob)"
date_published: ""
date_ingested: 2026-07-03
---

## TL;DR

Uma thread do Twitter atribuída a Robert C. Martin ("Uncle Bob") — SQL nunca foi pensado para ser embutido em programas, era uma linguagem de console para relatórios, e incorporá-la em código foi "um dos erros mais graves da nossa indústria" — gerou uma onda de comentários confusos, muita gente comparando SQL a NoSQL como se fosse a mesma discussão. Não é: o ponto é sobre **acoplar aplicação a SQL como linguagem de query**, não sobre relacional vs. documento. O autor usa isso como gancho para explicar, do zero, o que um banco de dados relacional realmente faz por baixo dos panos (armazenamento via B-tree/WAL, parser, query planner, execução) e por que ORMs e DSLs são wrappers em cima de SQL, não substitutos dele.

## Key Claims

- **SQL é uma linguagem, não o banco de dados.** *Structured Query Language* foi originalmente pensada como ferramenta de console para gerar relatórios — não para ser embutida em código de aplicação. [confiança: relatado como afirmação de Uncle Bob/Bob na thread, não verificado contra fonte primária]
- **A confusão do Twitter foi comparar SQL vs. NoSQL** quando a discussão original era sobre **escrever SQL direto no código de aplicação vs. abstrair isso** (via ORM, DSL, etc.). São eixos diferentes: um é "qual modelo de dados" (relacional vs. documento vs. grafo vs. chave-valor), o outro é "como a aplicação se comunica com o banco".
- **ORMs e DSLs não eliminam SQL — são wrappers em cima dele.** Doctrine, Hibernate, jOOQ: todos geram SQL por baixo. Mesmo uma DSL customizada em Kotlin/Java/TypeScript/Rust ainda delega a execução para o motor SQL do banco.
- **Supabase é Postgres com uma API por cima.** Mesmo quando você chama a API REST do Supabase em vez de escrever `SELECT`, o motor por baixo continua sendo Postgres executando SQL. A propaganda de "não escreva query" não elimina o SQL, só move onde ele é escrito.
- **Um banco de dados relacional tem, no mínimo, quatro camadas:** (1) armazenamento (B-tree, páginas, WAL para durabilidade), (2) uma forma de comunicação/query (SQL, DSL, ou qualquer linguagem declarativa), (3) um planner que decide como executar a query, (4) execução. Reimplementar isso do zero (ex: um fork do SQLite sem SQL) exige recriar transactions, indexação e otimização — a parte realmente difícil não é acessar os dados, é tudo em volta.
- **A discussão do artigo original provavelmente se refere ao post "Bob Tables: SQL is Demon Spawn, and No Self-Respecting Software Developer Should Ever Use It"** — não confirmado, o autor da transcrição diz que não leu o post na íntegra.
- **Comentário destacado na thread:** ORM e GraphQL são ambos abstrações em cima de SQL; propor eliminar SQL de sistemas relacionais é reinventar uma roda já testada — como o SQLite.

## Entidades Mencionadas

- [[wiki/entities/uncle-bob]] — Robert C. Martin, autor da thread original sobre SQL
- Supabase (BaaS sobre Postgres) — sem página própria ainda
- Firebase/Firestore (NoSQL documental) — mencionado por contraste
- TJ (contexto: retuitou a campanha do Supabase) — sem página própria

## Conceitos Relacionados

- [[wiki/concepts/sql-injection]] — a thread menciona "eliminar SQL para eliminar SQL attacks"; ver seção de contradição abaixo
- [[wiki/concepts/orm]]
- [[wiki/concepts/domain-specific-language]]
- [[wiki/concepts/postgresql]]
- [[wiki/concepts/nosql]]
- [[wiki/concepts/relational-vs-nosql]]
- [[wiki/concepts/datomic]] — citado como exemplo de banco com linguagem de query alternativa (Datalog)
- [[wiki/concepts/database-index]] — B-tree como estrutura de indexação
- [[wiki/concepts/database-transactions]] — transactions como parte difícil de reimplementar
- [[wiki/concepts/arvore]] — B-tree é o tipo de árvore usado internamente pelos bancos relacionais

## Contradições e Tensões com a Wiki

- **"Eliminar SQL elimina SQL attacks"** (afirmação atribuída a Uncle Bob na thread) é uma simplificação que a wiki já contradiz em parte: [[wiki/concepts/sql-injection]] documenta que a defesa real contra SQL Injection é **parametrização de queries**, não a ausência de SQL — um ORM mal usado com raw queries interpoladas continua vulnerável, e uma API REST sobre Postgres (como Supabase) ainda pode ter SQL Injection se a camada de tradução da API para SQL não parametrizar corretamente.
- **"Bob Tables" (o possível blog post de Uncle Bob) vs. "Bobby Tables"** (o meme do xkcd, já documentado em [[wiki/concepts/sql-injection]] como "Little Bobby Tables") são referências distintas que soam parecidas — vale registrar para não confundir numa consulta futura.

## Quotes Brutas Preservadas

> "SQL nunca foi pensado para ser usado em programas de computador, era uma linguagem de console para impressão de relatórios. Incorporá-la em programas foi um dos erros mais graves da nossa indústria."

> "A solução é eliminar o SQL dos sistemas inteiramente: if there is no SQL, você não tem engine de SQL, e aí não vai ter SQL attacks."

> "Se dentro do teu código tu usa SELECT * FROM table users WHERE... tu tá basicamente acoplando a tua aplicação ao banco."

> "Uma base de dados vai usar binary tree [...] conceitos de páginas e de WAL, que nada mais é do que logging."

> "Eu acabei de ler a postagem do blog e não consigo imaginar que não seja satírica [...] qualquer pessoa que estivesse propondo outra coisa estaria basicamente propondo reinventar uma roda que já foi testada e que é perfeita — como o SQLite."

## Open Questions

- Qual é, de fato, o post original de Uncle Bob referenciado? O autor especula que seja "Bob Tables: SQL is Demon Spawn..." mas não confirma.
- A thread nunca é citada com URL/data — não há como verificar a atribuição exata a Robert C. Martin vs. outro "Bob" no reply.
