---
type: entity
title: "Alexandria (Nubank)"
aliases: ["alexandria", "plataforma de observabilidade do nubank"]
date_created: 2026-09-15
date_updated: 2026-09-15
source_count: 1
tags: [nubank, observabilidade, logs, in-house-platform, fintech]
skill: tech-mentor-backend
status: stub
---

# Alexandria (Nubank)

## TL;DR

Plataforma de observabilidade/logs construída internamente pelo [[wiki/entities/nubank|Nubank]] depois que a solução de terceiros para logs se tornou financeiramente inviável na escala do banco (600 TB de logs/dia). Resultado: 50% mais barata que a solução externa anterior, com controle total sobre os dados.

## Motivação: Custo

Citação atribuída ao site do Nubank:

> "Chegamos a um ponto em que poderíamos contratar o Lionel Messi como engenheiro de software pagando o mesmo valor que pagávamos pela solução externa."

Esse é o padrão clássico de **build vs. buy** decidido por custo marginal em escala: uma solução de terceiro que é barata em baixo volume se torna proibitiva quando o volume cresce ordens de magnitude — nesse ponto, construir internamente (mesmo com o custo de engenharia dedicado) fica mais barato.

## Arquitetura (4 componentes)

1. **Ingestão** — microbatch via [[wiki/concepts/kafka|Kafka]]
2. **Processamento** — filtros e agregações customizados
3. **Storage** — S3 em formato colunar, com 95% de compressão
4. **Query engine** — distribuída

## Escala Reportada

- 600 TB de logs ingeridos por dia
- ~15.000 queries executadas por dia pelos engenheiros
- ~150 PB de dados escaneados (aproximado, conforme relatado na fonte)

## Relação com Observabilidade

Alexandria cobre a camada de **logs** dos [[wiki/concepts/observabilidade|três pilares clássicos de observabilidade]] (métricas, logs, traces) — a fonte não detalha se métricas e traces também passam pela mesma plataforma ou por stacks separadas.

## Key Sources

- [[wiki/sources/nubank-arquitetura-escala-122-milhoes-clientes]] — única fonte até o momento; solução terceirizada substituída não foi nomeada no vídeo (open question)
