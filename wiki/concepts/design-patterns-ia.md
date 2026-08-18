---
type: concept
title: "Design Patterns Focados em IA"
aliases: ["design patterns ia", "AI design patterns", "12 factor agents", "twelve factor agents"]
date_created: 2026-08-14
date_updated: 2026-08-14
source_count: 1
tags: [design-patterns, agentes-ia, arquitetura, seguranca, twelve-factor-agents]
skill: tech-mentor-ai
status: stub
---

# Design Patterns Focados em IA

Extensão do catálogo de [[wiki/concepts/design-patterns|Design Patterns]] tradicional para três categorias específicas de aplicações com LLM:

1. **Patterns de integração** — como uma aplicação comum se conecta a um LLM (ex.: padrões em torno de [[wiki/concepts/model-context-protocol|MCP]], roteamento de modelo, fallback — ver [[wiki/concepts/ai-gateway-llm-router]]).
2. **Patterns de criação de agentes** — arquiteturas recorrentes para orquestrar agentes: paralelo, sequencial, customizado (workflow forçado) e autônomo (o próprio agente decide como chamar outros agentes). Ver [[wiki/concepts/agente-ia]] e [[wiki/concepts/subagentes]].
3. **Patterns de segurança** — ex.: isolar agentes para que um não propague contexto contaminado por [[wiki/concepts/prompt-injection-jailbreak|prompt injection]] a outro agente da mesma pipeline.

## 12 Factor Agents

Iniciativa que aplica o mesmo espírito do **Twelve-Factor App** (metodologia de 12 fatores para software SaaS escalável, popularizada pela Heroku) ao desenho de agentes de IA. Pré-requisito para aproveitá-la: entender com clareza o que é um agente e como ele difere de software tradicional — sem essa base, os fatores individuais não fazem sentido.

## Relação com Outros Conceitos

- [[wiki/concepts/design-patterns]] — catálogo geral (GoF) do qual esta página é uma extensão específica de domínio.
- [[wiki/concepts/agent-to-agent-protocol]] — protocolo que viabiliza um dos patterns de criação de agentes (comunicação entre agentes autônomos).
- [[wiki/concepts/agent-containment]] — pattern de segurança relacionado (sandboxing/contenção), aplicável junto com isolamento de contexto contra contaminação.

## Key Sources

- [[wiki/sources/8-pontos-arquitetura-de-software-na-era-da-ia]] — enumera as três categorias de pattern e cita 12 Factor Agents como analogia direta ao Twelve-Factor App
