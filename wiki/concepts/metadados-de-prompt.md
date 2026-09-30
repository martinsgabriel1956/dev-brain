---
type: concept
title: "Metadados de Prompt"
aliases: ["prompt metadata", "ecossistema do prompt"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [prompt-versioning, metadados, rastreabilidade, temperatura, modelo]
skill: tech-mentor-ai
status: draft
---

# Metadados de Prompt

Conjunto de dados que acompanha o texto de um prompt em cada versão e permite reproduzi-lo e entender a mudança. Segundo [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]], versionar prompt é versionar esse "ecossistema", não só a string do system prompt.

## Campos citados pela fonte

| Campo | Para quê |
|---|---|
| Conteúdo (system prompt) | instruções, guardrails, tom, formato de saída |
| Modelo e provedor | mesmo texto rende diferente em outro modelo (ex.: Gemini vs. OpenAI) |
| Temperatura ([[wiki/concepts/hyperparameters-llm]]) | afeta variabilidade |
| Esforço de raciocínio (*effort*) | só onde o modelo suporta |
| Autor | responsabilização (quem desenvolveu também é variável) |
| Data de criação | linha do tempo |
| Motivo da mudança / comentário | o *porquê*, o que mais se perdia no bloco de notas |
| Tipo de versão | major / minor / correção ([[wiki/concepts/versionamento-semantico-de-prompt]]) |

Na implementação demonstrada, cada versão é um arquivo JSON com esses campos ([[wiki/concepts/prompt-registry-local]]).

## Lacunas (inferência)

Não citados na fonte, mas relevantes `[skill: tech-mentor-ai]`: seed, versão exata/snapshot do modelo, schema de saída, tools e versão do golden dataset usado na avaliação.

## Key sources

- [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]]
