---
type: source
title: "FinTech System Design — Ledger, Idempotência Financeira e Antifraude"
aliases: ["ledger dupla entrada", "double entry bookkeeping", "antifraude", "idempotencia financeira"]
date_created: 2026-04-23
date_updated: 2026-07-27
source_count: 0
tags: [fintech, ledger, double-entry, idempotencia-financeira, antifraude, conciliacao, system-design]
skill: tech-mentor-system-design
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/fintech-system-design.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# FinTech System Design — Ledger, Idempotência Financeira e Antifraude

## TL;DR

Sistemas financeiros têm três pilares: Ledger de dupla entrada (débito = crédito, imutável), Idempotência financeira (mesma operação N vezes = mesmo resultado), e Antifraude em camadas (rules engine + ML + revisão manual). Toda operação financeira deve ter idempotency key. Ledger é append-only: nunca update ou delete em transações.

## Key Claims

| Claim | Evidência |
|---|---|
| Ledger usa dupla entrada: cada transação gera duas entradas (débito e crédito) | Double Entry Bookkeeping — padrão contábil desde século XV |
| Idempotency key + Redis lock evita cobrança duplicada em retry | Padrão Stripe, Adyen, PayPal |
| Antifraude em camadas: rules engine síncrono (< 50ms) → ML assíncrono → revisão manual | Rules engine bloqueia; ML enriquece o score |
| Conciliação financeira compara ledger interno com extrato da adquirente/banco | Discrepâncias detectadas via diff diário/horário |
| Ledger deve ser append-only — soft delete, nunca UPDATE em transações | Audit trail obrigatório para regulatórias |

## Conceitos

- [[concepts/ledger-dupla-entrada]] — double entry bookkeeping
- [[concepts/idempotencia]] — pré-requisito para operações financeiras seguras
- [[concepts/antifraude]] — arquitetura em camadas
- [[concepts/conciliacao-financeira]] — comparação ledger vs extrato externo
- [[concepts/distributed-lock]] — lock por idempotency key para evitar race condition
- [[wiki/sources/idempotencia-pagamentos-retry-sistemas-distribuidos]] — detalha o mecanismo que esta fonte assume como dado ("idempotency key + Redis lock"): corrida resolvida por INSERT atômico, lançamento e status confirmando na mesma transação local, e identidades de negócio específicas por produto (saque ID, emissão ID, crédito ID, client order ID)

## Key Sources

_Este é o documento primário._
