---
type: concept
title: "Plan Mode"
aliases: ["modo planejamento", "auto-accept", "shift tab claude code"]
date_created: 2026-05-31
date_updated: 2026-08-11
source_count: 3
tags: [claude-code, plan-mode, agente-ia, workflow, context-engineering]
skill: tech-mentor-ai
status: stable
---

# Plan Mode

## TL;DR

Modo do [[claude-code]] onde o agente **apenas planeja** sem executar ações. Alternado com Shift+Tab. Permite revisar e refinar o plano antes de autorizar a execução — fundamental para evitar que o agente saia fazendo mudanças em direções erradas.

## Dois Modos de Operação

| Modo | Comportamento |
|------|---------------|
| **Auto-accept edits** | Aplica mudanças automaticamente sem pedir confirmação a cada passo |
| **Plan Mode** | Gera apenas um plano de ação; aguarda aprovação antes de executar |

**Alternância:** `Shift+Tab` dentro do Claude Code.

## Workflow Recomendado

```
1. Ative Plan Mode (Shift+Tab)
2. Descreva a tarefa (mesmo com prompt vago — o plano vai clarear)
3. Leia o plano gerado
4. Refine: "não, o correto é X. Reconsidere Y"
5. Repita até o plano estar alinhado
6. Autorize a execução: "pode começar"
7. Monitore os passos (ou use Auto-accept para tarefas de baixo risco)
```

## Por que Usar Plan Mode

Sem Plan Mode, o agente interpreta o prompt e sai executando. Se o prompt for ambíguo ou a tarefa complexa, ele pode:
- Escolher a abordagem errada
- Modificar arquivos que não deveriam ser tocados
- Gastar tokens em direção incorreta

Com Plan Mode, você investe poucos tokens para alinhar antes de gastar muitos executando.

## Plan Mode + Commands

Você pode codificar o comportamento de Plan Mode em [[slash-commands-agente]]:

```markdown
# Execução de tarefa

Antes de executar, crie:
1. Plano de alto nível (compreensão do problema)
2. Plano de baixo nível (arquivos a modificar, estratégia)

Aguarde aprovação do usuário antes de prosseguir.

Tarefas: $ARGUMENTS
```

Isso transforma seu workflow padrão em um comando reutilizável.

## Relação com HITL (Human-in-the-Loop)

Plan Mode é uma forma de [[human-in-the-loop]] leve: o humano revisa a intenção antes da execução, sem precisar aprovar cada ferramenta individualmente. É menos granular que aprovar cada `Edit`, mas mais seguro que Auto-accept cego.

## Guideline de Granularidade

Quando usar Plan Mode versus alternativas:

| Escopo da tarefa | Abordagem recomendada |
|-----------------|----------------------|
| Pontual, 1 arquivo, linha específica | Execução direta |
| 2–3 arquivos, complexidade moderada | Plan Mode |
| Múltiplos domínios (front+back), feature completa | [[wiki/concepts/spec-driven-development|Spec Driven Development]] |

## Persistindo o Plano

Uma boa prática é salvar o plano aprovado em arquivo dentro do projeto (com timestamp e slug). Isso permite:
- Rastrear decisões de planejamento ao longo do tempo
- Retomar após interrupções sem perder o plano
- Usar o plano como input para agentes de tech spec em fluxos SDD

O Codex não salva o plano automaticamente — configure o harness para fazê-lo se necessário.

## Key Sources

- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
- [[wiki/sources/formacao-ia-devs-aula-03-plan-mode]]
- [[wiki/sources/extrair-melhor-codigo-de-agentes-ia-planejamento-plan-mode-skills]] — modo plan na IDE [[wiki/entities/verdent-ai|Verdent]]: mapeia dependências, gera especificação técnica com diagrama Mermaid, pergunta em pontos ambíguos e só codifica ("build") após o plano ser revisado e comentado
