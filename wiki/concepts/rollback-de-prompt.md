---
type: concept
title: "Rollback de Prompt"
aliases: ["rollback instantâneo de prompt", "depreciar versão de prompt"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [prompt-versioning, rollback, producao, llmops]
skill: tech-mentor-ai
status: draft
---

# Rollback de Prompt

Voltar a uma versão anterior do prompt em produção com uma ação única, sem editar texto nem redeploy. Na fonte ([[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]]): um botão na interface ativa uma versão ou marca outra como depreciada; exemplo, a 2.0 "não deu certo" e volta-se à 1.2.1.

## Como funciona na demo

O ponteiro de "versão ativa" vive no `metadata.json`; o loader relê esse arquivo e monta o agente com o prompt, modelo e temperatura da versão ativa ([[wiki/concepts/prompt-registry-local]]). Trocar a versão ativa **é** o rollback. Mecanismo análogo a [[wiki/concepts/feature-flag]] `[inferência]`.

## Depende de reprodutibilidade

Só funciona bem se a versão antiga guardar modelo e temperatura ([[wiki/concepts/metadados-de-prompt]]); voltar só o texto pode dar comportamento diferente. Ver [[wiki/concepts/versionamento-de-prompt]].

## Ressalva

É controle **reativo**: descobre-se a regressão depois. O gate preventivo é [[wiki/concepts/teste-de-regressao-de-prompt]].

## Key sources

- [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]]
