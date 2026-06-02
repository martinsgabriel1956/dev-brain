---
type: source
title: "Formação IA para Devs — Aula 03 Parte 2: Skills"
aliases: ["aula 03 skills", "skills formacao ia devs", "skills pattern agents"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 0
tags: [skills, agents-skills, harness, context-engineering, lazy-loading, design-md]
skill: tech-mentor-ai
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/Aula 03 - Skills.md
source_url: ""
author: "Pedro Nauke, Rodrigo Branas"
date_published: 2026
date_ingested: 2026-06-02
---

# Formação IA para Devs — Aula 03 Parte 2: Skills

## TL;DR

Skills são pastas (não arquivos únicos) com `SKILL.md` obrigatório — o padrão nasceu na Anthropic em novembro. A grande sacada: só o **front-matter** (nome + descrição) é injetado no system prompt; o corpo é carregado **sob demanda** por tool call. Isso elimina o problema das rules que entulhavam o system prompt. Todos os harnesses implementaram o padrão da mesma forma (exceto Anthropic, que usa `.claude/skills/` em vez de `.agents/skills/`). `skills.sh` é o diretório público com ~100k skills instaláveis via `npx skills add`.

## Afirmações-chave

| Afirmação | Evidência | Confiança |
|---|---|---|
| Skill = pasta com SKILL.md obrigatório; outros arquivos são opcionais (templates, scripts, references) | Pedro Nauke | Alta |
| Só o front-matter entra no system prompt; corpo é lazy-loaded por tool call | Pedro Nauke | Alta |
| Skills são self-contained — podem ser zipadas e compartilhadas | Pedro Nauke | Alta |
| Todos os harnesses implementaram o padrão igual (exceto Anthropic: `.claude/skills/`) | Pedro Nauke | Alta |
| Modelos não carregam skills automaticamente bem — melhor referenciar no prompt ou mapear no agents.md | Pedro Nauke | Alta |
| Skill pode conter scripts executáveis — risco de código malicioso via skills de terceiros | Pedro Nauke (aviso) | Alta |
| Skills substituíram ~80% das rules | Pedro Nauke | Alta |
| Composer 2 é modelo exclusivo do cursor baseado em Kimi K2.5 rodando em infraestrutura Cerebras | Pedro Nauke | Média |

## Estrutura de uma Skill

```
.claude/skills/           (Anthropic)
.agents/skills/           (todos os outros)
  react/
    SKILL.md              ← obrigatório (front-matter + body)
    references/
      component-guide.md
    templates/
      component.tsx.tmpl
    scripts/
      generate.sh
```

### Front-matter da SKILL.md

```yaml
---
name: react
description: "Boas práticas para componentes React com TypeScript — arquitetura, hooks, performance"
version: 1.0.0
---

[corpo da skill — carregado sob demanda]
```

## Ciclo de Carregamento da Skill

```
Nível 1 (sempre no system prompt):
  name + description do front-matter

Nível 2 (carregado sob demanda via tool call):
  corpo da SKILL.md (instruções completas)

Nível 3 (carregado quando referenciado no corpo):
  references/, templates/, scripts/
```

## Skills vs Rules

| Critério | Rule | Skill |
|---|---|---|
| Propósito | Enforçar comportamento obrigatório | Fornecer know-how para concluir tarefa |
| Tipo | Prescritiva (sempre faça X, nunca Y) | Descritiva (como fazer Z) |
| Carregamento | Sempre no system prompt (inteira) | Só front-matter no system prompt; corpo sob demanda |
| Escopo | Condição estreita e constante | Domínio amplo e workflow |
| Exemplo | "Nunca comite segredos no git" | "Como desenhar uma Pay Rush" |
| Quando usar | Regras globais que SEMPRE valem | Contextos específicos e processos |

**Agents.md deve ter <300 linhas.** Tudo além disso vira skill.

## skills.sh — Diretório Público

- ~100k skills disponíveis
- Instalação: `npx skills add <owner>/<repo>`
- CLI lista e instala para múltiplos harnesses simultaneamente
- Repositório do Pedro Nauke: `github.com/pedronok/skills` — skills auditadas com estrelinhas

**Skills destacadas por Pedro:**
- `qa-report` + `qa-execution` — gera report estruturado de QA e executa via Playwright; resultado "absurdo"
- `create-slide` — criação de slides com padrão visual consistente
- `uiux-promax` — design opinado com animações
- `skill-best-practices` — usa IA para criar skills bem estruturadas

## Design.md — Padrão Google

Novo padrão (2026) criado pelo Google: arquivo `.md` com spec completa de design (tokens, fontes, cores, animações) que a LLM usa para gerar UIs consistentes.

- Site: `getdesign.md`
- Comandos: `npx get-design <marca>` (ex: Ferrari, Apple, BMW, Airbnb)
- Gera `design.md` que a skill de design interpreta

Exemplo ao vivo: `npx get-design ferrari` → aplicado ao weather app → resultado com cores/fontes Ferrari.

Ver [[wiki/concepts/design-md-padrao]].

## Como Referenciar Skills

**No prompt:** `Use /react /vitest` (Claude Code) ou `$react $vitest` (Codex)

**No agents.md (mapeamento):**
```
Quando criar componente React: use skill react
Quando escrever testes: use skill vitest
Quando trabalhar com TypeScript: use skill code-standards
```

Ambas as formas + mapeamento = máxima garantia de carregamento.

## Conceitos Introduzidos

- [[wiki/concepts/skills-agente]] — definição completa do padrão skills
- [[wiki/concepts/rules-agente]] — comparação e quando usar cada um
- [[wiki/concepts/design-md-padrao]] — padrão Google para spec de design
- [[wiki/concepts/context-engineering-harness]] — skills como camada de guias
- [[wiki/concepts/system-prompt-arquitetura]] — onde o front-matter das skills aterra

## Entidades Mencionadas

- [[wiki/entities/pedro-nauke]] — demonstrou criação e instalação de skills ao vivo; tem repositório próprio
- [[wiki/entities/rodrigo-branas]] — testou a skill de design nos slides da formação
- [[wiki/entities/anthropic]] — criou o padrão skills (novembro); é o outlier com `.claude/skills/`

## Open Questions

- O site `skills.sh` é mantido pela Vercel ou é independente? Pedro mencionou "foi feito pela Versal" — verificar.
- Harnesses mais novos (Hermes, Open Call) que criam skills automaticamente baseado em conversas — quais são os critérios de criação automática?
