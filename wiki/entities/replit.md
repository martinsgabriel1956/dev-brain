---
type: entity
title: "Replit"
aliases: ["Replit", "Replit Core", "Replit Agent"]
date_created: 2026-07-24
date_updated: 2026-07-24
source_count: 1
tags: [ferramenta, agentes-ia, saas, plataforma, vibe-coding]
skill: tech-mentor-system-design
status: stub
---

# Replit

Plataforma de desenvolvimento com agentes de IA (Replit Agent) usada para prototipar e construir produtos via [[wiki/concepts/vibe-coding|vibe coding]]. Suporta múltiplas sessões/tarefas em paralelo — a interface expõe isso como "workers", possivelmente um wrapper de `git worktree` (ver [[wiki/concepts/worktree-paralelismo]]), com merge automático de volta à sessão principal e resolução de conflitos pelo próprio harness.

## Recursos observados

- **Taskboard** estilo Kanban, com tarefas sugeridas automaticamente pelo agente (ex.: corrigir bugs identificados) além das criadas pelo usuário.
- **Testes end-to-end automáticos**: ao implementar uma funcionalidade, o agente escreve o teste, roda do início ao fim, verifica se o resultado bate com o pedido, e itera até passar — antes de reportar a tarefa como concluída.
- **Colaboração multiplayer**: convite de colaboradores como editores do mesmo projeto, com tarefas atribuídas a diferentes pessoas visíveis no mesmo taskboard.
- **Plano Replit Core**: $10 de crédito de bônus, 20 dólares/mês em créditos, até cinco colaboradores convidados, trabalho em paralelo com até dois agentes, publicação em qualquer região, múltiplos workspaces.

## Key Sources

- [[wiki/sources/system-design-simulador-hotel-booking-replit]] — demonstração de criação de um SaaS (simulador de system design) do zero, incluindo fluxo de tarefas paralelas e teste automático end-to-end
