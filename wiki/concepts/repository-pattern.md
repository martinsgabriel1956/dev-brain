---
type: concept
title: "Repository Pattern"
aliases: ["padrão repositório", "repository"]
date_created: 2026-05-01
date_updated: 2026-05-01
source_count: 1
tags: [design-patterns, data-access, repository, infrastructure]
skill: tech-mentor-backend
status: stub
---

## Definição

Camada de abstração entre a lógica de negócio e o acesso a dados. O repositório encapsula queries, retornando entidades de domínio — o restante do código não sabe se os dados vêm de banco, API ou outro storage.

## Data Mapper vs Active Record

- **Data Mapper:** entidades separadas dos repositórios (ex: Prisma, Doctrine) — padrão usado no exemplo do [[proxy-pattern]]
- **Active Record:** entidade conhece como persistir a si mesma (ex: Laravel Eloquent, Rails ActiveRecord)

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
