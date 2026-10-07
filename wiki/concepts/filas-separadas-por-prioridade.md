---
type: concept
title: "Filas (Tópicos) Separadas por Prioridade"
aliases: ["priority queues", "tópicos por prioridade", "head-of-line blocking"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [mensageria, kafka, prioridade, system-design]
skill: tech-mentor-system-design
status: draft
---

# Filas (Tópicos) Separadas por Prioridade

Isolar prioridade na infraestrutura: três tópicos [[wiki/concepts/kafka]] (crítico, normal, baixo), em vez de fila única. Evita que uma campanha de marketing (500 mil a 1 milhão de mensagens) atrase um código de autenticação. Resolver "no código do consumidor" não isola a carga. Variante do case em [[wiki/concepts/notification-system]] (SQS FIFO vs Standard `[skill: tech-mentor-system-design]`). Pendente: política anti-starvation do tópico de baixa prioridade . Ver [[wiki/concepts/filas-e-workers]], [[wiki/concepts/fila]].

## Key sources
- [[wiki/sources/desafio-sistema-notificacao-system-design-reprova-senior-ana]]
