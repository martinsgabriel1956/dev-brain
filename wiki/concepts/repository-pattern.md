---
type: concept
title: "Repository Pattern"
aliases: ["padrão repositório", "repository"]
date_created: 2026-05-01
date_updated: 2026-07-10
source_count: 2
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

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[wiki/sources/mappers-conversao-entre-camadas]]
