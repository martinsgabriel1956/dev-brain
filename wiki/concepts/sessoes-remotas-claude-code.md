---
type: concept
title: "Sessões Remotas e Remote Control (Claude Code)"
aliases: ["remote control", "sessão remota"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [claude-code, sessoes, remoto, remote-control]
skill: tech-mentor-ai
status: draft
---

# Sessões Remotas e Remote Control (Claude Code)

## TL;DR

Por padrão as sessões do [[wiki/entities/claude-code]] ficam armazenadas na máquina local (ver [[wiki/concepts/gerenciamento-de-sessoes-claude-code]]). Para refactors grandes ou trabalhos longos há duas opções descritas em [[wiki/sources/claude-code-dicas-worktrees-paralelismo-rotinas-sessoes-remotas-output-estruturado]].

## Duas opções

1. **Sessão na nuvem:** no aplicativo desktop (não na CLI), a partir de "Local" é possível mandar rodar na nuvem; a tarefa segue de forma contínua e disponível "de forma mais global".
2. **Remote Control:** a execução continua na sua máquina, mas você monitora por outro dispositivo (ex.: smartphone fora de casa).

## Ressalva do autor

Nunca usou e não recomenda o hábito de monitorar o agente pelo celular: para ele, estende o trabalho para fora do expediente. É opinião, não parte da documentação.

## Relação

Diferente de [[wiki/concepts/rotinas-agendadas-claude-code]] (disparo por tempo) e de [[wiki/concepts/fork-de-sessao-claude-code]] (bifurcação de contexto). Para longas execuções sem supervisão, ver [[wiki/concepts/agent-containment]].

## Key Sources

- [[wiki/sources/claude-code-dicas-worktrees-paralelismo-rotinas-sessoes-remotas-output-estruturado]]
