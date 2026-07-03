---
type: concept
title: "Subagentes"
aliases: ["subagents", "sub-agentes", "Task tool", ".claude/agents"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 1
tags: [subagentes, claude-code, multi-agent, paralelismo, context-engineering, harness]
skill: tech-mentor-ai
status: draft
---

# Subagentes

Padrão de paralelismo **a nível de janela de contexto**: o agente principal ([[wiki/concepts/ciclo-agente|chat pai]]) delega uma tarefa a uma instância separada do modelo, que roda numa janela de contexto própria, executa sua tarefa isoladamente e retorna **apenas o resultado final** — o raciocínio intermediário e os tool calls do subagente não entram no contexto do agente pai.

No [[wiki/entities/claude-code]], isso é implementado pela tool `Task`/`Agent`: cada subagente é, na prática, um processo separado sendo lançado pelo processo pai.

## Diferença Central para Worktrees

| | Subagentes | [[wiki/concepts/worktree-paralelismo|Worktrees]] |
|---|---|---|
| Nível de paralelismo | Contexto (mesma janela do Claude) | File system (cópia física do repo) |
| Resultado final | Convergido numa única síntese/PR | Branches e PRs separadas |
| Uso típico | Pesquisa, decisão, feature única dividida em partes (back+front+doc+teste) | Tarefas independentes que vão virar entregas separadas |
| Economia | De janela de contexto do agente pai | De conflito de arquivos entre agentes |

## Como Declarar um Subagente Customizado

Arquivo Markdown em `.claude/agents/*.md` (nível de projeto) ou equivalente a nível de usuário — mesma hierarquia de [[wiki/concepts/skills-agente|skills]] (usuário → projeto → diretório). Front-matter com nome, descrição (usada pelo Claude para decidir quando acionar) e cor; corpo com a instrução de comportamento.

Diferente de uma skill pura, um subagente pode fixar:

- **`model`** — ex.: Opus para um agente de Product Manager (decisões de maior peso), Sonnet para implementação, Haiku para documentação.
- **`tools`** — lista restrita de [[wiki/concepts/tool-call|tools]] disponíveis. Um subagente "code reviewer" só precisa de `Read`, `Grep`, `Glob`, `Bash` — sem `Write`/`Edit`, porque ele não escreve código, só analisa. Restringir tools reduz o system prompt do subagente e, por consequência, o custo em tokens.

## Padrão Orquestrador

Um subagente "CTO"/tech lead pode atuar como despachante de um time de subagentes especializados (backend, frontend, infra, product manager), cada um recebendo apenas as tarefas do seu domínio. Ver também o padrão Supervisor/Orchestrator em `references/ai/agents-orchestration.md` (skill `tech-mentor-ai`).

## Duas Formas de Disparo

1. **Automático** — o próprio modelo reconhece que uma tarefa é paralelizável (ex.: pesquisar 3 provedores de webhook ao mesmo tempo) e despacha subagentes via tool call, sem o usuário precisar nomear nenhum agente customizado.
2. **Explícito/customizado** — usuário ou prompt referencia diretamente o subagente pelo nome (ex.: "use o agente CTO"), garantindo que o roteamento não dependa da heurística automática do modelo.

**Risco observado:** com muitas skills e subagentes sobrepostos no mesmo projeto/usuário, o roteamento automático fica ambíguo — o modelo pode acionar uma skill genérica em vez do subagente customizado esperado, mesmo quando a descrição do subagente parecia cobrir o caso.

## Relação com Effort/Reasoning

Reasoning effort baixo pode impedir o reconhecimento de que uma tarefa é paralelizável — ver [[wiki/concepts/reasoning-level]]. O mesmo prompt disparou paralelismo automático só depois de subir o effort de low para high.

## Key Sources

- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
