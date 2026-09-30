---
type: concept
title: "Waves de Desenvolvimento"
aliases: ["waves", "ondas de desenvolvimento", "development waves"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [waves, paralelismo, spec-driven-development, agentes, planejamento, pull-request]
skill: tech-mentor-ai
status: draft
---

# Waves de Desenvolvimento

Divisão do projeto (por features ou histórias — critério livre) em **ondas** de trabalho, de modo que as tarefas independentes de uma onda rodem **em paralelo**: gera-se a spec de cada uma (ex.: tarefas 4, 7 e 12), cada uma vira um **pull request** e é autorrevisada por agentes.

## O que ganha (segundo [[wiki/sources/pilares-desenvolvimento-com-ia-contrato-de-revisao-waves]])

1. **Clareza** do que pode ser paralelizado.
2. **Especificação decente** por tarefa ([[wiki/concepts/spec-driven-development]]).
3. **Contrato claro** do que precisa acontecer ([[wiki/concepts/contrato-de-revisao]]).

Resolve o problema de "ficar parado olhando a IA" ([[wiki/concepts/token-anxiety]], [[wiki/concepts/ativo-vs-produtivo]]): o dev orquestra ~10 tarefas sem conversa constante.

## Detalhes

- O plano é em **etapas, não lista de tarefas** — o autor sentia que reduzir a tarefas perdia clareza.
- Execução isolada tipicamente via [[wiki/concepts/worktree-paralelismo]] [inferência; a fonte só cita branches/git].

## Ambiguidade de termo

"Waves" aqui = ondas de **planejamento/execução paralela**. Em [[wiki/sources/agent-waves-custo-modelos-fortes-fracos-kimi]] "Agent Waves" é rebatismo do padrão orquestrador com roteamento de modelos por papel ([[wiki/concepts/subagentes]]). Conceitos relacionados, não idênticos.

## Key sources

- [[wiki/sources/pilares-desenvolvimento-com-ia-contrato-de-revisao-waves]]
