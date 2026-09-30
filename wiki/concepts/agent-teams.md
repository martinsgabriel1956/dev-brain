---
type: concept
title: "Agent Teams (Claude Code)"
aliases: ["times de agentes", "agent teams"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [claude-code, agent-teams, orquestracao, experimental]
skill: tech-mentor-ai
status: draft
---

# Agent Teams (Claude Code)

## TL;DR

Recurso **experimental** do [[wiki/entities/claude-code]] em que o Claude planeja e supervisiona um grupo de sessões de trabalho que podem interagir entre si. Diferente de [[wiki/concepts/subagentes]], que delegam e devolvem resultado dentro de uma única conversa. Ver o quadro comparativo em [[wiki/concepts/modalidades-de-paralelismo-claude-code]].

## Regra de ouro: sem arquivos em comum

A recomendação atribuída à documentação é quebrar o trabalho para que **dois colegas do time não toquem os mesmos arquivos**. Se A trabalha numa feature e B em outra (ou em partes de ambas) e há um arquivo compartilhado, um pode sobrescrever o outro. Combina com isolamento por [[wiki/concepts/worktree-paralelismo]].

## Custo

Cada membro consome tokens; o custo cresce aproximadamente com o número de sessões. Ver [[wiki/concepts/modalidades-de-paralelismo-claude-code]].

## Verificação pendente

Nesta fonte o recurso é descrito só de forma oral e como experimental; comportamento e sintaxe não foram checados na documentação.

## Key Sources

- [[wiki/sources/claude-code-dicas-worktrees-paralelismo-rotinas-sessoes-remotas-output-estruturado]]
