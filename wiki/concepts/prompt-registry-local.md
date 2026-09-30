---
type: concept
title: "Prompt Registry Local (metadata.json + Loader)"
aliases: ["prompt manager", "prompt loader", "agent builder"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [prompt-versioning, arquitetura, agentes-ia, openrouter, implementacao]
skill: tech-mentor-ai
status: draft
---

# Prompt Registry Local (metadata.json + Loader)

Implementação demonstrada em [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]] para versionar prompts de um assistente financeiro (repositório "prompt manager", não acessado).

## Peças

- **Arquivos de versão**: cada versão de cada prompt é um JSON com nome, versão, conteúdo, temperatura, modelo etc. ([[wiki/concepts/metadados-de-prompt]]).
- **`metadata.json`** ("o comandante"): guarda a **versão ativa** de cada prompt.
- **Diretório de prompts** configurado por variável no `.env`.
- **Prompt loader + agent builder** (opcionais): leem o metadata, carregam o prompt ativo **com modelo e temperatura** e constroem o agente; releem com "certo controle de tempo" para não usar dado desatualizado.
- **UI web local**: criar (system prompt, modelo por presets/ID do [[wiki/entities/openrouter]], autor, temperatura, tipo semântico, esforço quando suportado) e gerenciar (ver versão ativa, ativar/depreciar, ler comentários).

## Trade-offs `[skill: tech-mentor-ai]`

Registries prontos (Langfuse Prompt Management, LangSmith Hub) e Git com PR são alternativas; a fonte não as compara. O ponteiro central no metadata é simples, mas sem revisão por PR nem gate de eval. Ver [[wiki/concepts/llmops]], [[wiki/concepts/rollback-de-prompt]].

## Key sources

- [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]]
