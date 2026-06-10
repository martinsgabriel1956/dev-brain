---
type: concept
title: "Task Looper"
aliases: ["task looper", "loop de tarefas", "executor automático de tarefas"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 1
tags: [task-looper, spec-driven, automacao, agente, execucao]
skill: tech-mentor-ai
status: stub
---

# Task Looper

## TL;DR

Componente do fluxo [[wiki/concepts/spec-driven-development|Spec Driven Development]] que executa automaticamente a lista de tarefas gerada pelo processo PRD → Tech Spec → Tarefas, sem intervenção humana entre uma tarefa e a próxima.

## Função no Fluxo SDD

No SDD básico, o humano executa cada tarefa manualmente (ou as dispara uma a uma). O task looper automatiza essa etapa:

```
[Tarefas aprovadas] → [Task Looper] → executa tarefa 1
                                    → verifica resultado
                                    → executa tarefa 2
                                    → ...
                                    → [QA final]
```

## Comportamento Esperado

- Executa cada tarefa isoladamente com o contexto correto (PRD + Tech Spec + descrição da tarefa)
- Verifica o critério de aceite de cada tarefa antes de prosseguir
- Pode incluir tarefas de QA automatizadas ao final do processo
- Interrompe e notifica o humano em caso de falha ou ambiguidade

## Quando Usar

Indicado para projetos grandes onde as tarefas são independentes e os critérios de aceite são objetivos o suficiente para verificação automatizada. Não recomendado quando as tarefas têm dependências ambíguas ou quando o risco de erro em cadeia é alto.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-04-agentes-planejamento]]
