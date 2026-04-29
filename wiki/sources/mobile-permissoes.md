---
type: source
title: "Permissões Runtime — iOS e Android"
aliases: ["mobile permissoes", "runtime permissions android", "ios permissions", "privacy manifest"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-permissoes.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, permissoes, runtime-permissions, privacy, ios, android, privacy-manifest]
skill: tech-mentor-mobile
status: stable
---

# Permissões Runtime — Mobile

## TL;DR

iOS: pedir permissão apenas quando necessário com contexto claro (`NSCameraUsageDescription`). Android 6+: runtime permissions com `ActivityResultContracts.RequestPermission`. Nunca pedir permissões no launch — usuário não entende o contexto. iOS Privacy Manifest obrigatório para apps na App Store 2024+. Projetar fluxo que funcione com permissão negada — degradação graciosa.

## Claims Principais

| Claim | Confiança |
|---|---|
| Pedir permissão no contexto de uso — não no launch — taxa de concessão 3x maior | Alta |
| iOS Privacy Manifest obrigatório — apps sem ele rejeitados na App Store desde maio 2024 | Alta |
| Android `shouldShowRequestPermissionRationale` — mostrar rationale antes do segundo pedido | Alta |
| Permissão negada permanentemente: direcionar para Settings — sem loop de pedidos | Alta |
| Projetar funcionalidade core sem permissão — permissão melhora UX, não bloqueia | Alta |

## Conceitos Abordados

- [[mobile-permissoes]] · [[mobile-seguranca]] · [[mobile-biometria]]
