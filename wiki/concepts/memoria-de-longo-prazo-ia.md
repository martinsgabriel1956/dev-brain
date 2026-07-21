---
type: concept
title: "Memória de Longo Prazo para Agentes"
aliases: ["long-term memory", "memória de longo prazo", "plano persistido", "research output salvo"]
date_created: 2026-06-01
date_updated: 2026-07-21
source_count: 2
tags: [context-engineering, coding-agents, rpi-workflow, refatoracao, subplano]
skill: tech-mentor-ai
status: draft
---

# Memória de Longo Prazo para Agentes

Técnica de salvar o output de uma fase de **research** como um arquivo `.md` para que ele possa ser usado como input em sessões futuras — sem precisar repetir a exploração do codebase.

## Quando usar

Quando a refatoração ou mudança é grande demais para ser planejada e executada em uma única sessão sem explodir a context window. Sintomas:

- O plano gerado teria mais de ~200 linhas
- A mudança impacta múltiplos módulos ou serviços
- Um único PR seria grande demais para revisão humana
- A mudança levaria dias ou semanas de trabalho

## O Padrão

```
Sessão 1 — Research
O agente escaneia o codebase e produz o diagnóstico.
    ↓
Salvar output em: refactoring-plan.md (memória de longo prazo)
    ↓
Revisão humana + validação pelo time
    ↓
Sessão 2 — Quebrar em subplanos
O agente lê refactoring-plan.md e divide em fases:
    - fase-1-outbox-pattern.md
    - fase-2-value-objects.md
    - fase-3-aggregates.md
    ↓
Sessões 3, 4, 5... — Implement (uma por subplano)
Cada sessão carrega só o subplano da fase atual.
Context window permanece baixa (~30%).
    ↓
PR por fase → revisão humana → merge
```

## O que cada subplano deve conter

```markdown
## Fase N — [Nome da fase]

**Pré-requisito:** Fase N-1 concluída e testes passando

**Contexto a carregar:** path/para/guidelines-relevantes.md

**Arquivos a modificar:**
- src/module/domain/entity.ts

**O que fazer:**
1. Passo específico
2. ...

**Comandos de validação:**
- npm run build
- npm test -- --testPathPattern=module

**Critério de sucesso:** build e testes passando, 100% dos casos de uso cobertos
```

## Por que funciona

- A context window de cada sessão de implementação é pequena (só o subplano)
- O ser humano valida o plano completo antes de qualquer execução
- PRs menores são revisáveis pelo time
- Cada fase tem critério objetivo de sucesso (build + testes)
- A memória persiste entre sessões — o agente não precisa redescobrir o que foi mapeado

## Relação com [[separacao-de-contextos]]

Memória de longo prazo é a extensão natural da separação de contextos: enquanto separação de contextos divide sessões para evitar contaminação, a memória de longo prazo conecta essas sessões via arquivo persistido em vez de re-exploração.

## Relação com outros conceitos

- [[rpi-workflow]] — memória de longo prazo é o mecanismo que permite aplicar RPI em mudanças grandes
- [[separacao-de-contextos]] — sessões separadas ligadas por memória persistida
- [[dumb-zone]] — subplanos mantêm cada sessão na smart zone
- [[progressive-disclosure-ia]] — disclosure entre sessões em vez de dentro de uma sessão

## Distinção de Escopo: Memória de Preferências vs. Memória de Refatoração

Esta página cobre memória persistida para uma única mudança grande (research → subplanos de uma refatoração). Para memória de propósito geral entre sessões distintas — preferências do usuário, padrões de tarefas recorrentes, skills geradas automaticamente — ver [[wiki/concepts/agent-memory-tres-camadas]] e [[wiki/concepts/closed-loop-skill-learning]], que descrevem um padrão irmão com escopo mais amplo.

## Key sources

- [[wiki/sources/context-engineering-codebases-grandes-rpi]] — padrão demonstrado com refatoração de SubscriptionService para DDD tático (13+ serviços, 6 PRs)
- [[wiki/sources/hermes-agent-open-claw-learning-loop]] — padrão irmão de memória entre sessões, com escopo mais amplo (preferências e skills, não só refactoring plans)
