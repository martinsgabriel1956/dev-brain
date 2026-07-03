---
type: entity
title: "Claude Code"
aliases: ["claude code cli"]
date_created: 2026-05-18
date_updated: 2026-07-03
source_count: 3
tags: [ferramenta, agentes-ia, anthropic, llmops, cli, mcp, hooks]
skill: tech-mentor-ai
status: stable
---

## O Que É

CLI da Anthropic que age como [[agente-ia]] de desenvolvimento diretamente no terminal. Lê/escreve arquivos, executa comandos, navega na web e se integra a servidores [[mcp-server|MCP]] externos. Integra com qualquer IDE baseada em VS Code via extensão oficial.

---

## Recursos Principais

| Recurso | O que faz |
|---------|-----------|
| [[claude-md]] | Arquivo de memória e regras persistentes; lido em toda sessão |
| [[plan-mode]] | Modo de planejamento antes de executar (Shift+Tab) |
| [[slash-commands-agente]] | Commands customizados em `.claude/commands/*.md` |
| [[hooks-agente]] | Automação garantida em eventos (PreToolUse, PostToolUse, Stop) |
| [[mcp-server]] | Integração com ferramentas externas via protocolo MCP |
| [[context-compaction]] | Compactação automática da janela de contexto (~200k tokens) |
| [[wiki/concepts/worktree-paralelismo]] | `claude --worktree <nome>` — cópia isolada do repo por agente, paralelismo de file system |
| [[wiki/concepts/subagentes]] | `.claude/agents/*.md` — paralelismo de contexto, model/tools customizáveis por subagente |

## Planos (referência da gravação — verificar preços atuais)

| Plano | Preço/mês | Características |
|-------|-----------|-----------------|
| Free | $0 | Uso muito limitado |
| Pro | ~$20 | Rate limiting rápido; uso ocasional |
| Max | $100 | 5× mais que Pro; acesso ao Opus |
| Max | $200 | 20× mais que Pro |

**Armadilha:** usar API Key diretamente (sem plano) cobra por token e pode custar centenas de dólares sem que o usuário perceba. Sempre autenticar com "Claude account with subscription".

## Integração com IDE

1. Instale a extensão "Claude Code" no VS Code/Cursor
2. Clique em "Run Claude Code" para abrir painel lateral
3. Dentro do Claude Code: `/ide` para conectar ao projeto aberto

## Configuração

Arquivos em `.claude/`:
- `settings.json` — commitado, compartilhado com o time
- `settings.local.json` — pessoal, não commitado (permissões, MCPs locais)

## Comandos Essenciais

```
/init          → gera CLAUDE.md analisando o codebase
/memory        → edita memória (CLAUDE.md) do projeto ou usuário
/ide           → conecta ao IDE aberta
/mcp           → lista servidores MCP ativos
/hooks         → gerencia hooks de eventos
/permissions   → visualiza permissões configuradas
/compact       → compacta o histórico para liberar contexto
Shift+Tab      → alterna entre Auto-accept e Plan Mode
Esc            → para a execução atual
```

---

## Relevância para Token Anxiety

O mecanismo de [[context-compaction]] da janela de contexto do Claude Code é um dos principais catalisadores do fenômeno [[token-anxiety]]: desenvolvedores sentem urgência de maximizar o uso dos tokens disponíveis antes do reset, distorcendo rotinas e prioridades.

---

## Key Sources

- [[wiki/sources/token-anxiety-agentes-ia-comportamento-devs]]
- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
