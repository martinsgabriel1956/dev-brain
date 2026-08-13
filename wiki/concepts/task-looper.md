---
type: concept
title: "Task Looper"
aliases: ["task looper", "loop de tarefas", "executor automático de tarefas"]
date_created: 2026-06-02
date_updated: 2026-08-12
source_count: 3
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

## Exemplo Concreto: Roadmap + Memória Entre Fases

[[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] descreve uma implementação concreta do task looper aplicado a [[wiki/concepts/loop-engineering|loop criador]]: um roadmap de fases (épicos), onde cada fase passa por planejar → implementar → verificar (subagente evaluator, com até 3 tentativas de correção) → atualizar o roadmap → próxima fase. Três artefatos dão contexto entre fases: `lessons.md` (lições aprendidas), *state* (o que foi feito, blockers) e *handoff* (o que a próxima fase precisa saber).

## Estado via Arquivo Simples (`state.md`), Sem Precisar Ser Determinístico

[[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]] descreve uma versão mais leve do mesmo padrão de estado: em vez de um framework dedicado, basta instruir via prompt ou skill que o agente mantenha um arquivo `.md` (ex.: `state.md`) trackeando tarefa concluída, próxima tarefa, lista de tarefas, decisões tomadas, erros e arquivos modificados. Numa spec de 10 tasks, o próprio agente cria esse arquivo com todas as informações para executar as tasks uma por uma, seguindo um padrão formalizado — mesma função do trio `lessons.md`/state/handoff acima, com menos estrutura.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-04-agentes-planejamento]]
- [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] — task looper com roadmap de fases, lessons.md, state e handoff como memória entre iterações
- [[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]] — versão leve via prompt/skill, arquivo único `state.md` trackeando tarefa/decisões/erros/arquivos modificados
