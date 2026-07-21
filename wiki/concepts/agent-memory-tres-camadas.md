---
type: concept
title: "Memória de Agente em Três Camadas (Sessão / Persistente / Skill)"
aliases: ["three-layer agent memory", "memória de três camadas", "session/persistent/skill memory"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [tech-mentor-ai, agent-memory, learning-loop, sqlite, fts5, hermes-agent]
skill: tech-mentor-ai
status: draft
---

# Memória de Agente em Três Camadas (Sessão / Persistente / Skill)

Padrão arquitetural para agentes de propósito geral que precisam reter contexto entre conversas, não só dentro de uma única sessão. Descrito em [[wiki/sources/hermes-agent-open-claw-learning-loop]] como base do Hermes Agent, mas apresentado como padrão comum a "quem já usa alguma orquestração de agentes" — não uma invenção exclusiva.

## As Três Camadas

1. **Memória de sessão** — a conversa atual. Equivalente à working memory in-context do Claude Code ou Codex: rápida, mas perdida ao fim da sessão.
2. **Persistent memory** — um `memory.md` (ou equivalente) que armazena e cura dados entre agentes e sessões diferentes. É o que sobrevive ao fechar a janela de contexto atual.
3. **Skill memory** — padrões extraídos de tarefas passadas, convertidos em skills reutilizáveis (ver [[wiki/concepts/closed-loop-skill-learning]]), indexadas por um arquivo `.md` próprio.

## Indexação via FTS5 (SQLite)

O caso descrito usa **FTS5** (full-text search do SQLite) para buscar sobre a sumarização LLM da memória persistente quando o contexto cresce — em vez de (ou além de) um vector store dedicado. Diferença prática frente às opções listadas em [[wiki/concepts/gerenciamento-de-memoria]]/`agent-memory.md`: FTS5 é busca lexical/full-text, não busca por similaridade semântica via embeddings — mais barato de rodar localmente (SQLite embutido, sem serviço externo), mas sem os mesmos ganhos de recall semântico de um vector store como Qdrant ou pgvector.

## Resultado Prático

O efeito observado, segundo a fonte: o agente passa a lembrar preferências implícitas do usuário (ex.: "você odeia NPM") depois de poucas sessões, sem que isso precise ser reescrito manualmente em um arquivo de regras a cada nova janela de contexto.

## Relação com Outros Conceitos

- [[wiki/concepts/closed-loop-skill-learning]] — o loop que alimenta a camada de skill memory
- [[wiki/concepts/memoria-de-longo-prazo-ia]] — padrão irmão, mas de escopo mais estreito (memória de research/refactoring plan entre sessões de uma única tarefa grande, não memória geral de preferências do usuário)
- [[wiki/concepts/skills-agente]] — skill memory é, na prática, um caso de skills geradas automaticamente em vez de escritas à mão
- [[wiki/concepts/hooks-agente]] — hooks são o mecanismo citado para popular a persistent/skill memory ao fim de uma sessão

## Key sources

- [[wiki/sources/hermes-agent-open-claw-learning-loop]]
