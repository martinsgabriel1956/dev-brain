---
type: concept
title: "MCP Server — Configuração e Uso no Claude Code"
aliases: ["mcp server claude code", "configurar mcp", "claude mcp cli"]
date_created: 2026-05-31
date_updated: 2026-09-14
source_count: 5
tags: [mcp, claude-code, agente-ia, ferramentas, llmops]
skill: tech-mentor-ai
status: stable
---

# MCP Server — Configuração no Claude Code

## TL;DR

[[claude-code]] suporta **servidores MCP** que expandem as capacidades do agente com ferramentas externas (Docker, bancos de dados, APIs, filesystems). Configurados via CLI com `claude mcp`. Podem ser globais (todos os projetos) ou locais (só este projeto, não commitado).

> Para entender o protocolo MCP em si → [[wiki/sources/mcp]]

## Gerenciar MCPs pelo CLI

```bash
claude mcp --help              # ajuda
claude mcp list                # listar servidores configurados
claude mcp add <nome> <cmd>    # adicionar servidor
claude mcp remove <nome>       # remover servidor
```

**Exemplo — MCP Docker:**
```bash
claude mcp add mcp-docker docker mcp gateway run
```

O Docker MCP Tool Kit gerencia múltiplos servidores MCP containerizados, expondo-os como um único gateway.

## Verificar MCPs na Sessão

```
/mcp
```

Lista os servidores ativos e status de conexão na sessão atual.

## Importar do Claude Desktop

```bash
claude mcp import-from-desktop
```

Importa os servidores MCP já configurados no Claude Desktop — evita reconfigurar do zero.

## Onde a Configuração é Salva

| Escopo | Arquivo | Commitar? |
|--------|---------|-----------|
| Local (você, este projeto) | `.claude/settings.local.json` | ❌ Não |
| Projeto (time todo) | `.claude/settings.json` | ✅ Sim |
| Global (todos os projetos) | `~/.claude/settings.json` | — |

```json
// settings.local.json
{
  "mcpServers": {
    "mcp-docker": {
      "command": "docker",
      "args": ["mcp", "gateway", "run"]
    }
  }
}
```

## Permissões de MCP

Quando o agente usa um servidor MCP pela primeira vez, pede confirmação. Você pode:
- Aprovar **só dessa vez**
- Aprovar **sempre nessa sessão**
- Aprovar **sempre** → salva em `settings.local.json` como permissão permanente

```json
"permissions": {
  "allow": ["mcp__mcp-docker__*"]
}
```

## Relação com o Protocolo MCP

MCP (Model Context Protocol) define como LLMs se conectam a ferramentas externas via JSON-RPC. O [[claude-code]] é um **cliente MCP** — ele conecta a servidores que implementam o protocolo e usa as tools/resources expostas.

Ver [[wiki/sources/mcp]] para detalhes do protocolo (Tools, Resources, Prompts, Sampling, transportes stdio/SSE).

## Exemplo de domínio: Grafana MCP para observabilidade

Um servidor MCP não precisa ser genérico (filesystem, Docker) — pode expor um domínio inteiro. O **Grafana MCP**, por exemplo, dá ao agente acesso a Prometheus (métricas), Loki (logs) e Tempo/Jaeger (traces) através do Grafana como hub único. Combinado com um MCP de documentação (ex. Context7, para obter a doc atualizada da lib que precisa de correção), um prompt simples do tipo "investigue os erros 500 desse endpoint nos últimos 15 minutos" pode virar um relatório de causa raiz com linha de código específica, gerado em minutos. Ver [[wiki/concepts/investigacao-de-incidentes-com-ia-e-mcp]].

### Custo: Grafana MCP no editor consome créditos do editor, chat web do Grafana Cloud não

Nem toda correlação automática de telemetria passa por um MCP server. O **Grafana Cloud** também expõe o mesmo tipo de correlação (logs + métricas + traces) via um assistente de IA embutido na própria interface web da plataforma — nesse caminho, o custo de IA é do plano do Grafana Cloud, não dos créditos do editor de código do usuário. Já o Grafana MCP, por rodar como tool dentro do editor (ex. Claude Code), consome os créditos de IA do próprio editor. Mesmo prompt genérico, mesmo resultado (causa raiz + linha de código) nos dois caminhos testados.

## Deploy Serverless com Spec Stateless (2026)

Segundo [[wiki/sources/mcp-stateless-fim-do-handshake-server-discover-lucas-montano]], com o core do MCP passando a ser stateless, um servidor MCP remoto simples pode ser implementado como um único arquivo POST, sem depender do MCP TypeScript SDK oficial, e deployado serverless/edge sem infraestrutura de sessão (Redis, sticky session). Ver [[wiki/concepts/mcp-stateless-server-discover]] para o mecanismo completo (handle mintado pelo servidor, `server discover`, headers de método/recurso).

## Marketplace de Plugins Corporativos via MCP + SSO

[[wiki/sources/guia-claude-code-para-startups-anthropic-ai-native-sdlc]] descreve um padrão de adoção corporativa de MCP citado num playbook da Anthropic com startups: conectar as ferramentas do dia a dia do time (Jira, Figma, Google Drive) via servidores MCP autenticados com login corporativo (SSO), organizados como um "marketplace de plugins" interno — em vez de cada dev configurar MCPs individualmente. A lógica citada na fonte: "o Claude não consegue entender o que não vê" — conectar fontes de dados confiáveis é pré-requisito para o agente ser útil em contexto de negócio real, não só em tarefas de código isoladas. Ver [[wiki/concepts/sdlc-nativo-de-ia]] (regra 5: prototype/dog food/productionize).

## Key Sources

- [[wiki/sources/guia-claude-code-para-startups-anthropic-ai-native-sdlc]] — marketplace de plugins corporativos via MCP + SSO (Jira, Figma, Drive)
- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
- [[wiki/sources/mcp-stateless-fim-do-handshake-server-discover-lucas-montano]] — deploy stateless/serverless de MCP server, implementação em arquivo único sem SDK oficial
- [[wiki/sources/mcp]]
- [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]] — Grafana MCP + Context7 usados juntos para investigação automatizada de incidentes
- [[wiki/sources/monitoramento-aplicacoes-ia-grafana-cloud-opentelemetry]] — contraste de custo entre Grafana MCP (créditos do editor) e chat web do Grafana Cloud (sem custo de editor)
