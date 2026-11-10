---
type: concept
title: "Design Doc como Fonte do Contexto"
aliases: ["design doc", "documento de design", "technical design doc", "fonte da verdade para agentes"]
date_created: 2026-11-10
date_updated: 2026-11-10
source_count: 1
tags: [design-doc, context-engineering, coding-agents, discovery, spec-driven]
skill: tech-mentor-ai
status: stub
---

# Design Doc como Fonte do Contexto

## TL;DR

Documento que produto e engenharia escrevem depois de uma discovery, com o contexto do projeto, as APIs envolvidas, o MVP e o que está definido ou não. Em fluxos com agentes, ele é a fonte da verdade revisada por humanos: dali em diante, a IA enriquece esse contexto e escreve o código ([[wiki/sources/fluxo-completo-feature-com-ia-design-doc-worktrees-valdemar-neto]]).

## O Que Contém no Exemplo

- Contexto do sistema e motivo da mudança.
- Fluxo e APIs que serão usadas, possivelmente explorados por humano e IA numa PoC.
- MVP com recorte explícito, no caso um fluxo de teste gratuito, sem cartão de crédito.
- Lista das coisas principais, marcando o que está definido. O indefinido fica fora do MVP.

## Como Entra no Fluxo

1. O agente lê o documento, no exemplo pelo MCP da Atlassian, e avalia se o MVP está definido.
2. O agente propõe tasks. O humano ajusta o tamanho: uma task por fase, em vez de passos pequenos.
3. As tasks vão para o rastreador, com contexto de alto nível.
4. Cada task vira um plano em contexto novo, seguindo o [[wiki/concepts/rpi-workflow]].

O local não importa: Confluence, Notion ou o próprio repositório. Se a tarefa já existe e está clara, ela mesma é o contexto.

## Relação com Outros Conceitos

- [[wiki/concepts/spec-driven-development]]: mesma ideia de escrever antes de gerar. O design doc descreve o projeto; a spec costuma descer ao comportamento de uma tarefa `[inferência]`.
- [[wiki/concepts/prd-product-requirements-document]] e [[wiki/concepts/rfc-request-for-comments]]: outros documentos citados como boas referências de contexto.
- [[wiki/concepts/adr-architecture-decision-record]]: registra uma decisão; o design doc descreve o trabalho a fazer `[inferência]`.
- [[wiki/concepts/janela-de-contexto]]: o que não virou artefato nunca entra na janela.

## Key Sources

- [[wiki/sources/fluxo-completo-feature-com-ia-design-doc-worktrees-valdemar-neto]]: design doc da integração com o Stripe como ponto de partida do fluxo
