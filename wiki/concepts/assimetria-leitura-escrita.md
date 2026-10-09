---
type: concept
title: "Assimetria entre Leitura e Escrita"
aliases: ["assimetria read/write", "critério de adoção do CQRS"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
tags: [cqrs, trade-off, read-model, write-model, decisao-arquitetural]
skill: tech-mentor-system-design
status: draft
---

# Assimetria entre Leitura e Escrita

## TL;DR

O critério que justifica [[wiki/concepts/cqrs]]: o lado de escrita (regras, invariantes, transições de estado) e o de leitura (telas, relatórios, projeções) precisam de **estruturas, cargas ou escalas significativamente diferentes**. Sem isso, dois modelos são só custo.

## Sinais de que existe

- **Modelo:** escrita exige agregado rico; leitura quer uma linha consolidada (pedido + pagamento + entrega + cliente).
- **Carga:** milhões de leituras do mesmo contador vs. escrita em alta frequência → contenção/lock ([[wiki/concepts/contencao-de-lock-leitura-escrita]]).
- **Múltiplas projeções:** usuário, dashboard, relatório, integração.
- **Escala independente:** armazenamento/índices diferentes por lado.
- **Simplificação:** o extrato não precisa conhecer estorno/conciliação.

## Não basta "muita leitura"

Proporção de volume sozinha não decide; conta a **natureza do trabalho** de cada lado. Cf. dois motivadores (volume e modelo) em [[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]].

## Sinais de que NÃO existe

CRUD simples, mesmo modelo atende bem, volume baixo, consultas diretas. Custo da adoção: dois módulos, sincronização, [[wiki/concepts/eventual-consistency]], debug em cadeia. Ver [[wiki/concepts/over-engineering]] e [[wiki/concepts/tradeoff-arquitetural]].

## Key sources

- [[wiki/sources/cqrs-quando-faz-sentido-cqs-bernardo-lobato]] — quatro critérios; exemplos pedido, contador de views, extrato
