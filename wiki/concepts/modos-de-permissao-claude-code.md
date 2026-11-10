---
type: concept
title: "Modos de Permissão do Claude Code"
aliases: ["permission modes", "acceptEdits", "dontAsk", "bypassPermissions", "auto mode claude code"]
date_created: 2026-11-10
date_updated: 2026-11-10
source_count: 1
tags: [claude-code, harness, permissoes, agentes-ia, seguranca]
skill: tech-mentor-ai
status: draft
---

# Modos de Permissão do Claude Code

## TL;DR

O modo de permissão define o que o [[wiki/concepts/harness|harness]] deixa o agente fazer sem perguntar. É uma trava aplicada pelo harness antes de cada ação, não uma instrução ao modelo.

## Os Seis Modos

Descrição segundo [[wiki/sources/claude-code-tudo-que-precisa-saber-harness-comandos-contexto]], conferida na [documentação oficial](https://code.claude.com/docs/en/permission-modes.md) `[external]`.

| Modo | O que libera | Uso sugerido pela fonte |
|---|---|---|
| Default | Só leitura; pergunta o resto | Pouco prático: pergunta o tempo todo |
| Accept Edits | Edições no diretório de trabalho e comandos comuns de arquivo (`mkdir`, `mv`, `cp`...) | Passo claro e repetitivo |
| [[wiki/concepts/plan-mode\|Plan]] | Só leitura até aprovar o plano | Código que você não conhece |
| Auto | Tudo, com um modelo classificador revisando cada ação | Dia a dia; automação com `-p` |
| Don't Ask | Só ferramentas pré-aprovadas; nega o resto em silêncio | CI, com `allowed tools` |
| Bypass Permissions | Tudo, sem checagem | Só em contêiner ou VM descartável |

Ressalvas da documentação `[external]`: o Auto é padrão em todos os planos nas versões recentes, e a restrição do Bypass a ambientes isolados é orientação, embora o Claude Code recuse iniciar nesse modo como root sem sandbox.

## Risco

Nenhum modo elimina [[wiki/concepts/prompt-injection]]: conteúdo hostil em arquivo ou site pode instruir o agente. Isolar o processo é o tema de [[wiki/concepts/agent-containment]].

## Relações

- [[wiki/entities/claude-code]]
- [[wiki/concepts/hooks-agente]]: bloqueio determinístico além dos modos.
- [[wiki/concepts/human-in-the-loop]]

## Key Sources

- [[wiki/sources/claude-code-tudo-que-precisa-saber-harness-comandos-contexto]]
