---
type: concept
title: "Harness"
aliases: ["AI harness", "harness de IA", "coding harness"]
date_created: 2026-06-02
date_updated: 2026-07-10
source_count: 7
tags: [harness, llm, tool-call, agente, context-engineering]
skill: tech-mentor-ai
status: stable
---

# Harness

Tudo que envolve um modelo LLM para torná-lo operacionalmente útil: gerenciamento de contexto, execução de [[wiki/concepts/tool-call|tool calls]], memória, subagentes, MCPs, system prompt e cache. O modelo em si é apenas um endpoint stateless; o harness é o que o "dá olhos e mãos".

## Por que o Conceito Importa

Um LLM isolado só consegue operar dentro do seu treinamento — não lê arquivos, não executa código, não consulta APIs. O harness conecta o modelo ao mundo real fornecendo:

1. **Tool calls registradas** — lista de operações que o modelo pode pedir (read_file, write_file, bash, web_search, MCP servers…)
2. **Contexto acumulado** — histórico da conversa + resultados das tools em cada ciclo
3. **Gerenciamento de janela** — compactação, cache, descarte de mensagens antigas
4. **Orquestração de subagentes** — paralelismo de tarefas em ambientes isolados ([[wiki/concepts/worktree-paralelismo]])
5. **System prompt** — regras, skills, CLAUDE.md — invisíveis ao usuário mas presentes em toda chamada

## Quem Executa as Tools?

**A LLM apenas orquestra. O harness executa.** Quando o modelo pede "liste os arquivos do diretório", é o processo local do harness que roda o `ls` e devolve o resultado ao contexto. Isso significa que tools maliciosas numa skill ou MCP não verificado rodam na máquina do usuário, não nos servidores do provider.

## Ciclo de Uso

```
Usuário escreve prompt
      ↓
Harness monta contexto (system prompt + tools disponíveis + histórico)
      ↓
LLM recebe o contexto e decide: responder OU pedir tool call
      ↓
Harness executa a tool (lê arquivo, roda bash, busca na web…)
      ↓
Resultado da tool entra no contexto
      ↓
LLM decide: mais tool calls OU resposta final
```

Um único prompt do usuário pode gerar 40+ ciclos de tool calls antes da resposta final.

## Harnesses Principais (2026)

| Harness | Provider principal | Diferencial |
|---|---|---|
| Claude Code | Anthropic | Mais inovador; nativo em rules/skills/MCP/worktrees |
| Codex | OpenAI | Reset a cada 5h; GPT-5.x base |
| Cursor | Multi | IDE integrada; vários modelos incluindo open source |
| Windsurf | Multi | Interface visual; ficou uma passada atrás em features |
| ChatGPT | OpenAI | Consumer; sem acesso ao filesystem por default |
| AntiGravity | Google | Harness do Google para Gemini |
| OpenCode | Multi | Conecta em qualquer modelo via variável de ambiente |
| Cairo | — | Incorpora spec-driven nativamente |
| Devin | — | Sandbox isolado; L4; ~$15k/mês para uso intenso |

## Relação com IDE

IDE e harness são camadas separadas. O harness usa `read_file`/`write_file` independente de qual editor está aberto. IDEs como Cursor expõem diagnósticos do compilador ao harness (problema lints), o que pode ajudar, mas não é obrigatório. A tendência é que IDEs percam relevância conforme mais trabalho migra para o terminal.

## Duas Camadas do Harness

**Provider harness** — o que Claude Code, Cursor, Codex trazem por padrão: system prompt do provider, tools built-in, gerenciamento de janela.

**User harness** — o que você fornece: rules, skills, MCPs, sensores. É onde está a maior alavanca de qualidade. Ver [[wiki/concepts/sensores-vs-guias]].

## Harness como Trabalho Central do Product Engineer

Dados de campo do Cursor (2026) mostram o harness em maturidade: code review automatizado por t-shirt size, specs estruturadas para agentes, MCP central com governança, self-healing por request, agents que abrem PRs sozinhos. Construir essa infraestrutura — não escrever o código em si — é a face 2 do [[product-engineer]]. A evolução do dev não é "deixar de construir" — é construir em camada diferente.

## Próximo Degrau: Loop Engineering

Depois de harness engineering (melhorar o ambiente ao redor do modelo), o degrau seguinte é [[wiki/concepts/loop-engineering|loop engineering]] — melhorar o ciclo completo de execução como estrutura repetível e disparável automaticamente (por prompt, schedule ou evento), não apenas uma execução isolada.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
- [[wiki/sources/formacao-ia-devs-aula-01-context-harness-engineering]]
- [[wiki/sources/product-engineer-vale-do-silicio-2026]]
- [[wiki/sources/loop-engineering-planner-critic-grafo]] — propõe loop engineering como degrau seguinte a harness engineering
