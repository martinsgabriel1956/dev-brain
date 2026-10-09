---
type: concept
title: "Trade-off Arquitetural"
aliases: ["trade-off", "tradeoff de arquitetura", "troca arquitetural"]
date_created: 2026-10-07
date_updated: 2026-10-09
source_count: 2
tags: [arquitetura, decisao-arquitetural, trade-off]
skill: tech-mentor-system-design
status: draft
---

# Trade-off Arquitetural

Toda decisão arquitetural **prioriza algumas características e aceita consequências em troca**. Segundo [[wiki/entities/bernardo-lobato]], é a tese de [[wiki/sources/decisoes-de-arquitetura-tradeoffs-e-contexto-bernardo-lobato]]: a decisão se avalia pelo problema que resolve **e** pelos que introduz.

| Decisão | Ganha | Paga |
|---|---|---|
| Arquitetura distribuída ([[wiki/concepts/microsservicos]]) | independência, escala seletiva, autonomia de evolução | rede/latência, observabilidade distribuída, consistência entre serviços, timeouts/retries, transações distribuídas |
| Abstração no código | facilidade de evoluir um comportamento | mais complexidade ([[wiki/concepts/complexidade-acidental]]) |
| Cache ([[wiki/concepts/tradeoff-de-cache]]) | menor latência | risco de inconsistência |
| Processamento assíncrono ([[wiki/concepts/comunicacao-assincrona]]) | melhor tempo de resposta | fluxo mais difícil de acompanhar |
| Arquitetura preparada para escala | suporta carga muito maior | mais infraestrutura e conhecimento para operar |

Pergunta de trabalho: *qual característica quero melhorar e quais consequências aceito pagar?* Ver [[wiki/concepts/escolher-os-problemas-que-voce-quer-ter]], [[wiki/concepts/contexto-na-decisao-arquitetural]], [[wiki/concepts/sem-balas-de-prata]]. Para registrar o trade-off aceito, [skill: tech-mentor-system-design] aponta ADR ([[wiki/concepts/adr-architecture-decision-record]]); o vídeo não cita.

## Key sources

- [[wiki/sources/decisoes-de-arquitetura-tradeoffs-e-contexto-bernardo-lobato]]

## Key sources (adição 2026-10-09)

- [[wiki/sources/cqrs-quando-faz-sentido-cqs-bernardo-lobato]] — "o benefício precisa justificar a complexidade": CQRS como trade-off modelado, não padrão por default
