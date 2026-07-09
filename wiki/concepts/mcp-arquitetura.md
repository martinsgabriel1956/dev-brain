---
type: concept
title: "MCP — Arquitetura Host/Client/Server"
aliases: ["mcp arquitetura", "mcp host client server", "mcp componentes"]
date_created: 2026-06-02
date_updated: 2026-07-09
source_count: 3
tags: [mcp, arquitetura, host, client, server, json-rpc, stdio, sse, streamable-http]
skill: tech-mentor-ai
status: stable
---

# MCP — Arquitetura Host/Client/Server

## Três Componentes

```
[Host]           [Client]        [Server]
Claude Code  →   conexão MCP  →  executável em execução
Cursor           instância       banco de dados
VS Code          de conexão      filesystem
Codex                            API interna
```

| Componente | O que é | Característica |
|------------|---------|----------------|
| **Host** | O harness (Claude Code, Cursor, Codex) | Gerencia a sessão e o contexto |
| **Client** | Instância de conexão dentro do host | Uma por servidor MCP conectado |
| **Server** | Executável que expõe tools/resources/prompts | **Deve permanecer em execução contínua** |

## O Server Deve Permanecer em Pé

Diferente de um script que sobe e cai, o server MCP mantém estado e conexão ativa. Isso explica o tempo de inicialização visível ao abrir Claude Code, Cursor ou Codex: é o handshake entre host e os servers registrados.

## Transportes

| Transporte | Uso | Característica |
|------------|-----|----------------|
| **stdio** | Processos locais | Host spawna o processo; stdin/stdout como canal; latência zero; ideal para CLI e integrações locais |
| **SSE** (Server-Sent Events) | Servidores remotos (legado) | HTTP + push de eventos; multi-tenant; deprecated em favor de Streamable HTTP |
| **Streamable HTTP** | Servidores remotos (atual) | Substituto moderno do SSE; suporta streaming bidirecional |

## Protocolo de Mensagens

O MCP usa **JSON-RPC 2.0** para troca de mensagens entre client e server. O handshake inicial define:
- Versão do protocolo
- Capacidades do server (quais tools, resources e prompts estão disponíveis)
- Configurações de sessão

## Custo de Contexto

Cada tool registrada pelo MCP ocupa espaço no contexto quando listada para o LLM. Servidores com muitas tools consomem mais tokens. Com janelas de 1M tokens isso é menos crítico, mas continua sendo um fator em projetos com dezenas de MCPs registrados.

## MCP como Hype em Formação

Citado como exemplo de hype tecnológico em formação (junto com Vibe Coding) em [[wiki/sources/como-identificar-o-proximo-hype-tecnologico]] — um dos sinais de assunto "pipocando" repetidamente em múltiplos canais ao mesmo tempo. Ver [[wiki/concepts/avaliar-hype-tecnologico]] para o modelo de decisão sobre embarcar ou não num hype como este.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-01-mcp-parte1]]
- [[wiki/sources/formacao-ia-devs-aula-02-mcp-parte2]]
- [[wiki/sources/como-identificar-o-proximo-hype-tecnologico]]
