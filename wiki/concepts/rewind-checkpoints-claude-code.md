---
type: concept
title: "Checkpoints e Rewind (Claude Code)"
aliases: ["rewind", "checkpoints claude code", "/rewind"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [claude-code, checkpoints, rewind, versionamento, agente-ia]
skill: tech-mentor-ai
status: draft
---

# Checkpoints e Rewind (Claude Code)

## TL;DR

Mecanismo do [[wiki/entities/claude-code]] que salva pontos de restauração ao longo de uma conversa, permitindo voltar (`rewind`) a um estado anterior do código e/ou do histórico de mensagens sem descartar a sessão inteira.

## Por Que Não Basta o Git

O Git permite reverter para um commit específico, mas commits marcam pontos discretos escolhidos pelo dev — não todo prompt intermediário vira um commit. Se uma conversa foi bem até a metade e degradou depois (o agente "perdeu o rumo"), o rewind permite voltar exatamente para esse meio-termo, preservando o que deu certo sem precisar reconstruir manualmente o estado a partir do último commit.

## Quando Usar

- Uma sequência de prompts levou o código a um estado pior do que o anterior e não há commit intermediário no ponto certo.
- Quer testar um caminho alternativo a partir de um ponto específico da conversa sem perder a ramificação anterior.

## Relação com Git

Complementar, não substituto: commits continuam sendo a forma durável de versionar o código entre sessões. O rewind atua dentro do ciclo de vida de uma única conversa/sessão.

## Key Sources

- [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]]
