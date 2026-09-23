---
type: concept
title: "Pré-condição, Pós-condição e Invariante"
aliases: ["precondition", "postcondition", "invariant", "pré-condições", "pós-condições", "invariantes"]
date_created: 2026-09-23
date_updated: 2026-09-23
source_count: 1
tags: [design-by-contract, pre-condicao, pos-condicao, invariante, asserção]
skill: tech-mentor-backend
status: draft
---

## TL;DR

Os três componentes de um contrato em [[wiki/concepts/design-by-contract]]. [[wiki/sources/design-by-contract-video]]

| Parte | O que é | Quem responde |
|---|---|---|
| **Pré-condição** | O que deve ser verdade **antes** de chamar a rotina (requisitos). Rotina nunca deve ser chamada se violada | **Chamador** passa bons dados |
| **Pós-condição** | O que a rotina **garante** após executar; implica que ela sempre termina (sem laço infinito) | **Rotina** |
| **Invariante** | Sempre verdadeira do ponto de vista do chamador; pode ser quebrada **durante** a execução, mas restaurada ao final | Rotina/classe |

## Exemplo (depósito)

- Pré: `quantia > 0` e conta aberta → senão, exceção/asserção falha.
- Pós: transação registrada no sistema.

[[wiki/sources/design-by-contract-video]]

## Conexões

- Invariante ↔ proteção de estado válido em [[wiki/concepts/encapsulamento]] (ver [[wiki/sources/encapsulamento-proteger-estado-invalido]]).
- Invariante ↔ propriedade em [[wiki/concepts/property-based-testing]].
- Violação ↔ [[wiki/concepts/excecao-vs-erro]].

## Key Sources

- [[wiki/sources/design-by-contract-video]]
