---
type: concept
title: "Mito da Padronização de Arquitetura"
aliases: ["monolito é melhor", "microsserviço é melhor", "regra universal de arquitetura"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [arquitetura, decisao-arquitetural, mito, hype]
skill: tech-mentor-system-design
status: draft
---

# Mito da Padronização de Arquitetura

Crença de que existe **um estilo universalmente melhor**: "monolito é melhor", "microsserviço é melhor", "event-driven é melhor", "clean architecture é melhor", "camadas é melhor". [[wiki/entities/bernardo-lobato]] ([[wiki/sources/decisoes-de-arquitetura-tradeoffs-e-contexto-bernardo-lobato]]) chama de "no mínimo perigoso" tratar uma decisão que depende de tanta coisa como regra.

Contra-exemplo: app pequena com equipe pequena e pouca escala tem problemas muito diferentes de uma plataforma multi-região, com milhões de operações e várias equipes. Mesmo entre sistemas parecidos, a capacidade de operar a complexidade (equipe, infra, experiência) decide.

Parente de [[wiki/concepts/cargo-cult-tecnologico]], [[wiki/concepts/avaliar-hype-tecnologico]] e [[wiki/concepts/sem-balas-de-prata]]. Antídoto: [[wiki/concepts/contexto-na-decisao-arquitetural]] e [[wiki/concepts/tradeoff-arquitetural]].

## Key sources

- [[wiki/sources/decisoes-de-arquitetura-tradeoffs-e-contexto-bernardo-lobato]]
