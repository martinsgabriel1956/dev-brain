---
type: source
title: "Monetização Mobile — IAP, Subscriptions, RevenueCat"
aliases: ["mobile monetizacao", "in-app purchases", "subscriptions mobile", "revenuecat", "storekit"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-monetizacao.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, monetizacao, iap, subscriptions, revenuecat, storekit, google-play-billing]
skill: tech-mentor-mobile
status: stable
---

# Monetização Mobile

## TL;DR

StoreKit 2 (iOS) e Google Play Billing Library 6+ (Android) para IAP e subscriptions. RevenueCat abstrai ambas as plataformas — entitlements, webhooks, analytics sem reimplementar. Sempre validar receipts no servidor — nunca confiar no cliente. Taxa da loja: 30% primeiros 12 meses, 15% após (pequenos desenvolvedores: 15% desde o início).

## Claims Principais

| Claim | Confiança |
|---|---|
| RevenueCat elimina implementação duplicada iOS/Android + webhooks de renovação | Alta |
| Validação de receipt DEVE ser server-side — cliente pode ser adulterado | Alta |
| StoreKit 2 (iOS 15+) usa async/await e transação verificada criptograficamente | Alta |
| Google Play Billing Library 6 substitui AIDL — PurchasesUpdatedListener obrigatório | Alta |
| Introductory offers (trial, desconto) aumentam conversão — configurar em ambas as stores | Alta |

## Conceitos Abordados

- [[mobile-monetizacao]] · [[mobile-seguranca]] · [[mobile-publicacao-aso]]
