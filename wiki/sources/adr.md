---
type: source
title: "ADR — Architecture Decision Record"
aliases: ["adr", "architecture decision record", "decision log"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/adr.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [adr, architecture-decision, decision-record, living-documentation, rfc]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

ADR é um documento curto que registra uma decisão arquitetural significativa: contexto, opções consideradas, decisão tomada, consequências. Vive no repositório (`docs/architecture/decisions/`), é imutável após aceito (decisões passadas não se reescrevem), e acumula como rastreabilidade histórica de "por que chegamos aqui".

## Key Claims

**Claim:** ADR captura o "porquê" da decisão — o que o código não consegue expressar.
**Evidence:** O código mostra o que foi feito. O ADR registra as alternativas consideradas, as restrições do contexto na época, e os trade-offs aceitos. Sem isso, o próximo dev que encontrar a decisão não entende por que não foi feito "o óbvio".
**Confidence:** alta

**Claim:** ADRs são imutáveis — decisões passadas não se reescrevem, são superseded.
**Evidence:** Status "Superseded by ADR-0042" mantém o histórico intacto. Rever um ADR antigo = criar um novo que o substitui. Isso preserva o raciocínio histórico e evita revisionism.
**Confidence:** alta

**Claim:** O que é "significativo" para um ADR: mudança de tecnologia core, padrão arquitetural novo, decisão com consequências difíceis de reverter.
**Evidence:** Trocar de Express para Fastify no projeto inteiro = ADR. Adicionar um endpoint = não é ADR. Adotar Event Sourcing = ADR. Refatorar um componente = não é ADR. Critério: se a decisão vai ser questionada em 6 meses, documente.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/adr]]
- [[concepts/living-documentation]]
- [[concepts/evolutionary-architecture]]
- [[concepts/rfc]]

## Open Questions

- Como evitar que ADRs virem documentação morta ignorada pelo time?
- Qual o processo de aprovação de ADR em times distribuídos sem reuniões síncronas?
