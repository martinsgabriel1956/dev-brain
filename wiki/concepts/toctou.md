---
type: concept
title: "TOCTOU (Time of Check to Time of Use)"
aliases: ["toctou", "time of check time of use", "race condition financeira", "double spend"]
date_created: 2026-07-04
date_updated: 2026-08-25
source_count: 2
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

[[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]] documenta a mesma mecânica exata (sem usar o termo TOCTOU) com dois exemplos didáticos: duas pessoas comprando a mesma cadeira de cinema (falso positivo de "disponível" no check) e estoque de e-commerce sobrescrito (segunda escrita ignora o resultado da primeira porque leu o valor antigo em memória).

## Correção

O check e o use precisam acontecer como uma operação **atômica** — ou os dois acontecem completos, sem interrupção, ou nenhum acontece. Três estratégias com tradeoffs diferentes, detalhadas em [[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]]:

- **[[wiki/concepts/pessimistic-locking]]** — `SELECT ... FOR UPDATE` + update dentro da mesma transaction, travando a linha até o commit. Serializa acesso; usar sob alta contenção ou quando o custo de um conflito é alto.
- **[[wiki/concepts/optimistic-concurrency-control]]** — não trava nada; detecta o conflito no `UPDATE` via condição no `WHERE` (contador ou coluna `version`). Usar quando conflitos são raros — degrada sob alta contenção (retries em cascata).
- **[[wiki/concepts/reservation-pattern]]** — quando há um usuário esperando na tela, mover o momento do conflito para antes do pagamento (reserva com TTL via Redis `SET NX EX`, por exemplo), em vez de deixar o usuário só descobrir o conflito depois de preencher os dados de pagamento.
- Semáforos ou locks distribuídos (ex: Redis lock) quando o recurso é compartilhado entre múltiplos serviços, não só múltiplas conexões ao mesmo banco — ver [[wiki/concepts/distributed-lock]].
- Filas — serializar as operações sobre o mesmo recurso em vez de processá-las em paralelo.

## Ver também

- [[wiki/concepts/idempotencia]] — resolve um problema adjacente (reprocessar o mesmo evento), mas não substitui a atomicidade do check+use
- [[wiki/concepts/race-condition]] — TOCTOU é a variante backend/concorrência da mesma família de bugs

## Key Sources

- [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]]
- [[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]] — exemplos de cadeira de cinema/estoque de e-commerce + três estratégias de correção (pessimistic locking, OCC, reservations)
