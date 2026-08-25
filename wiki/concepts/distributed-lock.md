---
type: concept
title: "Distributed Lock"
aliases: ["lock distribuído", "redis set nx", "distributed locking"]
date_created: 2026-04-22
date_updated: 2026-08-25
source_count: 5
tags: [system-design, redis, mysql, concorrencia, distributed-systems, race-condition]
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

## Exemplo Negativo: Reserva sem Lock Atômico (Cinema)

[[wiki/sources/system-design-entrevista-cinema-draw-io]] mostra o que acontece na ausência deste padrão. O sistema reserva um assento gravando `seatmapId`+`seatId` no Redis com TTL de 15 minutos, mas **não** faz um check-and-reserve atômico contra a API externa de seatmap antes de expor o assento como disponível — o `GET assentos` responde só com o estado "físico" do seatmap, ignorando reservas internas em andamento. Resultado: o frontend mostra um assento como disponível, o usuário escolhe, e só ao chegar no web server o sistema consulta o Redis e descobre que já foi reservado por outra pessoa. É o mesmo tipo de conflito do caso Uber (dois clientes competindo pelo mesmo recurso), mas sem o `SET NX` atômico que resolveria — o próprio autor da fonte reconhece isso como um erro do desenho, não como decisão consciente de trade-off. Bom contraponto didático ao caso Uber acima: mostra o custo concreto de pular a etapa de lock.

## Contraponto Positivo: Reserva com Lock Atômico (Ingressos)

[[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]] mostra a versão correta do padrão que falha no exemplo negativo acima: `SET show:{showId}:seat:{seatId} {userId} NX EX 600` reserva o assento de forma atomicamente check-and-set — `NX` garante que só quem chega primeiro consegue setar a chave, sem a janela de inconsistência entre "ler disponibilidade" e "gravar reserva" que o exemplo do cinema (draw.io) deixa aberta. Essa fonte usa o mesmo `SET NX EX` do caso Uber acima, mas para um propósito diferente: não é exclusão mútua entre workers/motoristas candidatos, é uma **reserva temporizada de UX** — ver [[wiki/concepts/reservation-pattern]] para o padrão completo (incluindo a alternativa mais simples e com bug estrutural de cron job).

### Fallback de duas camadas se o Redis cair

A mesma fonte cobre o edge case "e se o Redis cair": lock via Redis no caminho feliz + [[wiki/concepts/pessimistic-locking]] (`FOR UPDATE`) no banco como segunda camada de garantia só durante a janela em que o Redis está indisponível (ex.: ~60s para subir nova instância) — garante que mesmo nesse intervalo excepcional só uma pessoa complete a compra. Isso é distinto do problema de fencing token acima: aqui o Redis está **totalmente fora do ar**, não é o caso de um processo lento ressuscitando com um lock expirado enquanto o Redis segue de pé — a fonte não cobre esse segundo cenário, que continua exigindo [[concepts/fencing-token]].

## Relacionado

[[concepts/split-brain]] — Redlock tenta resolver, mas tem controvérsia (Martin Kleppmann vs antirez).
[[concepts/fencing-token]] — complemento obrigatório para locks em recursos críticos.
[[concepts/skip-locked]] — alternativa para filas de trabalho sem broker externo.
[[wiki/concepts/tuple-space]] / [[wiki/concepts/object-space]] — mesma garantia de exclusão mútua, obtida por remoção atômica (take) de uma tupla/objeto do espaço compartilhado em vez de uma primitiva de lock explícita.

## Key Sources

- [[sources/case-uber]]
- [[sources/skip-locked-fencing-token]]
- [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]] — reserva de estoque via linhas físicas + [[concepts/skip-locked]] no MySQL, sem lock explícito de aplicação
- [[wiki/sources/system-design-entrevista-cinema-draw-io]] — exemplo negativo: reserva de assento via Redis TTL sem check-and-reserve atômico contra a fonte de disponibilidade, gerando leitura inconsistente entre API externa e estado interno de reserva
- [[wiki/sources/tuple-space-wikipedia]] — modelo alternativo de exclusão mútua embutida (tuple space/Object Space): a remoção atômica da tupla/objeto do espaço já é o lock, sem primitiva separada
- [[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]] — contraponto positivo ao exemplo do cinema: reserva de ingresso via `SET NX EX` com check-and-set atômico de fato, mais fallback de duas camadas (Redis + lock pessimista no banco) para quando o Redis cai
