---
type: source
title: "TRD — Technical Requirements Document"
aliases: ["TRD", "Technical Requirements Document"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_file: /home/nemomartins/Documentos/new/dev-study/raw/trd-technical-requirements-document.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-05-17
source_count: 0
tags: [trd, documentação, requisitos, system-design, arquitetura]
skill: tech-mentor-system-design
status: stable
---

# TRD — Technical Requirements Document

## TL;DR

O TRD traduz **o que o produto precisa fazer** (PRD/BRD) em **como o sistema vai implementar isso** — especificações técnicas, contratos de API, restrições de performance, segurança e critérios de aceitação técnica.

## Cadeia de Documentos

```
Problema de negócio
       ↓
BRD — "o que o negócio precisa"
       ↓
PRD — "o que o produto faz"
       ↓
TRD — "como o sistema implementa"
       ↓
Implementação
```

O PRD responde **o quê**. O TRD responde **como**.

## Seções de um TRD

| Seção | Conteúdo |
|---|---|
| Contexto | Problema técnico que o documento resolve |
| Escopo | O que está dentro e fora da solução |
| Arquitetura | Diagrama de componentes, fluxo de dados |
| Interfaces | Contratos de API, payloads, schemas de DB |
| Requisitos não-funcionais | Performance, SLA, disponibilidade, latência |
| Segurança | Autenticação, autorização, criptografia, compliance |
| Dependências | Serviços externos, bibliotecas, times |
| Riscos técnicos | O que pode dar errado e como mitigar |
| Critérios de aceitação técnica | Como validar que a implementação está correta |

## Exemplo de Contrato Definido em TRD

```typescript
// Contrato definido no TRD — todos os consumidores dependem desse shape
type NotificationPayload = {
  orderId: string;       // UUID v4
  status: OrderStatus;   // enum definido no domínio
  timestamp: string;     // ISO 8601 com ms
};

type OrderStatus = "pending" | "processing" | "shipped" | "delivered" | "cancelled";
```

## Quando Usar / Quando Evitar

**Use TRD quando:**
- Feature envolve múltiplos serviços ou times
- Há contratos de API que outros times dependem
- Decisões de arquitetura têm impacto de longo prazo
- Requisitos de compliance precisam de rastreabilidade

**Não precisa de TRD quando:**
- Feature isolada, um serviço, um time
- Mudança de UI sem impacto backend
- Bug fix sem mudança de contrato

## TRD vs RFC vs ADR

| Doc | Foco | Quando usar |
|---|---|---|
| [[trd-technical-requirements-document]] | Especificação completa de uma feature | Antes de iniciar implementação complexa |
| [[rfc-request-for-comments]] | Proposta de mudança — busca feedback | Quando a decisão ainda está aberta |
| [[adr-architecture-decision-record]] | Registro de decisão tomada + contexto | Após a decisão, para rastreabilidade |

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| TRD antes do código | Alinha times, evita retrabalho | Tempo upfront, pode ficar desatualizado |
| TRD detalhado | Rastreabilidade, onboarding mais fácil | Overhead em features simples |
| Sem TRD | Velocidade inicial | Decisões implícitas, dívida de alinhamento |

## Conceitos Relacionados

[[trd-technical-requirements-document]] · [[prd-product-requirements-document]] · [[brd-business-requirements-document]] · [[rfc-request-for-comments]] · [[adr-architecture-decision-record]]
