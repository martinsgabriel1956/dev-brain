---
type: concept
title: "Fail Fast"
aliases: ["rejeição rápida", "fast failure"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [resiliencia, fail-fast, system-design, latencia]
skill: tech-mentor-system-design
status: stub
---

# Fail Fast

Rejeitar requisições imediatamente quando o sistema está sob pressão — ao invés de enfileirar e falhar após timeout longo.

## Por que Importa

Esperar 30s para falhar é pior que falhar em 1s: o cliente já desistiu, o recurso ficou preso, e o timeout cascateou.

## Com Bulkhead

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
```

Pool cheio → rejeita em 1s com erro explícito, não em 30s com timeout.

## Relação

[[concepts/bulkhead]] usa fail fast para evitar fila infinita. [[concepts/circuit-breaker]] usa fail fast quando o disjuntor está aberto.

## Key Sources

- [[sources/bulkhead]]
