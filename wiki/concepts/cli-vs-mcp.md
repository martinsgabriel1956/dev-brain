---
type: concept
title: "CLI vs MCP — Critério de Decisão"
aliases: ["cli vs mcp", "quando usar mcp", "quando usar cli"]
date_created: 2026-06-02
date_updated: 2026-09-14
source_count: 3
tags: [mcp, cli, context-engineering, harness, decisao]
skill: tech-mentor-ai
status: stable
---

# CLI vs MCP — Critério de Decisão

## Diferença Fundamental

| Aspecto | CLI | MCP |
|---------|-----|-----|
| **Conhecimento** | Usa conhecimento de treinamento da LLM sobre a ferramenta | Expõe tools explícitas e fechadas |
| **Contexto** | Tende a economizar contexto | Consome mais contexto (tools registradas) |
| **Descoberta** | Baseada em help flags e docs no treinamento | Dinâmica (antes: via handshake; ver nota abaixo) |
| **Controle** | Menor (LLM escolhe os flags) | Maior (tools delimitadas) |
| **Manutenção** | Zero (usa CLI existente) | Requer implementar e manter o server |

## Quando Usar CLI

- Quando a ferramenta tem CLI bem documentada e o LLM conhece bem (ex: `aws`, `gh`, `git`, `kubectl`)
- Quando o objetivo é economizar contexto
- Para operações pontuais sem necessidade de feedback estruturado

## Quando Usar MCP

- Para fornecer **sensores** ao LLM — mecanismos de verificação e autocorreção (ex: executar queries no banco e checar resultado)
- Quando as ferramentas não têm CLI ou têm APIs proprietárias
- Quando se quer delimitar exatamente o que o LLM pode fazer (tools fechadas)
- Para integrações com produtos que já oferecem MCP nativamente (ex: Salesforce, Supabase)

## Padrão Emergente

A IA trabalha melhor com documentos no file system do que com requests a APIs externas. Quando possível, prefer trazer o contexto para o sistema de arquivos ao invés de criar MCPs que fazem fetch de APIs externas em tempo real.

## Nota (2026): Descoberta Deixa de Depender de Handshake

Segundo [[wiki/sources/mcp-stateless-fim-do-handshake-server-discover-lucas-montano]], a spec core do MCP passou a ser stateless — a descoberta de tools/capabilities passa a acontecer via um método `server discover`, sem exigir a sessão/handshake que a tabela acima descrevia como base da "descoberta dinâmica" do MCP. O contraste MCP vs. CLI (tools fechadas vs. conhecimento de treinamento) continua válido; o mecanismo de descoberta é que muda. Ver [[wiki/concepts/mcp-stateless-server-discover]].

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-02-mcp-parte2]]
- [[wiki/sources/formacao-ia-devs-aula-05-qa]]
- [[wiki/sources/mcp-stateless-fim-do-handshake-server-discover-lucas-montano]] — descoberta via `server discover` em vez de handshake
