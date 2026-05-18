---
type: source
title: "High Level Design (HLD)"
aliases: ["HLD"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_file: /home/nemomartins/Documentos/new/dev-study/raw/high-level-design.md
source_url: ""
author: "tech-mentor-system-design"
date_published: 2026-05-17
date_ingested: 2026-05-17
tags: [system-design, arquitetura, hld, documentacao]
skill: tech-mentor-system-design
status: stable
---

# High Level Design (HLD)

## TL;DR

HLD é a primeira camada de documentação arquitetural — responde "o que o sistema faz e como os grandes blocos se conectam" antes de qualquer linha de código. Opera no nível de serviços, integrações e fluxo de dados. Alinha engenheiros, PMs e stakeholders técnicos sobre a direção do sistema.

## Key Claims

- **Nível de abstração:** serviços, integrações, fluxo de dados — sem detalhe de implementação. [[wiki/concepts/high-level-design]]
- **Cinco perguntas centrais:** quais componentes? como se comunicam? quais tecnologias por camada? monolito vs microsserviços? onde estão pontos de falha?
- **Feito cedo alinha:** times paralelos sem premissas divergentes; custo de realinhamento pós-código é muito maior
- **LLD é o próximo nível:** HLD define blocos, LLD define como cada bloco é implementado. [[wiki/concepts/low-level-design]]
- **C4 Model formaliza HLD:** Context + Container levels mapeiam exatamente o nível do HLD. [[wiki/concepts/c4-model]]

## Concepts

- [[wiki/concepts/high-level-design]]
- [[wiki/concepts/low-level-design]]
- [[wiki/concepts/adr-architecture-decision-record]]
- [[wiki/concepts/trd-technical-requirements-document]]

## Open Questions

- Em projetos com requisitos instáveis, qual é o nível mínimo de HLD que vale a pena documentar antes de começar?

## Raw Quotes

> "Sem HLD, times constroem em paralelo com premissas diferentes — e o custo de realinhamento depois que o código existe é muito maior."

> "Não importa como o Order Service implementa a criação de pedido. Importa que ele persiste em Postgres e publica evento no Kafka."
