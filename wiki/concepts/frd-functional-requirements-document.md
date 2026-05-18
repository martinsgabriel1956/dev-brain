---
type: concept
title: "FRD — Functional Requirements Document"
aliases: ["FRD", "Functional Requirements Document"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 1
tags: [produto, requisitos, documentacao, frd]
skill: tech-mentor-leadership
status: stable
---

# FRD — Functional Requirements Document

**TL;DR:** FRD detalha como o sistema deve se comportar funcionalmente. É derivado do [[prd-product-requirements-document]] e não prescreve arquitetura — apenas o contrato funcional que a implementação deve honrar.

## O Que É

Especificação técnica suficiente para engenharia implementar sem ambiguidade. Cobre fluxos funcionais, regras de negócio, entradas/saídas, estados do sistema e comportamentos de erro.

## Estrutura Típica

1. Visão geral do módulo/feature
2. Atores e permissões
3. Fluxos funcionais (happy path + alternativos)
4. Regras de negócio explícitas
5. Entradas, saídas, validações
6. Integrações e dependências externas
7. Tratamento de erros e estados de falha
8. Requisitos não-funcionais: performance, SLA, segurança

## Quando Usar / Evitar

**Usar:** sistemas regulados (PCI-DSS, LGPD, HIPAA), integrações críticas, times grandes/distribuídos sem contato diário com PM, features com SLA contratual.

**Evitar:** MVPs — [[user-stories]] com bons critérios de aceitação cobrem o mesmo espaço com menos overhead.

## Posição na Hierarquia

```
PRD (o quê + por quê)
  ↓
FRD (como o sistema se comporta)
  ↓
TRD (como o sistema é implementado)
```

## Key Sources

- [[wiki/sources/frd]]

## Conceitos Relacionados

[[prd-product-requirements-document]] · [[user-stories]] · [[trd-technical-requirements-document]] · [[adr-architecture-decision-record]]
