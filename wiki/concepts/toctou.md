---
type: concept
title: "TOCTOU (Time of Check to Time of Use)"
aliases: ["toctou", "time of check time of use", "race condition financeira", "double spend"]
date_created: 2026-07-04
date_updated: 2026-07-04
source_count: 1
tags: [toctou, race-condition, concorrencia, appsec, transactions]
skill: tech-mentor-security
status: stable
---

# TOCTOU (Time of Check to Time of Use)

Classe de vulnerabilidade de concorrência causada pelo intervalo de tempo entre **verificar** uma condição (o *check*) e **agir** com base nela (o *use*). Se duas requisições concorrentes passam pelo check antes de qualquer uma delas completar o use, ambas veem o estado "antigo" como válido e o efeito acontece em duplicidade.

Distinto da [[wiki/concepts/race-condition]] de frontend (fetch fora de ordem sobrescrevendo estado em React) — TOCTOU é uma condição de corrida sobre um **recurso compartilhado no backend/banco de dados**, não sobre ordem de respostas de rede no cliente.

## O exemplo clássico: saque duplicado

```
Saldo: R$ 100
Requisição A: verifica saldo (R$ 100 ✓) → processa saque de R$ 100
Requisição B: verifica saldo (R$ 100 ✓, A ainda não terminou) → processa saque de R$ 100

Resultado: dois saques de R$ 100 com apenas R$ 100 de saldo
```

Na prática não é preciso mandar exatamente duas requisições simultâneas — o delay natural de rede já faz múltiplas chegarem quase ao mesmo tempo, todas passando pelo check antes que qualquer use seja concluído.

Aplica-se a qualquer recurso finito e compartilhado: saldo de conta, estoque de um produto, like/voto único, ticket disponível.

## Correção

O check e o use precisam acontecer como uma operação **atômica** — ou os dois acontecem completos, sem interrupção, ou nenhum acontece.

- **Transactions no banco** (a solução mais comum) — `SELECT ... FOR UPDATE` + update dentro da mesma transaction, travando a linha até o commit.
- Semáforos ou locks distribuídos (ex: Redis lock) quando o recurso é compartilhado entre múltiplos serviços, não só múltiplas conexões ao mesmo banco.
- Filas — serializar as operações sobre o mesmo recurso em vez de processá-las em paralelo.

## Ver também

- [[wiki/concepts/idempotencia]] — resolve um problema adjacente (reprocessar o mesmo evento), mas não substitui a atomicidade do check+use
- [[wiki/concepts/race-condition]] — TOCTOU é a variante backend/concorrência da mesma família de bugs

## Key Sources

- [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]]
