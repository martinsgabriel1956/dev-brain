---
date: 2026-04-23
tags: [tech-mentor, mobile, feature-flags, ab-testing, launchdarkly, firebase-remote-config, rollout]
skill: tech-mentor-mobile/references/feature-flags
level: arquiteto
---

# Feature Flags + A/B Testing Mobile — LaunchDarkly, Firebase Remote Config, Rollout sem Release

## Contexto
Feature flags dissociam deploy de release: você faz deploy do código para todos os usuários mas ativa a feature para subconjuntos controlados — sem publicar uma nova versão na store. Isso habilita: rollout gradual (5% → 100%), A/B testing de features, kill switch imediato para reverter problema em produção, e canary releases para early adopters. É o que separa empresas que fazem deploy com confiança das que tremem a cada release.

## Como Funciona

### Firebase Remote Config (solução gratuita e integrada)

```typescript
// React Native — @react-native-firebase/remote-config
import remoteConfig from "@react-native-firebase/remote-config";

// Valores padrão (fallback se Remote Config não carregar)
const DEFAULTS = {
  new_checkout_enabled: false,
  product_grid_columns: 2,
  max_cart_items: 50,
  promo_banner_text: "",
  ab_test_variant: "control"
} as const;

type RemoteConfigKeys = keyof typeof DEFAULTS;

class FeatureFlagService {
  private initialized = false;

  async initialize(): Promise<void> {
    await remoteConfig().setDefaults(DEFAULTS);
    await remoteConfig().setConfigSettings({
      minimumFetchIntervalMillis: __DEV__ ? 0 : 3600000 // 1h em prod, 0 em dev
    });

    try {
      await remoteConfig().fetchAndActivate();
    } catch (err) {
      console.log({ message: "Remote config fetch failed, using defaults", error: err });
    }

    this.initialized = true;
  }

  getBoolean(key: RemoteConfigKeys): boolean {
    return remoteConfig().getValue(key).asBoolean();
  }

  getString(key: RemoteConfigKeys): string {
    return remoteConfig().getValue(key).asString();
  }

  getNumber(key: RemoteConfigKeys): number {
    return remoteConfig().getValue(key).asNumber();
  }

  // Verificar se feature está ativa para o usuário atual
  isEnabled(key: Extract<RemoteConfigKeys, "new_checkout_enabled">): boolean {
    return this.getBoolean(key);
  }
}

export const featureFlags = new FeatureFlagService();
```

```typescript
// Hook para consumir flags em componentes
export function useFeatureFlag(key: RemoteConfigKeys) {
  const [value, setValue] = useState(() => featureFlags.getBoolean(key as any));

  useEffect(() => {
    // Escutar mudanças em tempo real (quando Remote Config atualiza)
    const unsubscribe = remoteConfig().onConfigUpdated(async () => {
      await remoteConfig().activate();
      setValue(featureFlags.getBoolean(key as any));
    });
    return unsubscribe;
  }, [key]);

  return value;
}

// Uso no componente
export function CheckoutScreen() {
  const newCheckoutEnabled = useFeatureFlag("new_checkout_enabled");

  if (newCheckoutEnabled) return <NewCheckoutFlow />;
  return <LegacyCheckoutFlow />;
}
```

### LaunchDarkly (solução enterprise)

```typescript
// @launchdarkly/react-native-client-sdk
import LDClient from "@launchdarkly/react-native-client-sdk";

const LD_CONFIG = {
  mobileKey: process.env.EXPO_PUBLIC_LD_MOBILE_KEY,
  evaluationReasons: true // para debug de regras
};

// Contexto do usuário — base para targeting
const userContext = {
  kind: "user",
  key: user.id,
  email: user.email,
  plan: user.plan,
  country: user.country,
  custom: {
    accountAge: daysSinceCreation(user.createdAt),
    hasCompletedOnboarding: user.onboardingCompletedAt !== null
  }
};

await LDClient.configure(LD_CONFIG, userContext);

// Avaliar flag com default
const showNewOnboarding = LDClient.boolVariation("new-onboarding-v2", false);
const checkoutVersion = LDClient.stringVariation("checkout-variant", "control");
const maxItemsPerCart = LDClient.numberVariation("max-cart-items", 50);

// Track evento para análise de A/B test
LDClient.track("checkout_completed", { revenue: cart.total, itemCount: cart.items.length });
```

### A/B Testing — Implementação

```typescript
type ABVariant = "control" | "variant_a" | "variant_b";

// Distribuição: 33% cada
function getABVariant(userId: string, experimentKey: string): ABVariant {
  // Hash determinístico — mesmo usuário sempre vê a mesma variante
  const hash = murmurhash(`${userId}:${experimentKey}`);
  const bucket = hash % 100;

  if (bucket < 33) return "control";
  if (bucket < 66) return "variant_a";
  return "variant_b";
}

// OU via Remote Config (mais flexível)
const abVariant = featureFlags.getString("ab_test_variant") as ABVariant;

// Componente A/B
export function ProductCard({ product }: { product: Product }) {
  const variant = useFeatureFlag("product_card_layout") as ABVariant;

  // Rastrear exposição ao experimento
  useEffect(() => {
    analytics.track("experiment_exposure", {
      experimentKey: "product_card_layout",
      variant,
      productId: product.id
    });
  }, []);

  switch (variant) {
    case "variant_a":
      return <ProductCardHorizontal product={product} />;
    case "variant_b":
      return <ProductCardLarge product={product} />;
    default:
      return <ProductCardDefault product={product} />;
  }
}
```

### Rollout gradual sem release

```typescript
// Padrão: feature desabilitada por padrão, habilitada via Remote Config
// Sem nova versão na store

// 1. Publicar código com flag desabilitada (sem impacto)
export function NewFeatureScreen() {
  const enabled = useFeatureFlag("new_feature_enabled"); // default: false
  if (!enabled) return <Navigate to="home" />;
  return <NewFeature />;
}

// 2. No Firebase Console / LaunchDarkly:
//    - Ativar para 5% dos usuários
//    - Monitorar métricas e crash rate
//    - Aumentar para 20%, 50%, 100%
//    - Se problema: desabilitar imediatamente (sem deploy)

// 3. Kill switch — reverter em segundos sem release
//    new_feature_enabled: false → desabilita para 100% dos usuários
```

### Targeting avançado — quem vê o quê

```typescript
// Firebase Remote Config — conditions via console:
// Condition 1: country == "BR" AND plan == "premium" → variant_a
// Condition 2: deviceOS == "ios" → variant_b
// Default: control

// LaunchDarkly — targeting rules mais expressivas:
const targetingRules = {
  "new-checkout": {
    on: true,
    targets: [{ values: ["user-id-beta-tester-1", "user-id-beta-tester-2"], variation: 0 }],
    rules: [
      {
        clauses: [
          { attribute: "plan", op: "in", values: ["premium", "enterprise"] }
        ],
        variation: 0 // variante "on"
      }
    ],
    fallthrough: { variation: 1 }, // variante "off" para todos os outros
    offVariation: 1
  }
};
```

### Limpeza de flags antigas — tech debt

```typescript
// Flags devem ter data de expiração definida ao criar
// Após 100% de rollout confirmado, remover o código de flag

// ERRADO — flag orphan no código por meses
const enabled = featureFlags.getBoolean("new_checkout_enabled"); // feature lançada há 6 meses
if (enabled) return <NewCheckout />; // nunca mais vai ser false
return <OldCheckout />; // código morto

// CORRETO — após rollout completo
// 1. Remover a flag do Remote Config
// 2. Fazer PR removendo o if/else e o código legado
// 3. Código direto: return <NewCheckout />;
```

## Trade-offs

| Solução | Targeting | Tempo real | Analytics | Custo | Ideal para |
|---|---|---|---|---|---|
| Firebase Remote Config | Básico (conditions) | Não (fetch periódico) | GA4 | Grátis | Maioria dos apps |
| LaunchDarkly | Avançado (rules, segments) | Sim (streaming) | Built-in | Caro | Enterprise |
| Unleash (self-hosted) | Avançado | Sim | Básico | Infra própria | Enterprise com compliance |
| Flipt | Básico | Sim | Básico | Infra própria | Open source |

## Quando Usar / Quando Evitar

**Feature flags para:** novas features que precisam de rollout gradual, A/B tests, configurações que podem precisar de mudança em emergência (max_items, timeouts, textos de campanhas).

**Não usar flags para:** configurações permanentes do app (URL de API, timeout padrão), lógica de negócio crítica que não pode ser alterada dinamicamente.

**Limpeza obrigatória:** toda flag tem data de expiração. Feature em 100% de rollout por mais de 30 dias = PR de remoção. Flags acumuladas viram tech debt que ninguém entende.

## Conceitos Relacionados
[[mobile-design-system]] · [[mobile-monitoramento]] · [[mobile-cicd]] · [[mobile-plataforma-engineering]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
