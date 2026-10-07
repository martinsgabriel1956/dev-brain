---
type: concept
title: "Entidades de Primeira Classe no System Design"
aliases: ["entidades no system design", "delivery attempt", "user preference"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [system-design, modelagem, entrevistas]
skill: tech-mentor-system-design
status: draft
---

# Entidades de Primeira Classe no System Design

Passo de ≤3 min, muito pulado: listar as entidades do domínio revela como o serviço se divide. No sistema de notificação: User, Notification, Channel, Template (mensagem reutilizável com variáveis), **UserPreference** e **DeliveryAttempt** (cada tentativa por canal, com estado). Sem as duas últimas é impossível desenhar rate limit, fallback de canal ou rastreio de status. Teste de compreensão: quem só decorou "fila + workers" não as inclui. Ver [[wiki/concepts/notification-system]], [[wiki/concepts/api-e-consequencia-nao-ponto-de-partida]].

## Key sources
- [[wiki/sources/desafio-sistema-notificacao-system-design-reprova-senior-ana]]
