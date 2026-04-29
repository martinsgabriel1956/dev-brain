---
date: 2026-04-17
tags: [tech-mentor, arquitetura, principios, evolucao]
skill: tech-mentor-system-design/references/architecture-principles
level: arquiteto
---

# Evolutionary Architecture

## Contexto
Conceito de Neal Ford et al. — arquitetura que **suporta mudança incremental e guiada** ao longo de múltiplas dimensões (técnica, organizacional, domínio de negócio). O oposto de "big upfront design".

A premissa fundamental: você não pode prever o que o sistema precisará ser em 3 anos, então construa para que a arquitetura possa **evoluir com segurança**, não para que seja "perfeita agora".

## Três Princípios Centrais

### 1. Fitness Functions como guardrails
Testes automatizados de características arquiteturais. Se a arquitetura muda, os fitness functions quebram — você precisa atualizar tanto o código quanto as regras intencionalmente.

### 2. Mudança incremental
Nunca reescreva do zero — migre incrementalmente. O **Strangler Fig** é o padrão de implementação desse princípio. Cada mudança arquitetural deve ser deployável de forma independente.

### 3. Múltiplas dimensões de evolução
Arquitetura evolui em pelo menos três dimensões simultaneamente:
- **Técnica:** performance, segurança, escalabilidade
- **Domínio:** bounded contexts mudam conforme o negócio evolui
- **Operacional:** deployment, observabilidade, SRE

```
              Início              Evolutiva
         ┌───────────────┐   ┌───────────────────┐
Técnica  │ Monolito Rails │──►│ Microsserviços    │
         └───────────────┘   └───────────────────┘
              ───────────────────────────────────►
         ┌───────────────┐   ┌───────────────────┐
Domínio  │ Modelo único  │──►│ Bounded Contexts  │
         └───────────────┘   └───────────────────┘
              ───────────────────────────────────►
         ┌───────────────┐   ┌───────────────────┐
Ops      │ Deploy manual │──►│ GitOps + canary   │
         └───────────────┘   └───────────────────┘
```

## Práticas que Habilitam Evolução

### Acoplamento baixo como requisito não-funcional

```typescript
// Ruim — acoplamento direto entre módulos, difícil de separar depois
import { UserRepository } from "../../users/repositories/user.repository";
import { OrderRepository } from "../../orders/repositories/order.repository";

class CheckoutService {
  constructor(
    private userRepo: UserRepository,    // domínio de usuário vaza no checkout
    private orderRepo: OrderRepository
  ) {}
}

// Bom — checkout depende de interfaces, não de implementações
type UserProfile = { id: string; email: string; plan: string };
type OrderStore = { save: (order: Order) => Promise<void> };

class CheckoutService {
  constructor(
    private userProfile: UserProfile,
    private orderStore: OrderStore
  ) {}
}
```

### Strangler Fig — migração incremental

```
           Fase 1: proxy na frente do legado
   Request → Proxy → Legado (100% das rotas)

           Fase 2: novas rotas no novo sistema
   Request → Proxy → Novo (GET /products)
                   → Legado (demais rotas)

           Fase 3: migração completa
   Request → Proxy → Novo (100% das rotas)
                   → Legado desativado
```

### Feature Flags para evolução segura

```typescript
const flags = await featureFlag.get("new-checkout-flow");

if (flags.isEnabled("new-checkout-flow", { userId })) {
  return newCheckoutService.process(order);
}
return legacyCheckoutService.process(order);
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Flexibilidade | Adapta ao negócio sem reescritas | Complexidade maior que design estático |
| Risco | Mudanças menores e reversíveis | Disciplina de fitness functions exige cultura forte |
| Velocidade | Times autônomos movem-se independente | Coordenação de contratos entre partes ainda necessária |
| Dívida técnica | Tech debt identificado e pago incrementalmente | Sem big bang de melhoria — progresso é gradual |

## Quando Usar / Quando Evitar

**Usar quando:**
- O domínio de negócio ainda está amadurecendo (startups, novos produtos)
- Existe legado que não pode ser abandonado mas precisa evoluir
- O time cresce e times independentes precisam de autonomia

**Evitar quando:**
- O domínio é bem definido e estável (software fiscal, por exemplo)
- Overhead de fitness functions e infraestrutura de evolução não se justifica para o escopo

## Conceitos Relacionados
[[architecture-fitness-functions]] · [[strangler-fig]] · [[feature-flags]] · [[adr]] · [[conways-law]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
