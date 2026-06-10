---
type: source
title: "Formação IA para Devs — Aula 04: Agentes de Planejamento"
aliases: ["Aula Agentes Planejamento", "SDD PRD TechSpec Tarefas Formação"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/Aula 04 - Agentes de Planejamento (Negócio, Design e Arquitetura, Tarefas).md"
source_url: ""
author: "Pedro Nauke, Rodrigo Branas"
date_published: 2026
date_ingested: 2026-06-02
source_count: 0
tags: [spec-driven, prd, tech-spec, agentes, human-in-the-loop, decomposicao-tarefas, formacao-ia-devs]
skill: tech-mentor-ai
status: stable
---

# Formação IA para Devs — Aula 04: Agentes de Planejamento

## TL;DR

Aula central sobre Spec Driven Development, apresentando o fluxo completo: ideia → PRD → Tech Spec → Tarefas decompostas. Demonstra por que prompts simples falham para problemas complexos e como a decomposição em agentes especializados com human-in-the-loop resolve isso. Cada tarefa recebe PRD + Tech Spec isoladamente — não o projeto inteiro de uma vez.

## Key Claims

- Problemas complexos (múltiplos domínios, semanas de trabalho) não podem ser resolvidos com um único prompt nem com Plan Mode
- Fluxo Spec Driven: **PRD** (negócio) → **Tech Spec** (tecnologia) → **Tarefas** (execução)
- Cada etapa requer [[wiki/concepts/human-in-the-loop|human-in-the-loop]] porque envolve decisões de negócio e tecnologia
- O PRD é gerado por um [[wiki/concepts/agente-prd|agente interativo]] que faz perguntas ao usuário para refinar requisitos
- Tech Spec consome o PRD mais rules, skills e análise do código fonte como contexto
- Cada tarefa recebe PRD + Tech Spec + descrição isoladamente — não o projeto inteiro de uma vez
- **"PRD não é um documento feito para a empresa, é um documento feito para a IA"**
- Para projetos grandes: possível adicionar um [[wiki/concepts/task-looper|task looper]] e tarefas de QA automatizadas no final

## Entidades

- [[wiki/entities/pedro-nauke]]
- [[wiki/entities/rodrigo-branas]]
- Google Calendar, Linear, Jira, Trello (exemplos de sistemas)

## Conceitos Relacionados

- [[wiki/concepts/spec-driven-development]]
- [[wiki/concepts/prd-product-requirements-document]]
- [[wiki/concepts/tech-spec]]
- [[wiki/concepts/agente-prd]]
- [[wiki/concepts/human-in-the-loop]]
- [[wiki/concepts/task-looper]]
- [[wiki/concepts/decomposicao-de-tarefas]]
- [[wiki/concepts/context-engineering-harness]]
- [[wiki/concepts/ciclo-agente]]

## Quotes

> "A ideia do Spec Driven é pegar um problema que geralmente é complexo, que demora para fazer, que tem várias etapas, que não é possível de ser feito diretamente. Vamos converter com o apoio da pessoa que está conduzindo. E a gente vai passar o PRD, a Tech Spec, e isoladamente cada tarefa. Uma hora vai ser a tarefa 1. Quando ela acabar vai ser a tarefa 2."

> "PRD não é um documento feito para a empresa, é um documento feito para a IA."

## Open Questions

- Qual o tamanho ideal de uma tarefa no processo Spec Driven (granularidade)?
- Como o agente de PRD lida com requisitos ambíguos sem interação humana excessiva?
- Spec Driven se aplica a refactoring e migrações além de features novas? (respondido na Aula 05: sim)
