---
type: source
title: "Runbook"
aliases: ["Run Book", "Operational Runbook"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_file: /home/nemomartins/Documentos/new/dev-study/raw/runbook.md
source_url: ""
author: "tech-mentor-infra"
date_published: 2026-05-17
date_ingested: 2026-05-17
tags: [infra, ops, runbook, sre]
skill: tech-mentor-infra
status: stable
---

# Runbook

## TL;DR

Runbook é documentação operacional procedural — passos lineares para executar uma operação específica e repetível. A premissa é que a situação já está identificada. Qualquer engenheiro de plantão executa sem depender do autor original.

## Key Claims

- **Passos lineares, sem decisões:** situação identificada, agora é só executar. [[wiki/concepts/runbook]]
- **Estrutura:** Título → Pré-requisitos → Passos numerados (comandos exatos) → Verificação de sucesso → Rollback
- **Vive pré-incidente:** consultado durante deploys, manutenções programadas e operações rotineiras
- **Reduz MTTR em operações conhecidas:** elimina variação humana na execução de sequências longas
- **Requer manutenção:** desatualiza se não houver processo de revisão — runbook desatualizado é pior que não ter runbook
- **Playbook para o resto:** quando a causa não está identificada, use o [[wiki/concepts/playbook]]
- **Post-mortem gera runbooks:** action items de post-mortem frequentemente resultam em novos runbooks. [[wiki/concepts/post-mortem]]

## Concepts

- [[wiki/concepts/runbook]]
- [[wiki/concepts/playbook]]
- [[wiki/concepts/post-mortem]]

## Open Questions

- Como automatizar a validação de que runbooks estão sincronizados com a infraestrutura atual?

## Raw Quotes

> "Um runbook tem passos lineares, sem decisões ramificadas. A premissa é: a situação já está identificada, agora é só executar."
