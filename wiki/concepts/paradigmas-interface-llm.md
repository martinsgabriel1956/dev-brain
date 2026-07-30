---
type: concept
title: "Paradigmas de Interface de LLM (Site → App → Agente Autônomo)"
aliases: ["terceiro paradigma llm", "llm ux paradigms", "evolução da interface de ia"]
date_created: 2026-07-30
date_updated: 2026-07-30
source_count: 1
tags: [ux-llm, karpathy, ambient-agent, claude-tag, interface-de-ia]
skill: tech-mentor-ai
status: draft
---

# Paradigmas de Interface de LLM (Site → App → Agente Autônomo)

Framework popularizado por Andrej Karpathy (ver [[wiki/entities/andrej-karpathy]]) para descrever três reformulações sucessivas de como humanos interagem com LLMs:

1. **LLM como site** — acessado via browser (ex.: chat.openai.com, claude.ai). Interação síncrona, um usuário por vez, sem persistência além da sessão/histórico de conversa.
2. **LLM como aplicativo local** — baixado para o computador (ex.: Claude Desktop, Cursor, Claude Code CLI). Ganha acesso a arquivos locais e ferramentas, mas ainda é uma ferramenta *para um indivíduo*.
3. **LLM como entidade autônoma, persistente e assíncrona** — com ferramentas, memória e contexto compartilhados por toda a organização, trabalhando *com* o time, não apenas *para* um membro dele. Exemplo citado: Claude Tag (Claude integrado ao Slack por canal) — ver [[wiki/entities/anthropic]].

## Por que a Diferença Importa

A distinção não é sobre a interface superficial (chat vs @menção), e sim sobre **quem é o usuário do agente**: uma pessoa (paradigmas 1 e 2) vs um time inteiro compartilhando o mesmo contexto (paradigma 3). Isso muda o modelo de memória — ver [[wiki/concepts/agent-memory-tres-camadas]], que documenta memória em três camadas *por usuário/sessão*; o paradigma 3 introduz uma camada adicional de memória multiplayer por canal/equipe, ainda sem página dedicada na wiki.

## Ceticismo Técnico vs Estratégico

Segundo [[wiki/sources/claude-tag-slack-terceiro-paradigma-llm]], a crítica mais comum ao anúncio da Anthropic é que "um bot em chat com ferramenta e memória já existe há anos" — **tecnicamente correta**. O contra-argumento (de Gergely Orosz, ver [[wiki/entities/gergely-orosz]]) é que o breakthrough real não é a interface, mas a integração *confiável e sem manutenção manual* com todos os sistemas internos de uma empresa comum (Jira, banco de produção, RH, segurança/VPN) — algo historicamente caro e que exigia um time de plataforma dedicado.

## Analogia Geracional

O apresentador da fonte compara essa transição com a mudança de paradigma do sistema operacional: gerações que cresceram com aplicativos (não com conceito de pasta/arquivo/sistema operacional) tendem a considerar "conversar com uma IA" o modo padrão de interação, reservando "abrir um aplicativo específico" para tarefas muito pontuais — espelhando como sua própria geração relacionava-se com o sistema operacional (Windows 95) como camada padrão de interação com o computador.

## Relação com Outros Conceitos

- [[wiki/concepts/era-agentica]] — descreve a mudança de *modelo de custo* (autocomplete → tarefa completa) que acompanha essa transição de interface, mas foca em economia de tokens, não em quem é o "usuário" do agente.
- [[wiki/concepts/harness]] — o paradigma 3 exige um harness organizacional (não apenas individual): tools, integrações, ambientes de execução e segurança compartilhados por múltiplos usuários simultâneos.
- [[wiki/concepts/lock-in-vendor-ia]] — risco associado ao adotar o paradigma 3 via um único fornecedor: a memória organizacional acumulada fica presa ao vendor.

## Key Sources

- [[wiki/sources/claude-tag-slack-terceiro-paradigma-llm]] — origem do framework nesta wiki, via citação direta de tweet de Andrej Karpathy
