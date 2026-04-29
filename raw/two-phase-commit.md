---
date: 2026-04-14
tags: [tech-mentor, distributed-systems, transações, consistência, coordenação]
skill: tech-mentor-system-design/references/distributed-systems
level: avançado
---

# 2PC — Two-Phase Commit

## Contexto

2PC é o protocolo clássico para garantir atomicidade em transações distribuídas: ou todos os participantes commitam, ou nenhum commita. É o protocolo que bancos de dados usam para transações que envolvem múltiplos recursos (XA transactions).

Em microsserviços, 2PC é frequentemente citado como "o que não usar" — e a alternativa é Saga. Mas entender por que 2PC falha é essencial para projetar bem sistemas distribuídos.

## Como Funciona

### Fase 1 — Prepare (Voting)

O Coordinator pergunta a todos os participantes se eles conseguem commitar.

```
Coordinator → Participant A: "Pode commitar?"
Coordinator → Participant B: "Pode commitar?"
Coordinator → Participant C: "Pode commitar?"

Participant A: adquire locks, persiste dados em log → responde "Sim (PREPARED)"
Participant B: adquire locks, persiste dados em log → responde "Sim (PREPARED)"
Participant C: detecta violação de constraint         → responde "Não (ABORT)"
```

### Fase 2 — Commit ou Abort

Se todos responderam "Sim": Coordinator envia COMMIT. Se qualquer um respondeu "Não": Coordinator envia ABORT para todos.

```
Caso feliz (todos PREPARED):
  Coordinator → A: COMMIT
  Coordinator → B: COMMIT
  Coordinator → C: COMMIT

Caso de falha (C abortou):
  Coordinator → A: ABORT (libera locks)
  Coordinator → B: ABORT (libera locks)
  Coordinator → C: ABORT
```

### O Problema — Coordinator Crash

O ponto fraco do 2PC: se o Coordinator crasha após enviar PREPARE mas antes de enviar COMMIT, os participantes ficam **bloqueados indefinidamente** — segurando locks, esperando uma decisão que nunca vem.

```
Coordinator enviou PREPARE para A, B, C
A, B, C responderam PREPARED (segurando locks)
Coordinator crasha ← PONTO DE FALHA

A, B, C estão bloqueados:
  - Não podem commitar (não receberam COMMIT)
  - Não podem abortar (poderiam contradizer uma decisão do coordinator antes do crash)
  - Não podem liberar locks (recursos travados para outros usuários)

Solução: timeout + rollback manual, ou aguardar o coordinator se recuperar
→ Período de indisponibilidade garantido
```

### 3PC — A Tentativa de Solução

3PC adiciona uma fase intermediária (PRE-COMMIT) que permite a participantes decidirem autonomamente se o coordinator cai. Na prática, raramente usado — adiciona complexidade sem eliminar completamente o bloqueio em caso de partição de rede.

```
Fase 1: PREPARE (igual ao 2PC)
Fase 2: PRE-COMMIT (coordinator confirma que todos votaram SIM)
         → participants sabem que podem commitar se coordinator sumir
Fase 3: COMMIT
```

### XA Transactions — 2PC no Banco

Alguns bancos suportam 2PC via interface XA (eXtended Architecture). O PostgreSQL suporta `PREPARE TRANSACTION`:

```sql
-- Coordinator cria a transação preparada
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
PREPARE TRANSACTION 'transfer-txn-abc123';

-- Se o outro banco também preparou:
COMMIT PREPARED 'transfer-txn-abc123';

-- Se algo falhou:
ROLLBACK PREPARED 'transfer-txn-abc123';

-- Ver transações preparadas (que podem estar "penduradas"):
SELECT * FROM pg_prepared_xacts;
```

### 2PC vs. Saga

| Aspecto | 2PC | Saga |
|---|---|---|
| **Consistência** | Strong consistency (ACID) | Eventual consistency |
| **Disponibilidade** | Bloqueante — participante falho para tudo | Non-blocking — compensação assíncrona |
| **Performance** | Lento — múltiplos round trips, locks mantidos | Rápido — transações locais independentes |
| **Complexidade** | Simples de implementar, difícil de operar | Mais código (compensação), mais robusto |
| **Rollback** | Automático e atômico | Manual — lógica de compensação explícita |
| **Uso moderno** | Dentro de um único banco (XA), não entre serviços | Entre microsserviços |

## Quando Usar / Quando Evitar

**2PC ainda faz sentido em:**
- Transações dentro de um único banco com múltiplos schemas/bancos no mesmo servidor
- Sistemas que toleram bloqueio temporário em troca de garantia ACID (sistemas bancários legados)
- Quando você controla todos os participantes e podem reiniciar coordenadamente

**Evitar 2PC entre microsserviços porque:**
- Participantes de outros times podem não implementar XA
- Latência de rede torna o protocolo lento e o período de lock longo demais
- Um participante lento ou falho bloqueia a transação inteira
- Viola a autonomia de deploy — todos os serviços precisam estar compatíveis simultaneamente

**A alternativa é Saga + Outbox Pattern:** cada serviço faz sua transação local, publica um evento, e a lógica de compensação (rollback) é responsabilidade de quem falhou — sem coordinator centralizado.

## Conceitos Relacionados

[[saga-pattern]] · [[outbox-pattern]] · [[distributed-locks]] · [[cap-pacelc-consistencia]] · [[raft-leader-election]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-14*
