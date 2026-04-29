---
type: source
title: "2PC — Two-Phase Commit"
aliases: ["two-phase-commit", "2pc", "xa transactions"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 0
tags: [sistemas-distribuidos, consistencia, transacoes, 2pc, xa, saga, outbox]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-study/raw/two-phase-commit.md
source_url: ""
author: ""
date_published: 2026-04-14
date_ingested: 2026-04-22
---

# 2PC — Two-Phase Commit

## TL;DR

2PC garante atomicidade em transações distribuídas via um coordinator central. Funciona bem dentro de um único banco (XA). Entre microsserviços, o problema de blocking do coordinator torna Saga + Outbox a alternativa correta.

## Key Claims

**Claim:** 2PC opera em duas fases — Prepare (voting) e Commit/Abort — onde o coordinator centraliza a decisão.
**Evidence:** Fase 1: coordinator solicita PREPARED de todos os participantes, que bloqueiam recursos. Fase 2: se todos PREPARED → COMMIT para todos; se qualquer ABORT → ABORT para todos.
**Confidence:** alta

**Claim:** O ponto fraco fatal é o coordinator crash entre PREPARE e COMMIT — participants ficam bloqueados indefinidamente segurando locks.
**Evidence:** Participants pós-PREPARED não podem commitar (sem instrução), não podem abortar (podem contradizer decisão já tomada), não podem liberar locks. Resultado: indisponibilidade garantida até coordinator recuperar.
**Confidence:** alta

**Claim:** 3PC tenta resolver o blocking adicionando fase PRE-COMMIT, mas falha em redes com partição.
**Evidence:** PRE-COMMIT sinaliza que todos votaram SIM, permitindo participants decidirem autonomamente se coordinator cai. Na prática: adiciona complexidade, não elimina blocking em split-brain. Uso quase exclusivamente acadêmico.
**Confidence:** alta

**Claim:** PostgreSQL suporta 2PC via `PREPARE TRANSACTION` / `COMMIT PREPARED` / `ROLLBACK PREPARED`.
**Evidence:** SQL direto: `PREPARE TRANSACTION 'transfer-txn-abc123'` → `COMMIT PREPARED 'transfer-txn-abc123'`. Transações penduradas visíveis em `pg_prepared_xacts`.
**Confidence:** alta

**Claim:** A alternativa moderna é Saga + Outbox: transações locais independentes, sem coordinator centralizado, compensação explícita.
**Evidence:** Cada serviço faz transação local + publica evento. Rollback = lógica de compensação do serviço que falhou. Não requer XA nem coordinator.
**Confidence:** alta

## Comparativo 2PC vs Saga

| Aspecto | 2PC | Saga |
|---|---|---|
| Consistência | Strong (ACID) | Eventual |
| Disponibilidade | Bloqueante | Non-blocking |
| Performance | Lento (round trips + locks) | Rápido (transações locais) |
| Rollback | Automático e atômico | Manual (compensação) |
| Uso moderno | Dentro de um banco (XA) | Entre microsserviços |

## Quando Usar 2PC

- Transações dentro de um único banco com múltiplos schemas/bancos no mesmo servidor
- Sistemas bancários legados que toleram blocking em troca de ACID
- Quando todos os participantes são controlados e reiniciam coordenadamente

## Quando Evitar 2PC

- Entre microsserviços: participantes de outros times podem não implementar XA
- Latência de rede torna lock period longo demais
- Um participante lento bloqueia a transação inteira
- Viola autonomia de deploy — todos os serviços precisam ser compatíveis simultaneamente

## Concepts & Entities Touched

[[concepts/two-phase-commit]] · [[concepts/three-phase-commit]] · [[concepts/saga-pattern]] · [[concepts/outbox-pattern]] · [[concepts/distributed-transactions]] · [[concepts/distributed-lock]] · [[concepts/acid]]

## Open Questions

- Em quais bancos relacionais modernos (CockroachDB, Spanner) 2PC ainda é usado internamente?
- Saga orquestrado vs coreografado — quando cada um?
- Transações XA em Java (JTA) ainda são viáveis em stacks modernas?
