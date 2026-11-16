---
type: concept
title: "Chave primária"
aliases: ["primary key", "PK", "chave primária", "AUTOINCREMENT", "INTEGER PRIMARY KEY", "id"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [banco-de-dados, sql, modelagem, sqlite]
skill: tech-mentor-data
status: stub
---

# Chave primária

A coluna (ou conjunto de colunas) que identifica cada linha de uma tabela de forma única e não nula. Outras tabelas apontam para ela com chaves estrangeiras.

Pode ser natural (CPF, código) ou substituta (um id numérico sem significado). A substituta é a mais comum, porque não muda quando o dado de negócio muda.

No [[wiki/concepts/sqlite]]:
- **`INTEGER PRIMARY KEY`** vira um apelido do `rowid` e se preenche sozinho.
- **`AUTOINCREMENT`** só acrescenta a garantia de nunca reaproveitar ids apagados, a um pequeno custo. A documentação recomenda evitá-lo quando essa garantia não é necessária. `[external]` (https://www.sqlite.org/autoinc.html)

Ver [[wiki/concepts/database-index]] e [[wiki/concepts/relational-vs-nosql]].

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] justifica o id: buscar pelo nome falha "se o nome do local for o mesmo nome de outro local". A chave primária é "o campo principal que essa tabela aqui vai usar para identificar".

Com `AUTOINCREMENT`, depois de apagar o 5 o próximo é o 6, e a listagem mostra "1, 2, 3, 4, 6". Ele testa: apaga o registro 1, e o seguinte nasce com id 2.

Ele também explica, com clientes e estados, como um número que aponta para outra tabela evita repetir "São Paulo" dois mil vezes. É a ideia da chave estrangeira, sem dizer o nome.

## Key sources

- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: `id INTEGER PRIMARY KEY AUTOINCREMENT` na tabela places; ids não reaproveitados
