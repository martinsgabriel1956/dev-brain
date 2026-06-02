---
type: source
title: "Formação IA para Devs — Aula 04: Harness"
aliases: ["IA para Devs Aula 4", "Harness Branas Nauke"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 0
tags: [ia-para-devs, harness, tool-call, agente, context-engineering, mcp, precificacao]
skill: tech-mentor-ai
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/Aula 04 - Harness.md"
source_url: ""
author: "Rodrigo Branas, Pedro Nauke"
date_published: "2026"
date_ingested: 2026-06-02
---

# Formação IA para Devs — Aula 04: Harness

## TL;DR

Conceito central: harness é tudo que envolve o modelo LLM — gerenciamento de contexto, tool calls, memória, subagentes, MCP, system prompt. A LLM sozinha é stateless e cega; o harness dá a ela "olhos e mãos". Um prompt pode disparar 40+ ciclos de tool call. A diferença de produtividade vem majoritariamente da qualidade do contexto fornecido, não do harness ou modelo escolhido.

## Key Claims

- **Harness = tudo ao redor do LLM**: context window management, tool calls, memória, subagentes, MCP, system prompt, cache. O modelo em si é só um endpoint stateless. Evidência: demo com chamada raw via curl vs uso pelo Claude Code.
- **Tool calls (2023, OpenAI)** = game changer que deu "olhos" ao modelo. Antes, o modelo não conseguia nem ler um arquivo sem que você mandasse o conteúdo. Evidência: Branas demonstra que sem tools o modelo responde "não consigo acessar seu sistema de arquivos".
- **A LLM apenas ORQUESTRA — o harness EXECUTA**: a LLM pede "leia o diretório", o harness vai lá e lê; os bytes rodam na máquina do usuário, não na Anthropic/OpenAI. Evidência: Nauke confirma, pergunta explícita à plateia.
- **Um prompt → N ciclos de tool call**: exemplo de "corrija o bug" sem contexto = 7 chamadas (list dir → ler 4 arquivos → localizar bug → editar → executar). Com contexto explícito = 1 chamada. Evidência: demo ao vivo com contador de tool calls.
- **Melhor prompt = menos tool calls = menos custo = melhor resultado**: fornecer um "mapa" do projeto economiza ciclos de exploração do modelo. Evidência: comparação direta no demo.
- **Context engineering** = fornecer ao modelo um mapa de onde fica cada responsabilidade. "A LLM não conhece o seu projeto." Evidência: princípio central da aula com exemplo prático.
- **Modelos com melhor treinamento de tool call**: GPT-5.5, Opus 4.7, Kimi K2.6, GLM 5.0 — continuam fazendo tool calls em sequência sem parar. Modelos antigos (GPT-4.1) paravam no meio do loop. Evidência: observação empírica dos instrutores.
- **Embeds de browser** nos harnesses não são altruísmo — são necessidade porque sem browser o resultado é pior e o usuário atribui ao harness/modelo. Evidência: Branas explica a motivação dos fornecedores.
- **Claude Code inovações** (citadas por Nauke): memória, worktrees, tool search lazy load de MCPs, subagents, skills/rules/MCP (specs da Anthropic que viraram padrão), scheduler (`/schedule`), Dream Consolidation. Evidência: Nauke lista de memória.
- **Planos com reset** (Claude Code, Codex): melhor custo-benefício para uso individual intenso — reset a cada 5h. Plano de $20 → $100 → $200 dependendo do volume de paralelismo. Evidência: recomendação direta dos instrutores.
- **Claude Code e Codex estão na frente** entre harnesses de codificação; Windsurf e Cursor ficam uma passada atrás porque não fabricam seus modelos base. Evidência: análise dos instrutores + dados de mercado citados.
- **Google investiu bilhões na Anthropic** (cifra não confirmada em aula — sugestão de buscar). [external, não verificado na fonte]
- **Tool call rodando na máquina do usuário**: consequência direta é que um harness malicioso com skill maliciosa pode fazer coisas destrutivas. Segurança de harness é um tema emergente. Evidência: Branas relata que foi infectado por malware em extensão do Cursor.

## O que harness NÃO é

- **IDE não é harness**: VS Code, JetBrains são editores. O harness usa `read_file`/`write_file` independente de qual IDE está aberta. Algumas IDEs expõem problemas ao harness (diagnósticos do compilador), o que pode ajudar, mas não é a norma.
- **Auto mode**: delega escolha de modelo ao harness → harness escolhe o mais barato → pior qualidade. Nauke e Branas recomendam escolher manualmente modelo e nível de reasoning.

## Harnesses Citados

| Harness | Modelo Base | Obs |
|---|---|---|
| Claude Code | Anthropic Claude | Mais inovador; spec-driven nativo |
| Codex | OpenAI GPT | App; resets a cada 5h |
| Cursor | Multi-provider | Fork VS Code; Kimi K2.5/2.6 disponível |
| Windsurf | Multi-provider | Ficou passada atrasada em features |
| ChatGPT | OpenAI | Consumer; tem harness embutido |
| AntiGravity | Google Gemini | Harness do Google |
| OpenCode | Multi-provider | Conecta em qualquer modelo |
| Cairo | — | Incorpora elementos de spec-driven |
| Devin | — | Sandbox isolado; $15k/mês; L4 |

## Entities

- [[wiki/entities/rodrigo-branas]]
- [[wiki/entities/pedro-nauke]]
- [[wiki/entities/claude-code]]
- [[wiki/entities/codex-openai]]
- [[wiki/entities/anthropic]]
- [[wiki/entities/openai]]
- [[wiki/entities/cursor]]

## Concepts

- [[wiki/concepts/harness]]
- [[wiki/concepts/tool-call]]
- [[wiki/concepts/context-engineering-harness]]
- [[wiki/concepts/ciclo-agente]]
- [[wiki/concepts/mcp-server]]
- [[wiki/concepts/worktree-paralelismo]]
- [[wiki/concepts/reasoning-level]]
- [[wiki/concepts/degradacao-de-contexto]]

## Open Questions

- Existe um padrão de segurança para auditar skills/MCPs antes de instalá-los num harness?
- Qual o overhead de tokens do system prompt + tools registradas em harnesses populares (ex: Claude Code)?

## Raw Quotes

> "Harness é tudo aquilo que está ao redor da LLM — system prompt, tool calls, memória, subagentes, MCP, cache." — Rodrigo Branas (síntese)

> "A LLM não conhece o seu projeto. Lembra sempre disso." — Rodrigo Branas

> "Um prompt que você escreve pode derivar 40 chamadas." — Rodrigo Branas

> "Um bom exercício mental é: imagina, você roda na linha de comando. A IDE não contribui em praticamente nada." — Rodrigo Branas
