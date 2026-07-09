---
type: concept
title: "PRD — Product Requirements Document"
aliases: ["PRD", "Product Requirements Document"]
date_created: 2026-05-17
date_updated: 2026-07-09
source_count: 4
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

## "Grill Me": Alinhar o Design Concept Antes de Escrever o PRD

[[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] propõe uma etapa anterior à escrita do PRD: uma sessão de entrevista adversarial onde a IA interroga o dev sobre cada aspecto do plano (podendo chegar a 40–100 perguntas) até alcançar um [[wiki/entities/fred-brooks|design concept]] compartilhado. Só depois disso a conversa vira PRD (ou, para mudanças pequenas, issues diretamente). O autor argumenta que isso evita a falha "a IA não fez o que eu queria" — sintoma de um PRD escrito sem que dev e IA tivessem, de fato, a mesma teoria do que estava sendo construído.

## Key Sources

- [[wiki/sources/trd-technical-requirements-document]]
- [[wiki/sources/formacao-ia-devs-aula-04-agentes-planejamento]]
- [[wiki/sources/formacao-ia-devs-aula-05-qa]]
- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
