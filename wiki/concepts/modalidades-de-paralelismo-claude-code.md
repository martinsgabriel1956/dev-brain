---
type: concept
title: "Modalidades de Paralelismo no Claude Code"
aliases: ["formas de paralelizar claude code"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [claude-code, paralelismo, subagentes, agent-teams, custo]
skill: tech-mentor-ai
status: draft
---

# Modalidades de Paralelismo no Claude Code

## TL;DR

O [[wiki/entities/claude-code]] oferece cinco formas de paralelizar trabalho, cada uma com um objetivo próprio segundo a documentação da [[wiki/entities/anthropic]] (relatadas em [[wiki/sources/claude-code-dicas-worktrees-paralelismo-rotinas-sessoes-remotas-output-estruturado]]).

## As cinco formas

| Forma | Como funciona | Quando usar |
|---|---|---|
| **Vários terminais** | Abrir a CLI em dois ou mais terminais; cada uma age de forma independente | Tarefas sem relação; combinar com [[wiki/concepts/worktree-paralelismo]] se tocam o mesmo repo |
| **Subagentes** | Dentro de uma sessão, o Claude delega e coleta resultados na mesma conversa | Ver [[wiki/concepts/subagentes]] |
| **Agents View** | Você entrega tarefas individuais e visualiza os resultados depois | Trabalho de fundo por tarefa |
| **Agent Teams** | O Claude planeja e supervisiona um grupo de trabalhadores (sessões que interagem entre si); **experimental** | Ver [[wiki/concepts/agent-teams]] |
| **Workflow customizado** | Um script com o plano de um fluxo de trabalho | Processos repetíveis |

## Custos e limites (segundo a fonte)

- **Custo:** rodar em paralelo produz ~duas vezes mais tokens e custa ~duas vezes mais. É estimativa qualitativa do autor, sem medição.
- **Atenção:** você continua sendo uma pessoa; há um teto do quanto consegue acompanhar. Ver [[wiki/concepts/paralelismo-de-tarefas-ia]].
- **Colisão de arquivos:** dividir o trabalho para que dois trabalhadores não editem o mesmo arquivo.

## Nota de nomenclatura

O nome "Agents View" e o comportamento de "workflows dinâmicos" vêm só da fala do autor; não verificados contra a documentação atual.

## Key Sources

- [[wiki/sources/claude-code-dicas-worktrees-paralelismo-rotinas-sessoes-remotas-output-estruturado]]
