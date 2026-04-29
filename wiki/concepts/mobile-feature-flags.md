---
type: concept
title: "Feature Flags Mobile"
aliases: ["mobile remote config", "mobile ab testing", "firebase remote config", "launchdarkly mobile"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, feature-flags, remote-config, ab-testing, rollout, launchdarkly, firebase]
skill: tech-mentor-mobile
status: stable
---

# Feature Flags Mobile

Dissociam deploy de release — código vai para produção, ativação é controlada remotamente.

## Firebase Remote Config

```ts
const remoteConfig = getRemoteConfig(app);
remoteConfig.defaultConfig = { new_checkout: false }; // cache local

await fetchAndActivate(remoteConfig);
const isNewCheckout = getBoolean(remoteConfig, 'new_checkout');
```

Gratuito, suficiente para rollout por percentual e A/B básico.

## LaunchDarkly

```ts
const client = initialize('sdk-key', { key: user.id });
const showFeature = client.variation('new-feature', false);
```

Targeting por atributos de usuário (plano, região, segmento). Melhor para empresas com múltiplos segmentos.

## Padrões

```ts
// Wrapper que abstrai o provider
class FeatureFlagService {
    isEnabled(flag: string): boolean {
        return this.cache.get(flag) ?? this.defaults[flag] ?? false;
    }
}
```

Cache local obrigatório — app não pode depender de fetch bem-sucedido para renderizar.

## A/B Testing

```ts
// Atrelar métrica ao variant
analytics.track('checkout_started', { variant: getVariant('checkout_v2') });
```

Sem métrica de conversão atrelada, A/B é apenas um toggle.

## Ver também

- [[feature-flags]] — padrões gerais de feature flags
- [[mobile-cicd]] — integração com pipeline de release
- [[mobile-monitoramento]] — monitorar métricas por variant

## Key Sources

- [[wiki/sources/mobile-feature-flags]]
