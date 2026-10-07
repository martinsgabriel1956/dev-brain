---
type: source
title: "O Desafio Simples de System Design que Reprova Seniores: Sistema de Notificação (Ana)"
aliases: ["desafio de notificação reprova senior", "notification system interview"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/desafio-sistema-notificacao-system-design-reprova-senior-ana.md
source_url: ""
author: "Ana (sobrenome/canal não confirmados na transcrição)"
date_published: ""
date_ingested: 2026-10-07
source_count: 0
tags: [system-design, entrevistas, notificacao, kafka, prioridade, custo, senioridade]
skill: tech-mentor-system-design
status: draft
---

# O Desafio Simples de System Design que Reprova Seniores (Ana)

## TL;DR

Um sistema de notificação (push, e-mail, SMS) reprova seniores por hábito, não por conteúdo: começar pela [[wiki/concepts/api-e-consequencia-nao-ponto-de-partida|API]], ignorar a palavra "custo" ([[wiki/concepts/palavras-do-enunciado-mudam-a-arquitetura]]), pular as [[wiki/concepts/entidades-de-primeira-classe-system-design|entidades]] e não pensar em falha. Desenho-resposta: API de ingestão (idempotência, preferência, rate limit) → [[wiki/concepts/filas-separadas-por-prioridade|três tópicos Kafka por prioridade]] → [[wiki/concepts/channel-router-custo-fallback|channel router]] → workers por canal → callback → [[wiki/concepts/confirmacao-de-entrega-nao-confiavel|job de reconciliação]].

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| Ordem correta: requisitos → entidades (≤3 min) → alto nível → API | Candidato que abriu com `/v1/notifications` gastou ~15 de 45 min na API, sem perguntas | Média: anedota de mock interview; coerente com [[wiki/concepts/entrevista-system-design]] |
| Fila única deixa campanha de marketing atrasar código de autenticação | 3 tópicos crítico/normal/baixo | Alta: head-of-line blocking é consequência conhecida |
| SMS custa 10–500× push/e-mail; push → e-mail → SMS como fallback | Dito no vídeo | Média: faixa do autor `[external não verificado]` (preço varia por país/provedor) |
| Confirmação de entrega de push não é garantida | FCM/APNs não confirmam entrega ao dispositivo | Alta (comportamento conhecido de push) |
| UserPreference e DeliveryAttempt são o que permite rate limit, fallback e rastreio | Argumento do autor | Média |
| Valores de 5–25 mil por dia em SMS | Dito no vídeo, sem moeda explícita (provável US$) | Baixa: não verificado |

## Conceitos
[[wiki/concepts/notification-system]], [[wiki/concepts/api-e-consequencia-nao-ponto-de-partida]], [[wiki/concepts/entidades-de-primeira-classe-system-design]], [[wiki/concepts/filas-separadas-por-prioridade]], [[wiki/concepts/channel-router-custo-fallback]], [[wiki/concepts/confirmacao-de-entrega-nao-confiavel]], [[wiki/concepts/palavras-do-enunciado-mudam-a-arquitetura]], [[wiki/concepts/kafka]], [[wiki/concepts/idempotencia]], [[wiki/concepts/reconciliacao]].

## Open Questions
- Tópicos separados por prioridade vs. uma fila com prioridade/partição dedicada: o vídeo só afirma o primeiro. Ver [[wiki/concepts/filas-separadas-por-prioridade]].
- Anti-starvation: o que garante que "baixa prioridade" eventualmente seja consumida?
- Autoria e canal não identificados (só "Ana"); patrocinador Locaweb Cloud omitido.

## Quotes
- "Isso parece um progresso... mas é o que eu chamo de progresso falso."
- "A API é uma consequência de decisões arquiteturais e não um ponto de partida."
- "A gente se desespera por saber demais."
