---
type: concept
title: "PRD — Product Requirements Document"
aliases: ["PRD", "Product Requirements Document"]
date_created: 2026-05-17
date_updated: 2026-06-02
source_count: 3
tags: [prd, documentação, produto, requisitos, spec-driven, ia]
skill: tech-mentor-system-design
status: stable
---

# PRD — Product Requirements Document

Documento que descreve **o que o produto faz** — funcionalidades, comportamento esperado, personas, casos de uso. Não descreve como o sistema implementa.

Posição na cadeia: BRD → **PRD** → [[trd-technical-requirements-document]] → Implementação.

## PRD no Contexto de IA (Spec Driven Development)

No [[wiki/concepts/spec-driven-development|Spec Driven Development]], o PRD tem uma função diferente do PRD tradicional de produto:

- É gerado pelo [[wiki/concepts/agente-prd|Agente de PRD]] em sessão interativa com o dev
- É **um documento para a IA**, não para a empresa ou stakeholders
- Captura o contexto necessário para que o agente de [[wiki/concepts/tech-spec|Tech Spec]] tome as decisões técnicas corretas
- Não repete padrões de arquitetura que já estão nas [[wiki/concepts/rules-agente|rules]]

> "PRD não é um documento feito para a empresa, é um documento feito para a IA." — [[wiki/entities/pedro-nauke]]

## Key Sources

- [[wiki/sources/trd-technical-requirements-document]]
- [[wiki/sources/formacao-ia-devs-aula-04-agentes-planejamento]]
- [[wiki/sources/formacao-ia-devs-aula-05-qa]]
