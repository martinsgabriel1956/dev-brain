---
type: concept
title: "Agente de IA"
aliases: ["agente", "AI agent", "agentes de ia"]
date_created: 2026-05-18
date_updated: 2026-08-11
source_count: 5
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
- **Subagentes:** delega subtarefas a agentes especializados, cada um com janela de contexto própria — ver [[wiki/concepts/subagentes]] ([[hooks-agente]] permitem reagir ao fim de cada subagente via `SubagentStop`)
- **Worktrees:** paralelismo a nível de file system, alternativa aos subagentes quando as tarefas devem virar entregas/PRs separadas — ver [[wiki/concepts/worktree-paralelismo]]
- **Memória:** [[claude-md]] persiste contexto entre sessões; [[context-compaction]] gerencia janela

## Blueprint de Produção: as 5 Peças e os 4 Componentes

[[wiki/sources/oracle-demite-milhares-anatomia-agente-dba-autonomo]] descreve um blueprint replicável para agentes de produção orientados a evento (não a chat), usando um agente de DBA como exemplo:

**5 peças de arquitetura**: LLM Planner (system prompt com [[wiki/concepts/playbook|playbook]] do domínio) → tool call loop → módulo de observação → camada de decisão (tentar de novo / pedir humano / pedir confirmação) → write-back (log, ticket, notificação).

**4 componentes essenciais**: trigger (evento externo aciona o agente — não é a LLM decidindo sozinha quando agir), whitelist de ferramentas ([[wiki/concepts/principio-do-menor-privilegio|menor privilégio]] aplicado a tool calling — nunca inclui operações destrutivas), loop de observação, e [[wiki/concepts/human-in-the-loop|escape hatch]] (pausa e chama humano quando a confiança auto-reportada do modelo cai abaixo de um limiar).

## Key Sources

- [[wiki/sources/token-anxiety-agentes-ia-comportamento-devs]]
- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
- [[wiki/sources/oracle-demite-milhares-anatomia-agente-dba-autonomo]] — blueprint de 5 peças + 4 componentes para agentes orientados a evento em produção
- [[wiki/sources/vibe-coding-jogos-um-prompt-vs-varios-estagios-produto]] — modo agente do ChatGPT (com full access ao computador) fazendo setup, instalação de engine, escrevendo o próprio script de execução e testando o jogo sozinho; atritos triviais (falta de Git, login manual na Epic Games) ainda exigem humano
