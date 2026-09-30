---
type: concept
title: "Versionamento Semântico de Prompt"
aliases: ["semver de prompt", "major minor prompt"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [prompt-versioning, semver, llmops]
skill: tech-mentor-ai
status: draft
---

# Versionamento Semântico de Prompt

Uso da convenção major/minor/patch para sinalizar **o tamanho da mudança** num prompt. Na fonte ([[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]]):

- **Major**: altera quase toda a estrutura do prompt; espera-se mudança de comportamento do agente.
- **Minor**: pequena alteração; o comportamento provavelmente continua o mesmo.
- **Correção simples** (patch): ajuste pontual. A UI do autor pede essa escolha ao criar cada versão (exemplos de números: 1.2.1, 2.0, 3.0).

## Ressalva

A fonte não define critério objetivo para o que é major vs. minor, e uma palavra pode mudar a resposta (ver [[wiki/concepts/versionamento-de-prompt]]). Sem [[wiki/concepts/teste-de-regressao-de-prompt]], o rótulo é julgamento do autor, não garantia de compatibilidade de comportamento. Analogia com [[wiki/concepts/api-versioning]] `[inferência]`.

## Key sources

- [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]]
