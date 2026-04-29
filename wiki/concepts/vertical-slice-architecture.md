---
type: concept
title: "Vertical Slice Architecture"
aliases: ["vertical slice", "feature-first architecture", "slice por feature"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [arquitetura, modularidade, feature-first, agentes, tokens]
skill: tech-mentor-backend
status: stub
---

# Vertical Slice Architecture

Organização de código por *feature* (corte vertical), não por *camada* (corte horizontal). Cada feature contém tudo que precisa: handler, lógica de negócio, acesso a dados.

## Contraste com Clean Architecture Horizontal

**Horizontal (Clean Architecture):**
```
domain/
  user.entity.ts
application/
  create-user.usecase.ts
infrastructure/
  user.repository.ts
presentation/
  user.controller.ts
```
Uma feature toca 4+ arquivos em 4 pastas diferentes.

**Vertical Slice:**
```
features/
  create-user/
    handler.ts        # HTTP + validação
    logic.ts          # regra de negócio
    repository.ts     # acesso a dados
```
Uma feature = uma pasta, 2–3 arquivos.

## Por Que Importa com IA

O Navigation Paradox (ver [[concepts/navigation-paradox]]) mostra que arquitetura horizontal obriga o agente a abrir 7–13 arquivos para uma feature que em Vertical Slice seria 1–3. Cada arquivo a mais é token a mais e chance de perder uma dependência.

Vertical Slice não resolve tudo — shared code (auth, logging, DB client) ainda precisa de uma camada compartilhada. Mas o core de cada feature fica contido.

## Quando Usar

- Times que querem feature independence: um dev trabalha em `create-user/` sem tocar em `list-users/`
- Codebases onde o agente de IA é parte ativa do fluxo de desenvolvimento
- Projetos que precisam de clareza rápida do que pertence a cada feature

## Limitação

Sem discipline, Vertical Slice pode levar a duplicação de lógica entre features. A solução é extrair para `shared/` *depois* do segundo caso — ver [[concepts/yagni]].

## Key Sources

- [[sources/clean-architecture-ia-custo-real]]
