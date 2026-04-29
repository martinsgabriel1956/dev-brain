---
type: source
title: "Model Context Protocol (MCP)"
aliases: ["mcp", "model context protocol", "mcp tools", "mcp resources"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mcp.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [mcp, model-context-protocol, tools, resources, prompts, sampling, streamable-http, stdio, mcp-oauth, a2a-protocol, multi-tenant]
skill: tech-mentor-ai
status: stable
---

## TL;DR

MCP é o protocolo padrão (Anthropic, 2024) para conectar LLMs a tools e dados externos. 4 primitivas: Tools (ações com efeito), Resources (dados read-only, cacheable), Prompts (templates reutilizáveis), Sampling (server pede completion ao client). Transporte: stdio para processos locais, Streamable HTTP para servidores remotos. A2A (Google) é o protocolo equivalente para comunicação entre agentes.

## Key Claims

**Claim:** MCP padroniza a interface LLM↔tools — evita implementações proprietárias por provider.
**Evidence:** Antes do MCP, cada integração (LangChain, LlamaIndex, custom) tinha formato próprio. MCP define schema JSON-RPC 2.0 para tools, resources e prompts. Suportado por Claude, Cursor, Windsurf, e crescendo em outros clientes.
**Confidence:** alta

**Claim:** Tools têm efeitos colaterais; Resources são read-only e cacheable — distinção crítica.
**Evidence:** Tool: executa ação (cria pedido, envia e-mail, executa SQL). Resource: lê dado sem efeito (schema do banco, documentação, perfil de cliente). Resources podem ser cacheados pelo cliente. Tools nunca devem ser idempotentes por padrão.
**Confidence:** alta

**Claim:** Streamable HTTP é o transporte padrão para servidores remotos — substitui SSE.
**Evidence:** Endpoint único (`/mcp`). Suporta streaming via SSE quando necessário. Stateless por padrão (compatível com serverless). Requer auth via MCP OAuth para servidores públicos.
**Confidence:** alta

**Claim:** Multi-tenant MCP requer isolamento de sessão — contexto de um tenant não pode vazar para outro.
**Evidence:** Cada sessão recebe um contexto isolado. Tools de filesystem (MCP Roots) limitam acesso por escopo definido na inicialização. Sem isolamento, uma tool poderia acessar arquivos de outros tenants.
**Confidence:** alta

**Claim:** A2A (Google) é o protocolo complementar ao MCP para comunicação agent-to-agent.
**Evidence:** MCP: LLM ↔ tools/dados. A2A: agente ↔ agente (delegação de tasks, handoff, colaboração). A2A usa AgentCards (discovery), Tasks (unidade de trabalho), e Streams (resultados parciais). Complementar — não substituto.
**Confidence:** média

## Entities & Concepts Touched

- [[concepts/mcp-protocol]]
- [[concepts/tool-use-agents]]
- [[concepts/a2a-protocol]]
- [[concepts/mcp-oauth]]
- [[concepts/streamable-http]]

## Open Questions

- MCP Roots limita filesystem — como lidar com tools que precisam acessar múltiplos diretórios com escopos diferentes?
- A2A vs MCP Sampling: quando usar cada um para comunicação entre agentes?
