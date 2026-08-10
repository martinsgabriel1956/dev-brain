---
type: concept
title: "Planner-Executor-Critic (PEC)"
aliases: ["PEC", "planner executor critic", "loop reflexivo", "planner critic"]
date_created: 2026-07-10
date_updated: 2026-08-05
source_count: 3
tags: [planner-executor-critic, agentes, multi-agente, orquestracao, rubrica, verificador]
skill: tech-mentor-ai
status: stable
---

# Planner-Executor-Critic (PEC)

Padrão arquitetural de agentes em três papéis: um **Planner** decompõe a tarefa e gera instruções (e critérios de aceite) para subtarefas; um ou mais **Executores** (subagentes) realizam cada subtarefa; um **Critic**/verificador julga o resultado e decide entre aprovar ou devolver com feedback para nova tentativa.

## O Problema que Resolve

Agentes que executam diretamente, sem planejar nem validar, cometem erros que só são percebidos tarde — ou nunca são percebidos, porque ninguém verifica o resultado contra um critério explícito.

## Os Três Papéis

```
Entrada do usuário (ou evento/schedule)
        │
        ▼
   ┌──────────┐   prompt + rubrica   ┌───────────┐
   │ Planner  │ ────────────────────►│ Executor  │
   └──────────┘                      │(subagente)│
        ▲                            └───────────┘
        │                                  │
        │        aprovado / follow-up      │
        │                                  ▼
        │                            ┌──────────┐
        └──────── critique ──────────│  Critic  │
                                      │(verificador)│
                                      └──────────┘
```

1. **Planner** — recebe a entrada, decompõe em subtarefas (num exemplo documentado, até ~160 simultâneas), e para cada uma gera: objetivo, papel, resultado esperado, fontes sugeridas e uma **[[wiki/concepts/rubrica-de-verificacao|rúbrica]]** — os critérios que definem "tarefa cumprida". Tarefas de planejamento se beneficiam de um modelo mais forte (ex.: GPT-5.5), por exigirem mais raciocínio.
2. **Executor** — o subagente que recebe o prompt gerado dinamicamente e produz o resultado. Ver [[wiki/concepts/subagentes]].
3. **Critic/Verificador** — **obrigatoriamente um modelo diferente** do executor, para evitar que o mesmo viés valide a própria saída. Recebe a rúbrica e o resultado, e decide aprovar ou gerar um follow-up específico (ex.: "reescreva incluindo uma tabela markdown com colunas"). O critério de quantas tentativas de follow-up ocorrem antes de desistir é definido por quem constrói o sistema, não pela LLM.

## Por Que o Verificador Precisa Ser Outro Modelo

Usar o mesmo modelo para gerar e validar a própria resposta preserva o viés que produziu o erro em primeiro lugar. Um segundo modelo, sem o mesmo histórico de geração, avalia a saída de forma mais independente contra a rúbrica.

## Relação com Reflection Loop

PEC generaliza o padrão de Reflection Loop (gerar → criticar → regenerar, um único agente se autocorrigindo) para múltiplos subagentes especializados, cada um com seu próprio ciclo planner→executor→critic.

## Risco: Vira "Monstrinho" sem Critério de Parada

Sem rúbrica explícita e sem limite de tentativas definido deterministicamente, o padrão degenera no problema histórico de loops autônomos tipo AutoGPT — roda indefinidamente sem garantia de convergência. Ver [[wiki/concepts/loop-engineering]].

## Key Sources

- [[wiki/sources/agentes-orquestracao]] — definição original do padrão como "loop reflexivo", citado junto com Supervisor, Handoff e Swarm como um dos 4 padrões principais de multi-agente
- [[wiki/sources/loop-engineering-planner-critic-grafo]] — demonstração em vídeo do padrão em produção: planner gerando 4 prompts+rúbricas simultâneos, verificador com 3 tentativas de follow-up
- [[wiki/sources/graph-engineering-do-loop-ao-grafo]] — reforça o papel da rúbrica/checklist como o "peso" da aresta num [[wiki/concepts/grafo-como-abstracao-de-agentes|grafo]], notando que esse checklist em algum momento envolve aprovação humana
