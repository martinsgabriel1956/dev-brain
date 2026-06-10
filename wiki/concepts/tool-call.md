---
type: concept
title: "Tool Call"
aliases: ["function calling", "tool use", "chamada de ferramenta"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 2
tags: [tool-call, harness, agente, llm, function-calling]
skill: tech-mentor-ai
status: stable
---

# Tool Call

Mecanismo introduzido pela OpenAI em 2023 que permite a um LLM requisitar a execução de funções externas registradas no [[wiki/concepts/harness]]. Considerado o segundo grande game changer da história dos LLMs (o primeiro foi a abertura como API). Deu ao modelo a capacidade de agir sobre o mundo real em vez de apenas gerar texto.

## Como Funciona

1. O harness registra um conjunto de tools disponíveis (nomes + descrições + schemas de parâmetros) no contexto enviado ao modelo.
2. O modelo, em vez de responder diretamente, pode emitir uma "chamada de ferramenta" indicando qual tool invocar e com quais parâmetros.
3. **O harness recebe essa chamada e executa a tool na máquina do usuário** — não nos servidores do provider.
4. O resultado da execução é injetado de volta no contexto como mensagem do sistema.
5. O modelo decide: mais tool calls ou resposta final ao usuário.

## Tools Fundamentais

| Tool | O que faz |
|---|---|
| `read_directory` | Lista arquivos de um diretório |
| `read_file` | Lê conteúdo de um arquivo |
| `write_file` | Cria ou sobrescreve um arquivo |
| `edit_file` | Aplica patches em arquivo existente |
| `execute_bash` | Roda comandos shell (npm, git, make…) |
| `web_search` | Busca na internet |
| `browser` | Abre URL, tira screenshot, inspeciona DOM |

## Por Que Importa Para o Dev

- **1 prompt → N tool calls**: uma instrução vaga pode gerar dezenas de ciclos internos, cada um consumindo tokens. Contexto explícito reduz ciclos e custo.
- **Qualidade do tool call = qualidade do harness**: dois harnesses com o mesmo modelo entregam resultados diferentes porque implementam as tools de formas diferentes (ex: um usa grep, outro usa RAG para busca de arquivo).
- **Modelos treinados em tool call**: GPT-5.x, Opus 4.7, Kimi K2.6 têm fine-tuning específico para continuar executando loops de tool calls sem parar prematuramente. Modelos antigos (GPT-4.1) paravam no meio do loop.
- **Segurança**: tools rodam na sua máquina. Uma skill ou MCP malicioso pode usar tool calls para exfiltrar dados, deletar arquivos, etc.

## Analogia

Assim como um programa em JavaScript não sabe que horas são e faz uma syscall ao OS para obter o timestamp, o LLM não sabe o que tem no seu filesystem e faz uma "syscall" ao harness para descobrir.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
