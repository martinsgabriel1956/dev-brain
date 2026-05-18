---
type: source
title: "Request for Comments (RFC)"
aliases: ["RFC", "Request for Comments"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_file: /home/nemomartins/Documentos/new/dev-study/raw/request-for-comments.md
source_url: ""
author: "tech-mentor-system-design"
date_published: 2026-05-17
date_ingested: 2026-05-17
tags: [system-design, decisoes-tecnicas, colaboracao, rfc]
skill: tech-mentor-system-design
status: stable
---

# Request for Comments (RFC)

## TL;DR

RFC é o mecanismo para propor mudanças grandes demais para decidir em silêncio — breaking changes, migrações de infra, novos padrões que afetam múltiplos times. O objetivo não é convencer: é coletar objeções, alternativas e contexto que o autor não tem. RFC aceito sempre gera um ADR.

## Key Claims

- **Proposta, não decisão:** RFC documenta o que ainda não foi decidido; ADR registra o que já foi. [[wiki/concepts/rfc-request-for-comments]]
- **Fluxo:** Draft → Comment Period (ex: 1 semana) → Accepted / Rejected / Withdrawn
- **RFC aceito → ADR obrigatório:** o ADR registra a decisão final com contexto histórico. [[wiki/concepts/adr-architecture-decision-record]]
- **Estrutura:** Problema → Proposta → Alternativas Consideradas → Impacto → Perguntas em Aberto → Prazo → Autor
- **Alternativas descartadas são parte do valor:** evitam re-debate de opções já avaliadas
- **Quando NÃO usar:** você já sabe a resposta (RFC vira teatro), mudança local e reversível, urgência não permite revisão, time < 4 pessoas que fala todo dia

## Concepts

- [[wiki/concepts/rfc-request-for-comments]]
- [[wiki/concepts/adr-architecture-decision-record]]
- [[wiki/concepts/trd-technical-requirements-document]]

## Open Questions

- Como criar cultura de RFC sem torná-lo burocracia em times que precisam de velocidade?

## Raw Quotes

> "O objetivo não é convencer — é coletar objeções, alternativas e contexto que o autor não tem."

> "RFC e ADR são complementares, não substitutos: RFC (proposta + debate) → decisão tomada → ADR (registro permanente)."
