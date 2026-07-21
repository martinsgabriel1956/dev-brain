---
type: concept
title: "Compactação de Contexto"
aliases: ["context compaction", "compact", "context compression", "sumarização de contexto"]
date_created: 2026-05-31
date_updated: 2026-07-21
source_count: 2
tags: [claude-code, context-window, compactacao, agente-ia, llmops, context-engineering]
skill: tech-mentor-ai
status: stable
---

# Compactação de Contexto

## TL;DR

Mecanismo pelo qual o [[claude-code]] (e agentes em geral) resumem o histórico de conversação quando a [[context-window]] está quase cheia. Preserva o essencial para continuar trabalhando, mas inevitavelmente perde nuances do histórico completo. A melhor defesa é **terminar a sessão** ao terminar uma tarefa.

## O Problema

O Claude Code usa ~200.000 tokens de janela de contexto. Ao longo de uma sessão longa:

```
Sessão → tokens acumulando
  20% usado → ótimo
  60% usado → o agente começa a ter dificuldade com contexto antigo
  90% usado → compactação automática disparada
  após compactação → resumo substitui histórico → sessão continua
```

Após compactação, o agente opera com um **resumo** do que aconteceu, não com o histórico real. Isso significa:

- Pode esquecer decisões tomadas cedo na sessão
- Pode re-introduzir padrões que foram corrigidos
- Pode perder o contexto de por que certas escolhas foram feitas

## /compact — Compactação Manual

```
/compact
```

Dispara a compactação manualmente antes que a janela fique cheia. Útil quando:
- Você terminou uma sub-tarefa e quer "limpar" antes de começar outra
- Percebe que o agente está começando a perder o fio da meada

## Estratégia Recomendada

**Uma tarefa, uma sessão.**

```
Tarefa A → abre sessão → executa → fecha sessão
Tarefa B → abre nova sessão → executa → fecha sessão
```

Cada sessão começa com contexto limpo e lê o `CLAUDE.md` — que é a memória persistente real entre sessões.

## Como Minimizar o Impacto

1. **Mantenha o [[claude-md]] atualizado** — é lido no início de cada sessão
2. **Use [[slash-commands-agente]]** para codificar workflows em arquivos, não no histórico
3. **Crie design docs e planos em arquivos** — o agente pode ler arquivos; não dependa do histórico
4. **Feche a sessão ao terminar uma tarefa** — não acumule tarefas diferentes na mesma sessão

## /clear — Contexto Novo para Tarefas Não Relacionadas

```
/clear
```

Diferente de `/compact` (resume o histórico existente), `/clear` descarta o contexto e começa do zero. A recomendação oficial da Anthropic é usar `/clear` (ou um [[wiki/concepts/subagentes|subagente]]) sempre que a próxima tarefa não tem relação com a conversa atual — evita que raciocínio e decisões de uma tarefa anterior poluam o julgamento do agente na tarefa nova.

## /context — Inspecionar o Que Está Carregado

```
/context
```

Mostra o que está ocupando a janela de contexto no momento, permitindo decidir se algo deve ser removido (via `/clear` ou `/compact`) antes de continuar.

## Escopo de Diretório Como Redução de Contexto

Iniciar a sessão do Claude Code no menor diretório possível que resolve a tarefa também reduz o contexto necessário — num monorepo com frontend e backend, uma tarefa só de backend deve rodar com o diretório de trabalho já dentro de `backend/`, não na raiz do monorepo inteiro. Quando a tarefa de fato cruza as duas partes (ex.: frontend consumindo uma API nova do backend), aí faz sentido iniciar no monorepo como um todo.

## Relação com Token Anxiety

A compactação automática é um dos mecanismos que alimenta o fenômeno [[token-anxiety]]: a consciência de que o contexto "expira" cria urgência em desenvolvedores para maximizar o uso antes do reset.

A compactação não é idêntica a um reset completo — mas é uma degradação do contexto que pode ser frustrante quando você estava em um estado rico de raciocínio.

## Key Sources

- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
- [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]] — `/clear` para contexto não relacionado, `/context` para inspeção, escopo de diretório mínimo
