---
type: concept
title: "Quando Usar (e Não Usar) Mensageria"
aliases: ["quando usar rabbitmq", "mensageria vs http"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [mensageria, rabbitmq, decisao, over-engineering]
skill: tech-mentor-backend
status: draft
---

# Quando Usar (e Não Usar) Mensageria

**Use** para desacoplar sistemas, rodar processamento em background e lidar com falhas/retentativas. **Não use** quando o sistema é simples, com poucos processos externos e poucas dependências de fora — HTTP resolve ([[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]]). Usar sem precisar é "pior" que usar errado, segundo o autor: custo de [[wiki/concepts/over-engineering]].

Critério prático derivado do vídeo: há chamadas a sistemas externos lentos/instáveis no caminho do usuário? Se sim, publique evento ([[wiki/concepts/comunicacao-assincrona]], [[wiki/concepts/processamento-assincrono]]); se não, mantenha [[wiki/concepts/comunicacao-sincrona]]. Ver [[wiki/concepts/monolito-distribuido]].

## Key sources

- [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]]
