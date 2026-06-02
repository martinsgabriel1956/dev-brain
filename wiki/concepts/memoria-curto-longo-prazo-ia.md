---
type: concept
title: "Memória de Curto e Longo Prazo (Contexto IA)"
aliases: ["short term memory ia", "long term memory ia", "memoria agente ia"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 1
tags: [memoria-ia, context-window, system-prompt, harness, sessao]
skill: tech-mentor-ai
status: stable
---

# Memória de Curto e Longo Prazo (Contexto IA)

Distinção fundamental no design de harnesses: nem tudo que a LLM "sabe" numa sessão persiste para a próxima.

## Short-Term Memory (Curto Prazo)

**Onde vive:** Context window (conversa atual)

**Características:**
- Acumulada durante a sessão: prompts do usuário, tool calls, tool returns, respostas da LLM
- Apagada ao encerrar a tarefa / limpar o contexto
- Sujeita a compactação quando a janela enche (ver [[wiki/concepts/degradacao-de-contexto]])
- Toda vez que uma nova mensagem é enviada, TUDO da conversa atual vai junto para a LLM

## Long-Term Memory (Longo Prazo)

**Onde vive:** System prompt — reinjetada no início de cada nova sessão

**O que é injetado automaticamente:**
- Rules do projeto (`agents.md`, `CLAUDE.md`)
- Front-matter das skills registradas
- Schemas das MCPs registradas
- Schemas das tools built-in do harness

**Característica:** independente de quantas sessões passem, sempre presente.

## Memória entre Sessões (Indexação de Conversas)

Alguns harnesses (incluindo o Claude Code com Dream Consolidation) podem:
1. Armazenar conversas antigas em arquivos locais
2. Indexar essas conversas
3. Extrair insights que se tornam part do long-term memory (system prompt futuro)

**Risco:** conversas sobre domínios distintos (culinária + inglês) mescladas podem criar alucinações no futuro.

**Controle:** sempre configurável e opcional; requer aprovação do usuário.

## Tabela Comparativa

| Tipo | Vive em | Apagada? | Exemplo |
|---|---|---|---|
| Short-term | Context window | Sim (fim da sessão) | Conversa atual, resultados de tool calls |
| Long-term | System prompt | Não | Rules, skills front-matter, MCP schemas |
| Entre sessões | Indexação local | Depende de config | Dream Consolidation, arquivos de memória |

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-01-context-harness-engineering]]
