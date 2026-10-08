---
type: source
title: "Arquitetura Orientada a Eventos (Luiz 'Gago' Faria com Eduardo Macris e Otávio Santana)"
aliases: ["eda gago", "arquitetura orientada a eventos podcast"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/arquitetura-orientada-a-eventos-luiz-gago-faria-otavio-santana-eduardo-macris.md
source_url: ""
author: "Luiz Carlos Faria (Gago); apresentadores Eduardo Macris e Otávio Santana"
date_published: ""
date_ingested: 2026-10-08
source_count: 0
tags: [event-driven, eda, acoplamento, mensageria, microsservicos, hype, arquitetura, trade-offs]
skill: tech-mentor-backend
status: draft
---

# Arquitetura Orientada a Eventos (Gago, Macris e Santana)

## TL;DR

EDA existe para **reduzir acoplamento**: quem publica diz *o que aconteceu* (pela própria ótica) e não *o que o outro deve fazer*; comando é acoplamento direto, evento deixa o produtor [[wiki/concepts/evento-vs-comando|dono da informação]]. [[wiki/concepts/mensageria-vs-eda|Mensageria não é EDA]]: broker é só o transporte. O custo é complexidade, rastreabilidade e gestão de versões. Preferir [[wiki/concepts/evento-enxuto-vs-evento-gordo|evento enxuto]] primeiro. Adotar por hype, com banco compartilhado e time imaturo, é fachada sem benefício. A primeira adoção de qualquer tecnologia deve ser num [[wiki/concepts/primeira-adocao-de-tecnologia-com-conforto|caso de uso de baixo risco]].

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| Acoplamento é sempre custo; EDA desacopla ao inverter quem conhece quem | Argumento do convidado | Média-alta: consenso; ver [[wiki/concepts/acoplamento]] |
| Comando = acoplamento direto; evento = produtor dono da informação, relação 1→N ou 1→0 | Explicação do convidado | Alta: coerente com [[wiki/concepts/event-driven-architecture]] |
| Mensageria (fila como mediador) ≠ arquitetura orientada a eventos | Exemplo do webhook que enfileira p/ resiliência | Alta |
| Quatro padrões distintos: transferência de estado, CQRS, notificação de evento (+1 não lembrado) | Citados de memória | Média: provável referência a Fowler `[external não verificado]`; o quarto seria Event Sourcing (inferência) |
| Evento gordo espelha o banco → acoplamento alto e dor de versionamento; enxuto (só IDs) reduz | Experiência do convidado | Média |
| Versionamento de eventos "nunca vi funcionar bem" sem prazo de fim de vida (EOL) obrigatório | Experiência (viu diretoria cair) | Baixa-média: anedota; ver [[wiki/sources/event-versioning]] |
| Evento enxuto + consulta HTTP é resiliente se o consumo vem de fila, e reaproveita gestão de API (quem consome o quê, LGPD) | Argumento do convidado | Média |
| Rastreabilidade/tracing é um custo real de EDA; RabbitMQ não propaga rastreio sozinho | Trecho ASR ambíguo | Baixa para a parte do RabbitMQ |
| Projetos "EDA de fachada" (banco compartilhado, partem do banco, sem domínio) não têm benefício | Experiência | Média |
| Maturidade de pessoas e projeto pesa mais que o porte da empresa | Opinião | Média |

## Entidades

[[wiki/entities/luiz-carlos-faria]] (convidado), [[wiki/entities/eduardo-macris]], [[wiki/entities/otavio-santana]], [[wiki/entities/rabbitmq]].

## Conceitos

[[wiki/concepts/event-driven-architecture]], [[wiki/concepts/evento-vs-comando]], [[wiki/concepts/mensageria-vs-eda]], [[wiki/concepts/evento-enxuto-vs-evento-gordo]], [[wiki/concepts/primeira-adocao-de-tecnologia-com-conforto]], [[wiki/concepts/eda-de-fachada]], [[wiki/concepts/acoplamento]], [[wiki/concepts/mensageria]], [[wiki/concepts/cqrs]], [[wiki/concepts/microsservicos]], [[wiki/concepts/over-engineering]], [[wiki/concepts/avaliar-hype-tecnologico]], [[wiki/concepts/distributed-tracing]], [[wiki/concepts/api-versioning]], [[wiki/concepts/lgpd]], [[wiki/concepts/api-gateway]].

## Contraste com a skill [skill: tech-mentor-backend]

A skill (`architecture-eda-patterns.md`) cobre Outbox, Inbox, Process Manager e Saga, que a fonte **não** menciona; a fonte cobre o lado de *decisão* (quando e por quê). O alerta da skill de que consumo é *at-least-once* e exige idempotência ([[wiki/concepts/idempotencia]]) vale para os consumidores de evento enxuto da fonte. Ver também [[wiki/concepts/outbox-pattern]].

## Perguntas em aberto

- Qual o quarto padrão que o convidado não lembrou? (provável Event Sourcing, [[wiki/concepts/event-sourcing]])
- Como medir "maturidade" do time antes de adotar EDA?
- Quanto o custo de round-trip HTTP de eventos enxutos pesa em escala vs. o ganho de desacoplamento?

## Citações

> "Fulano não manda mensagem para Ciclano. Fulano só disse que aconteceu algo."
> "Comando é acoplamento direto. Quem publica evento é o dono da informação."
> "A primeira adoção tem que ser com o pé nas costas, para que na segunda faça sentido." (opinião declarada como controversa)
