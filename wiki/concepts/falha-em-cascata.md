---
type: concept
title: "Falha em Cascata"
aliases: ["cascading failure", "cascade failure", "falha cascata", "propagação de falha"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [resiliencia, system-design, falha, distribuído]
skill: tech-mentor-system-design
status: stable
---

# Falha em Cascata

Fenômeno onde a falha ou lentidão de um serviço se propaga para serviços dependentes, derrubando componentes que estavam saudáveis.

## Mecanismo

```
Payment Service (lento, timeout 30s)
        ↑ chamado por
Order Service
  ├── Thread 1: esperando Payment... (30s)
  ├── Thread 2: esperando Payment... (30s)
  │   ... 200 threads acumuladas ...
  └── Thread pool esgotada → Order rejeita novos requests
        ↑ chamado por
Checkout Service → chama Order (sem threads disponíveis) → Checkout cai

→ Payment estava lento. Order e Checkout caíram por consequência.
```

**A causa real não é a falha em si — é o serviço saudável ficar preso esperando o degradado, consumindo recursos até esgotá-los.**

## Condições que favorecem a cascata

- Timeouts longos (30s) → threads ficam presas muito tempo
- Thread pools grandes sem limites por downstream
- Sem fallback — chamador não tem resposta alternativa
- Retry sem backoff → amplifica o problema no downstream já sobrecarregado

## Padrões que previnem

| Padrão | Como previne |
|---|---|
| [[concepts/circuit-breaker]] | Rejeita imediatamente no OPEN — não acumula threads |
| [[concepts/bulkhead]] | Limita threads por downstream — esgotamento de um não afeta outros |
| [[concepts/retry-backoff]] | Backoff exponencial reduz pressão sobre downstream degradado |
| [[concepts/timeout]] | Timeout curto libera thread rapidamente |
| [[concepts/graceful-degradation]] | Fallback serve resposta degradada em vez de travar |

## Ver também

- [[concepts/circuit-breaker]] — solução principal para falha em cascata
- [[concepts/bulkhead]] — isolamento de pools por downstream

## Key Sources

- [[sources/circuit-breaker]]
