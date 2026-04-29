---
type: concept
title: "Bulkhead"
aliases: ["bulkhead pattern", "thread pool isolation", "isolamento de recursos"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [resiliencia, bulkhead, thread-pool, isolamento, system-design]
skill: tech-mentor-system-design
status: stable
---

# Bulkhead

Padrão de resiliência que isola recursos (threads, conexões, semáforos) por downstream. Falha de um serviço não esgota recursos dos outros.

## Analogia

Navios têm compartimentos estanques. Um inunda — o navio não afunda. Em software: pools separados por serviço.

## Implementação — Thread Pool

```typescript
class BoundedPool {
  private active = 0;
  private queue: Array<() => void> = [];

  constructor(private readonly maxConcurrent: number) {}

  async execute<T>(fn: () => Promise<T>): Promise<T> {
    await this.acquire();
    try {
      return await fn();
    } finally {
      this.release();
    }
  }

  private acquire(): Promise<void> {
    if (this.active < this.maxConcurrent) {
      this.active++;
      return Promise.resolve();
    }
    return new Promise(resolve => this.queue.push(resolve));
  }

  private release(): void {
    const next = this.queue.shift();
    if (next) {
      next();
    } else {
      this.active--;
    }
  }
}

// Pool separado por downstream — isolamento completo
const paymentPool      = new BoundedPool(20);
const inventoryPool    = new BoundedPool(10);
const notificationPool = new BoundedPool(5);
```

## Implementação — Connection Pool por Criticidade

```typescript
const oltp = new Pool({ max: 40, connectionTimeoutMillis: 3_000 });
const reporting = new Pool({ max: 10, connectionTimeoutMillis: 10_000 });
// OLTP nunca é afetado por relatórios pesados
```

## Dimensionamento

Via [[concepts/littles-law]]: `concorrência = throughput × latência_média`. Aplique margem de 2×.

## Quando Usar

- ✅ Múltiplos downstreams com criticidades diferentes
- ✅ Cargas heterogêneas (OLTP + relatórios no mesmo processo)
- ✅ APIs externas com rate limits
- ❌ Serviço com único downstream
- ❌ Chamadas via fila — a fila já é o bulkhead

## Relação com Circuit Breaker

[[concepts/circuit-breaker]] decide **SE** tenta. Bulkhead decide **QUANTOS** tentam ao mesmo tempo. Ordem correta: bulkhead envolve circuit breaker.

## Métricas

```
bulkhead_pool_active{service}    # calls em andamento
bulkhead_pool_queued{service}    # calls esperando
bulkhead_rejected_total{service} # calls rejeitadas
```

Pool constantemente cheio = downstream lento ou pool subdimensionado.

## Key Sources

- [[sources/bulkhead]]
