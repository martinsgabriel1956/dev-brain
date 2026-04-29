---
type: concept
title: "Distributed Lock"
aliases: ["lock distribuído", "redis set nx", "distributed locking"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, redis, concorrencia, distributed-systems, race-condition]
skill: tech-mentor-system-design
status: stable
---

# Distributed Lock

Mecanismo para garantir exclusão mútua entre processos distribuídos — evita que dois processos atuem sobre o mesmo recurso simultaneamente.

## Redis SET NX

```
Redis SET lock:driver:42 {ride_id} NX EX 15
  NX = só seta se não existir (atomic)
  EX 15 = expira em 15s (timeout do motorista)

Se lock adquirido → oferecer corrida ao motorista
Se lock existe   → driver:42 já está sendo ofertado → pular, tentar próximo

Motorista aceita → lock permanece até corrida finalizar
Motorista rejeita/timeout → DEL lock:driver:42 → libera para outros pedidos
```

## Por que SET NX é Atômico

`SET key value NX EX ttl` é uma operação atômica no Redis — check-and-set sem race condition entre o check e o set.

## Problema que Resolve no Uber

Dois passageiros solicitam ao mesmo tempo. Ambos recebem `driver:42` como candidato. Sem lock, `driver:42` aceita ambas as corridas — conflito. Com lock, apenas o primeiro adquire — o segundo pula para o próximo candidato.

## TTL é Obrigatório

Lock sem TTL = deadlock se o processo que adquiriu cair antes de liberar. TTL garante que o lock expire automaticamente.

## Alternativa: Redlock

Para lock com múltiplas instâncias Redis (sem ponto único de falha). Mais complexo — use apenas se a perda do lock por falha de nó único for inaceitável. **Não implementa fencing tokens** — ver [[concepts/fencing-token]].

## Problema do Lock Fantasma

Processo lento ressuscita após TTL expirar e acredita ainda ter o lock. Solução: [[concepts/fencing-token]] — token monotônico rejeitado pelo storage protegido.

## Relacionado

[[concepts/split-brain]] — Redlock tenta resolver, mas tem controvérsia (Martin Kleppmann vs antirez).
[[concepts/fencing-token]] — complemento obrigatório para locks em recursos críticos.
[[concepts/skip-locked]] — alternativa para filas de trabalho sem broker externo.

## Key Sources

- [[sources/case-uber]]
- [[sources/skip-locked-fencing-token]]
