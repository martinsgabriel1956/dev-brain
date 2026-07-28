---
type: concept
title: "Hooks de Agente"
aliases: ["hooks claude code", "agent hooks", "hooks automação"]
date_created: 2026-05-31
date_updated: 2026-07-21
source_count: 3
tags: [claude-code, hooks, automacao, agente-ia, llmops, context-engineering, harness]
skill: tech-mentor-ai
status: stable
---

# Hooks de Agente

## TL;DR

Hooks são comandos shell executados automaticamente em eventos específicos do [[claude-code]]. Diferente do [[claude-md]] (que o LLM pode ignorar), hooks são **garantidos** — o runtime os executa independentemente do modelo. Permitem automatizar validações, testes, formatação e qualquer lógica de controle de qualidade.

## Por que Hooks Existem

O `CLAUDE.md` é uma guideline em linguagem natural — o LLM "lê e tenta seguir". Mas não há garantia de execução. Hooks resolvem isso: são chamados pelo **runtime**, não pelo LLM.

```
CLAUDE.md: "sempre rode os testes após cada mudança"  → o LLM pode esquecer
Hook PostToolUse(Task): "npm test"                    → sempre executado
```

## Estrutura de um Hook

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Task",
        "hooks": [
          {
            "type": "command",
            "command": "npm test -- --watchAll=false"
          }
        ]
      }
    ]
  }
}
```

## Eventos Disponíveis

| Evento | Quando dispara |
|--------|----------------|
| `PreToolUse` | Antes de o agente usar qualquer ferramenta |
| `PostToolUse` | Após o agente usar uma ferramenta |
| `UserPromptSubmit` | Quando o usuário envia uma mensagem |
| `Stop` | Quando o agente principal termina a tarefa |
| `SubagentStop` | Quando um subagente termina |

## Matchers

Matchers filtram para qual ferramenta o hook se aplica:

| Matcher | Ferramenta |
|---------|------------|
| `Write` | Escreve arquivo |
| `Edit` | Edita arquivo |
| `MultiEdit` | Múltiplas edições |
| `Bash` | Executa comando shell |
| `Task` | Executa tarefa (subagente) |
| `WebFetch` | Acessa URL |

## Códigos de Retorno

| Exit code | Significado |
|-----------|-------------|
| `0` | Sucesso — agente continua |
| `2` | Erro — agente lê o stdout e tenta corrigir |

Isso permite criar loops de feedback: hook falha → agente vê o erro → agente corrige → hook roda novamente.

## Casos de Uso Práticos

```bash
# Rodar testes sempre que uma tarefa termina
PostToolUse(Task) → npm test

# Lint automático após cada escrita de arquivo TypeScript
PostToolUse(Write) → npx tsc --noEmit

# Notificar quando o agente termina (macOS)
Stop → osascript -e 'display notification "Claude terminou" with title "Claude Code"'

# Formatar código após edições
PostToolUse(Edit) → npx prettier --write $FILE
```

## Como Criar via CLI

```
/hooks
```

O assistente guia pelo processo: escolhe evento → matcher → comando → onde salvar.

## Onde São Armazenados

Hooks ficam nos arquivos `settings.json` ou `settings.local.json` (ver [[settings-agente]]):

- `settings.local.json` — pessoal, não commitado
- `settings.json` — compartilhado com o time
- `~/.claude/settings.json` — global para todos os projetos

## Relação com CLAUDE.md

[[claude-md]] = instruções em linguagem natural (o LLM tenta seguir)
Hooks = comandos garantidos pelo runtime (sempre executados)

Use os dois em conjunto: CLAUDE.md para contexto e diretrizes gerais, hooks para garantir comportamentos críticos.

## Caso: Hook de Fim de Sessão Alimentando Pattern Extraction

[[wiki/sources/hermes-agent-open-claw-learning-loop]] descreve um uso manual comum, precursor da automação do [[wiki/concepts/closed-loop-skill-learning|closed-loop skill learning system]] do Hermes Agent: um hook disparado ao fim da sessão (`Stop`) que coleta tudo que se repetiu na tarefa e alimenta uma chamada de LLM geradora de padrões, cujo output realimenta o arquivo de regras/skill do projeto — ou seja, `Stop` usado não só para notificação, mas como gatilho de curadoria de memória entre sessões.

## Hooks como um dos Componentes Nomeados do Harness

[[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] cita hooks como um dos sete componentes documentados de um harness completo (ver [[wiki/concepts/harness]]): pontos onde um humano ou sistema automatizado intervém, definidos explicitamente por quem constrói o harness — não é o agente decidindo por conta própria quando escalar ou parar.

## Key Sources

- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
- [[wiki/sources/hermes-agent-open-claw-learning-loop]] — hook de `Stop` como pattern extraction manual, precursor do closed-loop skill learning
- [[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] — hooks como componente nomeado do harness: pontos de intervenção definidos explicitamente, não decididos pelo agente
