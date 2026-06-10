---
type: source
title: "Claude Code — Guia Prático (Full Cycle)"
aliases: ["claude code full cycle", "claude code cli guia"]
date_created: 2026-05-31
date_updated: 2026-05-31
source_count: 0
tags: [claude-code, anthropic, cli, agente-ia, mcp, hooks, llmops, produtividade-dev, context-engineering]
skill: tech-mentor-ai
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/claude-code-guia-pratico-full-cycle.md
source_url: ""
author: "Full Cycle"
date_published: ""
date_ingested: 2026-05-31
---

# Claude Code — Guia Prático (Full Cycle)

## TL;DR

Guia prático do [[claude-code]] abordando instalação, planos, integração com IDE, [[claude-md]], memória, [[mcp-server|servidores MCP]], permissões, [[plan-mode]], [[slash-commands-agente|commands customizados]], [[hooks-agente|hooks]] e gestão de [[context-compaction|janela de contexto]]. Ênfase em evitar gastos desnecessários com API e extrair o máximo do agente sem perder controle.

---

## Claims Principais

### 1. Usar API Key diretamente custa muito mais que assinar um plano
**Evidência:** Usuário relatado gastou $500 sem perceber usando API Key em vez do plano de assinatura.
**Confidence:** Alta — experiência direta citada.
> Plano Max $100/mês oferece 5x mais uso que o Pro e é muito mais previsível que pagar por token.

### 2. Claude Code integra com IDEs via extensão VS Code
**Evidência:** Extensão "Claude Code" disponível no marketplace, abre painel lateral na IDE — funciona igual ao Cursor/Copilot Chat.
**Confidence:** Alta.

### 3. CLAUDE.md é a persistência de contexto entre sessões
**Evidência:** Arquivo lido no início de cada sessão. `/init` gera automaticamente. `/memory` adiciona regras.
**Confidence:** Alta.

### 4. Hooks garantem execução — CLAUDE.md apenas sugere
**Evidência:** CLAUDE.md é guideline que o LLM pode ignorar. Hooks executam comandos reais em eventos (PreToolUse, PostToolUse, Stop, SubagentStop).
**Confidence:** Alta — distinção explícita no vídeo.

### 5. Commands (.claude/commands/) transformam Markdown em scripts reutilizáveis
**Evidência:** Arquivo `.md` em `.claude/commands/` vira slash command com `$ARGUMENTS`. Permite codificar workflows complexos uma vez e invocar com `/nome-do-comando <tarefa>`.
**Confidence:** Alta.

### 6. settings.local.json não deve ser commitado; settings.json sim
**Evidência:** `.local.json` é pessoal (permissões, MCPs locais). `settings.json` é compartilhado com o time.
**Confidence:** Alta.

---

## Entidades Mencionadas

- [[claude-code]] — ferramenta central do vídeo
- [[anthropic]] — empresa criadora

---

## Conceitos Tocados

- [[claude-md]] — arquivo de memória e regras persistentes do projeto
- [[mcp-server]] — servidores MCP: configuração via CLI, global vs local
- [[plan-mode]] — modo de planejamento antes de executar (Shift+Tab)
- [[slash-commands-agente]] — commands customizados via .claude/commands/*.md
- [[hooks-agente]] — automação garantida em eventos do agente
- [[context-compaction]] — compactação da janela de contexto; /compact; gestão de sessão
- [[context-window]] — limite de tokens; Claude Code usa ~200k tokens por sessão
- [[agente-ia]] — Claude Code como exemplo concreto de agente de desenvolvimento
- [[llmops]] — permissões, configurações, gestão de custo

---

## Armadilhas Documentadas

1. **API Key vs Subscription** — usar API Key sem limite de gasto pode custar centenas de dólares
2. **npm start travando o terminal** — processos que não terminam bloqueiam o agente; usar `&` ou rodar em background
3. **Perda de contexto por sessão longa** — janela de 200k tokens enche; abrir nova sessão por tarefa
4. **Dependência do histórico da conversa** — documentar tudo em arquivos, não na memória da sessão

---

## Quotes Valiosas

> "Terminei a tarefa? Abre uma nova janela para não ter essa perda de contexto."

> "CLAUDE.md é uma guideline. Ele vai tentar seguir, mas não é garantido. Hooks são garantidos."

> "Você pode criar arquivos Markdown que executam tarefas — como se fossem shell scripts para o agente."

---

## Contradições / Questões Abertas

- O vídeo foi gravado com planos de $100/$200 — verificar preços atuais na documentação oficial.
- Plan Mode + Commands + Hooks: qual a combinação ideal para diferentes tipos de tarefa?
- Como hooks se integram com subagentes em cenários multi-agent?
