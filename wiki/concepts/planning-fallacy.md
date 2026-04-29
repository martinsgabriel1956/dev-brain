---
type: concept
title: "Planning Fallacy"
aliases: ["viés de planejamento", "planning fallacy", "subestimação de esforço"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [psicologia, estimativa, projetos, produtividade, carreira]
skill: tech-mentor-leadership
status: stable
---

# Planning Fallacy

Tendência cognitiva de subestimar o tempo, custo e riscos de tarefas futuras enquanto superestima os benefícios — especialmente em tarefas desconhecidas. Cunhado por Kahneman e Tversky (1979).

## Por Que Devs São Especialmente Vulneráveis

- Muitas tarefas envolvem domínios novos (frameworks, APIs, infra)
- O Efeito Dunning-Kruger amplifica: quanto menos sabe, mais confiante na estimativa
- Complexidade oculta só emerge durante a construção, não durante o planejamento

## Manifestação em Projetos Paralelos

```
Estimativa mental: "2 fins de semana"
Realidade: auth sozinho leva 1 semana
→ escopo creep para compensar → projeto abandona
```

## Contramedidas

- **Reference class forecasting**: quanto tempo projetos *similares* levaram, não o atual
- **[[concepts/mvp]]**: escopo mínimo reduz exposição à planning fallacy
- **Pre-mortem**: imaginar que o projeto falhou e identificar por quê antes de começar

## Ver Também

- [[concepts/scope-creep]] — consequência direta da planning fallacy
- [[concepts/dopamina-e-projetos]] — otimismo na ideação amplifica o viés

## Key Sources

- [[sources/por-que-devs-nao-terminam-projetos]]
