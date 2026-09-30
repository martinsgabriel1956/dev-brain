---
type: concept
title: "Webhook (Callback)"
aliases: ["callback", "webhook callback", "http callback"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [comunicacao-assincrona, webhook, callback, api-design]
skill: tech-mentor-backend
status: stub
---

# Webhook (Callback)

O receptor responde só com um **OK** ao receber a solicitação e, quando termina de processar, **chama um endpoint (webhook/callback) cadastrado previamente** na estrutura do solicitante, que trata os dados. Forma de [[wiki/concepts/comunicacao-assincrona]] sem broker; o oposto do cliente puxar o status por [[wiki/concepts/async-request-reply]].

Comum em integrações com APIs externas fora do seu controle ([[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]]). O vídeo não aborda segurança nem reentrega; ver [[wiki/concepts/webhook-signature-validation]] (HMAC, replay, idempotência) e [[wiki/concepts/idempotencia]].

## Key sources

- [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]] — webhook/callback como alternativa ao polling
