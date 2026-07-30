---
type: concept
title: "Database Recovery e Checkpoints"
aliases: ["recovery", "crash recovery", "checkpoint", "recuperação de falhas"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [banco-de-dados, recovery, checkpoint, wal, durabilidade, database-internals]
skill: tech-mentor-data
status: stub
---

# Database Recovery e Checkpoints

Processo pelo qual um banco de dados reconstrói o estado confirmado depois de uma queda (crash do processo, falta de energia, etc.), respondendo à pergunta: **quais transações já tinham sido confirmadas quando tudo parou?**

## Checkpoint

Ponto de controle: de tempos em tempos, o banco grava no arquivo de dados as páginas sujas pendentes (ver [[wiki/concepts/buffer-pool]]) e registra até onde chegou no [[wiki/concepts/write-ahead-log|WAL]]. Isso limita quanto log precisa ser relido depois de uma queda.

- Checkpoint recente → recovery tem pouco a refazer, banco volta a aceitar conexões mais rápido.
- Checkpoint atrasado → mais WAL acumulado para reprocessar, recovery mais lento.

Checkpoints frequentes custam mais I/O em operação normal; checkpoints espaçados custam mais tempo de recovery após uma falha — outro trade-off de engenharia, não uma escolha óbvia.

## Recovery

Ao subir depois de uma queda, o banco relê o WAL a partir do checkpoint necessário:

1. **Transações confirmadas** (commit já registrado no WAL) são refeitas, caso a página modificada ainda não tivesse sido persistida no arquivo de dados.
2. **Transações incompletas** (começaram mas não confirmaram) são descartadas ou desfeitas, dependendo de como aquele banco implementa a recuperação.

Esse mecanismo é o que dá substância à promessa de durabilidade: "commit OK" só significa algo real se o banco consegue, de fato, reconstruir aquele estado depois de uma falha.

## Relação com outros conceitos

- [[wiki/concepts/write-ahead-log]] — a fonte de verdade que o recovery relê
- [[wiki/concepts/buffer-pool]] — dirty pages são o que o checkpoint persiste
- [[wiki/concepts/acid]] — recovery é o mecanismo que sustenta a garantia de Durability
- [[wiki/concepts/database-transactions]] — a unidade que recovery reaplica ou desfaz por inteiro

## Key Sources

- [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]] — checkpoint e recovery explicados em sequência, incluindo o trade-off entre checkpoint frequente e recovery rápido
