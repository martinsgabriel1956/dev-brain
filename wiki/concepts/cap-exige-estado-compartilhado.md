---
type: concept
title: "CAP exige estado compartilhado"
aliases: ["nem toda falha é CAP", "CAP vs falha de comunicação simples"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 1
tags: [system-design, cap-theorem, microsservicos, sistemas-distribuidos]
skill: tech-mentor-system-design
status: draft
---

# CAP exige estado compartilhado

Nem toda falha de comunicação entre serviços é um problema de [[wiki/concepts/cap-theorem]]. Se o serviço A chama o B e B está fora do ar, é só falha de comunicação (tratada com timeout, retry, circuit breaker). O CAP entra quando **existe um estado compartilhado que dois serviços precisam coordenar** e o sistema precisa decidir o que fazer quando essa coordenação quebra.

## Exemplo: Estoque e Pedido

A consistência em jogo não é entre réplicas do mesmo banco, e sim do **estado de negócio** (quantidade em estoque) visto por dois serviços. Com uma unidade em estoque e o canal entre Pedido e Estoque cortado, a pergunta é: aceito o pedido sem dar baixa (A) ou paro a operação até a comunicação voltar (C)? Ver [[wiki/concepts/cap-por-servico]].

## Por que importa

É a ponte que justifica usar CAP para desenhar serviços e não só réplicas de banco. [external] Brewer (2012) endossa a leitura por granularidade fina (subsistema, operação, dado, usuário) ([[wiki/entities/eric-brewer]]). O autor avisa que o tema ainda gera debate em material acadêmico.

## Key sources

- [[wiki/sources/teorema-cap-decisao-de-arquitetura-quando-a-comunicacao-falha-bernardo-lobato]]
