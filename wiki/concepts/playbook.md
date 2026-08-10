---
type: concept
title: "Playbook"
aliases: ["Incident Playbook", "Playbook de Incidente"]
date_created: 2026-05-17
date_updated: 2026-08-06
source_count: 2
tags: [infra, ops, incident-response, sre]
skill: tech-mentor-infra
status: stable
---

# Playbook

**TL;DR:** Playbook é documentação operacional com **árvore de decisão** para incidentes com causa desconhecida. Guia a tomada de decisão sob pressão — hipóteses ordenadas por probabilidade, verificações e ações por hipótese.

## O Que É

Documento estratégico e situacional consultado **durante o incidente** quando um alerta dispara e a causa ainda é desconhecida.

## Estrutura Típica

- **Sintoma / Trigger** — qual alerta ou comportamento levou aqui
- **Hipóteses ordenadas por probabilidade** — do mais comum ao mais raro
- **Verificações por hipótese** — como confirmar ou descartar cada causa
- **Ações por hipótese** — o que fazer se a hipótese for verdadeira
- **Escalada** — quando e para quem escalar

## Diferença Playbook vs. Runbook

| | Playbook | Runbook |
|---|---|---|
| **Quando** | Causa desconhecida | Situação identificada |
| **Estrutura** | Árvore de decisão | Passos lineares |
| **Momento** | Durante investigação | Durante execução |

## Quando Usar / Evitar

**Usar:** alerta disparou com causa desconhecida, múltiplas causas possíveis com passos diferentes, onboarding de novos engenheiros em resposta a incidentes.

**Evitar:** operação bem definida sem decisões → use [[runbook]].

## Playbook como System Prompt de Agente

[[wiki/sources/oracle-demite-milhares-anatomia-agente-dba-autonomo]] usa "playbook" num sentido próximo mas distinto do incident playbook acima: o system prompt de um [[wiki/concepts/agente-ia|agente autônomo]] (ex.: um "playbook de DBA") — o conhecimento operacional e as regras de decisão de um domínio, compactado para orientar o **LLM Planner** do agente, em vez de um humano seguindo uma árvore de decisão durante um incidente.

## Key Sources

- [[wiki/sources/playbook]]
- [[wiki/sources/oracle-demite-milhares-anatomia-agente-dba-autonomo]] — playbook como conteúdo do system prompt de um agente autônomo

## Conceitos Relacionados

[[runbook]] · [[post-mortem]]
