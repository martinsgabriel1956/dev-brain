---
type: concept
title: "High Level Design (HLD)"
aliases: ["HLD", "High-Level Design"]
date_created: 2026-05-17
date_updated: 2026-07-20
source_count: 2
tags: [system-design, arquitetura, hld, documentacao]
skill: tech-mentor-system-design
status: stable
---

# High Level Design (HLD)

**TL;DR:** HLD é a primeira camada de documentação arquitetural — responde "o que o sistema faz e como os grandes blocos se conectam" antes de qualquer linha de código. Opera no nível de serviços, integrações e fluxo de dados.

## O Que É

Artefato que alinha engenheiros, PMs e stakeholders técnicos sobre a direção do sistema. Não entra em detalhe de implementação.

## Cinco Perguntas que o HLD Responde

1. Quais são os componentes principais (APIs, bancos, filas, CDNs, serviços externos)?
2. Como eles se comunicam (REST, gRPC, eventos, WebSocket)?
3. Quais tecnologias foram escolhidas por camada e por quê?
4. Quais são as decisões arquiteturais centrais (monolito vs. microsserviços, sync vs. async)?
5. Onde estão os pontos de falha e como são mitigados?

## Quando Usar / Evitar

**Usar:** iniciando projeto/feature de porte médio+, múltiplos times ou serviços envolvidos, aprovação de direção técnica antes de investir em implementação, onboarding.

**Evitar:** feature pequena e isolada, protótipo ou spike de validação, time de uma pessoa com contexto total.

## Relação com LLD

HLD define os blocos. [[low-level-design]] define como cada bloco é implementado internamente.

## Em entrevista de system design

Em uma [[wiki/concepts/entrevista-system-design|entrevista de system design]], o desenho do HLD é a última etapa da sessão, não a primeira — vem depois de levantar requisitos, montar plano de capacidade ([[wiki/concepts/estimativas-back-of-envelope]]) e modelar dados/API. O entrevistador avalia se o desenho é coerente com tudo que foi dito antes dele.

## Key Sources

- [[wiki/sources/high-level-design]]
- [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]]

## Conceitos Relacionados

[[low-level-design]] · [[adr-architecture-decision-record]] · [[trd-technical-requirements-document]] · [[wiki/concepts/entrevista-system-design]]
