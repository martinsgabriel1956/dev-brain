---
type: source
title: "Formação IA para Devs — Aula 01: MCPs Parte 1"
aliases: ["Aula MCP Parte 1", "MCP Introdução Formação"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/Aula 01 - MCPs - Parte 1.md"
source_url: ""
author: "Pedro Nauke, Rodrigo Branas"
date_published: 2026
date_ingested: 2026-06-02
source_count: 0
tags: [mcp, model-context-protocol, harness, tools, json-rpc, formacao-ia-devs]
skill: tech-mentor-ai
status: stable
---

# Formação IA para Devs — Aula 01: MCPs Parte 1

## TL;DR

Aula introdutória ao MCP criado pela Anthropic como solução para padronização de tools expostas a LLMs. Explica a arquitetura de três componentes (host, client, server) e os mecanismos de transporte. O MCP resolve o problema de integração fragmentada de tools, oferecendo um contrato único via JSON-RPC.

## Key Claims

- O MCP foi criado para resolver o problema de agrupamento e gerenciamento de tools — antes não havia uma maneira padronizada de expô-las a LLMs
- Arquitetura: **host** (o harness — Claude Code, Cursor, Codex), **client** (instância de conexão dentro do host), **server** (executável que se mantém em execução contínua)
- O server MCP deve permanecer em execução; não é um processo que sobe e cai
- O protocolo usa JSON-RPC para troca de mensagens entre client e server
- O handshake de conexão explica o tempo de inicialização visível ao abrir Claude Code, Cursor ou Codex
- MCPs populares citados: Figma, banco de dados, Atlassian, Supabase, Databricks, GitHub
- Com o surgimento das [[wiki/concepts/skills-agente|Skills]] como mecanismo alternativo, o MCP passou a ter "concorrência"
- A aula faz parte do mesmo módulo que a Aula 03 (Spec Driven Development)

## Entidades

- [[wiki/entities/anthropic]] — criadora do MCP
- [[wiki/entities/pedro-nauke]] — instrutor
- [[wiki/entities/rodrigo-branas]] — instrutor

## Conceitos Relacionados

- [[wiki/concepts/model-context-protocol]]
- [[wiki/concepts/mcp-arquitetura]]
- [[wiki/concepts/tool-call]]
- [[wiki/concepts/harness]]
- [[wiki/concepts/skills-agente]]
- [[wiki/concepts/sensores-vs-guias]]

## Quotes

> "A principal dor que o MCP quis resolver foi a questão de manipulação e uso de tools. O grande problema que a gente tinha antes do MCP é que tu não tinha uma maneira de agrupar todas as tools juntas."

> "O server MCP é qualquer tipo de executável. A única característica é que ele tem que se manter em pé. Ele não é um executável que tu vai executar e ele vai cair, ele tem que se manter sempre run."

## Open Questions

- Quando usar MCP versus CLI para integração com serviços (ex: GitHub, AWS)? A aula sugere preferência por CLI quando disponível, mas não formaliza o critério de decisão — ver [[wiki/sources/formacao-ia-devs-aula-02-mcp-parte2]] para continuação.
