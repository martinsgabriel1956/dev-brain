---
type: concept
title: "User Stories"
aliases: ["User Story", "Histórias de Usuário", "US"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 1
tags: [produto, requisitos, agile, bdd]
skill: tech-mentor-leadership
status: stable
---

# User Stories

**TL;DR:** Unidade mínima de valor entregável em contextos ágeis. Formato canônico força o time a pensar em valor antes de solução. Derivada do PRD, complementar ao FRD.

## Formato Canônico

```
Como [persona], quero [ação] para [benefício].
```

## Critérios de Aceitação — Given/When/Then

```
Dado que [contexto/pré-condição],
Quando [ação do usuário ou evento],
Então [resultado esperado e verificável].
```

## Definition of Ready (antes do sprint)

- Persona clara e conhecida
- Critérios de aceitação escritos
- Estimada pela equipe
- Dependências mapeadas
- Sem ambiguidade suficiente para bloquear desenvolvimento

## Definition of Done

- Código revisado e mergeado
- Testes automatizados escritos e passando
- Critérios validados (QA ou PO)
- Documentação atualizada se necessário

## Quando Usar / Evitar

**Usar:** times ágeis com PO presente, ciclos curtos, features com impacto direto na experiência do usuário.

**Evitar como substituto:** sistemas regulados (rastreabilidade), integrações críticas com SLA → complementar com [[frd-functional-requirements-document]], features puramente de infra sem impacto UX direto (usar tasks técnicas).

## Key Sources

- [[wiki/sources/user-stories]]

## Conceitos Relacionados

[[prd-product-requirements-document]] · [[frd-functional-requirements-document]] · [[trd-technical-requirements-document]]
