---
type: concept
title: "Simulador de System Design"
aliases: ["system design simulator", "playground de system design"]
date_created: 2026-07-24
date_updated: 2026-07-24
source_count: 1
tags: [system-design, saas, aprendizado, ferramenta, vibe-coding]
skill: tech-mentor-system-design
status: stub
---

# Simulador de System Design

Playground onde o usuário monta um diagrama de arquitetura (client, load balancer, cache, banco de dados, filas etc.) e roda uma simulação de tráfego sobre ele, recebendo de volta métricas em tempo real (latência, disponibilidade, gargalo) e uma correção de rota sugerida — em vez de apenas desenhar estaticamente o diagrama, como faria uma ferramenta genérica de diagramação (Excalidraw e afins).

## Por que não é só um desenho

A tese por trás do produto: qualquer ferramenta de diagramação já resolve "desenhar" um [[wiki/concepts/high-level-design|high-level design]] de graça. O valor de um produto pago está em (1) simular o comportamento do sistema desenhado sob carga, expondo gargalos reais, e (2) uma IA revisando se o desenho faz sentido e dando uma nota — fechando o loop entre teoria de [[wiki/concepts/entrevista-system-design|system design]] e prática executável.

## Componentes observados no protótipo

- Biblioteca de componentes: client, mobile, DNS, CDN, load balancer, WAF, API gateway, app server, cache, banco de dados, fila de mensageria (Kafka/EventBridge), entre outros.
- Simulador de tráfego: aumenta requisições simuladas e reporta latência, disponibilidade e sinalização de [[wiki/concepts/gargalo|bottleneck]] em tempo real por componente.
- "Simulador de caos": simula falha de data center ou availability zone — incluído no MVP inicial, mas apontado pelo próprio autor como possível erro de escopo nesse estágio (ver [[wiki/concepts/over-engineering]] e [[wiki/concepts/mvp]]).
- Score de IA: duas IAs avaliadoras chegam a um consenso e pontuam o desenho, apontando acertos e componentes faltantes ou introduzidos sem justificativa de uso.

## Quatro exercícios base

Escolhidos por serem clássicos de entrevista de [[wiki/concepts/entrevista-system-design]] e cobrirem a maioria dos tópicos que um programador (ou alguém fazendo [[wiki/concepts/vibe-coding]]) precisa resolver na prática: URL shortener, feed estilo Twitter/X, busca de motoristas estilo Uber (>1M req/s), e mensageria em tempo real estilo Slack.

## Key Sources

- [[wiki/sources/system-design-simulador-hotel-booking-replit]] — origem do produto e demonstração completa com exercício de hotel booking
