---
type: concept
title: "Dimensões de Decisão Arquitetural"
aliases: ["decisão estrutural vs design de código"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [arquitetura, decisao-arquitetural, design]
skill: tech-mentor-system-design
status: stub
---

# Dimensões de Decisão Arquitetural

[[wiki/sources/introducao-arquitetura-de-software-conceitos-decisoes-kiper-academy]] separa duas dimensões de decisão dentro de uma aplicação (depois de fixar o [[wiki/concepts/application-boundary]]):

- **Estrutural:** fronteira de execução e formato de deploy. Microsserviço ou não, event-driven, serverless, e a topologia de infraestrutura (serviço, front, API Gateway, banco, réplicas). Ver [[wiki/concepts/microsservicos]], [[wiki/concepts/event-driven-architecture]], [[wiki/concepts/api-gateway]].
- **Design do código:** fronteiras de responsabilidade e dependência *dentro* do código. [[wiki/concepts/clean-architecture]], [[wiki/concepts/hexagonal-architecture]], Onion, MVC.

As dimensões se combinam (ex.: quebrar o MVC em partes pode virar decisão estrutural).

**Exemplo (pagamentos):** *estrutural* = cobrança como serviço de deploy independente, falando com pedidos por mensagens; *design* = a regra de cobrança depende de uma interface de pagamento e o adapter de cada provedor a implementa ([[wiki/concepts/ports-adapters]], [[wiki/concepts/adapter-pattern]]), então a cobrança não depende do provedor externo. Ver [[wiki/concepts/arquitetura-de-software]].

## Key sources

- [[wiki/sources/introducao-arquitetura-de-software-conceitos-decisoes-kiper-academy]]
