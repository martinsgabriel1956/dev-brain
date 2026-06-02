---
type: concept
title: "Human-in-the-Loop (HITL)"
aliases: ["HITL", "human in the loop", "aprovação humana agente"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 2
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

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-04-agentes-planejamento]]
- [[wiki/sources/formacao-ia-devs-aula-05-qa]]
