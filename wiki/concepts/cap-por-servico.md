---
type: concept
title: "CAP por serviço (granularidade da escolha)"
aliases: ["escolha CAP por microsserviço", "CAP não é global", "consistência forte no booking e disponibilidade na busca"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 2
tags: [system-design, cap-theorem, microsservicos, entrevistas, consistencia, disponibilidade]
skill: tech-mentor-system-design
status: draft
---

# CAP por serviço (granularidade da escolha)

A escolha entre consistência e disponibilidade **não precisa ser única para o sistema inteiro**. Em arquiteturas de [[wiki/concepts/microsservicos]], cada serviço (ou feature) pode ficar de um lado.

## Exemplo canônico: sistema de ingressos de cinema

| Serviço | Escolha | Por quê |
|---|---|---|
| **Booking / reservas** | Consistência (C) | Dois usuários não podem comprar o mesmo assento; combina com [[wiki/concepts/reservation-pattern]] e [[wiki/concepts/pessimistic-locking]] |
| **Search / catálogo** | Disponibilidade (A) | Se alguém edita a descrição de um filme, travar a busca de todos até propagar seria absurdo; mostrar a descrição antiga por alguns segundos é aceitável ([[wiki/concepts/eventual-consistency]]) |

## Como decidir

Pergunta guia: *o que acontece com o negócio se este dado estiver velho por alguns segundos?* Ver [[wiki/concepts/feeling-de-produto-em-consistencia-vs-disponibilidade]].

## Marcador de senioridade

Na fonte, é o "plus" que eleva a resposta de entrevista: dizer "CP ou AP" para o sistema todo é a resposta de nível médio; separar por serviço é o diferencial sênior. Combina com a expectativa de vocabulário de CAP em [[wiki/concepts/niveis-de-senioridade-system-design]].

[external] Eric Brewer (2012): a escolha C vs. A "can occur many times within the same system at very fine granularity; not only can subsystems make different choices, but the choice can change according to the operation or even the specific data or user involved" ([[wiki/entities/eric-brewer]]). Também é análogo ao ajuste por operação do DynamoDB (leitura eventual vs. forte) citado em [[wiki/concepts/pacelc]].

## Mais exemplos: por funcionalidade

| Funcionalidade | Escolha | Por quê |
|---|---|---|
| Catálogo de filmes (Netflix) | A | Título velho por segundos é irrelevante; não entregar o vídeo é o problema |
| Busca de voos | A | Resultado aproximado é melhor que nenhum |
| Compra do bilhete | C | Evita vender o mesmo assento a dois usuários |

Ver [[wiki/concepts/cap-exige-estado-compartilhado]] e [[wiki/entities/netflix]].

## Key sources

- [[wiki/sources/teorema-cap-p-e-pre-condicao-escolha-entre-c-e-a-pedro-camaforte]]
- [[wiki/sources/teorema-cap-decisao-de-arquitetura-quando-a-comunicacao-falha-bernardo-lobato]] — segundo exemplo canônico: busca de voos (A) vs. compra do bilhete (C); catálogo Netflix (A); Estoque/Pedido
