---
type: concept
title: "Plano Vertical"
aliases: ["vertical plan", "implementação vertical", "plano incremental"]
date_created: 2026-05-04
date_updated: 2026-08-20
source_count: 3
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

## Fatia Vertical Também na Divisão do Trabalho, Não Só no Plano do Agente

[[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] aplica a mesma lógica de "fatia de ponta a ponta" a um nível diferente: não ao plano de implementação de um agente dentro de uma tarefa, mas à divisão do trabalho **entre pessoas** de um time. A fonte contrasta a separação tradicional por camada técnica (um dev forte em back, outro forte em front, cada um entregando sua parte horizontal) com um arranjo vertical: uma pessoa com bom domínio do negócio entrega a feature inteira de ponta a ponta, apoiada por agentes cobrindo a lacuna técnica na ponta em que ela é mais fraca. O argumento é o mesmo desta página em espírito — menos costura entre partes entregues isoladamente, contexto acumulado numa única linha de responsabilidade em vez de fragmentado entre pessoas — mas o "erro descoberto tarde" que a fonte quer evitar não é um bug de implementação, é o retrabalho de handoff entre duas pessoas que só descobrem a divergência na hora de integrar.

## Key Sources

- [[sources/erros-workflow-research-plan-implement]]
- [[sources/context-engineering-avancado-para-coding-agents]]
- [[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] — mesma lógica de fatia vertical aplicada à divisão de tarefas entre pessoas do time, não só ao plano de implementação de um agente
