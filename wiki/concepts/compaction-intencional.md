---
type: concept
title: "Compaction Intencional"
aliases: ["intentional compaction", "compressão de contexto", "context compaction"]
date_created: 2026-05-04
date_updated: 2026-05-04
source_count: 2
tags: [context-engineering, coding-agents, workflow]
skill: tech-mentor-ai
status: stable
---

# Compaction Intencional

Técnica de gerenciamento de context window que consiste em comprimir periodicamente o contexto acumulado num arquivo markdown estruturado, iniciar uma nova sessão com esse arquivo como input, e permitir que o agente retome o trabalho sem o ruído de turnos anteriores.

Diferente de simplesmente iniciar uma nova sessão (que perde contexto), a compaction intencional **preserva o que importa** — arquivos relevantes, decisões tomadas, próximos passos — em formato denso e revisável.

## O Que Compactar

O conteúdo ideal de uma compaction inclui:

- **Arquivos exatos e números de linha** relevantes ao problema sendo resolvido
- Decisões de arquitetura tomadas até aqui
- O que foi tentado e não funcionou (evita loops)
- Próximos passos pendentes

O que **não** incluir:
- Output de builds (ruído)
- Buscas de arquivos já resolvidas
- Histórico de correções (trajetória negativa)

## Quando Usar

- Periodicamente, independente de estar no caminho certo ou errado
- Antes de cruzar ~40% da context window ([[concepts/dumb-zone]])
- Ao mudar de fase (ex: de research para plan — compactar o research antes de iniciar o plan)
- Quando o output do agente começa a degradar — sinal de que está na dumb zone

## Compaction vs Nova Sessão Simples

| | Nova sessão simples | Compaction intencional |
|---|---|---|
| Contexto preservado | Não | Sim (comprimido) |
| Arquivos relevantes | Perdidos | Incluídos com linha exata |
| Decisões tomadas | Perdidas | Documentadas |
| O que foi tentado | Perdido | Registrado |

## Relação com Sub-agentes

Sub-agentes são a versão automatizada da compaction intencional para tarefas de exploração:
- Sub-agente explora o codebase (usa sua própria context window)
- Retorna apenas uma mensagem sucinta para o agente pai
- O pai nunca acumula o ruído da exploração — começa limpo com o resultado

Ver [[concepts/separacao-de-contextos]].

## Key Sources

- [[sources/erros-workflow-research-plan-implement]]
- [[sources/context-engineering-avancado-para-coding-agents]]
