---
type: concept
title: "Write-Ahead Log (WAL)"
aliases: ["WAL", "write ahead log", "log de transações"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [banco-de-dados, wal, durabilidade, postgresql, database-internals]
skill: tech-mentor-data
status: stub
---

# Write-Ahead Log (WAL)

Log sequencial em disco onde o banco registra toda mudança **antes** de aplicá-la ao arquivo de dados definitivo. "Escrito antes" é literal: nenhuma página suja é considerada durável até que a mudança correspondente já esteja no WAL.

## Por que existe

Gravar cada página modificada imediatamente no arquivo de dados final seria caro — o disco funciona melhor com escritas organizadas em lotes. Mas o banco não pode confiar só na cópia em memória (o [[wiki/concepts/buffer-pool]]), porque ela some se o processo cair. O WAL resolve isso: é a gravação mínima, sequencial e barata, que garante que a mudança pode ser reconstruída depois — mesmo que a página final só seja persistida bem mais tarde.

## O que isso viabiliza

- **Commit responde antes da página final ser gravada.** Depois que o registro entra no WAL, o banco já pode dizer "commit OK" — a gravação da página suja no arquivo de dados acontece de forma assíncrona, depois.
- **Recovery pós-queda.** Na inicialização, o banco relê o WAL desde o último [[wiki/concepts/database-recovery|checkpoint]]: reaplica o que estava confirmado (se a página final ainda não tinha sido persistida) e descarta/desfaz o que começou mas não foi confirmado.
- **Replicação.** Um standby pode replicar literalmente lendo o stream do WAL do primário.

## Relação com outros conceitos

- [[wiki/concepts/buffer-pool]] — o WAL existe justamente porque a memória (buffer pool) não é durável sozinha
- [[wiki/concepts/database-recovery]] — checkpoint e recovery leem o WAL para saber o que refazer
- [[wiki/concepts/acid]] — WAL é o mecanismo concreto por trás da propriedade de Durability
- [[wiki/concepts/arvore]] — junto com a B-tree, é uma das duas peças que [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]] cita como "o que uma base de dados deve fazer" (armazenamento)

## Key Sources

- [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]] — explicação completa: por que o commit não espera a página final, e como o recovery reaplica/descarta a partir do log
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]] — menção rápida ("conceitos de páginas e de WAL, que nada mais é do que logging"), sem aprofundar o mecanismo
