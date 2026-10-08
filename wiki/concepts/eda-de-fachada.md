---
type: concept
title: "EDA de Fachada"
aliases: ["event-driven cosmético", "eda para inglês ver"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [event-driven, anti-pattern, hype, acoplamento]
skill: tech-mentor-backend
status: draft
---

# EDA de Fachada

Anti-padrão descrito em [[wiki/sources/arquitetura-orientada-a-eventos-luiz-gago-faria-otavio-santana-eduardo-macris]]: usar o vocabulário de eventos/comandos/DDD mas manter **banco compartilhado**, serviços hiperacoplados e modelagem que parte do banco (sem camada de domínio; herança de código procedural). Sem roadmap independente entre os serviços, não há benefício de desacoplamento; é o mesmo caso de microsserviços que na prática são um serviço só.

Causas citadas: hype ("CRUD de DDD, CRUD de eventos, CRUD de microsserviço"), falta de discussão de domínio, time imaturo, ausência de condições para a arquitetura. Caso extremo: startup parada 3 meses sem entregar após decidir fazer tudo orientado a eventos.

Relacionados: [[wiki/concepts/event-driven-architecture]], [[wiki/concepts/microsservicos]], [[wiki/concepts/over-engineering]], [[wiki/concepts/avaliar-hype-tecnologico]], [[wiki/concepts/anti-pattern]], [[wiki/concepts/dominio]].

## Key sources

- [[wiki/sources/arquitetura-orientada-a-eventos-luiz-gago-faria-otavio-santana-eduardo-macris]]
