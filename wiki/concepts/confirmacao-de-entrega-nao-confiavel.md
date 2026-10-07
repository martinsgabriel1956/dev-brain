---
type: concept
title: "Confirmação de Entrega de Push Não É Confiável"
aliases: ["delivery callback", "reconciliation job", "push delivery receipt"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [system-design, confiabilidade, notificacao, reconciliacao]
skill: tech-mentor-system-design
status: draft
---

# Confirmação de Entrega de Push Não É Confiável

FCM/APNs não garantem entrega ao dispositivo; "enviado" ≠ "entregue". Para notificação crítica: registrar cada [[wiki/concepts/entidades-de-primeira-classe-system-design|DeliveryAttempt]], receber callback assíncrono dos provedores, e rodar um **job de reconciliação** com timeout que reprocessa falhas e escala de canal (ex.: push → SMS) quando falta confirmação. Exemplo de pensar em modo de falha sem ser perguntado. Ver [[wiki/concepts/reconciliacao]], [[wiki/concepts/idempotencia]] (idempotency key na ingestão), [[wiki/concepts/dlq]], [[wiki/concepts/mobile-push-notifications]].

## Key sources
- [[wiki/sources/desafio-sistema-notificacao-system-design-reprova-senior-ana]]
