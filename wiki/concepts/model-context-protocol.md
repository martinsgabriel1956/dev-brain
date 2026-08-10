---
type: concept
title: "Model Context Protocol (MCP)"
aliases: ["MCP", "model context protocol", "protocol mcp"]
date_created: 2026-06-02
date_updated: 2026-08-06
source_count: 5
tags: [mcp, model-context-protocol, tools, harness, json-rpc, anthropic]
skill: tech-mentor-ai
status: stable
---

# Model Context Protocol (MCP)

## TL;DR

Protocolo aberto criado pela Anthropic para padronizar como LLMs se conectam a ferramentas, dados e serviços externos. Funciona como "USB-C para integrações de IA": define um contrato único que qualquer host (Claude Code, Cursor, VS Code) e qualquer servidor (banco de dados, APIs, filesystems) pode implementar.

## Problema que Resolve

Antes do MCP, cada integração de LLM era proprietária — tool calling do OpenAI, plugins do ChatGPT, function calling do Gemini. Não havia maneira de agrupar múltiplas tools em um único ponto de integração reutilizável entre diferentes clientes.

## Três Primitivas

| Primitiva | Descrição | Exemplo |
|-----------|-----------|---------|
| **Tools** | Funções que o LLM pode invocar | `run_query`, `create_issue` |
| **Resources** | Dados que o LLM pode ler | arquivos, registros de banco |
| **Prompts** | Templates reutilizáveis com argumentos | prompt de revisão de PR |

## Arquitetura

Ver [[wiki/concepts/mcp-arquitetura]] para detalhes sobre host, client e server.

## MCP vs Skills

Com o surgimento das [[wiki/concepts/skills-agente|Skills]] como mecanismo alternativo de extensão de comportamento, o MCP passou a ter "concorrência". A distinção prática:

- **MCP**: expõe ferramentas externas (banco de dados, APIs, sistemas) ao LLM
- **Skills**: encapsula comportamentos e workflows do próprio harness

Exemplo concreto dessa distinção fora do ecossistema Claude: o assistente de IA embutido no Grafana Cloud usa MCP-like access a Prometheus/Loki/Tempo para os dados em si, mas oferece separadamente uma configuração de "skills" — contexto adicional ensinando o que colunas/campos específicos de uma fonte de dados significam, quando essa fonte é pouco padronizada. Não verificado se "skills" nesse produto é tecnicamente análogo às [[wiki/concepts/skills-agente|Skills]] do harness Claude ou apenas terminologia própria do produto.

## Decisão: MCP vs CLI

Ver [[wiki/concepts/cli-vs-mcp]].

## Tendência de Mercado

A tendência é que empresas como Salesforce passem a oferecer MCPs como interface principal para seus produtos, no lugar de (ou complementando) APIs REST tradicionais.

## Caso de uso: observabilidade

MCPs de domínio (Tools que expõem um backend inteiro, não uma função isolada) permitem que um agente correlacione dados sem que o humano escreva a query manualmente — ex. um MCP de Grafana expondo Prometheus/Loki/Tempo para investigação de incidentes. Ver [[wiki/concepts/investigacao-de-incidentes-com-ia-e-mcp]].

## Key Sources

- [[wiki/sources/mcp]]
- [[wiki/sources/formacao-ia-devs-aula-01-mcp-parte1]]
- [[wiki/sources/formacao-ia-devs-aula-02-mcp-parte2]]
- [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]] — Grafana MCP como exemplo de MCP de domínio para observabilidade
- [[wiki/sources/monitoramento-aplicacoes-ia-grafana-cloud-opentelemetry]] — configuração de "skills" no assistente do Grafana Cloud como exemplo prático da distinção MCP vs Skills fora do ecossistema Claude
