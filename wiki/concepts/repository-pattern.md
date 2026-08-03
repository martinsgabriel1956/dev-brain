---
type: concept
title: "Repository Pattern"
aliases: ["padrão repositório", "repository"]
date_created: 2026-05-01
date_updated: 2026-08-03
source_count: 4
tags: [design-patterns, data-access, repository, infrastructure]
skill: tech-mentor-backend
status: stub
---

## Definição

Camada de abstração entre a lógica de negócio e o acesso a dados. O repositório encapsula queries, retornando entidades de domínio — o restante do código não sabe se os dados vêm de banco, API ou outro storage.

## Data Mapper vs Active Record

- **Data Mapper:** entidades separadas dos repositórios (ex: Prisma, Doctrine) — padrão usado no exemplo do [[proxy-pattern]]
- **Active Record:** entidade conhece como persistir a si mesma (ex: Laravel Eloquent, Rails ActiveRecord)

Na prática de um repositório Data Mapper, a conversão campo-a-campo entre entidade de domínio e formato do ORM é isolada num [[wiki/concepts/mapper-pattern]] dedicado (ex: `PrismaNotificationMapper.toPrisma()`) — evita repetir a lógica de conversão em cada método do repositório.

## No Fluxo da Clean Architecture: Data Access Interface + Data Mapper

[[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] descreve esse mesmo padrão dentro do fluxo de [[wiki/concepts/clean-architecture]]: o Use Case acessa dados através de uma **Data Access interface** (inversão de dependência — o Use Case não conhece o banco concreto), e um **Data Mapper** transfere os dados brutos do banco (estrutura de dados pura) para dentro das Entities (objetos com comportamento). Ver [[wiki/concepts/objeto-vs-estrutura-de-dados]] para por que essa transferência nunca é um "mapeamento" simétrico — os dois lados representam coisas fundamentalmente diferentes.

## Concorrência: Unit of Work como alternativa mais robusta

[[wiki/sources/arquitetura-limpa-na-pratica]] reconhece uma limitação comum de repositórios simples (uma interface por agregado, sem transações): conflitos de concorrência (ex: editar a mesma nota em dois dispositivos) não são tratados. Alternativas citadas: deixar operações do repositório ou do caso de uso atômicas, ou usar o padrão **Unit of Work** (Fowler, *PoEAA*) em conjunto com o Repository — mantém uma lista de objetos afetados por uma transação, coordenando escritas e resolvendo conflitos ao final da requisição.

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[wiki/sources/mappers-conversao-entre-camadas]]
- [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] — Data Access interface + Data Mapper no fluxo completo da Clean Architecture
- [[wiki/sources/arquitetura-limpa-na-pratica]] — exemplo de repositório MongoDB (schemaless), crítica a ORMs que anotam entidades de domínio, e Unit of Work como alternativa para concorrência
