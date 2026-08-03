---
type: concept
title: "Saga Pattern"
aliases: ["saga", "saga distribuída", "compensating transactions"]
date_created: 2026-04-22
date_updated: 2026-08-03
source_count: 4
tags: [sistemas-distribuidos, consistencia, saga, microsservicos, compensação]
skill: tech-mentor-system-design
status: stub
---

# Saga Pattern

Padrão para transações distribuídas sem locks distribuídos — usa consistência eventual com transações de compensação.

## Problema que Resolve

[[concepts/two-phase-commit]] requer locks distribuídos. Em microsserviços, isso é impraticável — serviços são independentes, não compartilham banco.

## Mecanismo

Sequência de transações locais. Se uma falha, as anteriores são **compensadas** (revertidas via operação inversa).

```
T1 (Pagamento) → T2 (Reserva) → T3 (Envio)
         ↓ falha em T3
C2 (Cancela Reserva) → C1 (Estorna Pagamento)
```

## Dois Estilos

- **Coreografado** — cada serviço publica evento e reage a eventos de outros. Sem orquestrador central.
- **Orquestrado** — orquestrador central comanda cada passo. Mais visível, mais acoplado.

Essa escolha (coreografia vs. orquestração) é citada em [[wiki/sources/ciclo-de-mudanca-de-arquitetura]] como um exemplo de decisão de TO-BE que precisa ser validada por POC antes da migração — ver [[wiki/concepts/ciclo-de-mudanca-de-arquitetura]].

## Implementação com Fila (RabbitMQ) — Versão Didática

Uma explicação simplificada apresenta o Saga coreografado como: cada serviço (order, payments, shipping, inventory...) publica na fila (ex.: [[wiki/entities/rabbitmq]]), que garante ordem e evita gargalo de coordenação síncrona — em contraste direto com o [[wiki/concepts/two-phase-commit|two-phase commit]], que trava esperando aprovação sequencial. O trade-off citado: a fila resolve o problema de gargalo, mas cada serviço precisa implementar manualmente sua própria compensação/rollback caso uma etapa falhe — isso é descrito como a parte "muito difícil" de implementar Saga na prática. Essa arquitetura de fila é chamada de [[wiki/concepts/event-driven-architecture]]. Ver [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]].

## Trade-off

Consistência eventual — não ACID. Compensações podem falhar também (saga idempotente é obrigatória). Mais complexo que uma transação local, mas escala horizontalmente.

## Key Sources

- [[sources/3pc]]
- [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]] — saga pattern/consistência eventual citado como conceito que ajuda a lidar com cenários de concorrência e integração mesmo num único banco de dados, fora de arquitetura distribuída
- [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]] — versão didática coreografada via RabbitMQ, contrastada com o gargalo de coordenação do 2PC
- [[wiki/sources/ciclo-de-mudanca-de-arquitetura]] — coreografia vs. orquestração como exemplo de decisão de TO-BE a validar via POC
