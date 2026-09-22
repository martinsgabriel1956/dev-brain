---
type: concept
title: "Fan-out Pattern"
aliases: ["fanout", "fan-out on write", "fan-out on read", "fan out"]
date_created: 2026-04-22
date_updated: 2026-09-22
source_count: 3
tags: [system-design, distribuidos, notificacao, feed, escala]
skill: tech-mentor-system-design
status: stable
---

# Fan-out Pattern

Estratégia de distribuição de um evento para N destinatários. Dois modelos com trade-offs opostos.

## Fan-out on Write

Ao publicar o evento, gera e persiste cópias para todos os destinatários imediatamente.

```
OrderShipped → insere 1 notificação para o dono do pedido ✓
CommentOnPost → insere 10M notificações para cada seguidor ✗
```

- **Vantagem:** leitura é O(1) — notificações já estão prontas por usuário
- **Desvantagem:** write amplification — 1 evento × N destinatários × M canais = writes explosivos
- **Quando:** destinatários previsíveis e pequenos (< 1000)

## Fan-out on Read

Armazena apenas o evento. Ao usuário consultar, agrega dinamicamente.

- **Vantagem:** write é O(1) independente do número de seguidores
- **Desvantagem:** leitura é cara — agrega on-the-fly para cada usuário
- **Quando:** conteúdo viral, audiência imprevisível (celebridades, posts virais)

## Híbrido (Twitter/Instagram)

```
Usuário comum (< X seguidores) → fan-out on write (rápido, audiência pequena)
Celebridade  (> X seguidores) → fan-out on read  (write barato, leitura agrega)
```

Threshold típico: 10k–1M seguidores dependendo da arquitetura e custo de storage.

## Aparece em

- [[concepts/notification-system]] — fan-out de notificações por canal
- Feed de posts (Twitter, Instagram, LinkedIn)
- [[concepts/chat-distribuido]] — fan-out de mensagem para membros do grupo

## Key Sources

- [[wiki/sources/sqs-sns]] — SQS é uma fila gerenciada AWS (zero operação). Standard: alta throughput, ordenação best-effort. FIFO: ordering garantido por MessageGroupId, deduplicação nativa (5 min window), limitado a 3k msg/s...
- [[wiki/sources/webhook]] — Webhook é o inverso de polling: producer empurra eventos HTTP quando algo acontece. Problemas sérios: replay attacks, ordem de entrega, falhas de receiver, fanout. Solução: HMAC-SHA256 para...
- [[sources/notification-system]]
