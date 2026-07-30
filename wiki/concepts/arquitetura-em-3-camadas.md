---
type: concept
title: "Arquitetura em 3 Camadas (3-Tier)"
aliases: ["3-tier architecture", "layered architecture", "arquitetura em camadas"]
date_created: 2026-07-30
date_updated: 2026-07-30
source_count: 1
tags: [3-tier, arquitetura-em-camadas, business-layer, data-access-layer, presentation-layer]
skill: tech-mentor-backend
status: stub
---

# Arquitetura em 3 Camadas (3-Tier)

Padrão arquitetural tradicional dividido em três camadas com dependência linear e unidirecional:

```
Presentation Layer → Business Layer → Data Access Layer
```

- **Presentation layer**: interação com o mundo externo (controllers REST, resolvers GraphQL, gRPC, SPA).
- **Business layer**: lógica e regras de negócio.
- **Data access layer**: acesso a dados, tipicamente com dependência direta e explícita da business layer sobre ela (ex.: referência de projeto/pacote).

## Problema estrutural

Como a business layer depende diretamente da data access layer, e a presentation layer depende da business layer, a dependência de acesso a dados se torna **transitiva** — ao longo do tempo, lógica de acesso a dados tende a vazar tanto para dentro da business layer quanto até para a presentation layer, misturando responsabilidades.

## Contraste com Clean Architecture

Diferente da [[wiki/concepts/clean-architecture]], onde todas as dependências apontam para dentro, em direção ao domínio (que não conhece nada de infraestrutura), na 3-tier a cadeia de dependências aponta "para baixo", em direção ao banco de dados — nenhuma camada interna define interface para a externa implementar; o acoplamento é direto.

## Key Sources

- [[wiki/sources/clean-architecture-arquitetura-centrada-no-dominio]] — comparação direta entre os dois diagramas, usada para explicar por que Clean Architecture é chamada de "domain-centric"
