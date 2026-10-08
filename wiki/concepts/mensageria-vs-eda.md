---
type: concept
title: "Mensageria vs. Arquitetura Orientada a Eventos"
aliases: ["mensageria não é eda"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [mensageria, event-driven, arquitetura]
skill: tech-mentor-backend
status: draft
---

# Mensageria vs. Arquitetura Orientada a Eventos

**Mensageria** é infraestrutura de baixo nível: um mediador (broker) entre produtor e consumidor, útil sozinho para resiliência. Exemplo da fonte: um webhook recebe HTTP, enfileira e o consumidor processa depois, mesmo que o resto esteja offline. Isso **não** é um evento nem uma arquitetura orientada a eventos.

**EDA** é um desenho: planeja-se a intercomunicação entre pontos da aplicação como publicação e consumo de fatos de negócio, e os interessados seguem o fluxo a partir do que aconteceu. Sinal de que só há mensageria: o remetente ainda sabe quem é o próximo passo e o que ele precisa receber (acoplamento permanece). Fonte: [[wiki/sources/arquitetura-orientada-a-eventos-luiz-gago-faria-otavio-santana-eduardo-macris]].

A fonte cita quatro padrões sob o guarda-chuva "eventos": transferência de estado, CQRS, notificação de evento e um quarto não lembrado (provável Event Sourcing; `[external não verificado]`, possível referência a Martin Fowler).

Relacionados: [[wiki/concepts/mensageria]], [[wiki/concepts/event-driven-architecture]], [[wiki/concepts/cqrs]], [[wiki/concepts/event-sourcing]], [[wiki/concepts/evento-vs-comando]].

## Key sources

- [[wiki/sources/arquitetura-orientada-a-eventos-luiz-gago-faria-otavio-santana-eduardo-macris]]
