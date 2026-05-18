---
type: source
title: "FRD — Functional Requirements Document"
aliases: ["FRD", "Functional Requirements Document"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_file: /home/nemomartins/Documentos/new/dev-study/raw/frd.md
source_url: ""
author: "tech-mentor-leadership"
date_published: 2026-05-17
date_ingested: 2026-05-17
tags: [produto, requisitos, frd, documentacao]
skill: tech-mentor-leadership
status: stable
---

# FRD — Functional Requirements Document

## TL;DR

FRD detalha **como o sistema deve se comportar** funcionalmente. É derivado do [[wiki/concepts/prd-product-requirements-document]] e serve como especificação técnica suficiente para engenharia implementar sem ambiguidade. Inclui fluxos, regras de negócio, entradas/saídas, estados e comportamentos de erro.

## Key Claims

- **Derivado do PRD:** PRD responde "o quê" e "por quê"; FRD responde "como o sistema se comporta". [[wiki/concepts/prd-product-requirements-document]]
- **Estrutura: 7 seções obrigatórias** — visão geral, atores/permissões, fluxos (happy + alternativos), regras de negócio, entradas/saídas/validações, integrações, tratamento de erros + NFRs
- **Regras de negócio explícitas** permitem QA derivar casos de teste diretamente sem interpretação
- **Crítico em:** sistemas regulados (PCI-DSS, LGPD, HIPAA), integrações críticas (pagamentos, ERPs), times distribuídos sem contato diário com PM
- **Overhead não compensa em:** MVPs rápidos — [[wiki/concepts/user-stories]] com bons critérios de aceitação cobrem o mesmo espaço

## Concepts

- [[wiki/concepts/frd-functional-requirements-document]]
- [[wiki/concepts/prd-product-requirements-document]]
- [[wiki/concepts/user-stories]]
- [[wiki/concepts/trd-technical-requirements-document]]

## Open Questions

- Como manter o FRD sincronizado com o código em produtos com iteração rápida sem criar dívida de documentação?

## Raw Quotes

> "O FRD detalha fluxos funcionais, regras de negócio, entradas/saídas, estados do sistema e comportamentos de erro. Não prescreve arquitetura — apenas o contrato funcional que a implementação deve honrar."
