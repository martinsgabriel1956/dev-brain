---
type: concept
title: "Cache-Aside (Lazy Loading)"
aliases: ["lazy loading cache", "cache aside", "flyweight cache"]
date_created: 2026-06-26
date_updated: 2026-08-10
source_count: 2
tags: [cache, cache-aside, redis, padroes-arquiteturais, backend]
skill: tech-mentor-backend
status: stable
---

# Cache-Aside (Lazy Loading)

## TL;DR

Padrão onde a aplicação primeiro tenta o [[cache]]; em miss vai ao banco, salva o resultado no cache com TTL e retorna. O cache é populado sob demanda — nunca antecipadamente.

## Fluxo

```
Request → Cache hit? → retorna imediatamente
               ↓ miss
           Banco de Dados → salva no Cache (TTL) → retorna
```

## Analogia com Flyweight

A fonte chama esse padrão de **Flyweight aplicado ao cache**: construir objetos em memória de forma lazy e reutilizá-los enquanto o TTL for válido. Ao expirar, o ciclo recomeça.

## Código (TypeScript)

```typescript
async function getProduct(id: string): Promise<Product> {
  const cached = await redis.get(`product:${id}`)
  if (cached) return JSON.parse(cached)

  const product = await db.products.findById(id)
  await redis.setex(`product:${id}`, 3600, JSON.stringify(product))  // TTL: 1h
  return product
}
```

## TTL — Definindo a Longevidade

O TTL deve refletir a volatilidade do dado:

| Dado | TTL sugerido |
|---|---|
| Catálogo de produto | 7 dias |
| Perfil de usuário | 1h |
| Feature flags | 1h a 1 dia |
| Taxa de câmbio | 60s |

## Problema: Cache Stampede

Quando o TTL expira e muitos requests chegam simultaneamente — todos vão ao banco ao mesmo tempo (thundering herd). Solução: distribuited lock com [[redis]] (SET NX) ou probabilistic early expiration.

## Comparação com Outros Padrões

- **Cache-Aside** — aplicação controla explicitamente; miss implica leitura do banco
- **Write-Through** — banco e cache atualizados simultaneamente; sem stale mas latência de escrita maior
- **Write-Behind** — cache aceita escrita, banco é atualizado assincronamente; alto risco de perda

## Key Sources

- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
- [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]] — descreve o fluxo cache-aside como "o padrão mais comum": miss → banco → grava no cache → devolve; hits seguintes vão direto ao cache
