---
type: entity
title: "Pedro Camaforte"
aliases: ["Camaforte"]
date_created: 2026-07-03
date_updated: 2026-09-04
source_count: 4
tags: [instrutor, system-design, entrevistas, backend, youtube]
skill: tech-mentor-backend
status: stub
---

# Pedro Camaforte

Desenvolvedor sênior, atua há quase dois anos para empresas do exterior. Cria uma série de sete vídeos no YouTube sobre os principais conceitos de system design cobrados em entrevistas de empresas "tier" (faixa salarial R$20-40k+), com foco explícito no que separa uma resposta de entrevista mediana de uma que demonstra profundidade real (ex: por que citar Load Balancer L4 para WebSocket é um diferencial, não trivia).

A série é baseada num artigo de [[wiki/entities/lucas-faria]] sobre os sete conceitos que mais caem em entrevistas Tier S.

## Key Sources

- [[wiki/sources/updates-tempo-real-polling-sse-websocket]]
- [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]] — primeiro vídeo da série de System Design: escada de escalonamento de leitura (índices/pooling → read replicas → cache → CDN) e o erro que elimina 90% dos candidatos
- [[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]] — sexto vídeo da série: race condition/TOCTOU via cadeira de cinema e estoque de e-commerce, três estratégias de correção (pessimistic locking, OCC, reservations com Redis) demonstradas com código real, e os três erros que eliminam candidatos em entrevista
- [[wiki/sources/como-se-comportar-na-entrevista-de-system-design-tier-s]] — sétimo e último vídeo, fecha a série sem conteúdo técnico novo: mapeia os 7 conceitos da série de volta às features de Instagram/WhatsApp/YouTube, roteiro de 3-4 etapas antes de desenhar (requisitos → entidades → APIs → design), e a tese central de que o comportamental (comunicar raciocínio, receber feedback) pesa mais do que o repertório técnico na hora de diferenciar candidatos
