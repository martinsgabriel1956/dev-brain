---
date: 2026-04-13
tags: [tech-mentor, arquitetura, documentacao, c4-model, diagramas]
skill: tech-mentor-system-design/references/documentation
level: fundamento
---

# C4 Model

## Contexto

Criado por Simon Brown, o C4 Model é um framework para documentar arquitetura de software em **quatro níveis de abstração**, análogos a mapas em diferentes escalas: país → cidade → bairro → edifício.

O problema que resolve: **os diagramas de arquitetura tradicionais são ambíguos** — "caixa" pode significar microsserviço, monolito, biblioteca, banco de dados ou pessoa, dependendo de quem desenhou. C4 padroniza o vocabulário.

Ferramentas: Structurizr (oficial), PlantUML (C4 extension), Mermaid (limitado), Draw.io com stencils C4.

## Como Funciona

### Os 4 Níveis

**Level 1 — System Context**
O maior nível. Mostra o sistema como uma caixa preta e seu relacionamento com usuários e sistemas externos. Audiência: qualquer pessoa (técnica ou não).

```
┌─────────────────────────────────────────────────┐
│                System Context                    │
│                                                 │
│  [Usuário]──────→[Sistema: E-commerce]──→[Stripe]│
│                         │                       │
│                         └──→[SendGrid]           │
└─────────────────────────────────────────────────┘
```

**Level 2 — Container**
Dentro do sistema, mostra as unidades implantáveis: aplicações web, APIs, bancos de dados, filas, etc. Audiência: devs e ops.

```
┌────────────────────────────────────────────────────────┐
│  Sistema E-commerce                                     │
│                                                        │
│  [Browser]──→[Next.js App]──→[API Gateway]──→[Auth API]│
│                                   │                    │
│                         ┌─────────┴───────────┐        │
│                     [Order API]          [Product API] │
│                         │                    │         │
│                    [PostgreSQL]          [Redis]        │
│                         │                              │
│                    [Kafka Cluster]                      │
└────────────────────────────────────────────────────────┘
```

**Level 3 — Component**
Dentro de um container específico, mostra os componentes principais (controllers, use cases, repositories). Audiência: devs do time daquele serviço.

```
┌──────────────────────────────────────────────┐
│  Order API (Container)                        │
│                                              │
│  [Order Controller]──→[PlaceOrderUseCase]    │
│                              │               │
│                    [OrderRepository]         │
│                    [PaymentGateway Port]     │
│                    [EventPublisher]          │
└──────────────────────────────────────────────┘
```

**Level 4 — Code**
Diagramas UML de classes/sequência dentro de um componente. Audiência: o dev que vai modificar aquele código. **Raramente vale manter atualizado** — o código em si é mais preciso.

### Structurizr DSL (Recomendado)

Ao invés de diagramas manuais (que ficam desatualizados), use DSL que gera os diagramas:

```dsl
workspace "E-commerce" "Sistema de e-commerce simplificado" {

  model {
    user = person "Comprador" "Usuário que realiza compras"
    admin = person "Admin" "Gerencia produtos e pedidos"

    ecommerce = softwareSystem "E-commerce" "Plataforma de vendas online" {
      webapp = container "Next.js App" "Frontend React" "TypeScript/Next.js"
      api = container "Order API" "Gestão de pedidos" "Node.js/Express" {
        orderController = component "OrderController" "Endpoints HTTP de pedidos"
        placeOrderUseCase = component "PlaceOrderUseCase" "Regra de negócio de pedido"
        orderRepository = component "OrderRepository" "Acesso ao banco de pedidos"
      }
      db = container "PostgreSQL" "Banco relacional" "PostgreSQL 16" {
        tags "Database"
      }
      queue = container "Kafka" "Broker de eventos" "Apache Kafka" {
        tags "Queue"
      }
    }

    stripe = softwareSystem "Stripe" "Processamento de pagamentos" {
      tags "External"
    }

    user -> webapp "Acessa via browser"
    webapp -> api "API REST" "HTTPS/JSON"
    api -> db "Lê e escreve"
    api -> queue "Publica eventos"
    api -> stripe "Processa pagamento" "HTTPS"
    orderController -> placeOrderUseCase "Invoca"
    placeOrderUseCase -> orderRepository "Persiste"
  }

  views {
    systemContext ecommerce "SystemContext" {
      include *
      autolayout lr
    }

    container ecommerce "Containers" {
      include *
      autolayout lr
    }

    component api "Components" {
      include *
      autolayout lr
    }
  }
}
```

### Diagrama de Sequência Complementar

C4 não cobre fluxos temporais bem. Use sequência para isso:

```
Usuario    Next.js    OrderAPI    PostgreSQL    Stripe    Kafka
  │           │           │            │           │        │
  │─POST /checkout─→      │            │           │        │
  │           │─POST /orders─→         │           │        │
  │           │           │─INSERT─→   │           │        │
  │           │           │←─OK────    │           │        │
  │           │           │─charge()──────────→    │        │
  │           │           │←──payment_id──────     │        │
  │           │           │─publish(order.placed)──────────→│
  │           │←──201──   │            │           │        │
  │←──redirect│           │            │           │        │
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Comunicação | Vocabulário padronizado reduz ambiguidade | Curva inicial para o time aprender os níveis |
| Manutenção | DSL permite versionamento no git | Diagramas manuais ficam desatualizados rápido |
| Granularidade | 4 níveis atendem audiências diferentes | Level 4 (código) raramente vale o esforço |
| Adoção | Simples de aprender, difícil de fazer errado | Estruturizr tem plano pago para colaboração |

## Quando Usar / Quando Evitar

**Usar:**
- Onboarding de novos devs no sistema
- Discussões de arquitetura e ADRs
- Documentação de sistemas legados
- Comunicação com stakeholders não-técnicos (Level 1)

**Evitar:**
- Level 4 (código) — o código é a fonte de verdade
- Diagramas manuais para sistemas que mudam rápido — use DSL

## Relação com HLD e LLD

```
C4 Level 1 + 2  ≈  HLD  (visão macro: sistemas, containers e integrações)
C4 Level 3 + 4  ≈  LLD  (detalhe de implementação: componentes e código)
```

O C4 é a **convenção** para estruturar HLD e LLD com consistência. Sem ele, cada engenheiro desenha num nível diferente e ninguém sabe qual audiência deve consumir aquele artefato.

## Conceitos Relacionados

[[high-level-design]] · [[low-level-design]] · [[adr]] · [[wardley-maps]] · [[rfc]] · [[microsservicos]] · [[bounded-context]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-13*
