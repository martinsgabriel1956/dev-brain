---
type: source
title: "Formação IA para Devs — Aula 01: Abertura"
aliases: ["IA para Devs Aula 1", "Abertura Formação IA"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 0
tags: [ia-para-devs, formacao, abertura, llm, harness, spec-driven]
skill: tech-mentor-ai
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/Aula 01 - Abertura.md"
source_url: ""
author: "Rodrigo Branas, Pedro Nauke"
date_published: "2026"
date_ingested: 2026-06-02
---

# Formação IA para Devs — Aula 01: Abertura

## TL;DR

Aula inaugural do Módulo 1 ("Processo de Desenvolvimento com IA") da Formação IA para Devs, conduzida por Rodrigo Branas e Pedro Nauke. A aula apresenta o escopo do módulo — LLM, harness, prompt engineering, spec-driven development e subagentes — e contextualiza o nível de maturidade do mercado. É explicitamente introdutória mas serve como bússola para as aulas seguintes.

## Key Claims

- **Curso já treinou 3.500+ pessoas** no Brasil e internacionalmente (Vietnã, Singapura). Evidência: declaração dos instrutores na abertura.
- **Desníveis de adoção são normais**: vai desde quem cola código do ChatGPT até quem constrói pipelines autônomos de correção de bugs. Evidência: relato da experiência dos instrutores com múltiplas turmas.
- **Desenvolvimento autônomo custa ~$500/dia** com ferramentas como Devin. Evidência: Pedro Nauke menciona o custo operacional do pipeline da empresa.
- **Objetivo do módulo**: transformar o processo de desenvolvimento em algo que suporte paralelismo de tarefas via spec-driven + subagentes. Evidência: roadmap explicitado por Branas.
- **Módulo não cobre**: assistentes tipo OpenClaw (módulo 3); arquitetura de soluções (módulo 2 — ainda não gravado na época).

## Estrutura do Módulo (roadmap explicitado)

| Aula | Foco |
|---|---|
| Aula 1 | LLM, Harness, Prompt Engineering |
| Aula 2 | Context Engineering — rules, skills, MCPs |
| Aula 3 (final aula 2 / início aula 3) | Spec-Driven Development — fase de planejamento |
| Aula 4 | Execução — implementação, verificação, QA, subagents |

## Entities

- [[wiki/entities/rodrigo-branas]] — 25 anos de dev, 15 anos ensinando, 18 meses focado em IA; canal no YouTube; palestras de IA, DDD, blockchain.
- [[wiki/entities/pedro-nauke]] — 22 anos de programador; criador do [[wiki/entities/compose-tool]] (~600 stars GitHub); foco em tooling, Rust, Go; usa spec-driven extensivamente.

## Concepts Introduced

- [[wiki/concepts/harness]] — ferramental ao redor do modelo LLM
- [[wiki/concepts/spec-driven-development]] — abordagem planning-first para desenvolvimento com IA
- [[wiki/concepts/niveis-adocao-ia-l0-l4]] — escada de maturidade no uso de IA para devs
- [[wiki/concepts/paralelismo-de-tarefas-ia]] — rodar múltiplas tasks simultâneas via worktree + spec
- [[wiki/concepts/agente-autonomo]] — execução sem supervisão contínua (YOLO/unattended mode)

## Open Questions

- Qual o breakeven real entre ferramentas como Devin ($500/dia) e contratação de devs adicionais?
- Como o módulo 3 (assistentes) vai se conectar com as técnicas de harness do módulo 1?

## Raw Quotes

> "Hoje a gente tem investido cerca de 500 dólares por dia nesse tipo de ferramenta, então você coloca aí a conta mensal, muitas vezes sai cara." — Pedro Nauke

> "Esse é o curso de processo de desenvolvimento de software com IA." — Rodrigo Branas
