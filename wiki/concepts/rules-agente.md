---
type: concept
title: "Rules (Padrão de Harness)"
aliases: ["rules harness", "agents.md", "cursorrules", "guardrails ia", "regras agente"]
date_created: 2026-06-02
date_updated: 2026-07-07
source_count: 3
tags: [rules, agents-md, harness, system-prompt, guardrails, code-quality, projetos-novos]
skill: tech-mentor-ai
status: stable
---

# Rules (Padrão de Harness)

Arquivos Markdown que definem **guardrails e padrões obrigatórios** de um projeto para a LLM. Sempre injetados integralmente no system prompt — presentes em toda interação, independente da tarefa.

## Padrão de Arquivo por Harness

| Harness | Arquivo(s) de rules |
|---|---|
| Claude Code | `CLAUDE.md` ou `.claude/rules/*.md` |
| Cursor | `.cursor/rules/*.md` ou `agents.md` |
| Codex | `agents.md` (único arquivo) |
| Windsurf | `.windsurf/rules` ou `agents.md` |
| OpenCode | `agents.md` |
| Copilot | `.copilot/instructions` |

Padrão universal: `agents.md`. Anthropic é o outlier com `CLAUDE.md`.

**Simlink:** para times com harnesses diferentes, crie um arquivo único e crie symlinks para os outros. Ex: `ln -s CLAUDE.md agents.md`.

## O Que Vai numa Rule

**Vai:**
- Estrutura de pastas (onde ficam controllers, services, etc.)
- Anti-patterns proibidos do projeto
- Padrão de commits, PRs e branches
- Comandos do projeto (como startar, rodar testes, lint)
- Restrições absolutas ("nunca rode git restore sem permissão")
- Mapeamento de skills disponíveis

**Não vai:**
- Regras de negócio (calculadora de desconto, valor do PIX)
- Conhecimento que a LLM já tem (como escrever Java)
- Conteúdo contextual (regras específicas de front-end quando a task é back-end) → use skills

## O Problema de Rules Excessivas

Rules são injetadas **inteiras** no system prompt — mesmo quando irrelevantes para a tarefa. Isso cria dois problemas:

1. **Custo constante:** cada token de rule = custo em toda interação
2. **Diluição probabilística:** 5.000 linhas de rule diluem o peso de cada instrução. Uma linha `use red color` entre 5.000 linhas tem peso muito menor.

**Solução:** Após novembro (padrão skills), manter rules enxutas (<300 linhas) e mover conteúdo contextual para skills.

## Diferença de Skills

| Critério | Rule | Skill |
|---|---|---|
| Carregamento | Sempre, inteira, no system prompt | Só front-matter; corpo sob demanda |
| Propósito | Enforçar comportamento obrigatório | Fornecer know-how para tarefa específica |
| Escopo | Sempre global | Contextual / sob demanda |
| Tamanho ideal | < 300 linhas totais | Sem limite prático |
| Exemplo | "Nunca comite segredos no git" | "Como criar um componente React" |

**Regra prática:** se a rule só faz sentido em alguns contextos → vira skill. Se deve SEMPRE ser seguida → continua rule.

## Rules vs Onboarding

> "Rule é o onboarding digital do projeto. O que você falaria para um funcionário novo nos primeiros dias?" — Rodrigo Branas

Rules são a formalização em Markdown do conhecimento que a LLM não tem sobre **seu** projeto: seu padrão de arquitetura, suas convenções, sua cultura de código.

## AGENTS.md como Etapa do Setup Inicial de Projeto

No [[wiki/concepts/checklist-primeiro-dia-projeto]], escrever o `AGENTS.md` é a última etapa do dia 1, junto com o README (para humanos). O conteúdo recomendado é concreto: como rodar os testes, se o projeto segue TDD, quais os padrões de tipagem, qual a arquitetura e estrutura dos repositórios/serviços, e qual o objetivo explícito do projeto — na prática, uma aplicação direta de "o que vai numa rule" acima, só que documentada desde antes de existir qualquer feature.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-02-rules]]
- [[wiki/sources/formacao-ia-devs-aula-03-skills]]
- [[wiki/sources/5-ou-6-dicas-para-projetos-novos]]
