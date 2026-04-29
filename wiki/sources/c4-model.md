---
type: source
title: "C4 Model"
aliases: ["c4 model", "c4", "structurizr", "context diagram", "container diagram", "component diagram", "system design documentation"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/c4-model.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [c4-model, structurizr, architecture-documentation, system-context, container, component, diagrams-as-code]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

C4 Model (Simon Brown): 4 níveis de abstração para documentar arquitetura. L1 System Context (quem usa, que sistemas externos). L2 Container (apps, DBs, mensageria). L3 Component (internos de um container). L4 Code (classes — raramente vale). Structurizr DSL para diagrams-as-code versionado. Complementado por diagramas de sequência para fluxos dinâmicos.

## Key Claims

**Claim:** C4 resolve o problema de "um diagrama para todos" — cada nível tem audiência e propósito diferentes.
**Evidence:** L1 (System Context): para CTO, produto, stakeholders — sem detalhes técnicos. L2 (Container): para arquitetos e devs — tecnologias, comunicação. L3 (Component): para devs da equipe — internos de um serviço. L4 (Code): UML de classes — geralmente gerado, raramente mantido manualmente.
**Confidence:** alta

**Claim:** Structurizr DSL é diagrams-as-code — versionado em git, renderizado automaticamente, sem drag-and-drop.
**Evidence:** DSL define workspaces, sistemas, containers, relacionamentos em texto. Structurizr CLI gera imagens ou site interativo. Diferente de draw.io/Miro: o diagrama está no repositório, é atualizado no PR, não desatualiza. Suporte a múltiplas views (context, container, component, deployment) a partir de um único modelo.
**Confidence:** alta

**Claim:** C4 e diagramas de sequência são complementares — C4 para estrutura estática, sequência para fluxos dinâmicos.
**Evidence:** C4 mostra "o que existe e como está conectado". Sequência mostra "o que acontece quando o usuário faz X". Para uma feature crítica, o C4 L2 mostra os containers envolvidos; o diagrama de sequência mostra a ordem das chamadas, timeouts, retries.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/c4-model]]
- [[entities/structurizr]]
- [[concepts/architecture-documentation]]
- [[concepts/diagrams-as-code]]
- [[concepts/adr]]

## Open Questions

- C4 Model para microserviços com 50+ serviços — como manter L2 legível sem poluição visual?
- Structurizr self-hosted vs cloud — vale a complexidade operacional para equipes pequenas?
