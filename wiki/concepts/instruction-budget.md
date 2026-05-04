---
type: concept
title: "Instruction Budget"
aliases: ["orçamento de instruções", "limite de instruções", "instruction limit"]
date_created: 2026-05-04
date_updated: 2026-05-04
source_count: 2
tags: [context-engineering, coding-agents, llm, ai-engineering]
skill: tech-mentor-ai
status: draft
---

# Instruction Budget

Limite implícito de instruções que um LLM consegue seguir de forma consistente numa mesma context window. Não é documentado oficialmente por nenhum provider, mas a estimativa empírica — baseada em uso real com coding agents — é de **~150 a 200 instruções**. Além disso, a atenção começa a fragmentar e cada instrução adicional é um dado: o modelo pode ou não seguir.

## Por Que Importa

O orçamento não é só o system prompt. É a soma de:

- System prompt do agente (ex: 85 instruções)
- CLAUDE.md / `.cursor/rules` do projeto (ex: +30 instruções)
- Instruções injetadas por MCPs instalados
- Contexto acumulado da conversa

Devs que nunca contaram as instruções totais do seu agente frequentemente estão rodando além do budget sem saber.

## Consequências de Ultrapassar o Budget

- Regras que o modelo ignora silenciosamente
- Comportamento inconsistente entre turnos da mesma sessão
- Dificuldade de debugar — o modelo "sabe" as regras mas nem sempre as aplica
- Falsa sensação de segurança: você tem 85 regras no system prompt, mas só ~50 estão sendo seguidas de forma confiável

## Mitigações

1. **Contar as instruções totais** — system prompt + CLAUDE.md + MCPs + contexto
2. **Priorizar**: manter apenas as instruções que realmente importam; remover as redundantes
3. **Separar por fase** — instruções de research não precisam estar presentes na fase de implement
4. **MCPs seletivos** — cada MCP instalado injeta instruções; desinstalar os que não são usados na tarefa atual

## Relação com Dumb Zone

Instruction budget e [[concepts/dumb-zone]] são problemas relacionados mas distintos:
- Dumb zone: degradação por uso excessivo da *context window* (tokens)
- Instruction budget: degradação por excesso de *instruções* (não necessariamente tokens — uma instrução pode ser curta)

Um agente pode estar na smart zone (40% da context window) e ainda assim estar acima do instruction budget se o system prompt for muito denso em regras.

## Key Sources

- [[sources/erros-workflow-research-plan-implement]]
- [[sources/context-engineering-avancado-para-coding-agents]]
