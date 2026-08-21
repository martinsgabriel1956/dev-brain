---
type: concept
title: "Agent-to-Agent Protocol (A2A)"
aliases: ["A2A", "agent to agent protocol", "protocolo A2A"]
date_created: 2026-08-14
date_updated: 2026-08-14
source_count: 1
tags: [a2a, protocolo, agentes-ia, multi-agent, google, interoperabilidade]
skill: tech-mentor-ai
status: stub
---

# Agent-to-Agent Protocol (A2A)

Protocolo aberto criado pela Google para permitir que agentes de IA construídos em frameworks e tecnologias diferentes se comuniquem entre si. Enquanto o [[wiki/concepts/model-context-protocol|MCP]] padroniza a relação entre um agente e as *tools/resources* que ele consome, o A2A padroniza a relação **entre agentes** — comunicação horizontal numa equipe de agentes (multiagente), em vez de vertical (agente → ferramenta).

## Por que existe

Aplicações multiagênticas raramente rodam num único framework: um agente de orquestração pode estar num stack e um agente especializado em outro. Sem um protocolo comum, essa comunicação vira integração ponto a ponto proprietária — o mesmo problema que o MCP resolveu para tool calling, mas na camada de agente-para-agente.

## Relação com Outros Conceitos

- [[wiki/concepts/model-context-protocol]] — MCP (agente ↔ ferramenta/dado) e A2A (agente ↔ agente) são complementares, não concorrentes.
- [[wiki/concepts/subagentes]] — subagentes no Claude Code são um caso de orquestração multiagente dentro de um único harness; A2A endereça o caso entre harnesses/frameworks distintos.
- [[wiki/concepts/design-patterns-ia]] — arquiteturas de agentes paralelos, sequenciais, customizados e autônomos dependem de algum protocolo de comunicação subjacente; A2A é uma opção emergente de mercado para isso.

## Key Sources

- [[wiki/sources/8-pontos-arquitetura-de-software-na-era-da-ia]] — citado como protocolo emergente ao lado do MCP, com o aviso de que "a cada dia tem iniciativas de novos protocolos"
