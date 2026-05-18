---
type: source
title: "Playbook"
aliases: ["Playbook de Incidente", "Incident Playbook"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_file: /home/nemomartins/Documentos/new/dev-study/raw/playbook.md
source_url: ""
author: "tech-mentor-infra"
date_published: 2026-05-17
date_ingested: 2026-05-17
tags: [infra, ops, incident-response, playbook, sre]
skill: tech-mentor-infra
status: stable
---

# Playbook

## TL;DR

Playbook é um documento estratégico e situacional com **árvores de decisão** para responder a incidentes com causa desconhecida. Diferente do runbook (passos lineares, situação identificada), o playbook guia a **tomada de decisão sob pressão** — hipóteses ordenadas por probabilidade, verificações por hipótese, ações e critérios de escalada.

## Key Claims

- **Árvore de decisão, não passos lineares:** a premissa é "algo deu errado, descubra o quê". [[wiki/concepts/playbook]]
- **Estrutura:** Sintoma/Trigger → Hipóteses por probabilidade → Verificações por hipótese → Ações → Escalada
- **Vive durante o incidente:** consultado quando alerta dispara e causa ainda é desconhecida
- **Runbook cobre o depois:** situação identificada → passos lineares. [[wiki/concepts/runbook]]
- **Post-mortem cobre o depois:** análise retrospectiva após resolução. [[wiki/concepts/post-mortem]]
- **Reduz cognitive load em stress** mas pode dar falsa sensação de cobertura total — situações novas exigem improviso

## Concepts

- [[wiki/concepts/playbook]]
- [[wiki/concepts/runbook]]
- [[wiki/concepts/post-mortem]]

## Open Questions

- Como manter playbooks atualizados sem processo explícito de revisão após cada incidente?

## Raw Quotes

> "Um playbook tem árvores de decisão, não passos lineares. A premissa é: algo deu errado, agora preciso descobrir o quê e agir."
