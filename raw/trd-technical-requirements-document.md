---
date: 2026-05-17
tags: [tech-mentor, produto, requisitos, documentação]
skill: tech-mentor-system-design/references/trd
level: fundamento
---

# TRD — Technical Requirements Document

## Contexto

O TRD traduz o que o produto precisa fazer (requisitos funcionais do PRD/BRD) em **como o sistema vai implementar isso** — especificações técnicas, restrições, interfaces, segurança e performance.

## Como Funciona

```
Problema de negócio
       ↓
BRD (Business Requirements) — "o que o negócio precisa"
       ↓
PRD (Product Requirements)  — "o que o produto faz"
       ↓
TRD (Technical Requirements) — "como o sistema implementa"
       ↓
Implementação
```

O PRD responde "o quê". O TRD responde "como".

## Código de Referência

Exemplo de payload especificado em TRD para um sistema de notificações:

```typescript
// Contrato definido no TRD — todos os consumidores dependem desse shape
type NotificationPayload = {
  orderId: string;       // UUID v4
  status: OrderStatus;   // enum definido no domínio
  timestamp: string;     // ISO 8601 com ms
};

type OrderStatus = "pending" | "processing" | "shipped" | "delivered" | "cancelled";
```

## O que um TRD contém

| Seção | Conteúdo |
|---|---|
| **Contexto** | Problema técnico que o documento resolve |
| **Escopo** | O que está dentro e fora da solução |
| **Arquitetura** | Diagrama de componentes, fluxo de dados |
| **Interfaces** | Contratos de API, payloads, schemas de DB |
| **Requisitos não-funcionais** | Performance, SLA, disponibilidade, latência |
| **Segurança** | Autenticação, autorização, criptografia, compliance |
| **Dependências** | Serviços externos, bibliotecas, times |
| **Riscos técnicos** | O que pode dar errado e como mitigar |
| **Critérios de aceitação técnica** | Como validar que a implementação está correta |

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Escrever TRD antes do código | Alinha times, evita retrabalho | Tempo upfront, pode ficar desatualizado |
| TRD detalhado | Rastreabilidade, onboarding mais fácil | Overhead em features simples |
| Sem TRD | Velocidade inicial | Decisões implícitas, dívida de alinhamento |

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

## TRD vs. RFC vs. ADR

| Doc | Foco | Quando usar |
|---|---|---|
| **TRD** | Especificação completa de uma feature | Antes de iniciar implementação complexa |
| **RFC** | Proposta de mudança — busca feedback | Quando a decisão ainda está aberta |
| **ADR** | Registro de decisão tomada + contexto | Após a decisão, para rastreabilidade |

## Conceitos Relacionados

[[prd-product-requirements-document]] · [[adr-architecture-decision-record]] · [[rfc-request-for-comments]] · [[system-design]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-05-17*
