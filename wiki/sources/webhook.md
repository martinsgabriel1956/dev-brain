---
type: source
title: "Webhooks — HMAC, Retry e Fanout"
aliases: ["webhook", "webhooks", "hmac webhook", "webhook signing", "webhook retry", "webhook fanout"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/webhook.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [webhook, hmac, replay-attack, idempotency, fanout, event-delivery, integration-patterns]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Webhook é o inverso de polling: producer empurra eventos HTTP quando algo acontece. Problemas sérios: replay attacks, ordem de entrega, falhas de receiver, fanout. Solução: HMAC-SHA256 para autenticidade + timestamp para prevenir replay (janela de 5min) + `X-Webhook-Id` para deduplicação + processamento assíncrono após 200 OK imediato. Fanout via fila (SQS/Kafka) para múltiplos destinos.

## Key Claims

**Claim:** HMAC-SHA256 com comparação `timingSafeEqual` é o padrão de autenticidade para webhooks — sem isso, qualquer attacker pode forjar eventos.
**Evidence:** Producer assina o payload: `const sig = crypto.createHmac("sha256", secret).update(rawBody).digest("hex")`. Header: `X-Signature: sha256=<sig>`. Receiver verifica: `crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(received))`. Sem `timingSafeEqual`, comparação de strings vaza timing information permitindo ataques de timing side-channel. Sem assinatura, qualquer origem pode enviar eventos falsos.
**Confidence:** alta

**Claim:** Timestamp no payload previne replay attacks — janela de 5 minutos é o baseline padrão.
**Evidence:** Replay attack: attacker captura um webhook legítimo e o reenvia horas depois. Prevenção: producer inclui `timestamp` no payload assinado. Receiver verifica: `Math.abs(Date.now() - timestamp) > 5 * 60 * 1000 → rejeitar`. A janela de 5 minutos absorve clock skew entre sistemas. Sem isso, uma compra poderia ser processada múltiplas vezes com o mesmo payload capturado.
**Confidence:** alta

**Claim:** Processamento assíncrono após 200 OK imediato evita timeouts e garante entrega confiável.
**Evidence:** Producer tem timeout curto (tipicamente 5-30s). Se o receiver processar o evento sincronamente (banco, email, etc.), pode ultrapassar o timeout. Producer interpreta timeout como falha e re-entrega. Resultado: processamento duplicado. Padrão correto: retornar 200 imediatamente, enfileirar o evento (Redis, SQS, BullMQ), processar assincronamente. `X-Webhook-Id` para deduplicação no processamento.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/webhook]]
- [[concepts/hmac-signing]]
- [[concepts/replay-attack]]
- [[concepts/idempotency]]
- [[concepts/fanout-pattern]]
- [[concepts/at-least-once-delivery]]

## Open Questions

- Webhook vs Server-Sent Events vs WebSocket — quando webhook é claramente a escolha errada?
- Webhook fanout para 10k+ subscribers — como escalar sem degradar o producer?
