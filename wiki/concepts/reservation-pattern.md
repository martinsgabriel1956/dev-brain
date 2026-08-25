---
type: concept
title: "Reservation Pattern (Reservations)"
aliases: ["padrão de reserva", "reservations", "reserva temporizada", "TTL reservation", "assento reservado 10 minutos"]
date_created: 2026-08-25
date_updated: 2026-08-25
source_count: 1
tags: [concorrencia, race-condition, ux, redis, ttl, system-design, e-commerce]
skill: tech-mentor-system-design
status: draft
---

# Reservation Pattern (Reservations)

Estratégia de concorrência focada em **experiência do usuário**, não só em correção de dados: move o momento em que um conflito pode acontecer para o mais cedo possível no fluxo — a escolha do recurso —, em vez de deixá-lo estourar só na hora do pagamento.

## O problema que resolve

Tanto [[wiki/concepts/pessimistic-locking]] quanto [[wiki/concepts/optimistic-concurrency-control]] resolvem a race condition em si, mas ambos deixam o conflito estourar tarde: o usuário preenche todos os dados de pagamento, clica em confirmar, e só aí descobre que perdeu o recurso para outra pessoa. Frustração alta, na pior hora possível do fluxo.

## Como funciona

1. Ao clicar/selecionar o recurso (assento, ingresso, item de estoque), o cliente dispara uma reserva com um TTL curto (5, 10 ou 15 minutos) — status passa de "disponível" para "reservado", tipicamente com um timer visível na UI.
2. O usuário tem essa janela para completar o fluxo de pagamento.
3. Se ele finaliza a compra a tempo, status vira "comprado" (ação definitiva). Se o tempo expira sem finalizar, o recurso volta a "disponível" automaticamente.

O conflito, quando acontece, acontece no passo 1 — resolvido com feedback instantâneo ("esse já foi, escolha outro") — não depois de o usuário já ter investido tempo preenchendo cartão de crédito.

## Duas formas de implementar a expiração

### Cron job (mais simples, tem um bug de atraso)

Job periódico varre reservas expiradas e reverte o status. Problema: se o job roda a cada N minutos e a reserva expira logo depois de uma execução, ela só é revertida na próxima rodada — na prática dura até ~2×N minutos em vez de N. Reduzir o intervalo ajuda, mas custa mais disputa de recurso com o banco em alta escala. Aceitável para entrevista júnior/pleno; um entrevistador sênior tende a cobrar a alternativa abaixo.

### `SET NX EX` no Redis (expiração nativa, sem atraso)

```
SET show:{showId}:seat:{seatId} {userId} NX EX 600
```

- `NX` ("not exists") — atomic check-and-set: só grava se a chave ainda não existir. Elimina a race condition entre checar e setar.
- `EX 600` — expira nativamente em 600s, sem cron job e sem o atraso estrutural do polling.

O banco de dados passa a controlar só dois estados (disponível/ocupado); o Redis controla o terceiro estado transitório (reservado), via a presença/ausência da chave. Para listar recursos disponíveis, o servidor cruza o estado do banco com as chaves ativas no Redis — operação leve porque o conjunto de recursos reserváveis de uma vez (assentos de um show, por exemplo) nunca é gigantesco.

Esse é o mesmo primitivo `SET NX EX` documentado em [[wiki/concepts/distributed-lock]] a partir do caso Uber — mas aplicado a um problema diferente: ali é exclusão mútua entre motoristas candidatos concorrentes; aqui é reserva temporizada de UX. Ferramenta igual, propósito diferente.

## E se o Redis cair?

Fallback de duas camadas: o lock via Redis cobre o caminho feliz; se o Redis cai e volta depois de uma janela curta (ex.: ~60s para subir nova instância), aplica-se [[wiki/concepts/pessimistic-locking]] (`FOR UPDATE`) no banco como segunda camada de garantia só durante essa janela excepcional — garante que, mesmo sem o Redis, apenas uma pessoa complete a compra. A UX piora nesse intervalo raro, mas o trade-off costuma ser aceitável (validar com o time de produto).

> **Gap não coberto pela fonte** [skill: tech-mentor-system-design]: o cenário acima trata só "Redis totalmente indisponível". Há um risco relacionado mas distinto — clock skew ou pausa de processo (GC, swap) pode fazer um lock expirar antes do processo terminar de usá-lo, mesmo com o Redis no ar. A mitigação padrão para esse caso é **fencing token**, não coberta nesta fonte.

## Quando preferir reservations

Fluxos com interação direta do usuário e recurso limitado/disputado: compra de ingresso, e-commerce com estoque escasso, passagem aérea. Para conflitos puramente de back-end/automação sem usuário esperando na tela, [[wiki/concepts/pessimistic-locking]] ou [[wiki/concepts/optimistic-concurrency-control]] seguem sendo a escolha mais direta — reservations adiciona complexidade (cron job ou Redis como componente extra) que só se paga quando a experiência do usuário está em jogo.

## Key Sources

- [[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]] — introdução completa do padrão, comparação cron job vs. Redis `SET NX EX`, e o fallback de duas camadas para queda do Redis
