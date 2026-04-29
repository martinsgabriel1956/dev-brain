---
date: 2026-03-27
tags: [tech-mentor, system-design, resiliencia, graceful-degradation, fallback, fail-closed, fail-open]
skill: tech-mentor-system-design/references/graceful-degradation.md
level: intermediário
---

# Graceful Degradation

## Contexto

Resiliência completa não é só evitar falhas — é definir o que o sistema entrega quando parte dele está indisponível. Graceful Degradation é a estratégia de degradar funcionalidade de forma controlada em vez de falhar completamente. O usuário perde personalização — mas não perde a capacidade de usar o sistema.

## Como Funciona

### A Hierarquia de Fallbacks

```
1. Dado fresco do serviço           → ideal
       ↓ falha
2. Cache stale (dado desatualizado)  → aceitável
       ↓ sem cache
3. Resposta degradada (genérica)     → funcional, sem personalização
       ↓ impossível responder
4. Feature desabilitada              → página funciona sem aquela feature
       ↓ nem isso é possível
5. Página de manutenção              → último recurso — transparente ao usuário
```

### Fail-Closed vs Fail-Open

| Contexto | Comportamento | Motivo |
|---|---|---|
| Auth / permissões | Fail-closed (nega) | Segurança acima de disponibilidade |
| Pagamento | Fail-closed (nega) | Não processar cobrança com dado incerto |
| Recomendações | Fail-open (genérico) | UX degradada é melhor que vazio |
| Feature flags | Fail-open (permite) | Melhor ativar do que perder a feature |
| Rate limiting | Fail-open (permite) | Falso positivo é pior que ausência |

## Código de Referência

### Fallback 1 — Cache Stale

```typescript
async function getProductPrice(productId: string): Promise<Price> {
  const CACHE_KEY = `price:${productId}`;

  try {
    const fresh = await pricingService.getPrice(productId);
    await redis.set(CACHE_KEY, JSON.stringify(fresh), "EX", 300);
    return fresh;
  } catch (err) {
    console.log({ message: "Pricing service unavailable, trying stale cache", productId });

    const stale = await redis.get(CACHE_KEY);
    if (stale) {
      return { ...JSON.parse(stale), isStale: true };
    }

    throw new PricingUnavailableError(productId);
  }
}
```

### Fallback 2 — Resposta Degradada

```typescript
async function getRecommendations(userId: string): Promise<Product[]> {
  try {
    return await recommendationEngine.getPersonalized(userId);
  } catch (err) {
    console.log({ message: "Recommendation engine down, falling back to bestsellers" });
    try {
      return await catalogService.getBestsellers({ limit: 10 });
    } catch {
      return []; // seção some em vez de quebrar
    }
  }
}
```

### Fallback 3 — Feature Disable

```typescript
async function checkout(order: Order) {
  const installmentsEnabled = await featureFlags.isEnabled("installments");

  if (installmentsEnabled) {
    try {
      return await checkoutWithInstallments(order);
    } catch (err) {
      console.log({ message: "Installments failed, downgrading to simple checkout" });
    }
  }

  return await simpleCheckout(order); // sempre funciona
}
```

### Fail-Closed vs Fail-Open

```typescript
// FAIL-CLOSED — nega por padrão (auth, pagamentos)
async function getUserPermissions(userId: string): Promise<Permission[]> {
  try {
    return await authService.getPermissions(userId);
  } catch (err) {
    console.log({ message: "Auth service unavailable, denying access (fail-closed)" });
    return [];
  }
}

// FAIL-OPEN — permite por padrão (features não-críticas)
async function isFeatureEnabled(featureId: string, userId: string): Promise<boolean> {
  try {
    return await featureFlagService.check(featureId, userId);
  } catch (err) {
    console.log({ message: "Feature flag service unavailable, defaulting to enabled" });
    return true;
  }
}
```

### Padrão Completo — Promise.allSettled

```typescript
async function getProductPage(productId: string, userId: string) {
  const [product, price, recommendations] = await Promise.allSettled([
    productService.get(productId),
    getProductPrice(productId),
    getRecommendations(userId)
  ]);

  // Produto é obrigatório — sem ele, 404
  if (product.status === "rejected") {
    throw new ProductNotFoundError(productId);
  }

  return {
    product: product.value,
    price: price.status === "fulfilled"
      ? price.value
      : { amount: null, message: "Preço temporariamente indisponível" },
    recommendations: recommendations.status === "fulfilled"
      ? recommendations.value
      : []
  };
}
// Promise.allSettled: falha de um não cancela os outros
```

## Trade-offs

| Aspecto | Falha Total | Degradação Graceful |
|---|---|---|
| **Disponibilidade** | Cai com qualquer dependência | Mantém core funcional |
| **Consistência** | Sempre fresco ou nada | Pode servir dado desatualizado |
| **Complexidade** | Zero — erro propaga | Alta — cada feature tem fallback |
| **UX** | Erro genérico | Funcionalidade reduzida, mas funcional |
| **Debug** | Fácil — falha é óbvia | Difícil — degradação pode ser silenciosa |

## Quando Usar / Quando Evitar

**Implemente degradação para:**
- ✅ Features não-críticas (recomendações, personalização, anúncios)
- ✅ Serviços externos que você não controla (CEP, frete, câmbio)
- ✅ Funcionalidades que têm fallback razoável (genérico, cache, default)

**Não aplique degradação quando:**
- ❌ O dado é crítico e não tem substituto aceitável (saldo, inventário crítico)
- ❌ A degradação esconde um bug que deveria ser corrigido
- ❌ O fallback cria inconsistência de negócio (aprovar pedido sem verificar estoque)

## Conceitos Relacionados

[[fase-3-resiliencia]] · [[circuit-breaker]] · [[retry-backoff]] · [[bulkhead]] · [[cache]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
