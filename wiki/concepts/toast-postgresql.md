---
type: concept
title: "TOAST (The Oversized-Attribute Storage Technique)"
aliases: ["toast postgres", "armazenamento de valores grandes postgres"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 1
tags: [postgresql, banco-de-dados, armazenamento, performance]
skill: tech-mentor-backend
status: stub
---

# TOAST (The Oversized-Attribute Storage Technique)

Mecanismo do Postgres para armazenar valores de coluna grandes demais para caber numa página padrão (8 KB). Em vez de forçar a linha inteira a violar o tamanho da página, o Postgres move o valor grande para uma tabela TOAST auxiliar e deixa, no lugar original, apenas uma referência (ponteiro) — opcionalmente comprimindo o valor antes.

## Por que existe

Uma página do heap tem tamanho fixo. Uma linha com uma coluna `text`/`jsonb`/`bytea` muito grande (ex.: documento de ~24 KB, citado como exemplo didático) não caberia numa única página. Sem TOAST, isso exigiria mudar o tamanho de página inteiro do banco — solução cara e inflexível. Com TOAST, a coluna problemática é fatiada e armazenada fora da linha principal, mantendo o heap com páginas de tamanho previsível.

## Impacto: Performance, Não Custo Direto

Ler uma coluna TOASTed é mais lento — exige um acesso adicional à tabela auxiliar em vez de ler tudo de uma página só. Mas, diferente do modelo de cobrança do [[wiki/concepts/dynamodb|DynamoDB]] (que cobra WCU/RCU proporcional ao tamanho do payload), o Postgres não cobra mais pela operação em si por causa do TOAST — o custo aparece indiretamente em disco e I/O, não como uma tarifa por KB movimentado. Ver [[wiki/sources/como-escolher-banco-de-dados-criterios-alem-do-tipo-de-dado]].

## Relação com outros conceitos

- [[wiki/concepts/postgresql]] — mecanismo interno do motor
- [[wiki/concepts/buffer-pool]] — TOAST existe porque páginas têm tamanho fixo, a mesma restrição que motiva o buffer pool a trabalhar em páginas
- [[wiki/concepts/dynamodb]] — contraste direto: payload grande custa dinheiro no Dynamo, custa performance (não $) no Postgres

## Key Sources

- [[wiki/sources/como-escolher-banco-de-dados-criterios-alem-do-tipo-de-dado]] — exemplo de documento de ~24 KB acionando TOAST, e contraste explícito com o modelo de cobrança por payload do DynamoDB
