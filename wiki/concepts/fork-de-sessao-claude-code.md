---
type: concept
title: "Fork de Sessão (Claude Code)"
aliases: ["/fork", "fork de conversa"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [claude-code, sessoes, fork, subagentes, contexto]
skill: tech-mentor-ai
status: draft
---

# Fork de Sessão (Claude Code)

## TL;DR

`/fork` cria uma **nova sessão com cópia exata da sessão atual**; retorna o ID e executa o pedido feito na sessão forkeada num subagente, enquanto a sessão original permanece intacta ([[wiki/sources/claude-code-dicas-worktrees-paralelismo-rotinas-sessoes-remotas-output-estruturado]]).

## Quando usar

Num refactor em que não se sabe qual caminho gera o melhor código: bifurca-se, explora-se os dois e descarta-se ou mantém-se um. O autor compara sessões a branches/commits do Git.

## Comparações

- **vs. [[wiki/concepts/rewind-checkpoints-claude-code]]:** o rewind volta para um ponto anterior da mesma conversa; o fork mantém os dois caminhos vivos.
- **vs. [[wiki/concepts/subagentes]]:** o fork herda o contexto completo da conversa; ver a seção "Fork vs. Subagent" nessa página. Segundo a fonte, o fork spawna um subagente.
- **vs. [[wiki/concepts/worktree-paralelismo]]:** o fork bifurca o *contexto*; a worktree isola os *arquivos*. Para dois caminhos que editam código, tende a ser necessário combinar ambos (inferência, não afirmado na fonte).

## Verificação pendente

Sintaxe e semântica exatas do `/fork` não foram checadas na documentação.

## Key Sources

- [[wiki/sources/claude-code-dicas-worktrees-paralelismo-rotinas-sessoes-remotas-output-estruturado]]
