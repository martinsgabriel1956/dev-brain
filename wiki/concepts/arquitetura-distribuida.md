---
type: concept
title: "Arquitetura Distribuída"
aliases: ["distributed architecture", "sistema distribuído", "arquiteturas distribuídas"]
date_created: 2026-10-02
date_updated: 2026-10-07
source_count: 2
tags: [arquitetura-distribuida, sistemas-distribuidos, arquitetura, microsservicos, escalabilidade, resiliencia]
skill: tech-mentor-system-design
status: draft
---

# Arquitetura Distribuída

Sistema composto por múltiplos serviços ou componentes **tecnicamente independentes** que se comunicam entre si, normalmente pela rede ou internet. Oposto do [[wiki/concepts/monolito]], em que todos os módulos vivem no mesmo entregável; aqui os componentes podem ter implantações separadas, e a divisão pode ser técnica ou de negócio, conforme o estilo ([[wiki/concepts/microsservicos]], [[wiki/concepts/cqrs]], [[wiki/concepts/event-driven-architecture]], [[wiki/concepts/soa-service-oriented-architecture]]).

## Por que adotar (segundo Bernardo Lobato)

[[wiki/concepts/escalabilidade-independente]]; resiliência ([[wiki/concepts/tolerancia-a-falha]]: falha pontual não derruba tudo); flexibilidade tecnológica (stack por serviço); equipes independentes (deploy e entrega mais rápidos, escopo menor); menor [[wiki/concepts/acoplamento]]. Sinais de aderência: alta escala com múltiplas equipes, partes que crescem em ritmos diferentes, muitas integrações externas.

## Desafios

Complexidade operacional (monitorar e versionar vários serviços); [[wiki/concepts/observabilidade]] (tracing, logs, métricas; debug vira disciplina à parte); comunicação ([[wiki/concepts/comunicacao-sincrona]] vs. [[wiki/concepts/comunicacao-assincrona]]; falhas de rede, latência — ver [[wiki/concepts/falacias-da-computacao-distribuida]]); consistência de dados ([[wiki/concepts/eventual-consistency]]); custo de infraestrutura e integração; capacitação do time.

## Histórico resumido (aproximado, segundo o vídeo)

Anos 70–80: Arpanet e pesquisa acadêmica/militar → anos 90: [[wiki/concepts/arquitetura-cliente-servidor]] e internet comercial → início dos 2000: Google, Amazon, Yahoo exigem escala → meados dos 2000: [[wiki/concepts/soa-service-oriented-architecture]] → anos 2010: microsserviços e nuvem ([[wiki/concepts/cloud-como-modelo-de-consumo]]).

## Cuidado: motivo errado

Adoção por hype ou imitação ("a Netflix usa") é [[wiki/concepts/cargo-cult-tecnologico]]; mal feita vira [[wiki/concepts/distributed-monolith]]. Não é bala de prata ([[wiki/concepts/sem-balas-de-prata]]). Alternativa: [[wiki/concepts/desenhar-distribuido-implementar-monolito]] / [[wiki/concepts/monolith-first]].

## Key sources

- [[wiki/sources/arquitetura-distribuida-introducao-historico-desafios-bernardo-lobato]] — introdução da série de arquiteturas distribuídas de [[wiki/entities/bernardo-lobato]]

- [[wiki/sources/decisoes-de-arquitetura-tradeoffs-e-contexto-bernardo-lobato]] — custos da distribuição (rede, latência, observabilidade, consistência, timeouts/retries, transações distribuídas) como lado "pago" do trade-off; nem todo gargalo pede distribuir.
