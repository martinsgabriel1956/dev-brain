---
type: concept
title: "Agente de IA"
aliases: ["agente", "AI agent", "agentes de ia"]
date_created: 2026-05-18
date_updated: 2026-05-31
source_count: 2
tags: [agentes-ia, llm, llmops, automacao]
skill: tech-mentor-ai
status: draft
---

## Definição

Sistema baseado em LLM que executa tarefas de forma autônoma ou semi-autônoma, podendo usar ferramentas (leitura de arquivos, execução de código, chamadas de API) para atingir objetivos sem intervenção contínua do usuário.

Diferente de um simples chat com LLM, um agente possui um **loop de ação**: percebe o estado atual → decide a próxima ação → executa → observa o resultado → repete até concluir ou falhar.

---

## Características Centrais

- **Autonomia:** opera sem supervisão constante
- **Uso de ferramentas (tool use):** pode executar código, ler arquivos, fazer buscas
- **Loop de raciocínio:** ReAct, Chain-of-Thought, ou variantes
- **Janela de contexto:** limite de tokens que define o "alcance de memória" do agente — ver [[janela-de-contexto]]
- **Orquestração:** agentes podem ser coordenados por outros agentes (multi-agent)

## Impacto Operacional

A capacidade de rodar agentes em paralelo e de deixá-los executando tarefas enquanto o desenvolvedor faz outra coisa criou um novo paradigma de trabalho — e com ele, o fenômeno [[token-anxiety]].

## Terminologia de Controle

O campo começou a usar metáforas de controle de animais para descrever como gerenciar agentes:
- *Harness* (arreio)
- *Reins* (rédeas)
- *Leash* (coleira)

Reflete que ainda não existe vocabulário maduro para descrever as relações de supervisão humana sobre sistemas agênticos.

---

## Exemplo Concreto: Claude Code

[[claude-code]] é um agente de desenvolvimento que demonstra os padrões na prática:
- **Tool use:** lê/escreve arquivos, executa comandos, acessa MCP servers
- **Loop de ação:** plan → execute → observe → repeat
- **Subagentes:** delega subtarefas a agentes especializados ([[hooks-agente]] permitem reagir ao fim de cada subagente via `SubagentStop`)
- **Memória:** [[claude-md]] persiste contexto entre sessões; [[context-compaction]] gerencia janela

## Key Sources

- [[wiki/sources/token-anxiety-agentes-ia-comportamento-devs]]
- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
