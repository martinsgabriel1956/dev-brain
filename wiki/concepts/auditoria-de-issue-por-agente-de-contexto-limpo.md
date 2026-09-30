---
type: concept
title: "Auditoria de Issue por Agente de Contexto Limpo"
aliases: ['issue audit', 'auditoria de issues', 'orquestrador-writer-reviewer']
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [agentes-ia, workflow, issues, revisao, orquestracao, tech-mentor-ai]
skill: tech-mentor-ai
status: draft
---

# Auditoria de Issue por Agente de Contexto Limpo

Workflow do autor de [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]] para escalar trabalho com agentes:

1. Quebrar o [[wiki/concepts/prd-product-requirements-document|PRD]] em issues que caibam no contexto (34 no OMXTerm).
2. **Auditar** cada issue: agente A cria; agente B (contexto limpo) *explica o que entendeu*; A compara; um agente C (também limpo) julga se o entendimento é válido.
3. **Orquestrador → writer → reviewer** (contextos limpos), o orquestrador aplica correções, fecha a issue e **abre outro orquestrador limpo** para a próxima.

Custo declarado: muitos tokens. Ganho: reduz "não estava escrito"/mal-entendido de prompt. **Limite mostrado pelo próprio autor:** o resultado foram 10 mil linhas que ele não tocou; o processo garante consistência com a issue, não [[wiki/concepts/comprehension-debt|compreensão humana]] — recuperar isso custou quase dois meses. Ver [[wiki/concepts/revisao-por-agente-independente]], [[wiki/concepts/spec-driven-development]], [[wiki/concepts/vibe-coding]].

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
