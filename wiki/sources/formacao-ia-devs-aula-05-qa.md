---
type: source
title: "Formação IA para Devs — Aula 05: Q&A"
aliases: ["Aula 05 QA Formação", "Q&A Spec Driven MCP PRD"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/Aula 05 - Q&A.md"
source_url: ""
author: "Pedro Nauke, Rodrigo Branas"
date_published: 2026
date_ingested: 2026-06-02
source_count: 0
tags: [spec-driven, prd, rules, cli-vs-mcp, degradacao-de-contexto, formacao-ia-devs]
skill: tech-mentor-ai
status: stable
---

# Formação IA para Devs — Aula 05: Q&A

## TL;DR

Sessão de perguntas e respostas sobre cenários práticos do Spec Driven Development e MCP: o que fazer quando tokens acabam no meio de um processo, onde definir padrões de arquitetura, como iniciar um projeto do zero, e a diferença entre MCP e CLI em termos de consumo de contexto.

## Key Claims

- Quando tokens acabam no meio de um Spec Driven, o comando **Resume** retoma exatamente de onde parou
- Cada tarefa do Spec Driven é curta o suficiente para que interrupções causem perda mínima — pode-se reexecutar apenas a tarefa interrompida
- Padrões de arquitetura (framework, linguagem, infraestrutura) ficam em [[wiki/concepts/rules-agente|rules]], não no PRD ou Tech Spec
- PRD e Tech Spec referenciam as rules mas não as repetem
- Para projetos do zero: define-se primeiro o esqueleto base (agents.md, skills) antes de entrar no Spec Driven
- MCP consome mais contexto que CLI por registrar muitas tools; com 1M tokens a diferença é menos crítica
- O file system é o padrão de mercado para fornecer contexto à IA — mais eficiente que requests a APIs externas
- **Spec Driven funciona para features, refactoring e migrações** (confirmado nesta Q&A)

## Entidades

- [[wiki/entities/pedro-nauke]]
- [[wiki/entities/rodrigo-branas]]
- [[wiki/entities/anthropic]] — Claude Code
- [[wiki/entities/codex-openai]] — Codex
- Cloudflare, React, Mastra (tecnologias mencionadas)

## Conceitos Relacionados

- [[wiki/concepts/spec-driven-development]]
- [[wiki/concepts/degradacao-de-contexto]]
- [[wiki/concepts/rules-agente]]
- [[wiki/concepts/context-engineering-harness]]
- [[wiki/concepts/cli-vs-mcp]]
- [[wiki/concepts/human-in-the-loop]]
- [[wiki/concepts/prd-product-requirements-document]]
- [[wiki/concepts/tech-spec]]

## Quotes

> "Você pode inclusive fechar a janela e depois se você der o Resume, ele vai voltar exatamente daquela parte."

> "Esses padrões ficam no projeto. Os PRD e TechSpec não precisam repetir de novo, eles vão no máximo referenciar esses padrões. É rule."

## Open Questions

- Como estruturar o discovery inicial de um projeto open source antes do Spec Driven?
- Existe um template padrão para o agents.md do esqueleto base de projeto?
