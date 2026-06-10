---
type: concept
title: "System Prompt (Arquitetura)"
aliases: ["system prompt", "prompt escondido", "instrucoes ocultas llm"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 2
tags: [system-prompt, harness, context-window, rules, skills, mcp]
skill: tech-mentor-ai
status: stable
---

# System Prompt (Arquitetura)

Bloco de texto injetado no **topo da context window** antes de qualquer mensagem do usuário. É invisível ao usuário final, mas presente em toda chamada LLM. Define as regras do jogo da sessão.

## O Que Compõe o System Prompt

Em um harness de codificação (Claude Code, Cursor, Codex):

```
SYSTEM PROMPT
├── System prompt do provider (definido pela Anthropic/OpenAI/etc.)
│     • Instruções de comportamento
│     • Schemas das tools built-in (read_file, write_file, bash…)
│     • Personagem e limitações
├── Rules do projeto (agents.md / CLAUDE.md / .cursorrules)
│     • Folder structure, anti-patterns, code standards
├── Front-matter das skills registradas
│     • name + description de cada skill disponível
├── Definições de MCPs registrados
│     • Schemas das tools de terceiros (Slack, GitHub, Figma, DB…)
└── Contexto de projeto adicional (CLAUDE.md, README, etc.)
```

## Por Que Importa

1. **Tokens fixos por sessão** — tudo no system prompt custa tokens em TODA chamada, mesmo se irrelevante para a tarefa atual. Rules grandes → custo constante.

2. **Peso probabilístico** — system prompt tem maior peso que mensagens de usuário por design de treinamento dos modelos. Rules no system prompt tendem a ser mais seguidas que instruções no prompt do usuário.

3. **Problema de rules excessivas** — antes das skills, colocar 5.000 linhas de rules diluía o peso de cada instrução individual. Uma linha com `use red color` rodeada de 5.000 linhas perdia força probabilística.

4. **Lazy loading das skills** — solução: skills só colocam o front-matter (nome + descrição) no system prompt; o corpo é carregado por tool call quando necessário.

## Exemplo de Conteúdo Não Visível

Quando você usa o Claude Code, o system prompt contém (aproximadamente):
- Instruções de pensar estruturadamente antes de executar
- Instrução de varrer arquivos de configuração
- Instrução de analisar commits passados
- Lista de todas as tools disponíveis com seus schemas
- Suas rules do `CLAUDE.md` ou `.claude/rules/`
- Front-matter de cada skill registrada

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-01-context-harness-engineering]]
- [[wiki/sources/formacao-ia-devs-aula-02-rules]]
