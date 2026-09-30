---
type: concept
title: "Checkpoints e Rewind (Claude Code)"
aliases: ["rewind", "checkpoints claude code", "/rewind"]
date_created: 2026-07-21
date_updated: 2026-09-30
source_count: 2
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

## Rewind vs. Fork

O rewind volta a um ponto anterior da **mesma** conversa; o [[wiki/concepts/fork-de-sessao-claude-code]] mantém dois caminhos vivos a partir de um ponto, sem descartar nenhum.

## Key Sources

- [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]]
- [[wiki/sources/claude-code-dicas-worktrees-paralelismo-rotinas-sessoes-remotas-output-estruturado]] — contraste rewind x fork
