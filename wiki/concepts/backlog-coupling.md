---
type: concept
title: "Backlog Coupling (Acoplamento de Backlog)"
aliases: ["backlog coupling", "acoplamento de backlog", "dependencia entre times", "cross-team dependency"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [platform-engineering, backlog-coupling, dependencia, times, produtividade, autonomia, conways-law]
skill: tech-mentor-infra
status: draft
---

# Backlog Coupling (Acoplamento de Backlog)

## TL;DR

Termo de [[wiki/entities/evan-bottcher]] ([[wiki/sources/talk-about-platforms-evan-bottcher]]): **acoplamento de backlog** ocorre quando um item de trabalho de um time só avança se um item correspondente for feito **no backlog de outro time**. É o principal destruidor de produtividade que uma [[plataforma-digital]] existe para eliminar.

## O número

Estudo em uma empresa australiana de telecom acompanhou centenas de tarefas: as que dependiam de outro time foram **"10-12x mais lentas em tempo decorrido"** ("10-12x slower in elapsed time") comparadas às concluídas por um único time. (Ordem de grandeza ilustrativa, não benchmark — estudo interno único.)

## Danos além da lentidão

- reduz throughput e resposta ao cliente;
- força planejamento de longo prazo só para administrar dependências;
- corrói a **accountability** do time pelo resultado (dano de motivação);
- estimula terceirização de culpa entre times;
- sobrecarrega os times de serviço compartilhado, que viram gargalo atendendo vários clientes;
- "Agile em escala" muitas vezes troca autonomia/responsividade por alinhamento.

## Antídoto: self-service

A plataforma reduz o acoplamento entregando **self-service real** de provisionamento, configuração e operação. Cuidado com a versão "pela metade" (ver [[sensible-defaults-paved-road]] e a "private cloud superficial" do caso BigCo): dar VM de template fixo sem autoridade de configuração **não** quebra o acoplamento — o ticket continua existindo.

## Relação com a Lei de Conway

O acoplamento de backlog é a Lei de Conway operando contra a entrega: organizar infra por **silo técnico** (DBA, redes, middleware) faz cada mudança atravessar várias fronteiras de time. Ver [[contexto-organizacional-para-arquitetura]] e [[conways-law]].

## Trade-off ao eliminar

Eliminar acoplamento via autonomia total cria o custo oposto — **arrasto por diversificação tecnológica** (cada time reinventa sua stack). O equilíbrio é a plataforma com [[sensible-defaults-paved-road]].

## Key sources

- [[wiki/sources/talk-about-platforms-evan-bottcher]] — Evan Bottcher, *What I Talk About When I Talk About Platforms* (2018)
