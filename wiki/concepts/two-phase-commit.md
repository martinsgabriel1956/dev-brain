---
type: concept
title: "Two-Phase Commit (2PC)"
aliases: ["2pc", "two phase commit", "protocolo de duas fases", "xa transactions"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 2
tags: [sistemas-distribuidos, consistencia, transacoes, 2pc, xa]
skill: tech-mentor-system-design
status: stable
---

# Two-Phase Commit (2PC)

Protocolo de consenso distribuído para garantir atomicidade em transações que envolvem múltiplos participantes. Um coordinator centraliza a decisão: ou todos commitam, ou nenhum commita.

## As Duas Fases

**Fase 1 — Prepare (Voting)**

Coordinator envia PREPARE para todos os participantes. Cada participant adquire locks, persiste dados no log de recuperação, e responde PREPARED (sim) ou ABORT (não). Se qualquer participant responder ABORT, o coordinator encerra com ABORT global.

**Fase 2 — Commit ou Abort**

Se todos PREPARED → coordinator envia COMMIT para todos. Se qualquer ABORT → coordinator envia ABORT para todos, liberando locks.

## Problema Crítico: Blocking

Se o coordinator cai **após enviar PREPARE mas antes de enviar COMMIT**, os participants ficam bloqueados indefinidamente:
- Não podem commitar — não receberam instrução
- Não podem abortar — podem contradizer decisão já tomada pelo coordinator
- Não podem liberar locks — recursos travados para outros usuários

Resultado: indisponibilidade garantida até o coordinator se recuperar ou intervenção manual (timeout + rollback).

Esse é exatamente o problema que [[concepts/three-phase-commit]] tenta resolver — sem sucesso em redes com partição.

## XA Transactions — 2PC no PostgreSQL

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
PREPARE TRANSACTION 'transfer-txn-abc123';

-- Se o outro banco também preparou:
COMMIT PREPARED 'transfer-txn-abc123';

-- Se algo falhou:
ROLLBACK PREPARED 'transfer-txn-abc123';

-- Ver transações "penduradas":
SELECT * FROM pg_prepared_xacts;
```

## Quando Usar

- Dentro de um único banco com múltiplos schemas (XA intra-banco)
- Sistemas bancários legados que toleram blocking em troca de ACID
- Participantes todos controlados e com capacidade de reinício coordenado

## Quando Evitar

- Entre microsserviços: latência de rede torna o lock period longo demais e participantes externos podem não implementar XA
- Viola autonomia de deploy — todos os serviços precisam ser compatíveis simultaneamente
- Um participante lento ou falho bloqueia a transação inteira

## Alternativas

- [[concepts/saga-pattern]] — consistência eventual com compensação explícita, sem coordinator
- [[concepts/outbox-pattern]] — tabela outbox + CDC para entrega garantida sem lock distribuído
- [[concepts/raft-paxos]] — consenso distribuído com quorum (CockroachDB usa 2PC + Raft internamente)

## Key Sources

- [[sources/3pc]]
- [[sources/two-phase-commit]]
