---
type: concept
title: "Monetização Mobile — IAP, Subscriptions, RevenueCat"
aliases: ["in-app purchase mobile", "subscriptions ios android", "revenuecat", "storekit 2"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, monetizacao, iap, subscriptions, revenuecat, storekit, billing]
skill: tech-mentor-mobile
status: stable
---

# Monetização Mobile

## RevenueCat — Abstração Cross-Platform

```ts
await Purchases.configure({ apiKey: 'appl_xxx' });
const offerings = await Purchases.getOfferings();

const { customerInfo } = await Purchases.purchasePackage(
    offerings.current.monthly
);

if (customerInfo.entitlements.active['premium']) {
    // acesso liberado
}
```

RevenueCat gerencia: receipts, webhooks de renovação, status de entitlement, analytics por plataforma.

## iOS — StoreKit 2

```swift
// iOS 15+
let products = try await Product.products(for: ["com.app.premium.monthly"])
let result = try await products.first?.purchase()

switch result {
case .success(let verification):
    let transaction = try verification.payloadValue // verificado criptograficamente
    await transaction.finish()
}
```

## Android — Play Billing Library 6+

```kotlin
val billingClient = BillingClient.newBuilder(context)
    .setListener { billingResult, purchases -> /* processar */ }
    .enablePendingPurchases()
    .build()
```

## Validação Server-Side — Obrigatória

```
Client → compra na Store → recebe receipt
        ↓
Client → envia receipt para seu servidor
        ↓
Servidor → valida receipt na Apple/Google API
        ↓
Servidor → libera acesso no banco
```

Nunca confiar no cliente para liberar acesso — adulterável com Frida/jailbreak.

## Ver também

- [[mobile-seguranca]] — receipt validation
- [[mobile-publicacao-aso]] — configurar produtos na store

## Key Sources

- [[wiki/sources/mobile-monetizacao]]
