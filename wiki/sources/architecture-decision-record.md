---
type: source
title: "Architecture Decision Record (ADR)"
aliases: ["ADR"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_file: /home/nemomartins/Documentos/new/dev-study/raw/architecture-decision-record.md
source_url: ""
author: "tech-mentor-system-design"
date_published: 2026-05-17
date_ingested: 2026-05-17
tags: [system-design, decisoes-tecnicas, documentacao, adr]
skill: tech-mentor-system-design
status: stable
---

# Architecture Decision Record (ADR)

## TL;DR

ADR captura uma decisão arquitetural já tomada — imutável, datado, versionado com o código. Se a decisão mudar, cria-se um novo ADR que supersede o anterior. Resolve o problema de decisões técnicas invisíveis em projetos de longa duração.

## Key Claims

- **Imutabilidade é intencional:** ADR nunca é editado. Erros são corrigidos com novo ADR que supersede o anterior. Preserva contexto histórico fiel. [[wiki/concepts/adr-architecture-decision-record]]
- **Status progressivo:** `Proposed → Accepted → Deprecated → Superseded by ADR-XXXX`
- **Formato MADR:** Contexto → Decisão → Consequências (+ vantagens, - desvantagens)
- **Proximidade ao código:** fica em `docs/decisions/` ou `adr/`, versionado com git, visível no PR
- **RFC precede ADR:** proposta aberta → debate → decisão tomada → ADR registra. [[wiki/concepts/rfc-request-for-comments]]
- **Escopo por decisão:** apenas quando afeta estrutura, tecnologia, contrato de API ou schema de DB; difícil ou cara de reverter

## Entities

- [[wiki/entities/christopher-alexander]] — linguagem de patterns original que inspirou a formalização de ADRs

## Concepts

- [[wiki/concepts/adr-architecture-decision-record]]
- [[wiki/concepts/rfc-request-for-comments]]
- [[wiki/concepts/trd-technical-requirements-document]]
- [[wiki/concepts/high-level-design]]
- [[wiki/concepts/low-level-design]]

## Open Questions

- Em times pequenos (< 4 pessoas), quando o ADR vira burocracia desnecessária vs. ferramenta útil?

## Raw Quotes

> "Nunca é editado — se a decisão mudar, cria-se um novo ADR que supersede o anterior."

> "Usar quando: é difícil ou cara de reverter; vai aparecer em code review recorrentemente."
