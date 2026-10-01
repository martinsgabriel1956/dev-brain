---
type: concept
title: "Consistência do CAP vs. consistência do ACID"
aliases: ["C do CAP vs C do ACID", "homônimos consistência"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 1
tags: [system-design, cap-theorem, acid, consistencia, bancos-de-dados]
skill: tech-mentor-system-design
status: draft
---

# Consistência do CAP vs. consistência do ACID

Mesma palavra, conceitos diferentes.

| | CAP | [[wiki/concepts/acid]] |
|---|---|---|
| Significa | Depois de uma operação concluída, toda leitura em **qualquer nó** vê o resultado mais recente (na prática, [[wiki/concepts/linearizability]]) | Transação leva o banco de um estado válido a outro, respeitando regras de integridade (constraints) |
| Escopo | Réplicas / nós de um sistema distribuído | Um banco/transação |

Exemplo CAP: depósito confirmado no servidor A, leitura imediata no B ainda mostra o saldo antigo = sem consistência forte. O vídeo de Bernardo Lobato faz essa ressalva explicitamente; o vídeo de [[wiki/entities/pedro-camaforte]] não distingue (ver nota 4 em [[wiki/sources/teorema-cap-p-e-pre-condicao-escolha-entre-c-e-a-pedro-camaforte]]). Mais em [[wiki/concepts/consistency-models]].

## Key sources

- [[wiki/sources/teorema-cap-decisao-de-arquitetura-quando-a-comunicacao-falha-bernardo-lobato]]
