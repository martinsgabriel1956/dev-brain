---
type: concept
title: "Adapter Pattern para Analytics Mobile"
aliases: ["analytics adapter", "analytics provider pattern", "troca de provider analytics"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [mobile, analytics, adapter-pattern, design-patterns, platform-engineering]
skill: tech-mentor-mobile
status: stable
---

# Adapter Pattern para Analytics Mobile

O Adapter Pattern em analytics mobile resolve o problema de acoplamento direto a um provider (Firebase, Amplitude, Mixpanel): quando você chama o SDK do provider em 200 lugares e precisa trocar, o PR tem 500 linhas.

## Solução

Um `AnalyticsService` central registra múltiplos `AnalyticsProvider`. O app chama apenas `analytics.track()` — sem saber qual provider está ativo.

```typescript
type AnalyticsProvider = {
  initialize(): Promise<void>;
  identify(userId: string, traits?: EventProperties): void;
  track(event: string, properties?: EventProperties): void;
  screen(name: string, properties?: EventProperties): void;
  reset(): void;
};
```

O `AnalyticsService` itera sobre todos os providers registrados — permitindo multi-provider simultâneo (ex: Mixpanel + Firebase ao mesmo tempo).

## Benefícios

- Troca de provider = novo arquivo de implementação, zero mudança nos call sites
- Multi-provider sem duplicação de chamadas no código de produto
- Testável: injeta `MockProvider` nos testes

## Relacionado

- [[concepts/shared-sdk]] — o módulo de analytics faz parte do SDK compartilhado
- [[concepts/analytics-pipeline]] — pipeline assíncrono de analytics no backend
- [[sources/mobile-platform-engineering]]
