---
type: source
title: "Formação IA para Devs — Aula 03: Plan Mode"
aliases: ["Aula Plan Mode Formação", "Plan Mode Claude Code Aula"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/Aula 03 - Plan Mode.md"
source_url: ""
author: "Pedro Nauke, Rodrigo Branas"
date_published: 2026
date_ingested: 2026-06-02
source_count: 0
tags: [plan-mode, spec-driven, harness, context-engineering, formacao-ia-devs]
skill: tech-mentor-ai
status: stable
---

# Formação IA para Devs — Aula 03: Plan Mode

## TL;DR

Plan Mode (ativado via Shift+Tab) é um recurso embutido nos harnesses que força a LLM a gerar um plano estruturado antes de executar qualquer ação. Serve como ponte entre prompts simples e Spec Driven Development — indicado para tarefas de complexidade média. Uma boa prática é persistir o plano aprovado em arquivo dentro do projeto.

## Key Claims

- Plan Mode é ativado com Shift+Tab na maioria dos harnesses e força planejamento antes de execução
- O Codex não salva o plano em documento automaticamente — recomenda-se configurar o harness para fazê-lo
- Planos devem ser salvos com timestamp e slug para rastreabilidade ao longo do projeto
- **Guideline de granularidade:** prompt simples → execução direta; 2-3 arquivos → Plan Mode; múltiplos domínios (front+back) → Spec Driven Development
- Plan Mode pode ser emulado manualmente usando uma [[wiki/concepts/skills-agente|skill]] que induza o harness a planejar primeiro
- Sem Plan Mode, o harness tende a iniciar execução imediata sem explorar alternativas
- O plano aprovado deve ser atualizado se modificado posteriormente, mantendo o rastreamento histórico

## Entidades

- [[wiki/entities/pedro-nauke]]
- [[wiki/entities/rodrigo-branas]]
- [[wiki/entities/anthropic]] — Claude Code
- [[wiki/entities/codex-openai]] — Codex

## Conceitos Relacionados

- [[wiki/concepts/plan-mode]]
- [[wiki/concepts/spec-driven-development]]
- [[wiki/concepts/harness]]
- [[wiki/concepts/skills-agente]]
- [[wiki/concepts/ciclo-agente]]
- [[wiki/concepts/degradacao-de-contexto]]

## Quotes

> "Plan Mode é uma maneira já embutida dentro do Harness que permite que a LLM faça um plano antes de te entregar o resultado. Antes de ele fazer a execução, ele vai gerar uma espécie de documento ou plano para você."

> "Coisas muito pontuais, vai lá, aponta para qual é o arquivo, qual é a linha, o que você quer fazer, manda ver. É uma coisa que já mexe em dois, três arquivos, um pouquinho mais robusta, Plan Mode. É uma coisa que já mexe em vários lugares, em front-back, tarefinha já mais média, Spec Driven."

## Open Questions

- Como integrar Plan Mode com Spec Driven em projetos que usam task loopers automatizados?
- O plano salvo em arquivo serve como input direto para o agente de tech spec?
