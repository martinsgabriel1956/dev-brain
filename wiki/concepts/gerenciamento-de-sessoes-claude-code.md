---
type: concept
title: "Gerenciamento de Sessões (Claude Code)"
aliases: ["sessões claude code", "claude --resume", "/rename", "/go"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [claude-code, sessoes, contexto, agente-ia, retencao-de-dados]
skill: tech-mentor-ai
status: draft
---

# Gerenciamento de Sessões (Claude Code)

## TL;DR

O [[wiki/entities/claude-code]] salva cada conversa como uma sessão local, com histórico completo e contexto acumulado. Nomear, retomar e administrar essas sessões evita o problema comum de perder todo o raciocínio e as decisões que levaram a um determinado commit no Git.

## O Problema que Resolve

Fluxo comum sem gerenciamento de sessão: o dev chega a um commit no Git, mas todo o contexto que o Claude Code acumulou até ali (decisões, tentativas descartadas, raciocínio) fica preso numa sessão que não é retomada. Se o dev volta depois e só conversa de novo "como se o agente lembrasse de onde pararam", o agente pode não ter esse histórico disponível.

## Mecânica

- Cada nova instância cria uma sessão nova, salva localmente.
- Uma sessão pode ser renomeada para facilitar localização posterior, quando uma tarefa é pausada no meio para ser retomada depois.
- Uma sessão nomeada pode ser retomada mais tarde recuperando o histórico e o contexto completo — diferente de recomeçar do zero a partir de um commit específico no Git.

## `/go` — Objetivo Verificável de Longo Prazo

Quando o objetivo é grande e tem um critério de sucesso verificável automaticamente (ex.: "abra um PR só quando todos os testes passarem", "chegue a zero erros de lint"), um comando dedicado mantém o agente trabalhando em prol desse objetivo sem precisar de reforço manual a cada iteração.

## Retenção Local de Dados

Sessões ficam retidas localmente (por padrão, em `~/.claude/projects`) por um período configurável (30 dias por padrão), com possibilidade de exclusão individual. Isso permite auditar ou reconstruir contexto de trabalhos antigos mesmo depois de encerrada a sessão.

## Relação com Context Compaction

Gerenciar sessões é complementar a [[wiki/concepts/context-compaction]]: a estratégia de "uma tarefa, uma sessão" só funciona bem na prática se for fácil retomar uma sessão pausada mais tarde — caso contrário, o dev tende a empilhar tarefas não relacionadas na mesma sessão só para não perder contexto.

## Key Sources

- [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]]
