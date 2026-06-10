---
type: source
title: "Formação IA para Devs — Aula 01 Parte 2: Context e Harness Engineering"
aliases: ["aula 01 context harness", "context harness engineering formacao"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 0
tags: [harness, context-engineering, agentic-loop, system-prompt, rules, skills, mcp, memoria-ia]
skill: tech-mentor-ai
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/Aula 01 - Context e Harness Engineering.md
source_url: ""
author: "Rodrigo Branas, Pedro Nauke"
date_published: 2026
date_ingested: 2026-06-02
---

# Formação IA para Devs — Aula 01 Parte 2: Context e Harness Engineering

## TL;DR

O harness tem duas camadas: a do provider (Claude Code, Cursor, Codex) e a **sua** (rules, skills, MCPs, sensores). A diferença entre resultado medíocre e excelente está na qualidade dos **guias** (rules, skills) e dos **sensores** (testes, linter, banco, browser) que você fornece. A LLM orquestra; o harness executa. O ciclo agentico é um brute-force até funcionar — a qualidade dos sensores reduz as iterações.

## Afirmações-chave

| Afirmação | Evidência | Confiança |
|---|---|---|
| LLM é stateless — sem harness só traduz texto ou faz poesia | Rodrigo Branas, diagrama ao vivo | Alta |
| User harness = guias + sensores; qualidade dos sensores determina autocorreção | Pedro Nauke, arquitetura desenhada ao vivo | Alta |
| System prompt = tudo que entra no contexto sem o usuário ver (rules, skills, MCPs, schemas de tools) | Pedro Nauke | Alta |
| Short-term memory = context window (apagada); long-term memory = rules/skills/MCPs (sempre injetadas) | Pedro Nauke | Alta |
| O loop agentico é brute-force: LLM pede, harness executa, repete até funcionar ou desistir | Rodrigo Branas | Alta |
| Código fonte do Claude Code vazou — era código ruim (macarrão TypeScript) mas cheio de features criativas (Dream Consolidation, scheduler) | Pedro Nauke, que leu o código | Média |

## Arquitetura do Harness (System Design)

```
┌─────────────────────────────────────────────┐
│              CONTEXT WINDOW                  │
│  ┌─────────────────────────────────────────┐ │
│  │ SYSTEM PROMPT (vermelho)                │ │
│  │  • Tools registradas (read_file, bash…) │ │
│  │  • Rules (anti-patterns, folder struct) │ │
│  │  • Skills (front-matter apenas)         │ │
│  │  • MCPs registrados                     │ │
│  └─────────────────────────────────────────┘ │
│  ┌─────────────────────────────────────────┐ │
│  │ CONVERSA ACUMULADA (user + assistant)   │ │
│  │  • User prompt                          │ │
│  │  • Tool calls (amarelo)                 │ │
│  │  • Tool returns (verde)                 │ │
│  │  • Respostas da LLM                     │ │
│  └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
            ↑                  ↓
       [Usuário]            [LLM]
            ↑                  ↓
       [Harness]         [Executa tools]
         (fs, bash, browser, db, MCPs)
```

## Guias vs Sensores

**Guias** antecipam o comportamento e direcionam ação:
- Code standards, estrutura de pastas, blueprints de arquitetura, anti-patterns
- Implementados via rules e skills

**Sensores** fornecem feedback para autocorreção:
- Testes (unitários, E2E), linter, compilador, browser, banco de dados, LLM de revisão de código
- Cada sensor adicional reduz iterações do loop agentico

> "Qualidade dos seus sensores faz a diferença no resultado." — Rodrigo Branas

## Memória Curto vs Longo Prazo

| Tipo | Onde vive | Apagada? |
|---|---|---|
| Short-term | Context window (conversa atual) | Sim — limpa ao encerrar tarefa |
| Long-term | System prompt (rules, skills, MCPs, schemas) | Não — sempre reinjetada |

Conversas antigas ficam armazenadas pelo harness e podem ser indexadas para injetar no system prompt futuro (ex: Dream Consolidation do Claude Code) — requer configuração explícita.

## Exemplo Passo a Passo: "Corrigir bug no hello world.js"

```
User:      "No arquivo hello world, tem um bug. Pode corrigir?"
Assistant: Tool call → read_dir (descobre hello world.js)
Harness:   → [hello world.js, package.json]
Assistant: Tool call → read_file hello world.js
Harness:   → const msg = "hello world"; console.log(message);
Assistant: Tool call → write_file hello world.js (msg → message)
Harness:   → ok
Assistant: Tool call → bash execute (node hello world.js)
Harness:   → "hello world"
Assistant: "Arquivo corrigido. Variável message estava sem declaração."
```

5 ciclos para 1 bug simples. Com contexto ruim: potencialmente o dobro ou mais.

## Conceitos Introduzidos

- [[wiki/concepts/system-prompt-arquitetura]] — o prompt escondido que vem antes do seu
- [[wiki/concepts/sensores-vs-guias]] — a dicotomia central do user harness
- [[wiki/concepts/memoria-curto-longo-prazo-ia]] — short vs long term no contexto agêntico
- [[wiki/concepts/harness]] — definição completa
- [[wiki/concepts/ciclo-agente]] — o loop agentico com tool calls
- [[wiki/concepts/tool-call]] — como a LLM invoca ações externas
- [[wiki/concepts/degradacao-de-contexto]] — o que acontece quando a janela enche
- [[wiki/concepts/context-engineering-harness]] — rules + skills + MCPs como guias

## Entidades Mencionadas

- [[wiki/entities/rodrigo-branas]] — instrutor, arquitetura desenhada ao vivo
- [[wiki/entities/pedro-nauke]] — instrutor, leu o código-fonte do Claude Code vazado
- [[wiki/entities/anthropic]] — criou Claude Code; sistema de Dream Consolidation
- [[wiki/entities/codex-openai]] — mencionado como harness alternativo

## Open Questions

- O Dream Consolidation mencionado por Pedro é o mesmo "memory consolidation" descrito na documentação pública do Claude? Confirmar.
- A afirmação "LLM desiste quando a situação está ruim demais" tem um limite configurável? Qual o default?
