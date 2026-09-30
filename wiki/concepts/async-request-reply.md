---
type: concept
title: "Async Request-Reply (Polling por ID de Operação)"
aliases: ["request-reply assíncrono", "polling de status", "202 Accepted + job id"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [comunicacao-assincrona, polling, api-design, request-reply]
skill: tech-mentor-backend
status: stub
---

# Async Request-Reply (Polling por ID de Operação)

O serviço aceita a solicitação e devolve imediatamente um **ID da operação**; o cliente faz **polling** de um endpoint de status passando esse ID e recebe o **status** ou, quando concluído, os **dados** do processamento. Uma das formas de [[wiki/concepts/comunicacao-assincrona]] sem broker, útil quando não se controla os dois lados (API externa).

Forma típica de API [skill: tech-mentor-backend, `references/architecture-eda-patterns.md`]: `POST /exports → 202 Accepted { jobId }`, depois `GET /exports/{jobId}` → `processing` … `done`.

Alternativa em que o receptor avisa o cliente: [[wiki/concepts/webhook]]. Sobre o custo/escala do polling em si, ver [[wiki/concepts/websocket-vs-polling]].

## Key sources

- [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]] — descrição da técnica (sem código)
