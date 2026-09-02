---
type: concept
title: "User Stories"
aliases: ["User Story", "Histórias de Usuário", "US"]
date_created: 2026-05-17
date_updated: 2026-09-01
source_count: 3
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

## Estimativa em Sprint

Uma vez pronta (ver Definition of Ready), uma user story é estimada pelo time — tipicamente em [[wiki/concepts/story-points]] via [[wiki/concepts/planning-poker]] — antes de entrar no sprint. O [[wiki/concepts/scrum-master]] facilita esse processo, mas não deveria decidir a meta de pontos por conta própria: a estimativa precisa emergir da conversa do time sobre complexidade, não ser imposta de cima para baixo.

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

## Engineering Stories: o Requisito Que o Usuário Não Vê

[[wiki/sources/escopo-de-projetos-processo-nao-resultado-lorehub]] propõe um formato complementar para requisitos não-funcionais/internos, no mesmo molde da user story mas do ponto de vista do dev:

```
Como dev, eu quero [prática/qualidade interna] [porque/para benefício técnico].
```

Exemplos dados: "como dev, eu quero testes unitários", "como dev, eu quero evitar código duplicado". A justificativa é que o usuário final nunca vai avaliar a qualidade do código diretamente — só a experiência observável —, então requisitos de qualidade interna (testes, ausência de duplicação, arquitetura) precisam de um mecanismo próprio de registro no checklist do projeto, senão ficam de fora por padrão. Ver [[wiki/concepts/checklist-primeiro-dia-projeto]] para onde essas duas categorias de story se encontram na prática (checklist `.md` da v1 de um projeto).

Nota de terminologia: "engineering story" não é termo padronizado na literatura ágil consultada nesta wiki (Scrum/XP não a definem formalmente) — tratado aqui como vocabulário próprio popularizado pela fonte, funcionalmente equivalente a uma **task técnica** (ver seção "Quando Usar / Evitar" abaixo) escrita no formato canônico de user story.

## Quando Usar / Evitar

**Usar:** times ágeis com PO presente, ciclos curtos, features com impacto direto na experiência do usuário.

**Evitar como substituto:** sistemas regulados (rastreabilidade), integrações críticas com SLA → complementar com [[frd-functional-requirements-document]], features puramente de infra sem impacto UX direto (usar tasks técnicas).

## Key Sources

- [[wiki/sources/user-stories]]
- [[wiki/sources/story-points-po-forcando-30-40-pontos-por-sprint]]
- [[wiki/sources/escopo-de-projetos-processo-nao-resultado-lorehub]] — uso solo (fora de time ágil formal) para escopar projetos pessoais, e o complemento "engineering stories" para requisitos invisíveis ao usuário

## Conceitos Relacionados

[[prd-product-requirements-document]] · [[frd-functional-requirements-document]] · [[trd-technical-requirements-document]]
