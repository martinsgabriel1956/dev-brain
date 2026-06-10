---
type: source
title: "Formação IA para Devs — Aula 02 Parte 2: Rules"
aliases: ["aula 02 rules", "rules formacao ia devs", "guardrails agents.md"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 0
tags: [rules, agents-md, guardrails, harness, system-prompt, code-quality]
skill: tech-mentor-ai
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/Aula 02 - Rules.md
source_url: ""
author: "Pedro Nauke, Rodrigo Branas"
date_published: 2026
date_ingested: 2026-06-02
---

# Formação IA para Devs — Aula 02 Parte 2: Rules

## TL;DR

Rules são arquivos Markdown que definem guardrails de projeto para a LLM — sempre injetados no system prompt. O padrão de mercado é `agents.md` (Anthropic usa `CLAUDE.md`). Depois das skills (novembro), rules devem ser enxutas (<300 linhas), focadas em padrões obrigatórios que SEMPRE devem ser seguidos (folder structure, anti-patterns, commit conventions). Skills substituem rules para tudo que é contextual ou sob demanda.

## Afirmações-chave

| Afirmação | Evidência | Confiança |
|---|---|---|
| Rules são sempre injetadas no system prompt — ocupam contexto mesmo quando irrelevantes | Pedro Nauke | Alta |
| agents.md é o padrão de mercado; Anthropic usa CLAUDE.md (incompatível) | Pedro Nauke, tabela de harnesses | Alta |
| Rule mais enxuta é mais assertiva — peso probabilístico maior por linha | Pedro Nauke | Alta |
| Skills substituíram ~80% do que era colocado em rules | Pedro Nauke | Alta |
| Rules não devem ter regras de negócio — só padrões de código/arquitetura | Pedro Nauke, Rodrigo Branas | Alta |
| Rules devem ser commitadas e compartilhadas no repositório | Pedro Nauke | Alta |
| Simlink para agents.md/CLAUDE.md resolve divergência de harnesses no mesmo time | Pedro Nauke | Alta |
| Rules criadas por engenharia reversa do codebase são um ponto de partida, não verdade | Rodrigo Branas | Alta |

## Padrões de Arquivo por Harness

| Harness | Arquivo de rules |
|---|---|
| Claude Code | `CLAUDE.md` ou `.claude/rules/*.md` |
| Cursor | `.cursor/rules/*.md` ou `agents.md` |
| Codex | `agents.md` (único arquivo) |
| Windsurf | `.windsurf/rules` ou `agents.md` |
| OpenCode | `agents.md` |
| Copilot | `.copilot/instructions` |

> Padrão mais universal: `agents.md`. Anthropic é o outlier com `CLAUDE.md`.

## O Que Vai numa Rule

**Vai:**
- Estrutura de pastas (folder structure)
- Anti-patterns do projeto
- Padrões de commits e PRs
- Convenções de código (arquitetura, responsabilidades por camada)
- Comandos disponíveis no projeto (como startar, rodar testes, lint)
- Restrições absolutas ("nunca rode git restore sem permissão do usuário")

**Não vai:**
- Regras de negócio (valor do PIX, cálculo de desconto) — são immutáveis por definição
- Especificidades de linguagem que a LLM já sabe (como escrever Java)
- Tudo que só aparece em contextos específicos → use skill

## Exemplo de Estrutura Multi-Arquivo (Claude Code)

```
.claude/rules/
  folder-structure.md    ← onde ficam controllers, services, etc.
  anti-patterns.md       ← nunca use workarounds, nunca ignore warnings
  frontend-arch.md       ← componentes React, rotas, animações
  api-standards.md       ← status codes, nesting máximo de URLs
  code-standards.md      ← convenções JS/TS
  tests.md               ← Jest/Vitest, sem mocks desnecessários
  git.md                 ← padrão de commit, PR, mensagem de branch
```

## Demonstração: Antes e Depois com Rules

Mesmo prompt, sem e com rules:

**Sem rules:** 500 linhas em um arquivo único, sem testes, sem separação por camada.

**Com rules:** Estrutura `features/weather/` com `api/`, `components/`, `lib/`, hooks separados, feedback states, forecast chart, limitação de linhas por arquivo, back-end com `controllers/`, `services/`, `data/`.

**Resultado ausente:** testes no back-end — regra de "sempre crie testes" estava na rule mas não era imperativa ("se for fazer, faça assim"). Lição: tornar imperativo no `CLAUDE.md` ("ao finalizar toda feature back-end, crie testes com 80% de coverage").

## Relação Rule → Skill → agents.md

```
agents.md (obrigatório, enxuto, ~250–300 linhas)
  ├── Mapeamento de skills (quando usar qual)
  ├── Restrições absolutas e críticas
  └── Comandos e estrutura base do projeto

.claude/rules/ ou .cursor/rules/
  ├── folder-structure.md    ← global, sempre seguida
  ├── anti-patterns.md       ← global, sempre seguida
  └── [outras rules globais]

.claude/skills/ ou .agents/skills/
  ├── react/                 ← carregada sob demanda
  ├── vitest/                ← carregada sob demanda
  ├── database/              ← carregada sob demanda
  └── [outras skills]
```

## Conceitos Introduzidos

- [[wiki/concepts/rules-agente]] — definição completa do padrão rules
- [[wiki/concepts/system-prompt-arquitetura]] — onde as rules aterrissam
- [[wiki/concepts/context-engineering-harness]] — rules como camada de guias
- [[wiki/concepts/harness]] — o ecossistema completo

## Entidades Mencionadas

- [[wiki/entities/pedro-nauke]] — demonstrou ao vivo, tem regras globais de git restore
- [[wiki/entities/rodrigo-branas]] — definiu "rule é onboarding digital"
- [[wiki/entities/anthropic]] — padrão CLAUDE.md diferente do mercado

## Open Questions

- O `claude /init` mencionado por Rodrigo — gera CLAUDE.md por engenharia reversa do codebase. Verificar output qualidade em projetos grandes.
- Skills.sh foi mencionado como repositório de skills da Vercel — confirmar ownership (Vercel ou terceiros?).
