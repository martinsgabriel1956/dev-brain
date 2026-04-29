---
type: source
title: "Contract Testing"
aliases: ["pact", "consumer-driven contracts", "teste de contrato"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/nemomartins/Documentos/new/dev-study/raw/contract-testing.md
source_url: ""
author: "tech-mentor-testing skill"
date_published: 2026-03-27
date_ingested: 2026-04-22
source_count: 0
tags: [testes, contract-testing, pact, microservices, consumer-driven, ci]
skill: tech-mentor-testing
status: stable
---

# Contract Testing

## TL;DR

Valida que dois serviços concordam com o formato da comunicação — sem precisar rodá-los juntos. Consumer-Driven: o consumer define o que precisa, o provider verifica. `can-i-deploy` é o gate que impede deploy se algum consumer for quebrado. Não substitui E2E — são camadas diferentes.

## Claims Principais

| Claim | Confiança |
|---|---|
| Consumer-Driven inverte o fluxo tradicional — consumer define o contrato | Alta |
| can-i-deploy impede provider de fazer deploy se quebrar consumer | Alta |
| Não detecta bugs de lógica de negócio — só quebras de contrato de interface | Alta |
| Em monólito não faz sentido — requer serviços separados | Alta |

## Conceitos Abordados

- [[contract-testing]] · [[piramide-de-testes]] · [[bdd]] · [[living-documentation]]
