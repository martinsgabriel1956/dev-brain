---
type: concept
title: "System Prompt (Arquitetura)"
aliases: ["system prompt", "prompt escondido", "instrucoes ocultas llm"]
date_created: 2026-06-02
date_updated: 2026-08-24
source_count: 3
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

## A Demo Mais Elementar Possível: Sem Harness

[[wiki/sources/cs50-2026-semana-0-representacao-dados-algoritmos-scratch]] mostra a distinção system/user prompt isolada de qualquer camada de harness, rules, skills ou MCP — só uma chamada direta à Responses API da [[wiki/entities/openai]]:

```python
response = client.responses.create(
    input=user_prompt,        # o que o usuário digitou
    instructions=system_prompt,  # regras fixas, definidas pelo programador
    model="gpt-5",
)
```

`user_prompt` é a entrada dinâmica (ex.: "o que é o CS50?"); `system_prompt` é a instrução fixa que se aplica a toda chamada (ex.: "Limite sua resposta a uma frase", ou, por brincadeira, "Finja que você é um gato"). Sem essa separação, o usuário teria que repetir manualmente a instrução ("em uma frase...") a cada pergunta — exatamente o problema que motiva colocar instruções permanentes no `instructions`/system prompt em vez do prompt do usuário. É o mesmo princípio arquitetural descrito acima para harnesses de codificação (peso probabilístico maior, aplicação a toda chamada), só que reduzido ao caso mínimo possível, sem nenhuma das camadas (rules de projeto, skills, definições de MCP) que compõem o system prompt de uma ferramenta como Claude Code.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-01-context-harness-engineering]]
- [[wiki/sources/formacao-ia-devs-aula-02-rules]]
- [[wiki/sources/cs50-2026-semana-0-representacao-dados-algoritmos-scratch]] — demo mínima sem harness: `instructions` (system prompt) vs. `input` (user prompt) via Responses API da OpenAI
