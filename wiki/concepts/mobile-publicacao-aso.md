---
type: concept
title: "Publicação e ASO — App Store Optimization"
aliases: ["aso mobile", "app store optimization", "google play ranking", "store listing"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, publicacao, aso, app-store, google-play, screenshots, ratings]
skill: tech-mentor-mobile
status: stable
---

# Publicação e ASO

## Hierarquia de Impacto ASO

```
1. Título (30 chars) — peso máximo no ranking
2. Subtítulo / Short Description — keywords secundárias
3. Screenshots / Preview Video — conversão na store page
4. Ratings e Reviews — confiança e ranking
5. Keywords Field (iOS) — indexação sem aparecer para usuário
6. Descrição longa — keyword stuffing NÃO funciona
```

## Screenshots

- Primeira screenshot: proposta de valor clara em 1 linha
- Preview video aumenta conversão 20-30% vs screenshots estáticas
- Texto sobrepostos nas screenshots — usuário não lê a descrição
- Testar A/B de screenshots com Google Experiments / App Store Experiments

## Ratings

```ts
// Solicitar review após ação de sucesso — não no launch
async function handleOrderComplete() {
    await completeOrder();

    const ordersCompleted = await storage.get('orders_completed') + 1;
    await storage.set('orders_completed', ordersCompleted);

    if (ordersCompleted === 3) {
        await StoreReview.requestReview(); // iOS SKStoreReviewController
    }
}
```

Taxa de resposta 5x maior quando solicitado no contexto correto.

## Checklist de Publicação

- [ ] Privacy policy URL válida
- [ ] Screenshots em todos os tamanhos exigidos
- [ ] App em conformidade com guidelines (IAP obrigatório para digital goods)
- [ ] Privacy Manifest (iOS) preenchido
- [ ] Data Safety Form (Android) preenchido
- [ ] Rollout configurado (10% inicial)

## Review Times

- **App Store Connect:** 24-48h (expedited review disponível para hotfixes)
- **Google Play:** 1-3 dias (reviews automáticas para updates menores)

## Ver também

- [[mobile-monetizacao]] — configurar produtos antes de publicar
- [[mobile-cicd]] — automatizar upload do build

## Key Sources

- [[wiki/sources/mobile-publicacao-aso]]
