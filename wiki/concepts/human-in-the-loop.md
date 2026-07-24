---
type: concept
title: "Human-in-the-Loop (HITL)"
aliases: ["HITL", "human in the loop", "aprovação humana agente"]
date_created: 2026-06-02
date_updated: 2026-07-24
source_count: 3
tags: [hitl, human-in-the-loop, agente, spec-driven, aprovacao, controle]
skill: tech-mentor-ai
status: stable
---

# Human-in-the-Loop (HITL)

## TL;DR

Padrão onde o humano intervém e aprova decisões em pontos específicos do fluxo de um agente. Garante que decisões de negócio e tecnologia não sejam tomadas autonomamente pela IA em problemas complexos.

## Por que é Necessário

Agentes operam bem em escopo delimitado com critérios claros. Problemas complexos envolvem decisões com implicações de negócio, arquitetura ou experiência do usuário que a IA não tem autoridade para tomar autonomamente. O HITL preserva o controle humano sem eliminar a autonomia de execução.

## HITL no Spec Driven Development

No [[wiki/concepts/spec-driven-development|Spec Driven Development]], o HITL ocorre em três etapas obrigatórias:

| Etapa | Decisão humana |
|-------|----------------|
| **PRD** | "É isso que eu quero construir?" |
| **Tech Spec** | "É assim que eu quero construir?" |
| **Tarefas** | "Esta lista e ordem fazem sentido?" |

Após aprovação em cada etapa, a execução da etapa seguinte pode ser autônoma.

## Granularidade do HITL

| Nível | Exemplo | Overhead |
|-------|---------|----------|
| **Por tool call** | Aprovar cada `Edit` individualmente | Alto |
| **Por plan** | Plan Mode — revisar plano antes de executar | Médio |
| **Por etapa SDD** | Aprovar PRD → Tech Spec → Tarefas | Baixo |
| **Por deploy** | Revisar PR após execução completa | Mínimo |

O [[wiki/concepts/plan-mode|Plan Mode]] é uma forma leve de HITL: o humano revisa a intenção antes da execução sem aprovar cada ferramenta individualmente.

## HITL como "Nível 3" do Dev Loop

[[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] posiciona o humano-no-loop como o terceiro de três níveis do dev loop (loop React → spec driven → humano decide o próximo passo entre specs — abre PR, triagem de bug, consulta métricas). [[wiki/concepts/loop-engineering|Loop engineering]] é proposto como uma quarta camada que automatiza justamente essa decisão que hoje cabe ao humano nesse nível — mas a fonte é explícita que o loop não decide sozinho *qual* o próximo roadmap: essa continua sendo uma decisão humana mesmo em loops avançados ("loop criador").

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-04-agentes-planejamento]]
- [[wiki/sources/formacao-ia-devs-aula-05-qa]]
- [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] — HITL como nível 3 do dev loop; loop engineering automatiza a execução entre specs mas não a decisão de intenção/roadmap
