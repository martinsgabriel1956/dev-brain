---
type: concept
title: "Event Handler (Consumer que Projeta o Read Model)"
aliases: ["event handler", "consumer de eventos", "projetor"]
date_created: 2026-09-30
date_updated: 2026-11-16
source_count: 2
tags: [cqrs, eventos, mensageria, consumer, projecao]
skill: tech-mentor-backend
status: stub
---

# Event Handler

## TL;DR

Componente que recebe um evento ("formulário cadastrado"), **transforma** o dado e o persiste no [[wiki/concepts/read-model]] no formato final. Na descrição da fonte roda como **consumer assíncrono**, separado da aplicação de escrita, lendo mensagens de filas do broker ([[wiki/entities/rabbitmq]]).

## Pontos da fonte

- A aplicação de escrita só grava e publica o evento; não atualiza ativamente a base de leitura.
- O consumer pode ser **escalado independentemente** se o volume de eventos crescer.
- Introduz um pequeno delay: [[wiki/concepts/eventual-consistency]].
- Fonte: [[wiki/sources/cqrs-desbalanco-leitura-escrita-banco-de-leitura-eventos]].

## Cuidados não cobertos pela fonte [skill]

Entrega *at-least-once* exige handler **idempotente** ([[wiki/concepts/idempotencia]], [[wiki/concepts/garantia-de-entrega]]); a publicação do evento após o commit sofre do [[wiki/concepts/dual-write-problem]] (mitigado por [[wiki/concepts/outbox-pattern]]); ordenação e mensagens venenosas pedem chave de partição e DLQ. Ver [[wiki/concepts/filas-e-workers]] e [[wiki/concepts/event-driven-architecture]].

## Na NLW #2, dia 3 (Diego Fernandes)

`onClick={addNewScheduleItem}` (referência, não chamada), `onChange={e => ...}`, `onSubmit` com `FormEvent` tipado à mão e `e.preventDefault()` para não recarregar a página. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## Key sources

- [[wiki/sources/cqrs-desbalanco-leitura-escrita-banco-de-leitura-eventos]] — event handler/consumer que transforma e grava no banco de leitura
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: onSubmit, FormEvent e preventDefault
