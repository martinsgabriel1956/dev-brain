---
type: concept
title: "Outbox Pattern"
aliases: ["transactional outbox", "outbox + cdc", "outbox"]
date_created: 2026-04-22
date_updated: 2026-08-03
source_count: 3
tags: [sistemas-distribuidos, mensageria, outbox, cdc, consistencia, idempotencia, inbox]
skill: tech-mentor-system-design
status: stub
---

# Outbox Pattern

Garante entrega de mensagens/eventos sem [[concepts/two-phase-commit]] — usando uma tabela `outbox` no mesmo banco da transação.

## Mecanismo

```
1. Transação local: escreve no banco + escreve evento na tabela outbox
2. CDC (Debezium) lê o outbox e publica no broker (Kafka, etc.)
3. Broker entrega ao consumidor
```

Atomicidade garantida pela transação local — não precisa de lock distribuído.

## Por que Funciona

Escrever no banco principal e na tabela outbox é uma única transação ACID. O CDC é assíncrono — se falhar, retenta. Garante **at-least-once delivery**.

## Trade-off

Latência adicional (CDC é assíncrono). Consumidor deve ser idempotente (mensagem pode ser entregue mais de uma vez).

## Alternativa ao 2PC

[[concepts/two-phase-commit]] garante entrega síncrona com risco de blocking. Outbox garante entrega assíncrona com risco de duplicação — trade-off de latência vs complexidade.

## Cruzando a Fronteira de Serviço com Identidade Idempotente

Outbox resolve a publicação confiável de um lado da fronteira. Do outro lado, quem consome precisa do complementar — [[wiki/concepts/inbox-pattern]] — para não duplicar o efeito quando o mesmo evento chega mais de uma vez (at-least-once delivery). Em pagamentos, isso é o que permite que a mesma chave de [[wiki/concepts/idempotencia]] atravesse o processo que caiu no meio do caminho: se o processador externo já aprovou a cobrança mas o backend caiu antes de salvar a resposta local, repassar a chave idempotente ao retry (ou reconciliar contra uma referência estável) evita criar uma segunda cobrança.

## Key Sources

- [[sources/3pc]]
- [[wiki/sources/outbox-pattern]]
- [[wiki/sources/idempotencia-pagamentos-retry-sistemas-distribuidos]] — Outbox/Inbox como o par que mantém a identidade da operação atravessando fronteiras de serviço sob entrega at-least-once
- [[wiki/sources/ciclo-de-mudanca-de-arquitetura]] — citado como exemplo de decisão de TO-BE (Transaction Outbox) que exige o ciclo AS-IS/POC/migração, ver [[wiki/concepts/ciclo-de-mudanca-de-arquitetura]]
