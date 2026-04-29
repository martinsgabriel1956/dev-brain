---
date: 2026-03-27
tags: [tech-mentor, system-design, deploy, feature-flags, rollout, kill-switch, ab-testing]
skill: tech-mentor-system-design/references/zero-downtime-deployments.md
level: intermediário
---

# Feature Flags

## Contexto

Feature flags separam deploy (código vai para produção) de release (feature é ativada para usuários). Essa separação permite iteração rápida com risco controlado: código mergeado diariamente na main, feature desligada até estar pronta, e kill switch instantâneo sem rollback quando algo dá errado.

## Como Funciona

### Os Quatro Tipos de Toggle

```
Release Toggle    → liga feature nova gradualmente para usuários
Ops Toggle        → kill switch para funcionalidade problemática
Experiment Toggle → A/B testing
Permission Toggle → features por plano/tier/role
```

### Rollout Gradual por Usuário

```typescript
type FlagConfig = {
  enabled: boolean;
  rolloutPercent: number;
  allowlist?: string[];   // sempre recebem (equipe interna)
  denylist?: string[];    // nunca recebem
};

async function isFeatureEnabled(flag: string, userId: string): Promise<boolean> {
  const config = await getFlagConfig(flag);

  if (!config.enabled) return false;
  if (config.allowlist?.includes(userId)) return true;
  if (config.denylist?.includes(userId)) return false;

  // CRC32 garante que o mesmo usuário está sempre no mesmo grupo
  const hash = crc32(`${flag}:${userId}`) % 100;
  return hash < config.rolloutPercent;
}
// Math.random() seria não-determinístico — usuário mudaria de grupo a cada request
```

## Código de Referência

### Progressão de Implementação

```typescript
// Nível 1 — Env var (muda a flag exige novo deploy — não ideal)
const FLAGS = { newCheckout: process.env.FF_NEW_CHECKOUT === "true" } as const;

// Nível 2 — Redis (muda sem deploy)
async function isEnabled(flag: string): Promise<boolean> {
  const value = await redis.get(`ff:${flag}`);
  return value === "true";
}

// Nível 3 — Rollout gradual com config completa (padrão de produção)
async function isFeatureEnabled(flag: string, userId: string): Promise<boolean> { ... }
```

### Kill Switch — Ops Toggle

```typescript
async function checkout(order: Order, userId: string) {
  const shippingEnabled = await isFeatureEnabled("shipping-calculation", userId);

  if (shippingEnabled) {
    try {
      const shipping = await shippingService.calculate(order);
      return checkoutWithShipping(order, shipping);
    } catch (err) {
      console.log({ message: "Shipping service failed, using flat rate fallback" });
    }
  }

  return checkoutWithFlatRate(order); // sempre funciona
}

// Em produção, quando shipping service está lento:
// redis.set("ff:shipping-calculation", JSON.stringify({ enabled: false, rolloutPercent: 0 }))
// → Todos os usuários vão para flat rate instantaneamente, sem deploy
```

### Rollout Gradual na Prática

```typescript
// Semana 1: equipe interna (allowlist)
{ enabled: true, rolloutPercent: 0, allowlist: ["user_dev_1", "user_qa_1"] }

// Semana 2: rolloutPercent = 5   → 5% dos usuários
// Semana 3: rolloutPercent = 25  → monitorar métricas
// Semana 4: rolloutPercent = 100 → todos
// Semana 5: remover a flag do código (cleanup obrigatório)
```

### Limpeza — A Parte Mais Importante

```typescript
// ❌ Flags acumuladas — difícil de entender e manter
async function processOrder(order: Order) {
  if (await isEnabled("new-pricing-v1")) {
    if (await isEnabled("new-pricing-v2")) {
      return applyPricingV2(order);
    }
    return applyPricingV1(order);
  }
  return applyLegacyPricing(order);
}

// ✅ Após cleanup — código limpo
async function processOrder(order: Order) {
  return applyPricingV2(order);
}
```

**Regra:** defina o TTL da flag no momento de criação.
- Release toggle: remove após rollout 100% + 2 semanas de estabilidade
- Ops toggle: documente o motivo se for permanente
- Experiment: remove após análise estatística concluída

## Trade-offs

| Aspecto | Sem Feature Flags | Com Feature Flags |
|---|---|---|
| **Risco de deploy** | Alto — tudo ou nada | Baixo — rollout gradual |
| **Rollback** | Revert de código + deploy | Desliga a flag em segundos |
| **Complexidade do código** | Limpo | Bifurcações temporárias |
| **Deploy/release** | Acoplados | Desacoplados |
| **Branches longas** | Frequentes | Eliminadas com trunk-based dev |
| **Dívida técnica** | Zero flags | Flags não removidas se acumulam |

## Quando Usar / Quando Evitar

**Use feature flags para:**
- ✅ Features com risco de negócio — pagamento, checkout, preço
- ✅ Features grandes que precisam de rollout gradual
- ✅ Qualquer coisa que você quer poder desligar sem deploy
- ✅ A/B testing com análise de conversão

**Não use feature flags para:**
- ❌ Bugfix — corrija e deploye direto
- ❌ Refactoring interno sem mudança de comportamento
- ❌ Como substituto para testes

**Ferramentas:**
```
Simples:    env vars + Redis manual
Open source: Unleash, GrowthBook, Flagsmith
SaaS:        LaunchDarkly

Migre para ferramenta dedicada quando:
→ Mais de 10 flags ativos simultaneamente
→ Time de produto precisa de controle sem passar pelo dev
→ A/B testing com análise estatística
```

## Conceitos Relacionados

[[fase-4-deploy-operacoes]] · [[zero-downtime-deploy]] · [[graceful-degradation]] · [[circuit-breaker]] · [[cqrs]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
