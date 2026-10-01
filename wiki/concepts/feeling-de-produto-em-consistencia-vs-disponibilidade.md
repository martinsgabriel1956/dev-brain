---
type: concept
title: "Feeling de produto na escolha entre consistência e disponibilidade"
aliases: ["critério de produto no CAP", "quando escolher C ou A", "domínios de consistência forte"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 2
tags: [system-design, cap-theorem, produto, entrevistas, consistencia, disponibilidade]
skill: tech-mentor-system-design
status: draft
---

# Feeling de produto na escolha entre consistência e disponibilidade

A escolha C vs. A numa partição ([[wiki/concepts/particao-como-pre-condicao-do-cap]]) é, segundo [[wiki/entities/pedro-camaforte]], "muito do seu feeling de produto": quanto a feature impacta o usuário e quanto o dado pode ficar desatualizado sem prejudicar o negócio.

## Heurística de entrevista (da fonte)

| Prefere **consistência** | Prefere **disponibilidade** |
|---|---|
| Ingressos e assentos (cinema, shows, avião) | Redes sociais: foto nova, nome do perfil |
| Estoque (último item) | Comentários (ex.: YouTube) |
| Sistemas financeiros (ordem de transferências, saldo) | Dashboards |

Teste prático: **recarregar a página resolve?** Se sim, o dado pode atrasar. Se um erro vira cobrança duplicada, assento vendido duas vezes ou venda de item inexistente, não pode.

## Cautelas

- É heurística, não regra; o autor admite exceções.
- Consistência aqui = leitura igual em todos os nós ([[wiki/concepts/linearizability]]), não o "C" de [[wiki/concepts/acid]].
- Ver também a escolha de domínio em [[wiki/sources/anatomia-entrevista-system-design-bigtech]] (banco = forte; contador de likes = BASE, [[wiki/concepts/base-basically-available-soft-state-eventual]]).

## Key sources

- [[wiki/sources/teorema-cap-p-e-pre-condicao-escolha-entre-c-e-a-pedro-camaforte]]
- [[wiki/sources/teorema-cap-decisao-de-arquitetura-quando-a-comunicacao-falha-bernardo-lobato]] — casos Netflix, busca de voos (A) e compra (C); "entender o negócio" como critério
