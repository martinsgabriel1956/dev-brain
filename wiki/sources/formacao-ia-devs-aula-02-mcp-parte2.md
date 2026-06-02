---
type: source
title: "Formação IA para Devs — Aula 02: MCPs Parte 2"
aliases: ["Aula MCP Parte 2", "MCP Prática Sensores"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/Aula 02 - MCPs - Parte 2.md"
source_url: ""
author: "Pedro Nauke, Rodrigo Branas"
date_published: 2026
date_ingested: 2026-06-02
source_count: 0
tags: [mcp, sensores, cli-vs-mcp, harness, banco-de-dados, playwright, formacao-ia-devs]
skill: tech-mentor-ai
status: stable
---

# Formação IA para Devs — Aula 02: MCPs Parte 2

## TL;DR

Continuação prática do MCP, mostrando como construir um servidor MCP que conecta ao banco de dados como "sensor" para a LLM. Contrasta MCP com CLI e explica que a tendência de mercado é que empresas ofereçam MCPs como interface principal para seus produtos (ex: Salesforce).

## Key Claims

- MCPs são ideais para fornecer **sensores** — mecanismos que permitem à LLM verificar se o que ela fez funciona (ex: executar queries no banco e autocorrigir erros)
- A diferença entre MCP e CLI: CLI usa o conhecimento de treinamento da LLM; MCP oferece tools explícitas e fechadas; CLI tende a economizar contexto
- A tendência é que empresas como Salesforce passem a oferecer MCPs como interface principal para seus produtos
- Playwright pode atuar como sensor relevante, fornecendo interface com o browser para testes
- O padrão emergente: IA trabalha melhor com arquivos no file system do que com requests a APIs externas
- MCPs com muitas tools registradas consomem mais contexto; com 1M tokens isso é menos crítico

## Entidades

- [[wiki/entities/pedro-nauke]]
- [[wiki/entities/rodrigo-branas]]
- [[wiki/entities/anthropic]]
- Salesforce, AWS, Playwright (ferramentas)

## Conceitos Relacionados

- [[wiki/concepts/model-context-protocol]]
- [[wiki/concepts/mcp-arquitetura]]
- [[wiki/concepts/sensores-vs-guias]]
- [[wiki/concepts/cli-vs-mcp]]
- [[wiki/concepts/context-engineering-harness]]
- [[wiki/concepts/harness]]

## Quotes

> "Você precisa de duas coisas. Você precisa de guias e sensores. Esses guias é tudo aquilo que proativamente mostra para a LLM o caminho que ela deve seguir. A outra parte é você fornecer coisas que permitem que a LLM entenda se aquilo que ela fez de fato funciona ou não."

> "A IA trabalha melhor com documentos do file system para contexto. Não é o melhor dos casos, é o standard."

## Open Questions

- Qual o critério definitivo para escolher MCP versus CLI em projetos de produção?
- Como gerenciar múltiplos MCPs sem degradar o contexto disponível?
