---
date: 2026-03-27
tags: [tech-mentor, system-design, resiliencia, bulkhead, thread-pool, isolamento, concorrencia]
skill: tech-mentor-system-design/references/graceful-degradation.md
level: intermediário
---

# Bulkhead

## Contexto

O nome vem da engenharia naval: navios são divididos em compartimentos estanques. Se um compartimento inundar, os outros permanecem intactos — o navio não afunda inteiro. Em software: isolar os recursos (threads, conexões, semáforos) que cada downstream consome, para que a falha de um não esgote os recursos de todos.

## Como Funciona

### O Problema Sem Bulkhead

```
Pool compartilhado de 100 threads:

Serviço A (normal):   usa 10 threads
Serviço B (lento):    usa 10 → 20 → 50 → 80 → 100 threads
Serviço C (normal):   quer 10 threads → não tem → falha
Serviço D (crítico):  quer 5 threads  → não tem → falha

→ Um serviço lento consumiu tudo — blast radius: 1 derrubou 3
```

### Bulkhead + Circuit Breaker — A Combinação Correta

```
Circuit Breaker → decide SE tenta (abre quando há muitas falhas)
Bulkhead        → decide QUANTOS tentam ao mesmo tempo

Ordem correta: bulkhead envolve circuit breaker
```

## Código de Referência

### Bulkhead de Thread Pool

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

async function processOrder(order: Order) {
  const [payment, inventory] = await Promise.all([
    paymentPool.execute(() => paymentService.charge(order)),
    inventoryPool.execute(() => inventoryService.reserve(order))
  ]);

  // Não-crítica — se o pool estiver cheio, descarta silenciosamente
  notificationPool.execute(() => notificationService.send(order))
    .catch(err => console.log({ message: "Notification skipped", error: err.message }));

  return { payment, inventory };
}
```

### Bulkhead de Connection Pool — DB por Criticidade

```typescript
const oltp = new Pool({
  max: 40,          // reservado para operações transacionais
  min: 5,
  connectionTimeoutMillis: 3_000
});

const reporting = new Pool({
  max: 10,          // relatórios têm cota menor e separada
  min: 1,
  connectionTimeoutMillis: 10_000,
  idleTimeoutMillis: 30_000
});

// OLTP nunca é afetado por relatórios pesados
async function createOrder(data: CreateOrderDTO) {
  return oltp.query("INSERT INTO orders ...", [data]);
}

async function generateReport(filters: ReportFilters) {
  return reporting.query("SELECT ... FROM orders ...", [filters]);
}
```

### Fail Fast quando Pool Está Cheio

```typescript
async function execute<T>(fn: () => Promise<T>, timeoutMs = 1_000): Promise<T> {
  const acquired = await Promise.race([
    this.acquire().then(() => true),
    new Promise<boolean>(resolve => setTimeout(() => resolve(false), timeoutMs))
  ]);

  if (!acquired) {
    throw new Error("Bulkhead queue full — request rejected");
  }

  try {
    return await fn();
  } finally {
    this.release();
  }
}
// Rejeitar em 1s é melhor que esperar 30s para falhar
```

### Dimensionamento — Little's Law

```
Concorrência ideal = Throughput × Latência média

Exemplo:
  Payment service: 50 req/s, latência média 200ms
  Concorrência = 50 × 0.2 = 10 threads
  Com margem de 2×: pool de 20
```

## Trade-offs

| Aspecto | Sem Bulkhead | Com Bulkhead |
|---|---|---|
| **Blast radius** | Um serviço lento afeta todos | Isolado — outros protegidos |
| **Throughput** | Ilimitado até esgotar recursos | Limitado pelo tamanho do pool |
| **Latência sob pressão** | Alta — threads disputam o mesmo pool | Previsível — fila por serviço |
| **Complexidade** | Zero | Pool por downstream + monitoramento |
| **Rejeição explícita** | Nunca | Fail fast quando pool está cheio |

## Quando Usar / Quando Evitar

**Use Bulkhead quando:**
- ✅ Múltiplos downstreams com criticidades diferentes
- ✅ Cargas heterogêneas (OLTP + relatórios no mesmo processo)
- ✅ APIs externas com rate limits

**Não é necessário quando:**
- ❌ Serviço tem apenas um downstream
- ❌ Chamadas completamente assíncronas via fila — a fila já é o bulkhead

**Métricas para monitorar:**
```
bulkhead_pool_active{service}    # calls em andamento
bulkhead_pool_queued{service}    # calls esperando na fila
bulkhead_rejected_total{service} # calls rejeitadas por pool cheio
```
Pool constantemente cheio = downstream lento ou pool subdimensionado.

## Conceitos Relacionados

[[fase-3-resiliencia]] · [[circuit-breaker]] · [[retry-backoff]] · [[graceful-degradation]] · [[rate-limiting]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
