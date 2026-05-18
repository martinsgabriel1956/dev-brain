---
date: 2026-05-17
tags: [tech-mentor, system-design, arquitetura, hld]
skill: tech-mentor-system-design/references/hld-lld-c4
level: intermediário
---

# High Level Design (HLD)

## Contexto
HLD é a primeira camada de documentação arquitetural de um sistema. Responde à pergunta **"o que o sistema faz e como os grandes blocos se conectam?"** antes de qualquer linha de código ser escrita. É o artefato que alinha engenheiros, PMs e stakeholders técnicos sobre a direção do sistema.

Sem HLD, times constroem em paralelo com premissas diferentes — e o custo de realinhamento depois que o código existe é muito maior.

## Como Funciona

HLD opera no nível de **serviços, integrações e fluxo de dados**. Não entra em detalhe de implementação.

O que um HLD deve responder:
- Quais são os componentes principais (APIs, bancos, filas, CDNs, serviços externos)?
- Como eles se comunicam (REST, gRPC, eventos, WebSocket)?
- Quais tecnologias foram escolhidas por camada e por quê?
- Quais são as decisões arquiteturais centrais (monolito vs. microserviços, sync vs. async, stateless vs. stateful)?
- Onde estão os pontos de falha e como são mitigados?

### Exemplo — Sistema de E-commerce

```
[Browser / Mobile App]
        ↓ HTTPS
[API Gateway / Load Balancer]
        ↓
  ┌─────┴──────┐
  ↓            ↓
[Auth Service] [Order Service] → [PostgreSQL]
                    ↓
                 [Kafka]
                    ↓
         [Notification Service] → [Resend (Email)]
                                → [FCM (Push)]
```

Neste diagrama:
- Não importa como o `Order Service` implementa a criação de pedido
- Importa que ele persiste em Postgres e publica evento no Kafka
- A escolha de Kafka (vs. RabbitMQ, SQS) seria justificada no documento

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Feito cedo | Alinha o time antes de escrever código | Pode ser prematuro se os requisitos ainda mudam |
| Nível de abstração alto | Acessível para não-engenheiros | Pode esconder complexidades que importam |
| Tecnologias definidas no HLD | Reduz retrabalho de integração | Pode amarrar decisões antes de ter contexto suficiente |
| Diagrama de blocos simples | Fácil de criar e atualizar | Perde nuance de protocolos e contratos |

## Quando Usar / Quando Evitar

**Usar quando:**
- Iniciando um projeto ou feature de porte médio/grande
- Há múltiplos times ou serviços envolvidos
- Precisar aprovar a direção técnica antes de investir em implementação
- Onboarding de novos engenheiros no sistema

**Evitar (ou simplificar) quando:**
- Feature pequena e isolada dentro de um serviço já existente
- Protótipo ou spike de validação — o HLD virá depois, se validar
- Time de uma pessoa com contexto total do sistema

## Conceitos Relacionados
[[low-level-design]] · [[c4-model]] · [[adr]] · [[system-design-entrevista]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-05-17*
