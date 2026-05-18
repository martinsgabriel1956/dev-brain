---
type: concept
title: "TRD — Technical Requirements Document"
aliases: ["TRD", "Technical Requirements Document", "documento de requisitos técnicos"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 1
tags: [trd, documentação, requisitos, system-design, arquitetura]
skill: tech-mentor-system-design
status: stable
---

# TRD — Technical Requirements Document

Documento que traduz os requisitos de produto ([[prd-product-requirements-document]]) em especificações técnicas concretas: arquitetura, contratos de API, schemas, requisitos não-funcionais, segurança e critérios de aceitação técnica.

## Posição na Cadeia

```
BRD → PRD → TRD → Implementação
```

O TRD é o último documento antes do código — serve como contrato entre quem define o produto e quem implementa o sistema.

## Quando Escrever

Necessário quando: feature cross-team, contrato de API com dependentes externos, compliance, decisão arquitetural de longo prazo.

Desnecessário quando: feature isolada em um serviço, bug fix sem mudança de contrato, UI sem impacto backend.

## Relação com Outros Docs

- [[rfc-request-for-comments]] — proposta aberta buscando feedback (antes da decisão)
- [[adr-architecture-decision-record]] — registro histórico de decisão já tomada (após a decisão)
- [[trd-technical-requirements-document]] — especificação completa para implementação (antes do código)

## Key Sources

- [[wiki/sources/trd-technical-requirements-document]]
