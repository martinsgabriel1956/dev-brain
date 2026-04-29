---
type: concept
title: "Saga Pattern"
aliases: ["saga", "saga distribuída", "compensating transactions"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
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

## Trade-off

Consistência eventual — não ACID. Compensações podem falhar também (saga idempotente é obrigatória). Mais complexo que uma transação local, mas escala horizontalmente.

## Key Sources

- [[sources/3pc]]
