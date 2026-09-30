---
type: concept
title: "Rotinas Agendadas (Claude Code)"
aliases: ["routines", "/loop", "schedule claude code"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [claude-code, agendamento, automacao, cron, routines]
skill: tech-mentor-ai
status: draft
---

# Rotinas Agendadas (Claude Code)

## TL;DR

Formas de fazer o [[wiki/entities/claude-code]] executar tarefas de forma recorrente, sem intervenção: `/loop` no computador local e **rotinas** (routines) na nuvem da [[wiki/entities/anthropic]], criadas pela CLI (schedule) ou pela web em `/code/routines`.

## Como é descrito na fonte

- **Local:** `/loop` mantém algo rodando na sua máquina.
- **Nuvem:** agenda-se uma tarefa (ex.: "a cada uma hora, rode os testes") que a Anthropic executa; na web, conecta-se o GitHub ou o que a tarefa exigir.
- **Casos de uso:** health check da API com alerta em caso de erro; revisar os pull requests abertos. Analogia do autor: cron job.

## Relação com outros conceitos

- É a forma mais simples de [[wiki/concepts/loop-engineering]] com gatilho por tempo, em vez de gatilho por resultado.
- Tarefas na nuvem não dependem da máquina ligada, ao contrário do Remote Control de [[wiki/concepts/sessoes-remotas-claude-code]].
- Loops longos e sem supervisão pedem contenção: ver [[wiki/concepts/agent-containment]].

## Verificação pendente

Sintaxe de `/loop`, caminho `/code/routines`, limites de frequência e custo não foram verificados; vêm da fala do autor.

## Key Sources

- [[wiki/sources/claude-code-dicas-worktrees-paralelismo-rotinas-sessoes-remotas-output-estruturado]]
