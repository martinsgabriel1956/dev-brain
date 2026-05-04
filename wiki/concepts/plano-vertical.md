---
type: concept
title: "Plano Vertical"
aliases: ["vertical plan", "implementação vertical", "plano incremental"]
date_created: 2026-05-04
date_updated: 2026-05-04
source_count: 2
tags: [coding-agents, workflow, rpi, incremental-development]
skill: tech-mentor-ai
status: stable
---

# Plano Vertical

Estratégia de planejamento de implementação onde cada unidade entregue é **testável imediatamente**, em oposição ao plano horizontal que entrega uma camada inteira antes de passar para a próxima.

## Plano Horizontal vs Plano Vertical

**Plano horizontal** (viés natural do modelo):
```
Fase 1: Banco inteiro (todas as migrations, todos os schemas)
Fase 2: Serviços inteiros (todos os serviços)
Fase 3: API inteira (todos os endpoints)
```
Problema: após 1.200 linhas de código, nada é testável. Um erro no banco só é descoberto na fase da API. Refatora três camadas.

**Plano vertical** (uma fatia de ponta a ponta):
```
Fatia 1: Migration de users + UserService.create + POST /users → testável
Fatia 2: Migration de posts + PostService.create + POST /posts → testável
Fatia 3: ...
```
Cada fatia atravessa banco, serviço e API para uma funcionalidade específica. Se há erro, você para imediatamente — sem acumular 1.500 linhas de contexto contaminado.

## Por Que os Modelos Preferem o Plano Horizontal

LLMs têm um viés de treinamento para organizar trabalho por camada técnica (banco → serviço → API), não por funcionalidade. Sem instrução explícita de plano vertical, o modelo quase sempre vai propor o plano horizontal.

Para obter plano vertical: especificar explicitamente na fase de plan que cada entrega deve ser testável antes de prosseguir.

## Relação com PRs

O plano vertical gera PRs pequenos e focados. O plano horizontal gera o "PR horizontal" — o pior tipo para revisar: toca banco, serviço e API de uma vez, sem caminho testável no meio.

Um PR com 2 arquivos (migration + endpoint) é trivial de revisar. Um PR com 50 arquivos cobrindo a feature inteira é uma massa impossível.

Ver [[concepts/vertical-slice-architecture]] para a versão arquitetural desse princípio.

## Relação com Context Window

Plano vertical também beneficia a [[concepts/dumb-zone|smart zone]]: cada entrega é completada e testada com contexto baixo. No plano horizontal, o agente acumula contexto por todas as camadas antes de qualquer validação.

## Key Sources

- [[sources/erros-workflow-research-plan-implement]]
- [[sources/context-engineering-avancado-para-coding-agents]]
