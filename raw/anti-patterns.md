---
date: 2026-04-14
tags: [tech-mentor, arquitetura, anti-patterns, design]
skill: tech-mentor-system-design/references/arquitetura
level: avançado
---

# Anti-patterns Arquiteturais

## Contexto

Anti-patterns são soluções recorrentes para problemas recorrentes que parecem corretas no curto prazo mas criam dívida técnica severa. Reconhecê-los é metade do trabalho de um arquiteto — a outra metade é saber por qual pattern substituí-los.

## Big Ball of Mud

O anti-pattern mais comum. Um sistema sem estrutura perceptível: fronteiras ignoradas, dependências em todas as direções, sem separação de responsabilidades.

**Sintomas:**
- Impossível mudar qualquer coisa sem quebrar outra
- Ninguém entende o sistema inteiro
- Cada feature nova aumenta o acoplamento

**Como acontece:** Pressão de entrega constante, sem investimento em arquitetura, sem code review estrutural.

**Solução:** Não reescrever — aplicar Strangler Fig pattern para extrair módulos gradualmente com Bounded Contexts bem definidos.

## Distributed Monolith

O pior dos dois mundos: a complexidade operacional de microsserviços com o acoplamento de um monolito.

**Sintomas:**
- Serviços que só funcionam se deployados juntos
- Chamadas síncronas em cadeia (A → B → C → D) para qualquer operação
- Banco de dados compartilhado entre "microsserviços"
- Um serviço quebrado derruba os outros

```
❌ Distributed Monolith
orders-service → payments-service → inventory-service → notifications-service
(chamadas síncronas em cadeia — blast radius = sistema inteiro)

✅ Microsserviços reais
orders-service emite OrderCreated event
  ├── payments-service consome de forma autônoma
  ├── inventory-service consome de forma autônoma
  └── notifications-service consome de forma autônoma
```

**Como acontece:** Decomposição por função técnica em vez de domínio, sem autonomia de dados por serviço. Conway's Law não respeitada.

## God Object / God Class

Uma classe ou serviço que sabe tudo e faz tudo. O `UserService` que tem 3000 linhas com métodos de autenticação, faturamento, notificações e relatórios.

**Sintomas:**
- Classe importada em 80% dos outros arquivos
- Qualquer nova feature "cabe" nela
- Impossível testar em isolamento

```typescript
// ❌ God Class
class UserService {
  createUser() { ... }
  authenticateUser() { ... }
  chargeUser() { ... }         // pertence a BillingService
  sendWelcomeEmail() { ... }  // pertence a NotificationService
  generateReport() { ... }   // pertence a ReportingService
}

// ✅ Separado por responsabilidade
class UserRepository { ... }           // persistência
class AuthService { ... }              // autenticação (infra)
class BillingUseCase { ... }           // regra de negócio de cobrança
class UserRegistrationUseCase { ... }  // orquestração de criação
```

## Anemic Domain Model

Entidades que são apenas DTOs — sem comportamento, sem invariantes. Toda a lógica de negócio vive em Services ou UseCases que manipulam objetos passivos.

```typescript
// ❌ Anemic — Order é apenas um saco de dados
class Order {
  id: string;
  status: string;
  items: OrderItem[];
  total: number;
}

// OrderService tem 500 linhas de lógica de negócio sobre Order

// ✅ Rich Domain Model — Order protege suas invariantes
class Order {
  private status: OrderStatus;
  private items: OrderItem[];

  addItem(item: OrderItem) {
    if (this.status !== OrderStatus.DRAFT) {
      throw new OrderNotEditableError(this.id);
    }
    this.items.push(item);
    this.recalculateTotal();
  }

  confirm() {
    if (this.items.length === 0) {
      throw new EmptyOrderError(this.id);
    }
    this.status = OrderStatus.CONFIRMED;
    this.addDomainEvent(new OrderConfirmed(this.id));
  }
}
```

**Por que é perigoso:** lógica de negócio espalhada em múltiplos serviços, invariantes não protegidas, duplicação inevitável.

## Accidental Complexity vs. Essential Complexity

Essential complexity: complexidade inerente ao problema de negócio.
Accidental complexity: complexidade criada pela solução técnica.

Anti-patterns comuns de accidental complexity:
- Abstrações prematuras para casos de uso inexistentes
- Microsserviços para um time de 3 pessoas
- Event Sourcing para uma CRUD simples
- Camadas de abstração sobre abstrações

**Regra:** Se você não consegue explicar por que a complexidade existe em termos de negócio, provavelmente é acidental.

## Resume-Driven Development

Escolha de tecnologia baseada em "o que fica bem no curto prazo" — Kubernetes para 10 usuários, blockchain para rastreabilidade simples, GraphQL para uma API com 3 endpoints.

**Sinal de alerta:** A justificativa técnica não sobrevive à pergunta "qual problema de negócio isso resolve melhor do que a alternativa simples?"

## Trade-offs

| Anti-pattern | Causa raiz | Substituto |
|---|---|---|
| Big Ball of Mud | Sem fronteiras, pressão de entrega | Bounded Contexts + Strangler Fig |
| Distributed Monolith | Decomposição errada, DB compartilhado | Database per Service + eventos |
| God Object | SRP ignorado | Separação por responsabilidade de domínio |
| Anemic Domain Model | DDD ignorado | Rich Domain Model |
| Accidental Complexity | Over-engineering | YAGNI + design emergente |

## Quando Usar / Quando Evitar

Não existe "quando usar" anti-patterns — mas existe quando *reconhecê-los*:
- Em code review: God Class e Anemic Domain Model são detectáveis imediatamente
- Em planejamento de arquitetura: Distributed Monolith emerge quando discutimos fronteiras de serviço
- Em reuniões de decisão de stack: Resume-Driven Development é diagnosticável na justificativa
- Em debugging de incidentes: Big Ball of Mud e Distributed Monolith tornam o blast radius imprevisível

## Conceitos Relacionados

[[clean-architecture]] · [[hexagonal-architecture]] · [[ddd-tactical]] · [[microsservicos]] · [[conways-law]] · [[solid]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-14*
